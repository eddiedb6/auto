import AFWConst
from AFWWebElement import AFWWebElement

class AFWWebEditBox(AFWWebElement):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebElement.__init__(self, manager, configID, parentConfigID)
