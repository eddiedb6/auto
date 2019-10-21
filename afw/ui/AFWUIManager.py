import sys
import uuid

import AFWConst
from AFWLogger import *

### UI type import start ###
from AFWApp import AFWApp
from AFWDesktop import AFWDesktop
from AFWForm import AFWForm
from AFWAppDialog import AFWAppDialog
from AFWAppTab import AFWAppTab
from AFWAppTabPage import AFWAppTabPage
from AFWCheckableUI import AFWCheckableUI
from AFWClickableUI import AFWClickableUI
from AFWSelectableUI import AFWSelectableUI
from AFWInputableUI import AFWInputableUI
from AFWBrowser import AFWBrowser
from AFWWebEntry import AFWWebEntry
from AFWWebLink import AFWWebLink
from AFWWebPage import AFWWebPage
from AFWWebTable import AFWWebTable
### UI type import end ###

class AFWUIManager:
    def __init__(self, afw, config):
        self.__afw = afw
        self.__configPool = {}
        self.__uiPool = {}
        self.__configEntryID = self.__fillConfigPool(config[AFWConst.UI])

    def GetConfig(self, configID):
        if configID not in self.__configPool:
            raise Exception("No config ID exsists: " + configID)
        return self.__configPool[configID]

    def GetUI(self, uiID):
        if uiID not in self.__uiPool:
            raise Exception("No ui ID exsists: " + uiID)
        return self.__uiPool[uiID]

    def TryToFindUI(self, name, parentUI):
        return self.__tryToFindUI(name, parentUI, None)
    
    def StartApp(self, name):
        return self.__findUI(name, None, AFWConst.UIApp)

    def FindWinForm(self, name):
        return self.__findUI(name, None, AFWConst.UIForm)
    
    def OpenWebBrowser(self, name):
        return self.__findUI(name, None, AFWConst.UIBrowser)

    def GetBreakTime(self):
        return self.__afw.BreakTime

    def DumpUI(self, uiID):
        if uiID in self.__uiPool:
            del self.__uiPool[uiID] # This will delete both key and value
            return True
        return False
    
    ### Private ###

    def __findUI(self, name, parentUI, uiType):
        ui = self.__tryToFindUI(name, parentUI, uiType)
        if ui is None:
            raise Exception("Find UI failed!")
        return ui

    def __tryToFindUI(self, name, parentUI, uiType):
        result, configPath = self.__findConfig(name)
        if not result:
            return None

        if parentUI is not None:
            parentConfigID = parentUI.GetID()
            if parentConfigID not in configPath:
                Warning("UI is not under " + parentUI.GetName() + ": " + name)
                return None

        ui = None
        uiID = None
        lastConfigID = None
        for configID in configPath:
            if not self.__isUIBound(configID):
                config = self.GetConfig(configID)
                try:
                    uiID = self.__createUI(configID, lastConfigID)
                except:
                    Error("Exception: create UI " + config[AFWConst.Name] + "\n" + str(sys.exc_info()[0]) + "\n" + str(sys.exc_info()[1]))
                    return None
                if uiID is None:
                    Error("Failed to create UI: " + config[AFWConst.Name])
                    return None
            else:
                 uiID = configID   
            lastConfigID = configID

        ui = self.GetUI(uiID)
        if ui is not None and uiType is not None and ui.GetType() != uiType:
            Error("Found UI is not type of " + uiType + ": " + name)
            return None
        return ui

    def __isUIBound(self, configID):
        if configID in self.__uiPool:
            return True;
        config = self.GetConfig(configID)
        if config[AFWConst.Type] == AFWConst.UIRoot:
            # UIRoot will not be bound to any native object
            return True
        return False
        
    def __findConfig(self, name):
        configPath = []
        result = self.__findConfigImpl(name, self.__configEntryID, configPath)
        if not result:
            Warning("Could not find UI config: " + name)
        else:
            Debug("Find UI config: " + name)
        return result, configPath
    
    def __findConfigImpl(self, name, configID, configPath):
        config = self.GetConfig(configID)
        if config[AFWConst.Name] == name:
            # Find element config
            configPath.append(configID)
            return True
        if AFWConst.SubUI not in config:
            # Element not match and no sub config, so not find
            return False
        for subConfigID in config[AFWConst.SubUI]:
            configPath.append(configID)
            if self.__findConfigImpl(name, subConfigID, configPath):
                # Find element in sub config
                return True
            else:
                # Could not find in sub config, pop stack
                configPath.pop()
        return False

    def __createUI(self, configID, parentConfigID):
        if configID in self.__uiPool:
            raise Exception("UI guid is already in pool")
        config = self.GetConfig(configID)
        uiType = config[AFWConst.Type]
        if uiType in AFWUIManager.__uiFactory:
            uiObj = AFWUIManager.__uiFactory[uiType](self, configID, parentConfigID)
            self.__uiPool[configID] = uiObj
            return configID
        Error("UI type is not defined in ui factory: " + config[AFWConst.Type])
        return None

    def __fillConfigPool(self, config):
        guid = str(uuid.uuid1())
        if guid in self.__configPool:
            raise Exception("Config guid is already in pool")
        self.__configPool[guid] = config
        
        if AFWConst.SubUI in config:
            children = config[AFWConst.SubUI]
            for i in range(0, len(children)):
                children[i] = self.__fillConfigPool(children[i])
                
        return guid

    __uiFactory = {
### UI type factory initialize start ###
        AFWConst.UIApp: lambda manager, configID, parentConfigID: AFWApp(manager, configID, parentConfigID),
        AFWConst.UIDesktop: lambda manager, configID, parentConfigID: AFWDesktop(manager, configID, parentConfigID),
        AFWConst.UIForm: lambda manager, configID, parentConfigID: AFWForm(manager, configID, parentConfigID),
        AFWConst.UIAppDialog: lambda manager, configID, parentConfigID: AFWAppDialog(manager, configID, parentConfigID),
        AFWConst.UIAppTab: lambda manager, configID, parentConfigID: AFWAppTab(manager, configID, parentConfigID),
        AFWConst.UIAppTabPage: lambda manager, configID, parentConfigID: AFWAppTabPage(manager, configID, parentConfigID),
        AFWConst.UIClickable: lambda manager, configID, parentConfigID: AFWClickableUI(manager, configID, parentConfigID),
        AFWConst.UISelectable: lambda manager, configID, parentConfigID: AFWSelectableUI(manager, configID, parentConfigID),
        AFWConst.UIInputable: lambda manager, configID, parentConfigID: AFWInputableUI(manager, configID, parentConfigID),
        AFWConst.UIBrowser: lambda manager, configID, parentConfigID: AFWBrowser(manager, configID, parentConfigID),
        AFWConst.UIWebPage: lambda manager, configID, parentConfigID: AFWWebPage(manager, configID, parentConfigID),
        AFWConst.UIWebTable: lambda manager, configID, parentConfigID: AFWWebTable(manager, configID, parentConfigID),
        AFWConst.UIWebEntry: lambda manager, configID, parentConfigID: AFWWebEntry(manager, configID, parentConfigID),
        AFWConst.UIWebLink: lambda manager, configID, parentConfigID: AFWWebLink(manager, configID, parentConfigID),
### UI type factory initialize end ###
        "Dummy": "Dummy"
    }

# There are APIs in AFWUIManager should not be exposed to user script
# So wrapper the APIs should be exposed in AFWUIManagerWrapper for user script
class AFWUIManagerWrapper:
    def __init__(self, afw, config):
        self.__manager = AFWUIManager(afw, config)

    def StartApp(self, name):
        return self.__manager.StartApp(name)

    def FindWinForm(self, name):
        return self.__manager.FindWinForm(name)
    
    def OpenWebBrowser(self, name):
        return self.__manager.OpenWebBrowser(name)

