from AFWLogger import *
from AFWPluginWeb import AFWPluginWeb
from AFWProxyManager import AFWProxyManager
import AFWConst

class PluginProxyWeb(AFWPluginWeb):
    def __init__(self, config):
        AFWPluginWeb.__init__(self, config)
        if AFWConst.Proxy not in config:
            raise Exception("No proxy defined for proxy plugin: " + config[AFWConst.PluginName])
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

    ### Implement AFWPluginWeb ###

    def OpenBrowser(self, name):
        return self._proxy.OpenBrowser(name)

    def OpenWebPage(self, browser, url):
        return self._proxy.OpenWebPage(browser, url)

    def GetCurrentURL(self, browser):
        return self._proxy.GetCurrentURL(browser)

    def SendKeys(self, ui, keys):
        return self._proxy.SendKeys(ui, keys)
