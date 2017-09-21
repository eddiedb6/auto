import AFWConst
from AFWWebUI import AFWWebUI

class AFWWebElement(AFWWebUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebUI.__init__(self, manager, configID, parentConfigID)
        elementID = self._plugin.GetElement(configID, parentConfigID)
        if elementID is None:
            raise Exception("Failed to get web element: " + self.GetConfig(configID)[AFWConst.Name])

    ### Implement AFWUI ###

    def InputText(self, text):
        return self._plugin.SendKeys(self.GetID(), text)
