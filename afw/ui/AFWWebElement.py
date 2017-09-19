import AFWConst
from AFWWebUI import AFWWebUI

class AFWWebElement(AFWWebUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebUI.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        parentConfig = self.GetParentConfig()
        self._nativeId = self._plugin.GetElement(config, parentConfig)
        if self._nativeId is None:
            raise Exception("Failed to find Web element: " + config[AFWConst.Name])

    ### Implement AFWUI ###

    def InputText(self, text):
        return self._plugin.SendKeys(self, text)
