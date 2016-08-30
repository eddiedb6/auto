from AFWLogger import *
from AFWPluginApp import AFWPluginApp
import AFWConst

class PluginMSApp(AFWPluginApp):
    def __init__(self):
        AFWPluginApp.__init__(self)

    def StartApp(self, path):
        Info("Start app: " + path)
        return True

    def GetDesktop(self):
        Debug("Get desktop")
        return True

    def GetForm(self, config):
        Debug("Get form: " + config[AFWConst.Name])
        return True

    def GetElement(self, config, parent):
        Debug("Get element: " + config[AFWConst.Name])
        return True

    

