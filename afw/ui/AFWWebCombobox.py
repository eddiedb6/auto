import AFWConst
from AFWWebElement import AFWWebElement

class AFWWebCombobox(AFWWebElement):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebElement.__init__(self, manager, configID, parentConfigID)
