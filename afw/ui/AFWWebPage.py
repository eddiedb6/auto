import AFWConst

from AFWUI import AFWUI

class AFWWebPage(AFWUI):
    def __init__(self, manager, config, parentConfig):
        AFWUI.__init__(self, manager, config, parentConfig)
        self.__browser = parentConfig[AFWConst.UIObj].GetNativeUI()
        if self.__browser is None:
            raise Exception("Browser is not open")
        if parentConfig[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web page parent is not browser")
        if parentConfig[AFWConst.UIObj].GetCurrentURL() != config[AFWConst.URL]:
            if not self._plugin.OpenWebPage(self.__browser, config[AFWConst.URL]):
                raise Exception("Open web page failed: " + config[AFWConst.URL])

    ### Imeplement AFWUI ###

    def GetNativeUI(self):
        return self.__browser
            
    
