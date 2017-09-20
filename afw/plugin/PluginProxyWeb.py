from AFWLogger import *
from AFWPluginWeb import AFWPluginWeb
from AFWProxyManager import AFWProxyManager
import AFWConst

class PluginProxyWeb(AFWPluginWeb):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPluginWeb.__init__(self, pluginConfig, uiConfigPool)
        if AFWConst.Proxy not in pluginConfig:
            raise Exception("No proxy defined for web proxy plugin: " + pluginConfig[AFWConst.PluginName])
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

    ### Implement AFWPluginWeb ###

    def OpenBrowser(self, name, configID):
        return self._proxy.OpenBrowser(name, configID)

    def OpenWebPage(self, browserID, url):
        return self._proxy.OpenWebPage(browserID, url)

    def GetCurrentURL(self, browserID):
        return self._proxy.GetCurrentURL(browserID)

    def SendKeys(self, uiID, keys):
        return self._proxy.SendKeys(uiID, keys)
