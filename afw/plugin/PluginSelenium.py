import AFWConst
import AFWPluginUtil

from AFWLogger import *
from AFWPluginWeb import AFWPluginWeb

from selenium import webdriver

class PluginSelenium(AFWPluginWeb):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPluginWeb.__init__(self, pluginConfig, uiConfigPool)

    ### Implement AFWPlugin ###

    def GetElement(self, configID, parentConfigID):
        if parentConfigID is None:
            return None
        driverElement = self.GetNative(parentConfigID)
        if driverElement is None:
            return None
        return self.__getElement(driverElement, configID, parentConfigID)

    def SetFocus(self, uiID):
        # Web element do not need focus
        return True
    
    def Click(self, uiID):
        if uiID is None:
            return False
        self.GetNative(uiID).click() # No return result
        return True

    def IsChecked(self, uiID):
        # TODO
        return False

    def IsEnabled(self, uiID):
        if uiID is None:
            return False
        return self.GetNative(uiID).is_enabled()

    def PressKey(self, uiID, key):
        # TODO
        return False

    def ReleaseKey(self, uiID, key):
        # TODO
        return False

    def GetText(self, uiID):
        if uiID is None:
            return None
        return self.GetNative(uiID).text
    
    ### Implement AFWPluginWeb ###
    
    def OpenBrowser(self, name, configID):
        Info("Open browser: " + name)
        if name in PluginSelenium.__browserFactory:
            browser = PluginSelenium.__browserFactory[name]()
            self.AddNative(configID, browser)
        else:
            Error("Browser type is not supported: " + name)
            return None
        return configID

    def OpenWebPage(self, browserID, url):
        Info("Open web page: " + url)
        if browserID is None:
            return False
        if url is None or len(url) <= 0:
            return False
        browser = self.GetNative(browserID)
        browser.get(url)
        return True

    def GetCurrentURL(self, browserID):
        if browserID is None:
            return None
        browser = self.GetNative(browserID)
        return browser.current_url

    def SendKeys(self, uiID, keys):
        if uiID is None:
            return False
        self.GetNative(uiID).send_keys(keys)
        return True
    
    ### Private ###

    def __getElement(self, driverElement, configID, parentConfigID):
        element = None
        config = self._configPool.GetConfig(configID)
        if AFWConst.AttrID in config:
            element = self.__getElementByID(driverElement, config[AFWConst.AttrID])
            if element is not None:
                self.AddNative(configID, element)
                return configID
        if AFWConst.AttrName in config:
            element = self.__getElementByName(driverElement, config[AFWConst.AttrName])
            if element is not None:
                self.AddNative(configID, element)
                return configID
        if AFWConst.AttrClass in config:
            element = self.__getElementByClass(driverElement, config[AFWConst.AttrClass])
            if element is not None:
                self.AddNative(configID, element)
                return configID
        if AFWConst.AttrTag in config:
            element = self.__getElementByTag(driverElement, config[AFWConst.AttrTag], config)
            if element is not None:
                self.AddNative(configID, element)
                return configID
        element = self.__getElementByType(driverElement, config)
        if element is not None:
            self.AddNative(configID, element)
            return configID
        return None

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
            op = lambda text: self.__getElementByLinkText(driverElement, text) 
            return AFWPluginUtil.LoopTextArray(config[AFWConst.Text], op)
        return None
    
    __browserFactory = {
        AFWConst.BrowserChrome: lambda : webdriver.Chrome(),
        AFWConst.BrowserIE: lambda : webdriver.Ie(),
        AFWConst.BrowserFireFox: lambda : webdriver.Firefox()
    }
            
        
