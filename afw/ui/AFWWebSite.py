import AFWConst

from AFWUI import AFWUI

class AFWWebSite(AFWUI):
    def __init__(self, manager, config, parentConfig):
        AFWUI.__init__(self, manager, config, parentConfig)
        self.__browser = parentConfig[AFWConst.UIObj].GetNativeUI()
        if not self._plugin.OpenWebSite(self.__browser, config[AFWConst.URL]):
            raise Exception("Open web site failed: " + config[AFWConst.URL])

    ### Imeplement AFWUI ###

    def GetNativeUI(self):
        return self.__browser
            
    
