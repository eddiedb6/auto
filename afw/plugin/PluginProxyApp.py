from AFWLogger import *
from AFWPluginApp import AFWPluginApp
from AFWProxyManager import AFWProxyManager
import AFWConst

class PluginProxyApp(AFWPluginApp):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPluginApp.__init__(self, pluginConfig, uiConfigPool)
        if AFWConst.Proxy not in pluginConfig:
            raise Exception("No proxy defined for app proxy plugin: " + pluginConfig[AFWConst.PluginName])
        self._proxy = AFWProxyManager().CreateProxy(pluginConfig[AFWConst.Proxy])

    ### Implement AFWPlugin ###

    def GetElement(self, configID, parentConfigID):
        return self._proxy.GetElement(configID, parentConfigID)
    
    def SetFocus(self, uiID):
        return self._proxy.SetFocus(uiID)

    def Click(self, uiID):
        return self._proxy.Click(uiID)

    def IsChecked(self, uiID):
        return self._proxy.IsChecked(uiID)

    def IsEnabled(self, uiID):
        return self._proxy.IsEnabled(uiID)

    def PressKey(self, uiID, key):
        return self._proxy.PressKey(uiID, key)

    def ReleaseKey(self, uiID, key):
        return self._proxy.ReleaseKey(uiID, key)

    def GetText(self, uiID):
        return self._proxy.GetText(uiID)

    ### Implement AFWPluginApp ###

    def StartApp(self, path, configID):
        return self._proxy.StartApp(path, configID)

    def GetDesktop(self, configID):
        return self._proxy.GetDesktop(configID)

    def GetForm(self, configID):
        return self._proxy.GetForm(configID)
    
