import AFWConst
from AFWUI import AFWUI

class AFWWebUI(AFWUI):
    def __init__(self, manager, config, parentConfig):
        AFWUI.__init__(self, manager, config, parentConfig)
        self._element = self._plugin.GetElement(config, parentConfig)
        if self._element is None:
            raise Exception("Failed to find Web element: " + config[AFWConst.Name])

    ### Implement AFWUI ###

    def GetNativeUI(self):
        return self._element
