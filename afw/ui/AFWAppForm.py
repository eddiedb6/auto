import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppForm(AFWAppUI):
    def __init__(self, manager,  configID, parentConfigID):
        AFWAppUI.__init__(self, manager, configID, parentConfigID)
        formID = self._plugin.GetForm(configID)
        if formID is None:
            raise Exception("Failed to get form: " + self.GetConfig()[AFWConst.Name])
