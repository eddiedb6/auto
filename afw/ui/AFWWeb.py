import AFWConst
from AFWUI import AFWUI
from AFWPluginManager import AFWPluginManager

class AFWWeb(AFWUI):
    def __init__(self, manager, config):
        AFWUI.__init__(self, manager, config, None)
        self._plugin = AFWPluginManager().GetPlugin(config[AFWConst.Plugin])
        if self._plugin is None:
            raise Exception("Get web plugin failed")
        self.__browser = self._plugin.OpenBrowser(config[AFWConst.Browser])
        if self.__browser is None:
            raise Exception("Open browser failed")

    ### Implement AFWUI ###
    def GetNativeUI(self):
        return self.__browser
