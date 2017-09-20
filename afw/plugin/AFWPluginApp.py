from AFWPlugin import AFWPlugin

class AFWPluginApp(AFWPlugin):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPlugin.__init__(self, pluginConfig, uiConfigPool)

    def StartApp(self, path, configID):
        return None

    def GetDesktop(self, configID):
        return None

    def GetForm(self, configID):
        return None
