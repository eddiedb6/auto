import AFWConst
from AFWUI import AFWUI

class AFWWebEntry(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        parentConfig = self.GetParentConfig()
        if parentConfig[AFWConst.Type] != AFWConst.UIBrowser:
            raise Exception("Web entry parent is not browser: " + config[AFWConst.Name])
        parentUI = manager.GetUI(parentConfigID)
        if parentUI is None:
            raise Exception("Web entry parent is not bound")
        entryID = self._plugin.OpenWebURL(parentConfigID, config[AFWConst.URL], configID)
        if entryID is None:
            raise Exception("Open web url failed: " + config[AFWConst.URL])
