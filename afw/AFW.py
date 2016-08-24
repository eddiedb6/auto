import sys
import os
import logging
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../schema"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "ui"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "plugin"))
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "."))

import AFWConst
from AFWLogger import *
from SchemaChecker import SchemaChecker
from AFWUIManager import AFWUIManager

class AFW:
    def __init__(self):
        self.__logLevel = logging.INFO
        self.__breakTime = 50 # ms
        self.__config = None
        self.__configPath = None
        self.__uiManager = None

    def Load(self, path):
        try:
            logging.basicConfig(level=self.__logLevel)
            result, self.__config = self.__checkConfig(path)
            if not result:
                Error("Configuration is not correct format")
                return False
        except:
            Error(str(sys.exc_info()[0]) + ": " + str(sys.exc_info()[1]))
            return False
        self.__configPath = path
        self.__uiManager = AFWUIManager(self.__config)
        return True

    def Execute(self):
        try:
            if not self.__configPath or not self.__config:
                Error("Could not execute without correct configuration")
                return False
            return self.__executeAction(self.__config[AFWConst.Action])
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
            return False, None
        afwPath = os.path.split(os.path.realpath(__file__))[0]
        schemaPath = os.path.join(afwPath, "AFWSchema.py")
        constPath = os.path.join(afwPath, "AFWConst.py")
        checker = SchemaChecker(path, schemaPath, constPath)
        return checker.Check()

    def __executeAction(self, action):
        if AFWConst.Script in action:
            path = os.path.join(os.path.split(os.path.abspath(self.__configPath))[0], action[AFWConst.Script])
            if not os.path.exists(path):
                Error("Action script does not exist: " + action[AFWConst.Script])
                return False
            afw = self.__uiManager
            execfile(path)
        if AFWConst.SubAction in action:
            for subAction in action[AFWConst.SubAction]:
                if not self.__executeAction(subAction):
                    return False
        return True
