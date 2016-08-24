import AFWConst
from AFWPluginManager import AFWPluginManager

class AFWUI:
    def __init__(self, config, parent):
        self.__config = config
        self.__parent = parent
        self.__pluginManager = AFWPluginManager()

    def GetType(self):
        return self.__config[AFWConst.Type]

    def GetName(self):
        return self.__config[AFWConst.Name]

    def GetParent(self):
        return self.__parent

    def GetConfig(self):
        return self.__config

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
            
    def GetPlugin(self, name):
        return self.__pluginManager.GetPlugin(name)
