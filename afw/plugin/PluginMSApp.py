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

    def StartApp(self, path):
        Info("Start app: " + path)
        return MS.MSWrapper.StartApp(path)

    def GetDesktop(self):
        return MS.MSWrapper.GetDesktop()

    def GetForm(self, config):
        Debug("Get form: " + config[AFWConst.Name])
        return MS.MSWrapper.GetForm(config[AFWConst.Caption])

    def GetElement(self, config, parent):
        Debug("Get element: " + config[AFWConst.Name])
        if AFWConst.UIObj not in parent:
            Error("Parent is not bound yet: " + parent[AFWConst.Name])
            return None
        return MS.MSWrapper.GetElementByTextDescendant(config[AFWConst.Text], parent[AFWConst.UIObj].GetNativeUI())

    

