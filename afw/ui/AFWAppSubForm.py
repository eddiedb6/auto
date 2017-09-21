import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppSubForm(AFWAppUI):
    def __init__(self, manager,  configID, parentConfigID):
        AFWAppUI.__init__(self, manager, configID, parentConfigID)
        subFormID = self._plugin.GetElement(configID, parentConfigID)
        if subFormID is None:
            raise Exception("Failed to find sub form: " + self.GetConfig(configID)[AFWConst.Name])
