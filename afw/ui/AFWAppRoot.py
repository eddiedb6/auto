import AFWConst
from AFWAppUI import AFWAppUI
from AFWPluginManager import AFWPluginManager
from AFWLocalConfigPool import AFWLocalConfigPool

class AFWAppRoot(AFWAppUI):
    def __init__(self, manager, configID, parentConfigID):
        parent = manager.GetConfig(parentConfigID)
        if parent is not None and parent[AFWConst.Type] != AFWConst.UIApp:
            # This is not from start App, but find win form directly
            parentConfigID = None
        AFWAppUI.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        if parentConfigID is None:
            if self._plugin is None :
                if AFWConst.Plugin not in config:
                    raise Exception("Plugin is not defined for App root when get win form directly")
                self._plugin = AFWPluginManager().CreatePlugin(config[AFWConst.Plugin], AFWLocalConfigPool(manager))
                if self._plugin is None:
                    raise Exception("Get app plugin in App root failed")
            else:
                raise Exception("Should not come to here")
        else:
            if self._plugin is None:
                raise Exception("Plugin for App root is invalid")
        self._plugin.GetDesktop(configID)
