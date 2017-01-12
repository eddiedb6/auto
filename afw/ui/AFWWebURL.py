import AFWConst
from AFWWebBase import AFWWebBase

class AFWWebURL(AFWWebBase):
    def __init__(self, manager, config, parentConfig):
        AFWWebBase.__init__(self, manager, config, parentConfig)
        if parentConfig[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web URL parent is not browser")
        self._native = parentConfig[AFWConst.UIObj].GetNativeUI()
        if self._native is None:
            raise Exception("Browser is not open")
        if not self._plugin.OpenWebPage(self._native, config[AFWConst.URL]):
            raise Exception("Open web page failed: " + config[AFWConst.URL])
