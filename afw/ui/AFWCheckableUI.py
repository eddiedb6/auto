import AFWConst
from AFWUI import AFWUI
from AFWCheckable import AFWCheckable

class AFWCheckableUI(AFWUI, AFWCheckable):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        AFWCheckable.__init__(self, self._plugin)
