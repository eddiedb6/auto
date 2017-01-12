import AFWConst
from AFWWebUI import AFWWebUI

class AFWWebElement(AFWWebUI):
    def __init__(self, manager, config, parentConfig):
        AFWWebUI.__init__(self, manager, config, parentConfig)
        self._element = self._plugin.GetElement(config, parentConfig)
        self._native = self._element
        if self._element is None:
            raise Exception("Failed to find Web element: " + config[AFWConst.Name])

    ### Implement AFWUI ###

    def InputText(self, text):
        return self._plugin.SendKeys(self, text)
