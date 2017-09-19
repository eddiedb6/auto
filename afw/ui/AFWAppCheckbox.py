import AFWConst
from AFWAppElement import AFWAppElement
from AFWCheckable import AFWCheckable

class AFWAppCheckbox(AFWAppElement, AFWCheckable):
    def __init__(self, manager, configID, parentConfigID):
        AFWAppElement.__init__(self, manager, configID, parentConfigID)
        AFWCheckable.__init__(self, self._plugin)
