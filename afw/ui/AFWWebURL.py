import AFWConst
from AFWWebBase import AFWWebBase

class AFWWebURL(AFWWebBase):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebBase.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        parentConfig = self.GetParentConfig()
        if parentConfig[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web URL parent is not browser")
        parentUI = manager.GetUI(parentConfigID)
        if parentUI is None:
            raise Exception("Web URL parent is not bound")
        if not self._plugin.OpenWebPage(parentConfigID, config[AFWConst.URL]):
            raise Exception("Open web page failed: " + config[AFWConst.URL])
