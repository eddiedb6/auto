import sys
import os
import socket
import zlib
import uuid
import logging

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], ".."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "."))

from AFWLogger import *
import AFWConst

__objPool = {}
__objPool.clear()

paramLen = len(sys.argv)
if paramLen < 3:
    raise Exception("[Local Client] No log level, plugin name and guid passed in")
    sys.exit(0)

logLevel = int(sys.argv[paramLen - 1])
guid = sys.argv[paramLen - 2]
pluginName = sys.argv[paramLen - 3]

logging.basicConfig(level = logLevel)

# Helpers

def __addObj(obj):
    guid = str(uuid.uuid1())
    __objPool[guid] = obj
    return guid

def __getObj(guid):
    if guid not in __objPool:
        Fatel("[Local Client] No guid in object pool: " + guid)
        return None
    return __objPool[guid]

def __clearObj():
    __objPool.clear()

def __handleCommand(cmd):
    msg = eval(zlib.decompress(cmd))
    msgName = msg[AFWConst.MsgName]
    Debug("[Local Client] Get command " + msgName + " to handle")
    result = {
        AFWConst.MsgName: msgName,
        AFWConst.MsgResult: None
    }
    isContinue = True
    if msgName == AFWConst.MsgNameCloseClient:
        __clearObj()
        isContinue = False
    elif msgName == AFWConst.MsgNameGetElement:
        obj = pluginInstance.GetElement(msg[AFWConst.MsgParam1], msg[AFWConst.MsgParam2])
        result[AFWConst.MsgResult] = __addObj(obj)
    elif msgName == AFWConst.MsgNameSetFocus:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.SetFocus(obj)
    elif msgName == AFWConst.MsgNameClick:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.Click(obj)
    elif msgName == AFWConst.MsgNameIsChecked:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.IsChecked(obj)
    elif msgName == AFWConst.MsgNameIsEnabled:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.IsEnabled(obj)
    elif msgName == AFWConst.MsgNamePressKey:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.PressKey(obj, msg[AFWConst.MsgParam2])
    elif msgName == AFWConst.MsgNameReleaseKey:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.ReleaseKey(obj, msg[AFWConst.MsgParam2])
    elif msgName == AFWConst.MsgNameGetText:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.GetText(obj)
    elif msgName == AFWConst.MsgNameOpenBrowser:
        obj = pluginInstance.OpenBrowser(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = __addObj(obj)
    elif msgName == AFWConst.MsgNameOpenWebPage:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.OpenWebPage(obj, msg[AFWConst.MsgParam2])
    elif msgName == AFWConst.MsgNameGetCurrentURL:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.GetCurrentURL(obj)
    elif msgName == AFWConst.MsgNameSendKeys:
        obj = __getObj(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = pluginInstance.SendKeys(obj, msg[AFWConst.MsgParam2])
    elif msgName == AFWConst.MsgNameStartApp:
        obj = pluginInstance.StartApp(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = __addObj(obj)
    elif msgName == AFWConst.MsgNameGetDesktop:
        obj = pluginInstance.GetDesktop()
        result[AFWConst.MsgResult] = __addObj(obj)
    elif msgName == AFWConst.MsgNameGetForm:
        obj = pluginInstance.GetForm(msg[AFWConst.MsgParam1])
        result[AFWConst.MsgResult] = __addObj(obj)
    else:
        Warning("[Local Client] Not recognized command: " + msgName)
    return result, isContinue

# Load plugin
pluginModule = __import__(pluginName)
if not pluginModule:
    Error("[Local Client] No plugin imported for " + pluginName)
    sys.exit(0)
else:
    Info("[Local Client] Load plugin: " + pluginName)
pluginClass = getattr(pluginModule, pluginName)
pluginInstance = pluginClass(None)

# Start client
HOST = "localhost"
PORT = AFWConst.ProxyHostPort
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
Info("[Local Client] Connect to host successfully for client " + guid)

# Regisger client
registerMsg = {
    AFWConst.MsgName: AFWConst.MsgNameRegisterClient,
    AFWConst.MsgParam1: guid
}
s.sendall(str(registerMsg))

# Handle proxy command
isContinue = True
while isContinue:
    cmd = s.recv(AFWConst.MsgLength)
    resultMsg, isContinue = __handleCommand(cmd)
    s.sendall(str(resultMsg))
s.close()
Info("[Local Client] Disconnect for client " + guid)
