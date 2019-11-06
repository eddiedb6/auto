import AFWConst
from AFWUI import AFWUI
from AFWInputable import AFWInputable

class AFWInputableUI(AFWUI, AFWInputable):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        AFWInputable.__init__(self, self._plugin)
        id = self._plugin.GetElement(configID, parentConfigID)
        if id is None:
            raise Exception("Failed to get inputable UI: " + self.GetConfig()[AFWConst.Name])
