import AFWConst
from AFWWebElement import AFWWebElement

class AFWWebPanel(AFWWebElement):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebElement.__init__(self, manager, configID, parentConfigID)
