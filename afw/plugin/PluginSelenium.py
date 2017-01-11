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

    def Click(self, ui):
        if ui is None or ui.GetNativeUI() is None:
            return False
        ui.GetNativeUI().click() # No return result
        return True
    
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
        if AFWConst.AttrID in config:
            return self.__getElementByID(driverElement, config[AFWConst.AttrID])
        elif AFWConst.AttrName in config:
            return self.__getElementByName(driverElement, config[AFWConst.AttrName])
        return self.__getElementByType(driverElement, config)

    def __getElementByID(self, driverElement, attrId):
        Debug("Find by id: " + attrId)
        return driverElement.find_element_by_id(attrId)

    def __getElementByName(self, driverElement, attrName):
        Debug("Find by name: " + attrName)
        return driverElement.find_element_by_name(attrName)

    def __getElementByType(self, driverElement, config):
        if config[AFWConst.Type] == AFWConst.WebLink and AFWConst.Text in config:
            Debug("Find by link: " + config[AFWConst.Text])
            return driverElement.find_element_by_link_text(config[AFWConst.Text])
        return None
        
    __browserFactory = {
        AFWConst.BrowserChrome: lambda : webdriver.Chrome(),
        AFWConst.BrowserIE: lambda : webdriver.Ie(),
        AFWConst.BrowserFireFox: lambda : webdriver.Firefox()
    }
            
        
