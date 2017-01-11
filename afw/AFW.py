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
from AFWUIManager import AFWUIManagerWrapper

class AFW:
    def __init__(self):
        self.__logLevel = logging.INFO
        self.__breakTime = 50 # ms
        self.__config = None
        self.__configPath = None
        self.__uiManager = None

    def Load(self, path):
        try:
            # Logging level must be set before any log function is called
            # Otherwise there will be no logging
            logging.basicConfig(level = self.LogLevel)

            Info("Start configuration loading")
            result, self.__config = self.__checkConfig(path)
            if result:
                Info("Load configuration successfully")
            else:
                Error("Load configuration failed: configuration is not correct format")
                return False
        except:
            Error("Exception for config loading")
            return False
        self.__configPath = path
        self.__uiManager = AFWUIManagerWrapper(self, self.__config)
        return True

    def Execute(self):
        try:
            Info("Start execute script")
            if self.__configPath is None or self.__config is None:
                Error("Could not execute without correct configuration")
                return False
            result = self.__executeAction(self.__config[AFWConst.Action])
            if result:
                Info("Execute scripts successfuly")
            else:
                Error("Execute scripts failed")
        except:
            Error("Exception for script execution")
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
