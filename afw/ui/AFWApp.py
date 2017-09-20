import AFWConst
from AFWAppBase import AFWAppBase
from AFWPluginManager import AFWPluginManager
from AFWLocalConfigPool import AFWLocalConfigPool

class AFWApp(AFWAppBase):
    def __init__(self, manager, configID, parentConfigID):
        AFWAppBase.__init__(self, manager, configID, None)
        config = self.GetConfig()
        self._plugin = AFWPluginManager().CreatePlugin(config[AFWConst.Plugin], AFWLocalConfigPool(manager))
        if self._plugin is None:
            raise Exception("Get app plugin failed")
        self._plugin.StartApp(config[AFWConst.Path], configID)
