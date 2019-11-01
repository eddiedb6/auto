import AFWConst
from AFWUI import AFWUI

class AFWCommon(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        id = self._plugin.GetElement(configID, parentConfigID)
        if id is None:
            raise Exception("Failed to get common UI: " + self.GetConfig()[AFWConst.Name])
