from AFWPlugin import AFWPlugin

class AFWPluginApp(AFWPlugin):
    def __init__(self):
        AFWPlugin.__init__(self)

    def StartApp(self, path):
        return False

    def GetDesktop(self):
        return False

    def GetForm(self, config):
        return False

    def GetElement(self, config, parentConfig):
        return False

    
