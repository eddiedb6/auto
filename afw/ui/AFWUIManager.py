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
        self.__config = config

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
        if parentUI is not None and parentUI.GetConfig() not in configPath:
            Warning("UI is not under " + parentUI.GetName() + ": " + name)
            return None
        ui = None
        lastConfig = None
        for config in configPath:
            if not self.__isUIBound(config):
                try:
                    config[AFWConst.UIObj] = self.__createUI(config, lastConfig)
                except:
                    Error("Create UI exception: " + config[AFWConst.Name])
                    return None
                if config[AFWConst.UIObj] is None:
                    Error("Failed to create UI: " + config[AFWConst.Name])
                    return None
            lastConfig = config
        ui = configPath.pop()[AFWConst.UIObj]
        if ui is not None and uiType is not None and ui.GetType() != uiType:
            Error("Found UI is not type of " + uiType + ": " + name)
            return None
        return ui

    def __isUIBound(self, config):
        if AFWConst.UIObj in config and config[AFWConst.UIObj] is not None:
            return True
        elif config[AFWConst.Type] == AFWConst.UIRoot:
            # UIRoot will not be bound to any native object
            return True
        return False
        
    def __findConfig(self, name):
        configPath = []
        result = self.__findConfigImpl(name, self.__config[AFWConst.UI], configPath)
        if not result:
            Warning("Could not find UI config: " + name)
        else:
            Debug("Find UI config: " + name)
        return result, configPath
    
    def __findConfigImpl(self, name, node, configPath):
        if node[AFWConst.Name] == name:
            # Find element node
            configPath.append(node)
            return True
        if AFWConst.SubUI not in node:
            # Element not match and no sub node, so not find
            return False
        for subNode in node[AFWConst.SubUI]:
            configPath.append(node)
            if self.__findConfigImpl(name, subNode, configPath):
                # Find element in sub node
                return True
            else:
                # Could not find in sub node, pop stack
                configPath.pop()
        return False

    def __createUI(self, config, parentConfig):
        uiType = config[AFWConst.Type]
        if uiType in AFWUIManager.__uiFactory:
            return AFWUIManager.__uiFactory[uiType](self, config, parentConfig)
        Error("UI type is not defined in ui factory: " + config[AFWConst.Type])
        return None

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

