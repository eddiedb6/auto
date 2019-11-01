import AFWConst
from AFWUI import AFWUI

class AFWAppTab(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        id = self._plugin.GetElement(configID, parentConfigID)
        if id is None:
            raise Exception("Failed to get app tab: " + self.GetConfig()[AFWConst.Name])
