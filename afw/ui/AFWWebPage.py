import AFWConst

from AFWWebUI import AFWWebUI

class AFWWebPage(AFWWebUI):
    def __init__(self, manager, config, parentConfig):
        AFWWebUI.__init__(self, manager, config, parentConfig)
        if parentConfig[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web page parent is not browser")
        self.__browser = parentConfig[AFWConst.UIObj].GetNativeUI()
        self._native = self.__browser
        if self.__browser is None:
            raise Exception("Browser is not open")
        if parentConfig[AFWConst.UIObj].GetCurrentURL() != config[AFWConst.URL]:
            if not self._plugin.OpenWebPage(self.__browser, config[AFWConst.URL]):
                raise Exception("Open web page failed: " + config[AFWConst.URL])
