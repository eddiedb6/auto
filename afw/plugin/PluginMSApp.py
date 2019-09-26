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
        if parentConfigID is None:
            return None
        config = self._getConfig(configID)
        parentConfig = self._getConfig(parentConfigID)
        parentNative = self._getNative(parentConfigID)
        Debug("Get element: " + config[AFWConst.Name])
        op = lambda text: MS.MSWrapper.TryGetElementByText(text, parentNative)
        element = None
        if AFWConst.Text in config:
            element = AFWPluginUtil.LoopTextArray(config[AFWConst.Text], op)
        elif AFWConst.Caption in config:
            element = AFWPluginUtil.LoopTextArray(config[AFWConst.Caption], op)
        else:
            element = MS.MSWrapper.TryGetElementByType(config[AFWConst.Type], parentNative)
        if element is not None:
            self._addNative(configID, element)
            return configID
        return None

    def SetFocus(self, uiID):
        if uiID is None:
            return False
        return MS.MSWrapper.SetFocus(self._getNative(uiID))

    def Click(self, uiID):
        if uiID is None:
            return False
        return MS.MSWrapper.Click(self._getNative(uiID))

    def Select(self, uiID, itemValue):
        if uiID is None:
            return False
        # [TODO]
        return False

    def IsChecked(self, uiID):
        if uiID is None:
            return False
        config = self._getConfig(uiID)
        if config[AFWConst.Type] != AFWConst.AppCheckbox:
            return False
        return MS.MSWrapper.IsCheckboxChecked(self._getNative(uiID))

    def IsEnabled(self, uiID):
        if uiID is None:
            return False
        return MS.MSWrapper.IsEnabled(self._getNative(uiID))

    def PressKey(self, uiID, key):
        MS.MSWrapper.SendKeyEvent(key, 0, 0, 0)
        return True

    def ReleaseKey(self, uiID, key):
        MS.MSWrapper.SendKeyEvent(key, 0, 2, 0)
        return True

    def GetText(self, uiID):
        if uiID is None:
            return None
        return MS.MSWrapper.GetText(self._getNative(uiID))

    def GetCellText(self, uiID, row, column):
        if uiID is None:
            return None
        # [TODO]
        return None

    ### Implement AFWPluginApp ###

    def StartApp(self, path, configID):
        Info("Start app: " + path)
        app = MS.MSWrapper.StartApp(path)
        if app is not None:
            self._addNative(configID, app)
            return configID
        return None

    def GetDesktop(self, configID):
        desktop = MS.MSWrapper.GetDesktop()
        if desktop is not None:
            self._addNative(configID, desktop)
            return configID
        return None

    def GetForm(self, configID):
        config = self._getConfig(configID)
        Debug("Get form: " + config[AFWConst.Name])
        op = lambda text: MS.MSWrapper.GetForm(text)
        form = AFWPluginUtil.LoopTextArray(config[AFWConst.Caption], op)
        if form is not None:
            self._addNative(configID, form)
            return configID
        return None
                                       
