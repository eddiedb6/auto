import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppForm(AFWAppUI):
    def __init__(self, manager,  config, parentConfig):
        AFWAppUI.__init__(self, manager, config, parentConfig)
        self._native = self._plugin.GetForm(config)
        if self._native is None:
            raise Exception("Failed to get App form: " + config[AFWConst.Name])
