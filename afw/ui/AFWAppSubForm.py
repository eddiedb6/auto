import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppSubForm(AFWAppUI):
    def __init__(self, manager,  configID, parentConfigID):
        AFWAppUI.__init__(self, manager, configID, parentConfigID)
        self._nativeId = self._plugin.GetElement(configID, parentConfigID)
        if self._nativeId is None:
            config = self.GetConfig()
            raise Exception("Failed to get App sub form: " + config[AFWConst.Name])
