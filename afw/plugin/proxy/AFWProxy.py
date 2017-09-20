import AFWConst
import AFWProxyUtil
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

    def GetElement(self, configID, parentConfigID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetElement,
            AFWConst.MsgParam1: configID,
            AFWConst.MsgParam2: parentConfigID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]
    
    def SetFocus(self, uiID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameSetFocus,
            AFWConst.MsgParam1: uiID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def Click(self, uiID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameClick,
            AFWConst.MsgParam1: uiID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def IsChecked(self, uiID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameIsChecked,
            AFWConst.MsgParam1: uiID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def IsEnabled(self, uiID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameIsEnabled,
            AFWConst.MsgParam1: uiID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def PressKey(self, uiID, key):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNamePressKey,
            AFWConst.MsgParam1: uiID,
            AFWConst.MsgParam2: key
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def ReleaseKey(self, uiID, key):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameReleaseKey,
            AFWConst.MsgParam1: uiID,
            AFWConst.MsgParam2: key
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def GetText(self, uiID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetText,
            AFWConst.MsgParam1: uiID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    ### Implement AFWPluginWeb ###

    def OpenBrowser(self, name, configID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameOpenBrowser,
            AFWConst.MsgParam1: name,
            AFWConst.MsgParam2: configID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def OpenWebPage(self, browserID, url):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameOpenWebPage,
            AFWConst.MsgParam1: browserID,
            AFWConst.MsgParam2: url
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def GetCurrentURL(self, browserID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetCurrentURL,
            AFWConst.MsgParam1: browserID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def SendKeys(self, uiID, keys):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameSendKeys,
            AFWConst.MsgParam1: uiID,
            AFWConst.MsgParam2: keys
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    ### Implement AFWPluginApp ###

    def StartApp(self, path, configID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameStartApp,
            AFWConst.MsgParam1: path,
            AFWConst.MsgParam2: configID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def GetDesktop(self, configID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetDesktop,
            AFWConst.MsgParam1: configID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    def GetForm(self, configID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetForm,
            AFWConst.MsgParam1: configID
        }
        result = self.__handleMessage(msg)
        return result[AFWConst.MsgResult]

    ### Private ###
    
    def __getConn(self):
        conn = self.__manager.GetClientConn(self.__guid)
        if conn is None:
            raise Exception("No connection for proxy " + self.__guid)
        return conn

    def __handleMessage(self, msg):
        conn = self.__getConn()
        msgZip, msgStr = AFWProxyUtil.CompressProxyMessage(msg)
        conn.sendall(msgZip)
        Debug("Send proxy client message: " + msgStr)
        result = conn.recv(AFWConst.MsgLength)
        resultDict, resultStr = AFWProxyUtil.DecompressProxyMessage(result)
        Debug("Recv proxy client result: " + resultStr)
        if AFWConst.MsgName not in resultDict or AFWConst.MsgResult not in resultDict or resultDict[AFWConst.MsgName] != msg[AFWConst.MsgName]:
            raise Exception("Message result is not returned: " + msg[AFWConst.MsgName])
        return resultDict
