import time
import copy

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

    def IsDynamic(self):
        config = self.GetConfig()
        if AFWConst.IsDynamic in config and config[AFWConst.IsDynamic]:
            return True
        return False

    def GetDynamicUIName(self, name, index):
        return name + "_" + str(index)

    ### Properties and Operations when bound ###

    def TryToFindSubUI(self, name):
        return self.__manager.TryToFindUI(name, self)

    def FindSubUI(self, name):
        ui = self.__manager.TryToFindUI(name, self)
        if ui is None:
            msg = "Failed to find UI: " + name
            Warning(msg)
            raise Exception(msg)
        return ui

    def TryToFindDynamicSubUI(self, config):
        self.DumpDynamicSubUI()

        items = []
        count = self._plugin.GetDynamicElement(self.GetID(), config)
        if count <= 0:
            Warning("Find NO dynamic UI: " + config[AFWConst.Name])
        for i in range(0, count):
            iConfig = copy.deepcopy(config)
            iConfig[AFWConst.UICacheIndex] = i
            self.__allocateDynamicUIConfig(i, iConfig)
            self.__manager.AddDynamicUI(self.GetID(), iConfig)

            # This call is to bind native ui immediatly
            # Because the item native ui is cached in plugin
            # And it will be flushed on next call of GetItems
            item = self.__manager.TryToFindUI(iConfig[AFWConst.Name], self)
            if item is not None:
                items.append(item)
            else:
                Warning("Failed to find dynamic UI: " + iConfig[AFWConst.Name])

        return items

    def Dump(self):
        return self.__doDump(False)

    def DumpSubUI(self):
        return self.__doDumpSubUI(False)

    def DumpDynamic(self):
        return self.__doDump(True)

    def DumpDynamicSubUI(self):
        return self.__doDumpSubUI(True)

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

    def GetAttribute(self, name):
        return self._plugin.GetAttribute(self.__id, name)

    def ScrollHere(self):
        return self._plugin.ScrollTo(self.__id)

    ### Private ###

    def __allocateDynamicUIConfig(self, index, config):
        config[AFWConst.Name] = self.GetDynamicUIName(config[AFWConst.Name], index)
        config[AFWConst.IsDynamic] = True
        if AFWConst.SubUI not in config:
            return
        for subConfig in config[AFWConst.SubUI]:
            self.__allocateDynamicUIConfig(index, subConfig)

    def __doDumpSubUI(self, isDeleteDynamic):
        isDumped = True
        childrenCount = self.GetChildCount()
        for i in range(0, childrenCount):
            # Iterate from the last because there will be no impact when delete during loop
            index = childrenCount - 1 - i
            childID = self.GetChildID(index)
            childUI = None
            isChildDelete = False
            try:
                childUI = self.__manager.GetUI(childID)
            except:
                childUI = None
            if childUI is not None:
                if isDeleteDynamic:
                    isDumped = isDumped & childUI.DumpDynamicSubUI()
                    isChildDelete = childUI.IsDynamic()
                else:
                    isDumped = isDumped & childUI.DumpSubUI()
            if isChildDelete:
                isDumped = isDumped & self.__manager.DumpDynamicUI(childID)
                del self.GetConfig()[AFWConst.SubUI][index]
            else:
                isDumped = isDumped & self.__manager.DumpUI(childID)
            if self._plugin is not None:
                isDumped = isDumped & self._plugin.DumpUI(childID)
        return isDumped

    def __doDump(self, isDeleteDynamic):
        if not self.__doDumpSubUI(isDeleteDynamic):
            return False
        isDumped = False
        if isDeleteDynamic and self.IsDynamic():
            isDumped = self.__manager.DumpDynamicUI(self.GetID())
        else:
            idDumped = self.__manager.DumpUI(self.GetID())
        if self._plugin is not None:
            isDumped = isDumped & self._plugin.DumpUI(self.GetID())
        return isDumped
