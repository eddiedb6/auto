from AFWPlugin import AFWPlugin

class AFWPluginWeb(AFWPlugin):
    def __init__(self):
        AFWPlugin.__init__(self)

    def OpenBrowser(self, name):
        return None

    def OpenWebSite(self, url):
        return False
