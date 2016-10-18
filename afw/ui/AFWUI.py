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

    def GetChildrenCount(self):
        if AFWConst.SubUI in self.__config:
            return len(self.__config[AFWConst.SubUI])
        return 0

    def GetChild(self, index):
        if index < 0:
            return None
        if AFWConst.SubUI in self.__config and len(self.__config[AFWConst.SubUI]) > index:
            return self.__config[AFWConst.SubUI][index]
        return None

    def GetNativeUI(self):
        return None

    def IsEditable(self):
        return False

    def IsEnabled(self):
        return True

    ### Operations ###

    def SetFocus(self):
        return self._plugin.SetFocus(self)

    def PressKey(self, key):
        return self._plugin.PressKey(self, key)

    def ReleaseKey(self, key):
        return self._plugin.ReleaseKey(self, key)

    def InputText(self, text):
        Debug("Input text: " + text)
        if not self.IsEditable():
            return False
        for char in text:
            key, needShift = AFWUIHelper.GetKeyFromChar(char)
            if key is None:
                continue
            if needShift:
                self.PressKey(AFWConst.AFWKeyShift)
            self.PressKey(key)
            self.ReleaseKey(key)
            if needShift:
                self.ReleaseKey(AFWConst.AFWKeyShift)
        return True

    def GetText(self):
        return None

    def Click(self):
        return False