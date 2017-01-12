import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppRoot(AFWAppUI):
    def __init__(self, manager, config, parentConfig):
        AFWAppUI.__init__(self, manager, config, parentConfig)
        self._native = self._plugin.GetDesktop()
        if self._native is None:
            raise Exception("Failed to get App root")
