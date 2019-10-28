from AFWLogger import *
from AFWPluginApp import AFWPluginApp
from AFWProxyManager import AFWProxyManager
import AFWConst

class PluginProxyApp(AFWPluginApp):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPluginApp.__init__(self, pluginConfig, uiConfigPool)
        if AFWConst.Proxy not in pluginConfig:
            raise Exception("No proxy defined for app proxy plugin: " + pluginConfig[AFWConst.PluginName])
        self.__proxy = AFWProxyManager().CreateProxy(pluginConfig[AFWConst.Proxy], uiConfigPool)

    ### Implement AFWPlugin ###

    def GetElement(self, configID, parentConfigID):
        return self.__proxy.GetElement(configID, parentConfigID)
    
    def SetFocus(self, uiID):
        return self.__proxy.SetFocus(uiID)

    def Click(self, uiID):
        return self.__proxy.Click(uiID)

    def Select(self, uiID, itemValue):
        return self.__proxy.Select(uiID, itemValue)

    def IsChecked(self, uiID):
        return self.__proxy.IsChecked(uiID)

    def IsEnabled(self, uiID):
        return self.__proxy.IsEnabled(uiID)

    def PressKey(self, uiID, key):
        return self.__proxy.PressKey(uiID, key)

    def ReleaseKey(self, uiID, key):
        return self.__proxy.ReleaseKey(uiID, key)

    def SetText(self, uiID, text):
        return self.__proxy.SetText(uiID, text)

    def GetText(self, uiID):
        return self.__proxy.GetText(uiID)

    def GetCellText(self, uiID, row, column):
        return self.__proxy.GetCellText(uiID, row, column)

    def GetDynamicElement(self, parentID, config):
        return self.__proxy.GetDynamicElement(parentID, config)

    def GetAttribute(self, uiID, name):
        return self.__proxy.GetAttribute(uiID, name)

    def DumpUI(self, uiID):
        return self.__proxy.DumpUI(uiID)

    ### Implement AFWPluginApp ###

    def StartApp(self, path, configID):
        return self.__proxy.StartApp(path, configID)

    def GetDesktop(self, configID):
        return self.__proxy.GetDesktop(configID)

    def GetForm(self, configID):
        return self.__proxy.GetForm(configID)
    
