from AFWPlugin import AFWPlugin

class AFWPluginWeb(AFWPlugin):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPlugin.__init__(self, pluginConfig, uiConfigPool)

    def OpenBrowser(self, name, configID):
        return None

    def CloseBrowser(self, browserID):
        return False

    def OpenWebURL(self, browserID, url, configID):
        return False

    def GetCurrentURL(self, browserID):
        return None

    def GetWebPage(self, browserID, configID):
        return None
