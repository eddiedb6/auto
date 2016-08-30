import AFWConst
from AFWLogger import *

from AFWApp import AFWApp
from AFWAppRoot import AFWAppRoot
from AFWAppForm import AFWAppForm
from AFWAppButton import AFWAppButton

from AFWWeb import AFWWeb

class AFWUIManager:
    def __init__(self, afw, config):
        self.__afw = afw
        self.__config = config

    def FindUI(self, name):
        result, elementPath = self.__findElement(name)
        if not result:
            return None
        lastElement = None
        for element in elementPath:
            if not self.__isElementBound(element):
                element[AFWConst.UIObj] = self.__createUI(element, lastElement)
                if not element[AFWConst.UIObj]:
                    Error("Failed to get UI element: " + element[AFWConst.Name])
                    return None
            lastElement = element
        return elementPath.pop()[AFWConst.UIObj]

    def StartApp(self, name):
        result, elementPath = self.__findElement(name)
        if not result:
            return None
        appConfig = elementPath.pop()
        if appConfig[AFWConst.Type] != AFWConst.UIApp:
            Error("UI element is not type of App: " + name)
            return None
        if self.__isElementBound(appConfig):
            return appConfig[AFWConst.UIObj]
        appConfig[AFWConst.UIObj] = self.__createUI(appConfig, None)
        return appConfig[AFWConst.UIObj]

    def GetBreakTime(self):
        return self.__afw.BreakTime

    def __isElementBound(self, element):
        if AFWConst.UIObj in element and element[AFWConst.UIObj] is not None:
            return True
        return False
        
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
            path.append(node)
            if self.__findElementImpl(name, subNode, path):
                # Find element in sub node
                return True
            else:
                # Could not find in sub node, pop stack
                path.pop()

        return False

    def __createUI(self, config, parent):
        uiType = config[AFWConst.Type]
        if uiType in AFWUIManager.__uiFactory:
            return AFWUIManager.__uiFactory[uiType](self, config, parent)
        Error("UI type is not defined in ui factory: " + config[AFWConst.Type])
        return None

    __uiFactory = {
        AFWConst.UIApp: lambda manager, config, parent: AFWApp(manager, config),
        AFWConst.AppRoot: lambda manager, config, parent: AFWAppRoot(manager, config, parent),
        AFWConst.AppButton: lambda manager, config, parent: AFWAppButton(manager, config, parent),
        AFWConst.AppForm: lambda manager, config, parent: AFWAppForm(manager, config, parent),
        
        AFWConst.UIWeb: lambda manager, config, parent: AFWWeb(manager, config)
    }
