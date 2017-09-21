import AFWConst
from AFWWebBase import AFWWebBase

class AFWWebURL(AFWWebBase):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebBase.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        parentConfig = self.GetParentConfig()
        if parentConfig[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web URL parent is not browser: " + config[AFWConst.Name])
        parentUI = manager.GetUI(parentConfigID)
        if parentUI is None:
            raise Exception("Web URL parent is not bound")
        urlID = self._plugin.OpenWebURL(parentConfigID, config[AFWConst.URL], configID)
        if urlID is None:
            raise Exception("Open web url failed: " + config[AFWConst.URL])
