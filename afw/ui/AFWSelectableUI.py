import AFWConst
from AFWUI import AFWUI
from AFWSelectable import AFWSelectable

class AFWSelectableUI(AFWUI, AFWSelectable):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        AFWSelectable.__init__(self, self._plugin)
        id = self._plugin.GetElement(configID, parentConfigID)
        if id is None:
            raise Exception("Failed to get selectable UI: " + self.GetConfig(configID)[AFWConst.Name])
