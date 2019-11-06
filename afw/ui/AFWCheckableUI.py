import AFWConst
from AFWUI import AFWUI
from AFWCheckable import AFWCheckable

class AFWCheckableUI(AFWUI, AFWCheckable):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        AFWCheckable.__init__(self, self._plugin)
        id = self._plugin.GetElement(configID, parentConfigID)
        if id is None:
            raise Exception("Failed to get checkable UI: " + self.GetConfig()[AFWConst.Name])
