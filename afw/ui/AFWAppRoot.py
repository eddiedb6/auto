import AFWConst
from AFWAppUI import AFWAppUI
from AFWPluginManager import AFWPluginManager

class AFWAppRoot(AFWAppUI):
    def __init__(self, manager, config, parentConfig):
        parent = parentConfig
        if parent is not None and parent[AFWConst.Type] != AFWConst.UIApp:
            # This is not from start App, but find win form directly
            parent = None
        AFWAppUI.__init__(self, manager, config, parent)
        self._native = None
        if parent is None:
            if self._plugin is None :
                if AFWConst.Plugin not in config:
                    raise Exception("Plugin is not defined for App root when get win form directly")
                self._plugin = AFWPluginManager().GetPlugin(config[AFWConst.Plugin])
                if self._plugin is None:
                    raise Exception("Get app plugin in App root failed")
            else:
                raise Exception("Should not come to here")
        else:
            if self._plugin is None:
                raise Exception("Plugin for App root is invalid")
        self._native = self._plugin.GetDesktop()
        if self._native is None:
            raise Exception("Failed to get App root")
