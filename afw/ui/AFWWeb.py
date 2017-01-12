import AFWConst
from AFWWebBase import AFWWebBase
from AFWPluginManager import AFWPluginManager

class AFWWeb(AFWWebBase):
    def __init__(self, manager, config, parentConfig):
        AFWWebBase.__init__(self, manager, config, None)
        self._plugin = AFWPluginManager().GetPlugin(config[AFWConst.Plugin])
        if self._plugin is None:
            raise Exception("Get web plugin failed")
        self._native = self._plugin.OpenBrowser(config[AFWConst.Browser])
        if self._native is None:
            raise Exception("Open browser failed")

    def GetCurrentURL(self):
        return self._plugin.GetCurrentURL(self._native)

    def OpenURL(self, name):
        url = self.TryToFindSubUI(name)
        if not url:
            return False
        if url.GetType() != AFWConst.WebURL:
            return False
        return True
