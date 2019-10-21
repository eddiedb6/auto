import AFWConst
from AFWUI import AFWUI

class AFWForm(AFWUI):
    def __init__(self, manager,  configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        formID = self._plugin.GetForm(configID)
        if formID is None:
            raise Exception("Failed to get form: " + self.GetConfig()[AFWConst.Name])
