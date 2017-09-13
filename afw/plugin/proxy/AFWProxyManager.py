import socket
import subprocess
import uuid
import sys
import os
import logging

import AFWConst
from AFWLogger import *
from AFWProxyMsgUtil import *
from AFWProxyThread import AFWProxyThread
from AFWProxy import AFWProxy

class AFWProxyManager:
    def __init__(self):
        self.__config = None

    def GetClientConn(self, guid):
        if guid in AFWProxyManager.__clientConn:
            return AFWProxyManager.__clientConn[guid]
        return None

    def CreateProxy(self, config):
        proxyType = config[AFWConst.ProxyType]
        if proxyType == AFWConst.ProxyLocal:
            return self.__createLocalProxy(config)
        elif proxyType == AFWConst.ProxyRemote:
            # TBD for remote proxy
            pass
        else:
            raise Exception("Wrong proxy type: " + proxyType)
        return None

    def SetLogLevel(self, level):
        AFWProxyManager.__logLevel = level

    def Destroy(self):
        self.__closeProxies()
        self.__closeClients()
        self.__closeSocketHost()
        self.__closeThreads()
        
    def __createLocalProxy(self, config):
        if AFWProxyManager.__socket is None:
            self.__startSocketHost()
        guid = str(uuid.uuid1())
        self.__config = config
        self.__config[AFWConst.ProxyGUID] = guid
        threadRegister = AFWProxyThread("Regisger Client " + guid, self.__registerClient)
        threadRegister.start()
        threadStart = AFWProxyThread("Startup Client " + guid, self.__startClient)
        AFWProxyManager.__threads.append(threadStart)
        threadStart.start()
        
        # Wait client register finished so following action based on it will not failed
        threadRegister.join()
        
        proxy = AFWProxy(guid, self)
        if guid in AFWProxyManager.__proxy:
            raise Exception("Proxy already there for GUID: " + guid)
        AFWProxyManager.__proxy[guid] = proxy
        return proxy

    def __registerClient(self):
        conn, addr = AFWProxyManager.__socket.accept()
        msg = conn.recv(AFWConst.MsgLength)
        msgDict, msgStr = DecompressProxyMessage(msg)
        if msgDict[AFWConst.MsgName] != AFWConst.MsgNameRegisterClient or AFWConst.MsgParam1 not in msgDict:
            raise Exception("Wrong message when register client: " + self.__config[AFWConst.ProxyGUID])
        guid = msgDict[AFWConst.MsgParam1]
        Info("Client connected: " + str(addr) + ", " + guid)
        if guid in AFWProxyManager.__clientConn:
            raise Exception("Connection already there for GUID: " + guid)
        AFWProxyManager.__clientConn[guid] = conn
                                    
    def __startClient(self):
        paramConfig = []
        paramConfig.append(self.__config[AFWConst.ProxyLauncher])
        if self.__config[AFWConst.ProxyType] == AFWConst.ProxyLocal:
            proxyMainFile = os.path.join(os.path.split(os.path.realpath(__file__))[0], AFWConst.ProxyLocalEntry)
            paramConfig.append(proxyMainFile)
        else:
            raise Exception("Proxy type not supported yet")
        paramConfig.append(self.__config[AFWConst.PluginName])
        paramConfig.append(self.__config[AFWConst.ProxyGUID])
        paramConfig.append(str(AFWProxyManager.__logLevel))
        subprocess.call(paramConfig, stdout = sys.stdout)

    def __closeClients(self):
        for key in AFWProxyManager.__clientConn:
            conn = AFWProxyManager.__clientConn[key]
            conn.close()
        AFWProxyManager.__clientConn.clear()
        
    def __startSocketHost(self):
        HOST = ''
        PORT = AFWConst.ProxyHostPort
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(1)
        AFWProxyManager.__socket = s
        Info("Start proxy host successfully")

    def __closeSocketHost(self):
        if AFWProxyManager.__socket is not None:
            AFWProxyManager.__socket.close()
            AFWProxyManager.__socket = None
            Info("Stop proxy host successfully")

    def __closeProxies(self):
        for key in AFWProxyManager.__proxy:
            AFWProxyManager.__proxy[key].Close()
        AFWProxyManager.__proxy.clear()

    def __closeThreads(self):
        for thread in AFWProxyManager.__threads:
            thread.join()
        AFWProxyManager.__threads = []
        
    __socket = None
    __threads = []
    __clientConn = {}
    __proxy = {}
    __logLevel = logging.DEBUG
    
