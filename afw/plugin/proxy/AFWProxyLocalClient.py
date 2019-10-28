import sys
import os
import socket
import uuid
import logging

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], ".."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../pool"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../.."))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../util"))

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

def __handleMessage(msg):
    msgName = msg[AFWConst.MsgName]
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
    elif msgName == AFWConst.MsgNameSelect:
        uiID = msg[AFWConst.MsgParam1]
        itemValue = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.Select(uiID, itemValue)
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
    elif msgName == AFWConst.MsgNameGetCellText:
        uiID = msg[AFWConst.MsgParam1]
        row = msg[AFWConst.MsgParam2]
        column = msg[AFWConst.MsgParam3]
        result[AFWConst.MsgResult] = pluginInstance.GetCellText(uiID, row, column)
    elif msgName == AFWConst.MsgNameGetDynamicElement:
        parentID = msg[AFWConst.MsgParam1]
        config = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.GetDynamicElement(parentID, config)
    elif msgName == AFWConst.MsgNameGetAttribute:
        uiID = msg[AFWConst.MsgParam1]
        name = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.GetAttribute(uiID, name)
    elif msgName == AFWConst.MsgNameDumpUI:
        uiID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.DumpUI(uiID)
    elif msgName == AFWConst.MsgNameOpenBrowser:
        name = msg[AFWConst.MsgParam1]
        browserID = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.OpenBrowser(name, browserID)
    elif msgName == AFWConst.MsgNameCloseBrowser:
        browserID = msg[AFWConst.MsgParam1]
        result[AFWConst.MsgResult] = pluginInstance.CloseBrowser(browserID)
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
    elif msgName == AFWConst.MsgNameSetText:
        uiID = msg[AFWConst.MsgParam1]
        text = msg[AFWConst.MsgParam2]
        result[AFWConst.MsgResult] = pluginInstance.SetText(uiID, text)
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
    # Load plugin
    pluginModule = __import__(pluginName)
    if not pluginModule:
        Error("[Local Client] No plugin imported for " + pluginName)
        sys.exit(0)
    else:
        Info("[Local Client] Load plugin: " + pluginName)
    pluginClass = getattr(pluginModule, pluginName)
    pluginInstance = pluginClass(None, AFWProxyConfigPool(s))

    # Regisger client
    registerMsg = {
        AFWConst.MsgName: AFWConst.MsgNameRegisterClient,
        AFWConst.MsgParam1: guid
    }
    regMsgZip, regMsgStr = AFWProxyUtil.CompressProxyMessage(registerMsg)
    Debug("[Local Client] Send proxy host register request: " + regMsgStr)
    s.sendall(regMsgZip)

    # Handle proxy command
    isContinue = True
    while isContinue:
        cmd = s.recv(AFWConst.MsgLength)
        msg, msgStr = AFWProxyUtil.DecompressProxyMessage(cmd)
        Debug("[Local Client] Recv proxy host message: " + msgStr)
        resultMsg, isContinue = __handleMessage(msg)
        msgZip, msgStr = AFWProxyUtil.CompressProxyMessage(resultMsg)
        Debug("[Local Client] Send proxy host result: " + msgStr)
        s.sendall(msgZip)
except:
    Error("Exception: local proxy client\n" + str(sys.exc_info()[0]) + "\n" + str(sys.exc_info()[1]))

s.close()
Info("[Local Client] Disconnect for client " + guid)
