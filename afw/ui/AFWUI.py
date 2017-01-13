import time

import AFWConst
import AFWUIHelper

from AFWLogger import *

class AFWUI:
    def __init__(self, manager, config, parentConfig):
        self.__manager = manager
        self.__config = config
        self.__parentConfig = parentConfig
        self._plugin = None
        self._native = None
        if parentConfig is not None:
            if AFWConst.UIObj in parentConfig and parentConfig[AFWConst.UIObj] is not None:
                self._plugin = parentConfig[AFWConst.UIObj]._plugin
            else:
                raise Exception("Parent UI is not bound: " + parentConfig[AFWConst.Name])
        if AFWConst.BreakTime in config:
            time.sleep(config[AFWConst.BreakTime] / 1000)
        else:
            time.sleep(self.__manager.GetBreakTime() / 1000)

    ### Properties ###

    def GetType(self):
        return self.__config[AFWConst.Type]

    def GetName(self):
        return self.__config[AFWConst.Name]

    def GetConfig(self):
        return self.__config

    def GetParentConfig(self):
        return self.__parentConfig

    def GetChildConfigCount(self):
        if AFWConst.SubUI in self.__config:
            return len(self.__config[AFWConst.SubUI])
        return 0

    def GetChildConfig(self, index):
        if index < 0:
            return None
        if AFWConst.SubUI in self.__config and len(self.__config[AFWConst.SubUI]) > index:
            return self.__config[AFWConst.SubUI][index]
        return None

    def GetNativeUI(self):
        return self._native

    ### Properties and Operations when bound ###

    def TryToFindSubUI(self, name):
        return self.__manager.TryToFindUI(name, self)
        
    def FindSubUI(self, name):
        ui = self.__manager.TryToFindUI(name, self)
        if ui is  None:
            msg = "Failed to find UI: " + name
            Warning(msg)
            raise Exception(msg)
        return ui

    def SetFocus(self):
        return self._plugin.SetFocus(self)

    def IsEnabled(self):
        return self._plugin.IsEnabled(self)

    def PressKey(self, key):
        return self._plugin.PressKey(self, key)

    def ReleaseKey(self, key):
        return self._plugin.ReleaseKey(self, key)

    def InputText(self, text):
        return False

    def GetText(self):
        return self._plugin.GetText(self)
