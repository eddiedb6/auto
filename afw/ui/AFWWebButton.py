import AFWConst
from AFWWebElement import AFWWebElement
from AFWClickable import AFWClickable

class AFWWebButton(AFWWebElement, AFWClickable):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebElement.__init__(self, manager, configID, parentConfigID)
        AFWClickable.__init__(self, self._plugin)
