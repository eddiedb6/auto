from AFWLogger import *
from AFWPluginApp import AFWPluginApp
from AFWSocket import AFWSocket
import AFWConst

class PluginSocketApp(AFWPluginApp, AFWSocket):
    def __init__(self):
        AFWPluginApp.__init__(self)
        AFWSocket.__init__(self)

    ### Implement AFWPlugin ###

    def GetElement(self, config, parentConfig):
        pass
    
    def SetFocus(self, ui):
        pass

    def Click(self, ui):
        pass

    def IsChecked(self, ui):
        pass

    def IsEnabled(self, ui):
        pass

    def PressKey(self, ui, key):
        return True

    def ReleaseKey(self, ui, key):
        return True

    def GetText(self, ui):
        return None

    ### Implement AFWPluginApp ###

    def StartApp(self, path):
        pass

    def GetDesktop(self):
        pass

    def GetForm(self, config):
        pass
    
