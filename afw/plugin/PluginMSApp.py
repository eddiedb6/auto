import os
import sys
import time

from AFWLogger import *
from AFWPluginApp import AFWPluginApp
import AFWConst

sys.path.append(os.path.join(os.path.split(os.path.realpath(__file__))[0], "../../plugin/ms/bin"))

import clr
clr.AddReferenceToFile("MS.dll")
import MS

class PluginMSApp(AFWPluginApp):
    def __init__(self):
        AFWPluginApp.__init__(self)

    ### Implement AFWPlugin ###

    def SetFocus(self, ui):
        if ui is None:
            return False
        return MS.MSWrapper.SetFocus(ui.GetNativeUI())

    def Click(self, ui):
        if ui is None:
            return False
        return MS.MSWrapper.Click(ui.GetNativeUI())

    def IsCheckboxChecked(self, ui):
        if ui is None:
            return False
        if ui.GetType() != AFWConst.AppCheckbox:
            return False
        return MS.MSWrapper.IsCheckboxChecked(ui.GetNativeUI())

    def PressKey(self, ui, key):
        MS.MSWrapper.SendKeyEvent(key, 0, 0, 0)
        return True

    def ReleaseKey(self, ui, key):
        MS.MSWrapper.SendKeyEvent(key, 0, 2, 0)
        return True

    ### Implement AFWPluginApp ###

    def StartApp(self, path):
        Info("Start app: " + path)
        return MS.MSWrapper.StartApp(path)

    def GetDesktop(self):
        return MS.MSWrapper.GetDesktop()

    def GetForm(self, config):
        Debug("Get form: " + config[AFWConst.Name])
        return MS.MSWrapper.GetForm(config[AFWConst.Caption])

    def GetElement(self, config, parentConfig):
        Debug("Get element: " + config[AFWConst.Name])
        if AFWConst.UIObj not in parentConfig:
            Error("Parent is not bound yet: " + parentConfig[AFWConst.Name])
            return None
        if AFWConst.Text in config:
            return MS.MSWrapper.GetElementByTextInDescendantScope(config[AFWConst.Text], parentConfig[AFWConst.UIObj].GetNativeUI())
        elif AFWConst.Caption in config:
            return MS.MSWrapper.GetElementByTextInChildrenScope(config[AFWConst.Caption], parentConfig[AFWConst.UIObj].GetNativeUI())
        return MS.MSWrapper.GetElementByTypeInDescendantScope(config[AFWConst.Type], parentConfig[AFWConst.UIObj].GetNativeUI())

    

