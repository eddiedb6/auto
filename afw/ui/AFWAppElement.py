import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppElement(AFWAppUI):
    def __init__(self, manager, config, parentConfig):
        AFWAppUI.__init__(self, manager, config, parentConfig)
        self._element = self._plugin.GetElement(config, parentConfig)
        if not self._element:
            raise Exception("Failed to find App element: " + config[AFWConst.Name])

    def Click(self):
        return self._plugin.Click(self)

    ### Implement AFWUI ###

    def GetNativeUI(self):
        return self._element