import AFWConst
from AFWUI import AFWUI

class AFWAppSubForm(AFWUI):
    def __init__(self, manager,  config, parentConfig):
        AFWUI.__init__(self, manager, config, parentConfig)
        self.__subform = self._plugin.GetElement(config, parentConfig)
        if not self.__subform:
            raise Exception("Failed to get App sub form: " + config[AFWConst.Name])

    ### Implement AFWUI ###

    def GetNativeUI(self):
        return self.__subform