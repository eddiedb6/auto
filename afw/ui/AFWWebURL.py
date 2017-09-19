import AFWConst
from AFWWebBase import AFWWebBase

class AFWWebURL(AFWWebBase):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebBase.__init__(self, manager, configID, parentConfigID)
        config = self.GetConfig()
        parentConfig = self.GetParentConfig(0
        if parentConfig[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web URL parent is not browser")
        parentUI = manager.GetUI(parentConfigID)
        if parentUI is None:
            raise Exception("Web URL parent is not bound")
        self._nativeId = parentUI.GetNativeUIID()
        if self._nativeId is None:
            raise Exception("Browser is not open")
        if not self._plugin.OpenWebPage(self._nativeId, config[AFWConst.URL]):
            raise Exception("Open web page failed: " + config[AFWConst.URL])
