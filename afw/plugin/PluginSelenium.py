import AFWConst

from AFWLogger import *
from AFWPluginWeb import AFWPluginWeb
from selenium import webdriver

class PluginSelenium(AFWPluginWeb):
    def __init__(self):
        AFWPluginWeb.__init__(self)

    ### Implement AFWPlugin ###
    def GetElement(self, config, parentConfig):
        if parentConfig is None:
            return None
        driverElement = parentConfig[AFWConst.UIObj].GetNativeUI()
        if driverElement is None:
            return None
        return self.__getElement(driverElement, config, parentConfig)

    ### Implement AFWPluginWeb ###
    
    def OpenBrowser(self, name):
        Info("Open browser: " + name)
        if name in PluginSelenium.__browserFactory:
            return PluginSelenium.__browserFactory[name]()
        else:
            Error("Browser type is not supported: " + name)
            return None

    def OpenWebPage(self, browser, url):
        Info("Open web page: " + url)
        if browser is None:
            return False
        if url is None or len(url) <= 0:
            return False
        browser.get(url)
        return True

    def GetCurrentURL(self, browser):
        if browser is None:
            return None
        return browser.current_url

    ### Private ###

    def __getElement(self, driverElement, config, parentConfig):
        # TODO
        return None
    
    __browserFactory = {
        AFWConst.BrowserChrome: lambda : webdriver.Chrome(),
        AFWConst.BrowserIE: lambda : webdriver.Ie(),
        AFWConst.BrowserFireFox: lambda : webdriver.Firefox()
    }
            
        
