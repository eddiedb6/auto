import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppElement(AFWAppUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWAppUI.__init__(self, manager, configID, parentConfigID)
        self._plugin.GetElement(configID, parentConfigID)
