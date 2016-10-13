import AFWConst
from AFWLogger import *

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

class AFWUIManager:
    def __init__(self, afw, config):
        self.__afw = afw
        self.__config = config

    def FindUI(self, name):
        ui = self.TryToFindUI(name)
        if ui is None:
            Error("Find UI failed: " + name)
            raise Exception("Find UI failed: " + name)
        return ui

    def TryToFindUI(self, name):
        result, configPath = self.__findConfig(name)
        if not result:
            return None
        lastConfig = None
        for config in configPath:
            if not self.__isUIBound(config):
                config[AFWConst.UIObj] = self.__createUI(config, lastConfig)
                if not config[AFWConst.UIObj]:
                    Error("Failed to bind UI: " + config[AFWConst.Name])
                    return None
            lastConfig = config
        return configPath.pop()[AFWConst.UIObj]

    def StartApp(self, name):
        app = self.TryToStartApp(name)
        if app is None:
            Error("Start App failed: " + name)
            raise Exception("Start App failed: " + name)
        return app

    def TryToStartApp(self, name):
        result, configPath = self.__findConfig(name)
        if not result:
            return None
        appConfig = configPath.pop()
        if appConfig[AFWConst.Type] != AFWConst.UIApp:
            Error("UI config is not type of App: " + name)
            return None
        if self.__isUIBound(appConfig):
            return appConfig[AFWConst.UIObj]
        appConfig[AFWConst.UIObj] = self.__createUI(appConfig, None)
        return appConfig[AFWConst.UIObj]

    def GetBreakTime(self):
        return self.__afw.BreakTime

    ### Private ###

    def __isUIBound(self, config):
        if AFWConst.UIObj in config and config[AFWConst.UIObj] is not None:
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
        AFWConst.UIApp: lambda manager, config, parentConfig: AFWApp(manager, config),
        AFWConst.AppRoot: lambda manager, config, parentConfig: AFWAppRoot(manager, config, parentConfig),

        AFWConst.AppForm: lambda manager, config, parentConfig: AFWAppForm(manager, config, parentConfig),
        AFWConst.AppSubForm: lambda manager, config, parentConfig: AFWAppSubForm(manager, config, parentConfig),

        AFWConst.AppTab: lambda manager, config, parentConfig: AFWAppTab(manager, config, parentConfig),
        AFWConst.AppTabPage: lambda manager, config, parentConfig: AFWAppTabPage(manager, config, parentConfig),

        AFWConst.AppButton: lambda manager, config, parentConfig: AFWAppButton(manager, config, parentConfig),
        AFWConst.AppCheckbox: lambda manager, config, parentConfig: AFWAppCheckbox(manager, config, parentConfig),
        AFWConst.AppEditBox: lambda manager, config, parentConfig: AFWAppEditBox(manager, config, parentConfig),

        AFWConst.UIWeb: lambda manager, config, parentConfig: AFWWeb(manager, config)
    }
