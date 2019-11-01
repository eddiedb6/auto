import AFWConst
from AFWUI import AFWUI

class AFWWebTable(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        id = self._plugin.GetElement(configID, parentConfigID)
        if id is None:
            raise Exception("Failed to get web table: " + self.GetConfig()[AFWConst.Name])

    def GetCellText(self, row, column):
        return self._plugin.GetCellText(self.GetID(), row, column)
        
