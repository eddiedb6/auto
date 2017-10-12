import AFWConst
import AFWProxyUtil
from AFWLogger import *

class AFWProxy:
    def __init__(self, guid, manager, configPool):
        self.__guid = guid
        self.__manager = manager
        self.__configPool = configPool

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

    def Select(self, uiID, itemValue):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameSelect,
            AFWConst.MsgParam1: uiID,
            AFWConst.MsgParam2: itemValue
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

    def GetCellText(self, uiID, row, column):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetCellText,
            AFWConst.MsgParam1: uiID,
            AFWConst.MsgParam2: row,
            AFWConst.MsgParam3: column
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

    def OpenWebURL(self, browserID, url, configID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameOpenWebURL,
            AFWConst.MsgParam1: browserID,
            AFWConst.MsgParam2: url,
            AFWConst.MsgParam3: configID
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

    def GetWebPage(self, browserID, configID):
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetWebPage,
            AFWConst.MsgParam1: browserID,
            AFWConst.MsgParam2: configID
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

    def __sendConfig(self, configID):
        conn = self.__getConn()
        config = self.__configPool.GetConfig(configID)
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetConfig,
            AFWConst.MsgResult: config
        }
        msgZip, msgStr = AFWProxyUtil.CompressProxyMessage(msg)
        Debug("Send proxy client get config result: " + msgStr)
        conn.sendall(msgZip)

    def __handleMessage(self, msg):
        conn = self.__getConn()
        msgZip, msgStr = AFWProxyUtil.CompressProxyMessage(msg)
        Debug("Send proxy client message: " + msgStr)
        conn.sendall(msgZip)
        while True:
            result = conn.recv(AFWConst.MsgLength)
            resultDict, resultStr = AFWProxyUtil.DecompressProxyMessage(result)
            if AFWConst.MsgName not in resultDict:
                raise Exception("Message result name is not defined: " + msg[AFWConst.MsgName])
            if resultDict[AFWConst.MsgName] == AFWConst.MsgNameGetConfig:
                # It's not result but new requst to get config
                Debug("Recv proxy client get config request: " + resultStr)
                if AFWConst.MsgParam1 not in resultDict:
                    raise Exception("Config ID is not defined in request")
                configID = resultDict[AFWConst.MsgParam1]
                self.__sendConfig(configID)
            else:
                # Now it's request result returned
                Debug("Recv proxy client result: " + resultStr)
                if AFWConst.MsgResult not in resultDict:
                    raise Exception("Message result is not defined: " + msg[AFWConst.MsgName])
                if resultDict[AFWConst.MsgName] != msg[AFWConst.MsgName]:
                    raise Exception("Message result name is not match: " + msg[AFWConst.MsgName])
                return resultDict
        return None
