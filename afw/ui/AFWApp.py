import AFWConst
from AFWUI import AFWUI
from AFWPluginManager import AFWPluginManager
from AFWLocalConfigPool import AFWLocalConfigPool

class AFWApp(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, None)
        config = self.GetConfig()
        self._plugin = AFWPluginManager().CreatePlugin(config[AFWConst.Plugin], AFWLocalConfigPool(manager))
        if self._plugin is None:
            raise Exception("Get app plugin failed")
        appID = self._plugin.StartApp(config[AFWConst.Path], configID)
        if appID is None:
            raise Exception("Start app failed: " + config[AFWConst.Name])
