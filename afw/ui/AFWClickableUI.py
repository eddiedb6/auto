import AFWConst
from AFWUI import AFWUI
from AFWClickable import AFWClickable

class AFWClickableUI(AFWUI, AFWClickable):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        AFWClickable.__init__(self, self._plugin)
