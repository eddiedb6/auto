from AFWConfigPool import AFWConfigPool
from AFWLogger import *
import AFWProxyUtil
import AFWConst

class AFWProxyConfigPool(AFWConfigPool):
    def __init__(self, socket):
        self.__socket = socket
        self.__configPool = {}

    ### Implements AFWConfigPool ###

    def GetConfig(self, configID):
        if self.GetConfigDirty():
            # Clear all cache on dirty
            self.__configPool = {}
        elif configID in self.__configPool:
            return self.__configPool[configID]

        # Send request
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetConfig,
            AFWConst.MsgParam1: configID            
        }
        msgZip, msgStr = AFWProxyUtil.CompressProxyMessage(msg)
        Debug("[Local Client] Send proxy host get config request: " + msgStr)
        self.__socket.sendall(msgZip)
        # Get config
        result = self.__socket.recv(AFWConst.MsgLength)
        resultDict, resultStr = AFWProxyUtil.DecompressProxyMessage(result)
        Debug("[Local Client] Recv proxy host get config result: " + resultStr)
        if AFWConst.MsgName not in resultDict or AFWConst.MsgResult not in resultDict or resultDict[AFWConst.MsgName] != AFWConst.MsgNameGetConfig:
            raise Exception("Get config result is not match: " + msgName)
        config = resultDict[AFWConst.MsgResult]
        self.__configPool[configID] = config
        return config

    def GetConfigDirty(self):
        # Send request
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameCheckConfigDirty
        }
        msgZip, msgStr = AFWProxyUtil.CompressProxyMessage(msg)
        Debug("[Local Client] Send proxy host check config dirty: " + msgStr)
        self.__socket.sendall(msgZip)
        # Get dirty result
        result = self.__socket.recv(AFWConst.MsgLength)
        resultDict, resultStr = AFWProxyUtil.DecompressProxyMessage(result)
        Debug("[Local Client] Recv proxy host check config dirty result: " + resultStr)
        if AFWConst.MsgName not in resultDict or AFWConst.MsgResult not in resultDict or resultDict[AFWConst.MsgName] != AFWConst.MsgNameCheckConfigDirty:
            raise Exception("Check config dirty result is not match: " + msgName)
        return resultDict[AFWConst.MsgResult]
