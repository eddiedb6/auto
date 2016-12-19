import AFWConst
from AFWUI import AFWUI
from AFWPluginManager import AFWPluginManager

class AFWApp(AFWUI):
    def __init__(self, manager, config, parentConfig):
        AFWUI.__init__(self, manager, config, None)
        self._plugin = AFWPluginManager().GetPlugin(config[AFWConst.Plugin])
        if self._plugin is None:
            raise Exception("Get app plugin failed")
        self.__app = self._plugin.StartApp(config[AFWConst.Path])
        if self.__app is None:
            raise Exception("Start app failed")
