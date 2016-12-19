import AFWConst

from AFWLogger import *
from AFWPluginWeb import AFWPluginWeb
from selenium import webdriver

class PluginSelenium(AFWPluginWeb):
    def __init__(self):
        AFWPluginWeb.__init__(self)

    ### Implement AFWPluginWeb ###
    
    def OpenBrowser(self, name):
        Info("Open browser: " + name)
        if name in PluginSelenium.__browserFactory:
            return PluginSelenium.__browserFactory[name]()
        else:
            Error("Browser type is not supported: " + name)
            return None

    def OpenWebSite(self, browser, url):
        Info("Open web site: " + url)
        if browser is None:
            return False
        if url is None or len(url) <= 0:
            return False
        browser.get(url)
        return True

    def GetElement(self, config, parentConfig):
        return None # TODO

    __browserFactory = {
        AFWConst.BrowserChrome: lambda : webdriver.Chrome(),
        AFWConst.BrowserIE: lambda : webdriver.Ie(),
        AFWConst.BrowserFireFox: lambda : webdriver.Firefox()
    }
            
        
