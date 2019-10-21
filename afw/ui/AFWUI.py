import time

import AFWConst
from AFWLogger import *
from AFWAbility import *

class AFWUI:
    def __init__(self, manager, configID, parentConfigID):
        self.__manager = manager
        self.__id = configID
        self.__parentId = parentConfigID
        self._plugin = None
        self._abilityObj = AFWAbility(None)
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
        return self.__id

    def GetParentID(self):
        return self.__parentId

    def GetChildID(self, index):
        if index < 0:
            return None
        config = self.GetConfig()
        if AFWConst.SubUI in config and len(config[AFWConst.SubUI]) > index:
            subConfigID = config[AFWConst.SubUI][index]
            return subConfigID
        return None

    def GetConfig(self):
        return self.__manager.GetConfig(self.__id)

    def GetParentConfig(self):
        return self.__manager.GetConfig(self.__parentId)

    def GetChildConfig(self, index):
        childID = self.GetChildID(index)
        if childID is not None:
            return self.__manager.GetConfig(childID)    
        return None

    def GetChildCount(self):
        config = self.GetConfig()
        if AFWConst.SubUI in config:
            return len(config[AFWConst.SubUI])
        return 0

    def GetType(self):
        return self.GetConfig()[AFWConst.Type]

    def GetName(self):
        return self.GetConfig()[AFWConst.Name]

    def GetAbility(self):
        return AFWAbilityChecker(self._abilityObj)

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

    def Dump(self):
        isDumped = True
        childrenCount = self.GetChildCount()
        # Dump children first
        for index in range(0, childrenCount):
            childID = self.GetChildID(index)
            childUI = None
            try:
                childUI = self.__manager.GetUI(childID)
            except:
                childUI = None
            if childUI is not None:
                isDumped = isDumped & childUI.Dump()
        # Now dump itself
        isDumped = isDumped & self.__manager.DumpUI(self.__id)
        if self._plugin is not None:
            isDumped = isDumped & self._plugin.DumpUI(self.__id)
        return isDumped

    def SetFocus(self):
        return self._plugin.SetFocus(self.__id)

    def IsEnabled(self):
        return self._plugin.IsEnabled(self.__id)

    def PressKey(self, key):
        return self._plugin.PressKey(self.__id, key)

    def ReleaseKey(self, key):
        return self._plugin.ReleaseKey(self.__id, key)

    def GetText(self):
        return self._plugin.GetText(self.__id)
