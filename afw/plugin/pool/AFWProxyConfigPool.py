from AFWConfigPool import AFWConfigPool
import AFWProxyUtil
import AFWConst

class AFWProxyConfigPool(AFWConfigPool):
    def __init__(self, socket):
        self.__socket = socket
        self.__configPool = {}

    ### Implements AFWConfigPool ###
    
    def GetConfig(self, configID):
        if configID in self.__configPool:
            return self.__configPool[configID]
        # Send request
        msg = {
            AFWConst.MsgName: AFWConst.MsgNameGetConfig,
            AFWConst.MsgParam1: configID            
        }
        msgZip, msgStr = AFWProxyUtil.CompressProxyMessage(msg)
        self.__socket.sendall(msgZip)
        Debug("Send get config message: " + msgStr)
        # Get config
        result = s.recv(AFWConst.MsgLength)
        resultDict, resultStr = AFWProxyUtil.DecompressProxyMessage(result)
        Debug("Recv get config result: " + resultStr)
        if AFWConst.MsgName not in resultDict or AFWConst.MsgResult not in resultDict or resultDict[AFWConst.MsgName] != AFWConst.MsgNameGetConfig:
            raise Exception("Get config result is not match: " + msgName)
        config = resultDict[AFWConst.MsgResult]
        self.__configPool[configID] = config
        return config

