from AFWPlugin import AFWPlugin

class AFWPluginApp(AFWPlugin):
    def __init__(self, config):
        AFWPlugin.__init__(self, config)

    def StartApp(self, path):
        return None

    def GetDesktop(self):
        return None

    def GetForm(self, config):
        return None
