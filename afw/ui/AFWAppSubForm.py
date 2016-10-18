import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppSubForm(AFWAppUI):
    def __init__(self, manager,  config, parentConfig):
        AFWAppUI.__init__(self, manager, config, parentConfig)
        self.__subform = self._plugin.GetElement(config, parentConfig)
        if self.__subform is None:
            raise Exception("Failed to get App sub form: " + config[AFWConst.Name])

    ### Implement AFWUI ###

    def GetNativeUI(self):
        return self.__subform