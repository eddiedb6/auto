import sys
import os
import logging
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../schema"))

import AFWConst
from AFWLogger import *
from SchemaChecker import SchemaChecker

class AFW:
    def __init__(self):
        self.__logLevel = logging.INFO
        self.__breakTime = 50 # ms
        self.__config = None

    def Load(self, path):
        try:
            if not self.__checkConfig(path):
                Error("Configuration is not correct format")
                return False
            configFile = open(path)
            configContent = configFile.read()
            self.__config = eval(configContent)
        except:
            Error(str(sys.exc_info()[0]) + ": " + str(sys.exc_info()[1]))
            return False
        return True

    def Execute(self):
        try:
            print "TODO, execute"
        except:
            Error(str(sys.exc_info()[0]) + ": " + str(sys.exc_info()[1]))
            return False
        return True

    @property
    def LogLevel(self):
        return self.__logLevel

    @LogLevel.setter
    def LogLevel(self, value):
        self.__logLevel = value

    @LogLevel.deleter
    def LogLevel(self):
        del self.__logLevel

    @property
    def BreakTime(self):
        return self.__breakTime

    @BreakTime.setter
    def BreakTime(self, value):
        self.__breakTime = value

    @BreakTime.deleter
    def BreakTime(self):
        del self.__breakTime

    def __checkConfig(self, path):
        if not os.path.exists(path):
            Error("Configure file path is not correct")
            return False
        afwPath = os.path.split(os.path.realpath(__file__))[0]
        schemaPath = os.path.join(afwPath, "AFWSchema.py")
        constPath = os.path.join(afwPath, "AFWConst.py")
        checker = SchemaChecker(path, schemaPath, constPath)
        return checker.Check()
