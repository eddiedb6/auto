import sys
import os
import socket
import uuid
import logging

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], ".."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))

from AFWLogger import *
from AFWProxyConfigPool import AFWProxyConfigPool
import AFWProxyUtil
import AFWConst

paramLen = len(sys.argv)
if paramLen < 3:
    raise Exception("[Local Client] No log level, plugin name and guid passed in")
    sys.exit(0)

logLevel = int(sys.argv[paramLen - 1])
guid = sys.argv[paramLen - 2]
pluginName = sys.argv[paramLen - 3]
pluginInstance = None

logging.basicConfig(level = logLevel)

# Helpers

def __handleCommand(msg):
    msgName = msg[AFWConst.MsgName]
    Debug("[Local Client] Get command " + msgName + " to handle")
    result = {
        AFWConst.MsgName: msgName,
        AFWConst.MsgResult: None
    }
    isContinue = True
    if msgName == AFWConst.MsgNameCloseClient:
        isContinue = False
    elif msgName == AFWConst.MsgNameGetElement:
        elementID = pluginInstance.GetElement(msg[AFWConst.MsgParam1], msg[AFWConst.MsgParam2])
        result[AFWConst.MsgResult] = elementID
    elif msgName == AFWConst.MsgNameSetFocus:
        uiID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.SetFocus(uiID)
    elif msgName == AFWConst.MsgNameClick:
        uiID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.Click(uiID)
    elif msgName == AFWConst.MsgNameIsChecked:
        uiID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.IsChecked(uiID)
    elif msgName == AFWConst.MsgNameIsEnabled:
        uiID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.IsEnabled(uiID)
    elif msgName == AFWConst.MsgNamePressKey:
        uiID = msg[AFWConst.MsgParam1]
        key = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.PressKey(uiID, key)
    elif msgName == AFWConst.MsgNameReleaseKey:
        uiID = msg[AFWConst.MsgParam1]
        key = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.ReleaseKey(uiID, key) 
    elif msgName == AFWConst.MsgNameGetText:
        uiID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.GetText(uiID)
    elif msgName == AFWConst.MsgNameOpenBrowser:
        name = msg[AFWConst.MsgParam1]
        browserID = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.OpenBrowser(name, browserID)
    elif msgName == AFWConst.MsgNameOpenWebURL:
        browserID = msg[AFWConst.MsgParam1]
        url = msg[AFWConst.MsgParam2]
        configID = msg[AFWConst.MsgParam3]
        result[AFWConst.MsgResult] = pluginInstance.OpenWebURL(browserID, url, configID)
    elif msgName == AFWConst.MsgNameGetCurrentURL:
        browserID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.GetCurrentURL(browserID)
    elif msgName == AFWConst.MsgNameGetWebPage:
        browserID = msg[AFWConst.MsgParam1]
        configID = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.GetWebPage(browserID, configID)
    elif msgName == AFWConst.MsgNameSendKeys:
        uiID = msg[AFWConst.MsgParam1]
        keys = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.SendKeys(uiID, keys)
    elif msgName == AFWConst.MsgNameStartApp:
        path = msg[AFWConst.MsgParam1]
        configID = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.StartApp(path, configID)
    elif msgName == AFWConst.MsgNameGetDesktop:
        configID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.GetDesktop(configID)
    elif msgName == AFWConst.MsgNameGetForm:
        configID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.GetForm(configID)
    else:
        Warning("[Local Client] Not recognized command: " + msgName)
    return result, isContinue

# Start client
HOST = "localhost"
PORT = AFWConst.ProxyHostPort
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
Info("[Local Client] Connect to host successfully for client " + guid)

try:
    # Regisger client
    registerMsg = {
        AFWConst.MsgName: AFWConst.MsgNameRegisterClient,
        AFWConst.MsgParam1: guid
    }
    regMsgZip, regMsgStr = AFWProxyUtil.CompressProxyMessage(registerMsg)
    s.sendall(regMsgZip)

    # Load plugin
    pluginModule = __import__(pluginName)
    if not pluginModule:
        Error("[Local Client] No plugin imported for " + pluginName)
        sys.exit(0)
    else:
        Info("[Local Client] Load plugin: " + pluginName)
    pluginClass = getattr(pluginModule, pluginName)
    pluginInstance = pluginClass(None, AFWProxyConfigPool(s))

    # Handle proxy command
    isContinue = True
    while isContinue:
        cmd = s.recv(AFWConst.MsgLength)
        msg, msgStr = AFWProxyUtil.DecompressProxyMessage(cmd)
        resultMsg, isContinue = __handleCommand(msg)
        msgZip, msgStr = AFWProxyUtil.CompressProxyMessage(resultMsg)
        s.sendall(msgZip)
except:
    Error("Local proxy client exception: \n" + str(sys.exc_info()[0]) + "\n" + str(sys.exc_info()[1]))

s.close()
Info("[Local Client] Disconnect for client " + guid)
