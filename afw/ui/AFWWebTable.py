import AFWConst
from AFWWebElement import AFWWebElement

class AFWWebTable(AFWWebElement):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebElement.__init__(self, manager, configID, parentConfigID)

    def GetCellText(self, row, column):
        return self._plugin.GetCellText(self.GetID(), row, column)
        
