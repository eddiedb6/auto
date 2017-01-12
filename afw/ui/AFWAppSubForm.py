import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppSubForm(AFWAppUI):
    def __init__(self, manager,  config, parentConfig):
        AFWAppUI.__init__(self, manager, config, parentConfig)
        self._native = self._plugin.GetElement(config, parentConfig)
        if self._native is None:
            raise Exception("Failed to get App sub form: " + config[AFWConst.Name])
