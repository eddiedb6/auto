from AFWPlugin import AFWPlugin

class AFWPluginWeb(AFWPlugin):
    def __init__(self, config):
        AFWPlugin.__init__(self, config)

    def OpenBrowser(self, name):
        return None

    def OpenWebPage(self, browser, url):
        return False

    def GetCurrentURL(self, browser):
        return None

    def SendKeys(self, ui, keys):
        return False
