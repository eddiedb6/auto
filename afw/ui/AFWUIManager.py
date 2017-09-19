import uuid

import AFWConst
from AFWLogger import *

### UI type import start ###
from AFWApp import AFWApp
from AFWAppRoot import AFWAppRoot
from AFWAppForm import AFWAppForm
from AFWAppSubForm import AFWAppSubForm
from AFWAppTab import AFWAppTab
from AFWAppTabPage import AFWAppTabPage
from AFWAppButton import AFWAppButton
from AFWAppCheckbox import AFWAppCheckbox
from AFWAppEditBox import AFWAppEditBox
from AFWWeb import AFWWeb
from AFWWebPage import AFWWebPage
from AFWWebElement import AFWWebElement
from AFWWebEditBox import AFWWebEditBox
from AFWWebLink import AFWWebLink
from AFWWebButton import AFWWebButton
from AFWWebURL import AFWWebURL
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
        return self.__findUI(name, None, AFWConst.AppForm)
    
    def OpenWebBrowser(self, name):
        return self.__findUI(name, None, AFWConst.UIWeb)

    def GetBreakTime(self):
        return self.__afw.BreakTime
    
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
        
        if parentUI is not None
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
                    Error("Create UI exception: " + config[AFWConst.Name])
                    return None
                if uiID is None:
                    Error("Failed to create UI: " + config[AFWConst.Name])
                    return None
            lastConfigID = configID

        ui = self.GetUI(uiID)
        if ui is not None and uiType is not None and ui.GetType() != uiType:
            Error("Found UI is not type of " + uiType + ": " + name)
            return None
        return ui

    def __isUIBound(self, configID):
        if configID in self.__uiPool:
            return true;
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
        parentConfig = self.GetConfig(parentConfigID)
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
        AFWConst.UIApp: lambda manager, config, parentConfig: AFWApp(manager, config, parentConfig),
        AFWConst.AppRoot: lambda manager, config, parentConfig: AFWAppRoot(manager, config, parentConfig),
        AFWConst.AppForm: lambda manager, config, parentConfig: AFWAppForm(manager, config, parentConfig),
        AFWConst.AppSubForm: lambda manager, config, parentConfig: AFWAppSubForm(manager, config, parentConfig),
        AFWConst.AppTab: lambda manager, config, parentConfig: AFWAppTab(manager, config, parentConfig),
        AFWConst.AppTabPage: lambda manager, config, parentConfig: AFWAppTabPage(manager, config, parentConfig),
        AFWConst.AppButton: lambda manager, config, parentConfig: AFWAppButton(manager, config, parentConfig),
        AFWConst.AppCheckbox: lambda manager, config, parentConfig: AFWAppCheckbox(manager, config, parentConfig),
        AFWConst.AppEditBox: lambda manager, config, parentConfig: AFWAppEditBox(manager, config, parentConfig),
        AFWConst.UIWeb: lambda manager, config, parentConfig: AFWWeb(manager, config, parentConfig),
        AFWConst.WebPage: lambda manager, config, parentConfig: AFWWebPage(manager, config, parentConfig),
        AFWConst.WebElement: lambda manager, config, parentConfig: AFWWebElement(manager, config, parentConfig),
        AFWConst.WebEditBox: lambda manager, config, parentConfig: AFWWebEditBox(manager, config, parentConfig),
        AFWConst.WebLink: lambda manager, config, parentConfig: AFWWebLink(manager, config, parentConfig),
        AFWConst.WebButton: lambda manager, config, parentConfig: AFWWebButton(manager, config, parentConfig),
        AFWConst.WebURL: lambda manager, config, parentConfig: AFWWebURL(manager, config, parentConfig),
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

