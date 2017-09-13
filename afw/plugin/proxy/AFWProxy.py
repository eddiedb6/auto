import zlib

import AFWConst
from AFWLogger import *

class AFWProxy:
    def __init__(self, guid, manager):
        self.__guid = guid
        self.__manager = manager

    def Close(self):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameCloseClient
        }
        self.__handleMessage(msg)

    ### Implement AFWPlugin ###

    def GetElement(self, config, parentConfig):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetElement,
            AFWConst.MsgParam1: config,
            AFWConst.MsgParam2: parentConfig
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]
    
    def SetFocus(self, ui):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameSetFocus,
            AFWConst.MsgParam1: ui
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def Click(self, ui):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameClick,
            AFWConst.MsgParam1: ui
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def IsChecked(self, ui):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameIsChecked,
            AFWConst.MsgParam1: ui
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def IsEnabled(self, ui):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameIsEnabled,
            AFWConst.MsgParam1: ui
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def PressKey(self, ui, key):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNamePressKey,
            AFWConst.MsgParam1: ui,
            AFWConst.MsgParam2: key
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def ReleaseKey(self, ui, key):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameReleaseKey,
            AFWConst.MsgParam1: ui,
            AFWConst.MsgParam2: key
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def GetText(self, ui):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetText,
            AFWConst.MsgParam1: ui
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    ### Implement AFWPluginWeb ###

    def OpenBrowser(self, name):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameOpenBrowser,
            AFWConst.MsgParam1: name
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def OpenWebPage(self, browser, url):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameOpenWebPage,
            AFWConst.MsgParam1: browser,
            AFWConst.MsgParam2: url
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def GetCurrentURL(self, browser):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetCurrentURL,
            AFWConst.MsgParam1: browser
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def SendKeys(self, ui, keys):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameSendKeys,
            AFWConst.MsgParam1: ui,
            AFWConst.MsgParam2: keys
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    ### Implement AFWPluginApp ###

    def StartApp(self, path):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameStartApp,
            AFWConst.MsgParam1: path
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def GetDesktop(self):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetDesktop
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def GetForm(self, config):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetForm,
            AFWConst.MsgParam1: config
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    ### Private ###
    
    def __getConn(self):
        conn = self.__manager.GetClientConn(self.__guid)
        if conn is None:
            raise Exception("No connection for proxy " + self.__guid)
        return conn

    def __compressMessage(self, msg):
        msgStr = str(msg)
        msgZip = zlib.compress(msgStr)
        if len(msgStr) > 128:
            msgStr = msgStr[0:127] + "..."
        return msgZip, msgStr

    def __handleMessage(self, msg):
        conn = self.__getConn()
        msgZip, msgStr = self.__compressMessage(msg)
        conn.sendall(msgZip)
        Debug("Send proxy client message: " + msgStr)
        result = conn.recv(AFWConst.MsgLength)
        Debug("Recv proxy client result: " + result)
        resultDict = eval(result)
        if AFWConst.MsgName not in resultDict or AFWConst.MsgResult not in resultDict or resultDict[AFWConst.MsgName] != msg[AFWConst.MsgName]:
            raise Exception("Message result is not returned: " + msg[AFWConst.MsgName])
        return resultDict
