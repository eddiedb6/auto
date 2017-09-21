from AFWLogger import *
from AFWPluginWeb import AFWPluginWeb
from AFWProxyManager import AFWProxyManager
import AFWConst

class PluginProxyWeb(AFWPluginWeb):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPluginWeb.__init__(self, pluginConfig, uiConfigPool)
        if AFWConst.Proxy not in pluginConfig:
            raise Exception("No proxy defined for web proxy plugin: " + pluginConfig[AFWConst.PluginName])
        self.__proxy = AFWProxyManager().CreateProxy(pluginConfig[AFWConst.Proxy], uiConfigPool)

    ### Implement AFWPlugin ###

    def GetElement(self, configID, parentConfigID):
        return self.__proxy.GetElement(configID, parentConfigID)
    
    def SetFocus(self, uiID):
        return self.__proxy.SetFocus(uiID)

    def Click(self, uiID):
        return self.__proxy.Click(uiID)

    def IsChecked(self, uiID):
        return self.__proxy.IsChecked(uiID)

    def IsEnabled(self, uiID):
        return self.__proxy.IsEnabled(uiID)

    def PressKey(self, uiID, key):
        return self.__proxy.PressKey(uiID, key)

    def ReleaseKey(self, uiID, key):
        return self.__proxy.ReleaseKey(uiID, key)

    def GetText(self, uiID):
        return self.__proxy.GetText(uiID)

    ### Implement AFWPluginWeb ###

    def OpenBrowser(self, name, configID):
        return self.__proxy.OpenBrowser(name, configID)

    def OpenWebURL(self, browserID, url, configID):
        return self.__proxy.OpenWebURL(browserID, url, configID)

    def GetCurrentURL(self, browserID):
        return self.__proxy.GetCurrentURL(browserID)

    def GetWebPage(self, browserID, configID):
        return self.__proxy.GetWebPage(browserID, configID)

    def SendKeys(self, uiID, keys):
        return self.__proxy.SendKeys(uiID, keys)
