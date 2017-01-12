import AFWConst
from AFWWebBase import AFWWebBase
from AFWPluginManager import AFWPluginManager

class AFWWeb(AFWWebBase):
    def __init__(self, manager, config, parentConfig):
        AFWWebBase.__init__(self, manager, config, None)
        self._plugin = AFWPluginManager().GetPlugin(config[AFWConst.Plugin])
        if self._plugin is None:
            raise Exception("Get web plugin failed")
        self.__browser = self._plugin.OpenBrowser(config[AFWConst.Browser])
        self._native = self.__browser
        if self.__browser is None:
            raise Exception("Open browser failed")

    def GetCurrentURL(self):
        return self._plugin.GetCurrentURL(self.__browser)
