import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppForm(AFWAppUI):
    def __init__(self, manager,  configID, parentConfigID):
        AFWAppUI.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        self._nativeId = self._plugin.GetForm(config)
        if self._nativeId is None:
            raise Exception("Failed to get App form: " + config[AFWConst.Name])
