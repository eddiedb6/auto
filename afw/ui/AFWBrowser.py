import AFWConst
from AFWUI import AFWUI
from AFWPluginManager import AFWPluginManager
from AFWLocalConfigPool import AFWLocalConfigPool

class AFWBrowser(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, None)
        self.__urlCache = {}
        config = self.GetConfig()
        self._plugin = AFWPluginManager().CreatePlugin(config[AFWConst.Plugin], AFWLocalConfigPool(manager))
        if self._plugin is None:
            raise Exception("Get web plugin failed")
        browserID = self._plugin.OpenBrowser(config[AFWConst.Browser], configID)
        if browserID is None:
            raise Exception("Open browser failed: " + config[AFWConst.Browser])

    def GetCurrentURL(self):
        return self._plugin.GetCurrentURL(self.GetID())

    def OpenURL(self, name):
        if name in self.__urlCache:
            # This url is opened already
            # Now need to dump all its sub UI and reopen it
            self.__urlCache[name].Dump()
            del self.__urlCache[name]
        url = self.TryToFindSubUI(name)
        if url is None:
            return False
        if url.GetType() != AFWConst.UIWebEntry:
            return False
        self.__urlCache[name] = url
        return True

    def Quit(self):
        if self._plugin.CloseBrowser(self.GetID()):
            return self.Dump()
        return False
        
