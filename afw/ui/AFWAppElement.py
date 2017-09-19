import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppElement(AFWAppUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWAppUI.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        parentConfig = self.GetParentConfig()
        self._nativeId = self._plugin.GetElement(config, parentConfig)
        if self._nativeId is None:
            raise Exception("Failed to find App element: " + config[AFWConst.Name])
