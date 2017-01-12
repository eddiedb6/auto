import AFWConst
from AFWAppBase import AFWAppBase
from AFWPluginManager import AFWPluginManager

class AFWApp(AFWAppBase):
    def __init__(self, manager, config, parentConfig):
        AFWAppBase.__init__(self, manager, config, None)
        self._plugin = AFWPluginManager().GetPlugin(config[AFWConst.Plugin])
        if self._plugin is None:
            raise Exception("Get app plugin failed")
        self._native = self._plugin.StartApp(config[AFWConst.Path])
        if self._native is None:
            raise Exception("Start app failed")
