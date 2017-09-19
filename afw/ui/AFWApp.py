import AFWConst
from AFWAppBase import AFWAppBase
from AFWPluginManager import AFWPluginManager

class AFWApp(AFWAppBase):
    def __init__(self, manager, configID, parentConfigID):
        AFWAppBase.__init__(self, manager, configID, None)
        config = self.GetConfig()
        self._plugin = AFWPluginManager().GetPlugin(config[AFWConst.Plugin])
        if self._plugin is None:
            raise Exception("Get app plugin failed")
        self._nativeId = self._plugin.StartApp(config[AFWConst.Path])
        if self._nativeId is None:
            raise Exception("Start app failed")
