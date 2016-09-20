import AFWConst
from AFWUI import AFWUI
from AFWPluginManager import AFWPluginManager

class AFWApp(AFWUI):
    def __init__(self, manager, config):
        AFWUI.__init__(self, manager, config, None)
        self._plugin = AFWPluginManager().GetPlugin(config[AFWConst.Plugin])
        if not self._plugin:
            raise Exception("Get plugin failed")
        self.__app = self._plugin.StartApp(config[AFWConst.Path])
        if not self.__app:
            raise Exception("Start app failed")

    def GetNativeUI(self):
        return self.__app
