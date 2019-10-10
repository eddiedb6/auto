import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppElement(AFWAppUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWAppUI.__init__(self, manager, configID, parentConfigID)
        elementID = self._plugin.GetElement(configID, parentConfigID)
        if elementID is None:
            raise Exception("Failed to get app element: " + self.GetConfig()[AFWConst.Name])
