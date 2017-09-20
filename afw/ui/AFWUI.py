import time

import AFWConst
from AFWLogger import *

class AFWUI:
    def __init__(self, manager, configID, parentConfigID):
        self.__manager = manager
        self._id = configID
        self._parentId = parentConfigID
        self._plugin = None
        if parentConfigID is not None:
            parentConfig = self.GetParentConfig()
            parentUI = manager.GetUI(parentConfigID)
            if parentUI is not None:
                self._plugin = parentUI._plugin
            else:
                raise Exception("Parent UI is not bound: " + parentConfig[AFWConst.Name])
        config = self.GetConfig()
        if AFWConst.BreakTime in config:
            time.sleep(config[AFWConst.BreakTime] / 1000)
        else:
            time.sleep(self.__manager.GetBreakTime() / 1000)

    ### Properties ###

    def GetID(self):
        return self._id

    def GetType(self):
        return self.GetConfig()[AFWConst.Type]

    def GetName(self):
        return self.GetConfig()[AFWConst.Name]

    def GetConfig(self):
        return self.__manager.GetConfig(self._id)

    def GetParentConfig(self):
        return self.__manager.GetConfig(self._parentId)

    def GetChildConfigCount(self):
        config = self.GetConfig()
        if AFWConst.SubUI in config:
            return len(config[AFWConst.SubUI])
        return 0

    def GetChildConfig(self, index):
        if index < 0:
            return None
        config = self.GetConfig()
        if AFWConst.SubUI in config and len(config[AFWConst.SubUI]) > index:
            subConfigID = config[AFWConst.SubUI][index]
            return self.__manager.GetConfig(subConfigID)
        return None

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
        return self._plugin.SetFocus(self._id)

    def IsEnabled(self):
        return self._plugin.IsEnabled(self._id)

    def PressKey(self, key):
        return self._plugin.PressKey(self._id, key)

    def ReleaseKey(self, key):
        return self._plugin.ReleaseKey(self._id, key)

    def InputText(self, text):
        return False

    def GetText(self):
        return self._plugin.GetText(self._id)
