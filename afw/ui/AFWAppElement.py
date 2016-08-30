import AFWConst
from AFWUI import AFWUI

class AFWAppElement(AFWUI):
    def __init__(self, manager, config, parent):
        AFWUI.__init__(self, manager, config, parent)
        self._element = self._plugin.GetElement(config, parent)
        if not self._element:
            raise Exception("Failed to find App element: " + config[AFWConst.Name])
