import AFWConst
from AFWUI import AFWUI

class AFWAppDialog(AFWUI):
    def __init__(self, manager,  configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        dialogID = self._plugin.GetElement(configID, parentConfigID)
        if dialogID is None:
            raise Exception("Failed to find sub form: " + self.GetConfig()[AFWConst.Name])
