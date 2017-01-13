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

    def SetFocus(self, ui):
        # Web element do not need focus
        return True
    
    def Click(self, ui):
        if ui is None or ui.GetNativeUI() is None:
            return False
        ui.GetNativeUI().click() # No return result
        return True

    def IsChecked(self, ui):
        # TODO
        return False

    def IsEnabled(self, ui):
        if ui is None or ui.GetNativeUI() is None:
            return False
        return ui.GetNativeUI().is_enabled()

    def PressKey(self, ui, key):
        # TODO
        return False

    def ReleaseKey(self, ui, key):
        # TODO
        return False

    def GetText(self, ui):
        if ui is None or ui.GetNativeUI() is None:
            return None
        return ui.GetNativeUI().text
    
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

    def SendKeys(self, ui, keys):
        if ui is None or ui.GetNativeUI() is None:
            return False
        ui.GetNativeUI().send_keys(keys)
        return True
    
    ### Private ###

    def __getElement(self, driverElement, config, parentConfig):
        element = None
        if AFWConst.AttrID in config:
            element = self.__getElementByID(driverElement, config[AFWConst.AttrID])
            if element is not None:
                return element
        if AFWConst.AttrName in config:
            element = self.__getElementByName(driverElement, config[AFWConst.AttrName])
            if element is not None:
                return element
        if AFWConst.AttrClass in config:
            element = self.__getElementByClass(driverElement, config[AFWConst.AttrClass])
            if element is not None:
                return element
        if AFWConst.AttrTag in config:
            element = self.__getElementByTag(driverElement, config[AFWConst.AttrTag], config)
            if element is not None:
                return element
        return self.__getElementByType(driverElement, config)

    def __getElementByID(self, driverElement, attrId):
        Debug("Find by id: " + attrId)
        return driverElement.find_element_by_id(attrId)

    def __getElementByName(self, driverElement, attrName):
        Debug("Find by name: " + attrName)
        return driverElement.find_element_by_name(attrName)

    def __getElementByClass(self, driverElement, attrClass):
        Debug("Find by class: " + attrClass)
        return driverElement.find_element_by_class_name(attrClass)

    def __getElementByLinkText(self, driverElement, attrText):
        Debug("Find by link text: " + attrText)
        return driverElement.find_element_by_link_text(attrText)

    def __getElementByTag(self, driverElement, tag, config):
        Debug("Find by tag")
        if AFWConst.Attributes not in config:
            return None
        elements = driverElement.find_elements_by_tag_name(tag)
        for element in elements:
            isMatch = True
            for attribute in config[AFWConst.Attributes]:
                if element.get_attribute(attribute) != config[AFWConst.Attributes][attribute]:
                    isMatch = False
                    break
            if isMatch:
                return element
        return None
        
    def __getElementByType(self, driverElement, config):
        if config[AFWConst.Type] == AFWConst.WebLink and AFWConst.Text in config:
            return self.__getElementByLinkText(driverElement, config[AFWConst.Text])
        return None
    
    __browserFactory = {
        AFWConst.BrowserChrome: lambda : webdriver.Chrome(),
        AFWConst.BrowserIE: lambda : webdriver.Ie(),
        AFWConst.BrowserFireFox: lambda : webdriver.Firefox()
    }
            
        
