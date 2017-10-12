import AFWConst
from AFWWebElement import AFWWebElement
from AFWSelectable import AFWSelectable

class AFWWebCombobox(AFWWebElement, AFWSelectable):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebElement.__init__(self, manager, configID, parentConfigID)
        AFWSelectable.__init__(self, self._plugin)
