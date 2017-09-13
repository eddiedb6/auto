import pickle
import zlib

def __generateMsgStr(msg):
    msgStr = str(msg)
    if len(msgStr) > 128:
        msgStr = msgStr[0:127] + " ..."
    return msgStr
    
def CompressProxyMessage(msg):
    msgDump = pickle.dumps(msg)
    msgZip = zlib.compress(msgDump)
    msgStr = __generateMsgStr(msg)
    return msgZip, msgStr

def DecompressProxyMessage(msg):
    msgDump = zlib.decompress(msg)
    msgResult = pickle.loads(msgDump)
    msgStr = __generateMsgStr(msgResult)
    return msgResult, msgStr
