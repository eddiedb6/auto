import AFWConst
from AFWAppElement import AFWAppElement
from AFWClickable import AFWClickable

class AFWAppEditBox(AFWAppElement, AFWClickable):
    def __init__(self, manager, configID, parentConfigID):
        AFWAppElement.__init__(self, manager, configID, parentConfigID)
        AFWClickable.__init__(self, self._plugin)
