import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppForm(AFWAppUI):
    def __init__(self, manager,  config, parentConfig):
        AFWAppUI.__init__(self, manager, config, parentConfig)
        self.__form = self._plugin.GetForm(config)
        if self.__form is None:
            raise Exception("Failed to get App form: " + config[AFWConst.Name])

    ### Implement AFWUI ###

    def GetNativeUI(self):
        return self.__form