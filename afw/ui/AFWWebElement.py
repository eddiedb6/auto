import AFWConst
from AFWWebUI import AFWWebUI

class AFWWebElement(AFWWebUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebUI.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        parentConfig = self.GetParentConfig()
        self._plugin.GetElement(configID, parentConfigID)

    ### Implement AFWUI ###

    def InputText(self, text):
        return self._plugin.SendKeys(self.GetID(), text)
