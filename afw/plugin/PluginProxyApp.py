from AFWLogger import *
from AFWPluginApp import AFWPluginApp
from AFWProxyManager import AFWProxyManager
import AFWConst

class PluginProxyApp(AFWPluginApp):
    def __init__(self, config):
        AFWPluginApp.__init__(self, config)
        self._proxy = AFWProxyManager().CreateProxy(config[AFWConst.Proxy])

    ### Implement AFWPlugin ###

    def GetElement(self, config, parentConfig):
        return self._proxy.GetElement(config, parentConfig)
    
    def SetFocus(self, ui):
        return self._proxy.GetForm(ui)

    def Click(self, ui):
        return self._proxy.Click(ui)

    def IsChecked(self, ui):
        return self._proxy.IsChecked(ui)

    def IsEnabled(self, ui):
        return self._proxy.IsEnabled(ui)

    def PressKey(self, ui, key):
        return self._proxy.PressKey(ui, key)

    def ReleaseKey(self, ui, key):
        return self._proxy.ReleaseKey(ui, key)

    def GetText(self, ui):
        return self._proxy.GetText(ui)

    ### Implement AFWPluginApp ###

    def StartApp(self, path):
        return self._proxy.StartApp(path)

    def GetDesktop(self):
        return self._proxy.GetDesktop()

    def GetForm(self, config):
        return self._proxy.GetForm(config)
    
