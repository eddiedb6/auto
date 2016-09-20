import AFWConst
from AFWUI import AFWUI

class AFWAppForm(AFWUI):
    def __init__(self, manager,  config, parent):
        AFWUI.__init__(self, manager, config, parent)
        self.__form = self._plugin.GetForm(config)
        if not self.__form:
            raise Exception("Failed to get App form: " + config[AFWConst.Name])

    def GetNativeUI(self):
        return self.__form