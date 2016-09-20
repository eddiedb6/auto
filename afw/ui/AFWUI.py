import time

import AFWConst

class AFWUI:
    def __init__(self, manager, config, parent):
        self.__manager = manager
        self.__config = config
        self.__parent = parent
        self._plugin = None
        if parent is not None:
            if AFWConst.UIObj in parent and parent[AFWConst.UIObj] is not None:
                self._plugin = parent[AFWConst.UIObj]._plugin
            else:
                raise Exception("Parent UI is not bound: " + parent[AFWConst.Name])
        if AFWConst.BreakTime in config:
            time.sleep(config[AFWConst.BreakTime] / 1000)
        else:
            time.sleep(self.__manager.GetBreakTime() / 1000)

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

    def GetNativeUI(self):
        return None
