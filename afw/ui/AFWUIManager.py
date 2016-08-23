import sys
import os
sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], ".."))

import AFWConst
from AFWLogger import *
from AFWApp import AFWApp

class AFWUIManager:
    def __init__(self, config):
        self.__config = config

    def BindUI(self, name):
        # TODO
        return None

    def StartApp(self, name):
        result, elementPath = self.__findElement(name)
        if not result:
            return None
        appConfig = elementPath.pop()
        if appConfig[AFWConst.Type] != AFWConst.UIApp:
            Error("UI element is not type of App: " + name)
            return None
        if AFWConst.UIObj in appConfig and appConfig[AFWConst.UIObj] is not None:
            # App already bound
            return appConfig[AFWConst.UIObj]
        appConfig[AFWConst.UIObj] = self.__createUI(appConfig, None)
        # TODO start process
        return appConfig[AFWConst.UIObj]

    def __findElement(self, name):
        elementPath = []
        result = self.__findElementImpl(name, self.__config[AFWConst.UI], elementPath)
        if not result:
            Warning("Could not find UI element: " + name)
        else:
            Debug("Find UI element: " + name)
        return result, elementPath
    
    def __findElementImpl(self, name, node, path):
        if node[AFWConst.Name] == name:
            # Find element node
            path.append(node)
            return True
        if AFWConst.SubUI not in node:
            # Element not match and no sub node, so not find
            return False
        for subNode in node[AFWConst.SubUI]:
            path.append(subNode)
            if self.__findElementImpl(name, subNode, path):
                # Find element in sub node
                return True
            else:
                # Could not find in sub node, pop stack
                path.pop()
        return False

    def __createUI(self, config, parent):
        if config[AFWConst.Type] in AFWUIManager.__uiFactory:
            return AFWUIManager.__uiFactory[config[AFWConst.Type]](config, parent)
        Error("UI type is not defined in ui factory: " + config[AFWConst.Type])
        return None

    __uiFactory = {
        AFWConst.UIApp: lambda config, parent: AFWApp(config)
    }

    __pluginFactory = {
    }
