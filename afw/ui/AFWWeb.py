import AFWConst
from AFWWebBase import AFWWebBase
from AFWPluginManager import AFWPluginManager
from AFWLocalConfigPool import AFWLocalConfigPool

class AFWWeb(AFWWebBase):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebBase.__init__(self, manager, configID, None)
        config = self.GetConfig()
        self._plugin = AFWPluginManager().CreatePlugin(config[AFWConst.Plugin], AFWLocalConfigPool(manager))
        if self._plugin is None:
            raise Exception("Get web plugin failed")
        self._plugin.OpenBrowser(config[AFWConst.Browser], configID)

    def GetCurrentURL(self):
        return self._plugin.GetCurrentURL(self.GetID())

    def OpenURL(self, name):
        url = self.TryToFindSubUI(name)
        if not url:
            return False
        if url.GetType() != AFWConst.WebURL:
            return False
        return True
