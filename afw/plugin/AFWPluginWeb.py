from AFWPlugin import AFWPlugin

class AFWPluginWeb(AFWPlugin):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPlugin.__init__(self, pluginConfig, uiConfigPool)

    def OpenBrowser(self, name, configID):
        return None

    def OpenWebPage(self, browserID, url):
        return False

    def GetCurrentURL(self, browserID):
        return None

    def SendKeys(self, uiID, keys):
        return False
