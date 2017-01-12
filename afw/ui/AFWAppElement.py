import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppElement(AFWAppUI):
    def __init__(self, manager, config, parentConfig):
        AFWAppUI.__init__(self, manager, config, parentConfig)
        self._element = self._plugin.GetElement(config, parentConfig)
        self._native = self._element
        if self._element is None:
            raise Exception("Failed to find App element: " + config[AFWConst.Name])
