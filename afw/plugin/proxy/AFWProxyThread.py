import threading

from AFWLogger import *

class AFWProxyThread(threading.Thread):
    def __init__(self, name, func):
        threading.Thread.__init__(self)
        self.__name = name
        self.__func = func

    def run(self):
        Info("Thread start: " + self.__name)
        self.__func()
        Info("Thread end: " + self.__name)

        
