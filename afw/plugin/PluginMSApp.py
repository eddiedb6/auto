import os
import sys
import time

from AFWLogger import *
from AFWPluginApp import AFWPluginApp
import AFWConst
import AFWPluginUtil

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../plugin/ms/bin"))

import clr
clr.AddReferenceToFile("MS.dll")
import MS

class PluginMSApp(AFWPluginApp):
    def __init__(self, pluginConfig, uiConfigPool):
        AFWPluginApp.__init__(self, pluginConfig, uiConfigPool)

    ### Implement AFWPlugin ###

    def GetElement(self, configID, parentConfigID):
        config = self._configPool.GetConfig(configID)
        parentConfig = self._configPool.GetConfig(parentConfigID)
        parentNative = self.GetNative(parentConfigID)
        Debug("Get element: " + config[AFWConst.Name])
        op = lambda text: MS.MSWrapper.GetElementByTextInDescendantScope(text, parentNative)
        element = None
        if AFWConst.Text in config:
            element = AFWPluginUtil.LoopTextArray(config[AFWConst.Text], op)
            self.AddNative(configID, element)
            return configID
        elif AFWConst.Caption in config:
            element = AFWPluginUtil.LoopTextArray(config[AFWConst.Caption], op)
            self.AddNative(configID, element)
            return configID            
        element = MS.MSWrapper.GetElementByTypeInDescendantScope(config[AFWConst.Type], parentNative)
        self.AddNative(configID, element)
        return configID

    def SetFocus(self, uiID):
        if uiID is None:
            return False
        return MS.MSWrapper.SetFocus(self.GetNative(uiID))

    def Click(self, uiID):
        if uiID is None:
            return False
        return MS.MSWrapper.Click(self.GetNative(uiID))

    def IsChecked(self, uiID):
        if uiID is None:
            return False
        config = self._configPool.GetConfig(uiID)
        if config[AFWConst.Type] != AFWConst.AppCheckbox:
            return False
        return MS.MSWrapper.IsCheckboxChecked(self.GetNative(uiID))

    def IsEnabled(self, uiID):
        if uiID is None:
            return False
        return MS.MSWrapper.IsEnabled(self.GetNative(uiID))

    def PressKey(self, uiID, key):
        MS.MSWrapper.SendKeyEvent(key, 0, 0, 0)
        return True

    def ReleaseKey(self, uiID, key):
        MS.MSWrapper.SendKeyEvent(key, 0, 2, 0)
        return True

    def GetText(self, uiID):
        if uiID is None:
            return None
        return MS.MSWrapper.GetText(self.GetNative(uiID))

    ### Implement AFWPluginApp ###

    def StartApp(self, path, configID):
        Info("Start app: " + path)
        app = MS.MSWrapper.StartApp(path)
        self.AddNative(configID, app)
        return configID

    def GetDesktop(self, configID):
        desktop = MS.MSWrapper.GetDesktop()
        self.AddNative(configID, desktop)
        return configID

    def GetForm(self, configID):
        config = self._configPool.GetConfig(configID)
        Debug("Get form: " + config[AFWConst.Name])
        op = lambda text: MS.MSWrapper.GetForm(text)
        form = AFWPluginUtil.LoopTextArray(config[AFWConst.Caption], op)
        self.AddNative(configID, form)
        return configID
                                       
