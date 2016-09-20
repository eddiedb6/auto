import os
import re

import AFWConst
from AFWLogger import *

class AFWPluginManager: 
    def __init__(self):
        pass

    def GetPlugin(self, name):
        if len(AFWPluginManager.__plugins) <= 0:
            self.__loadPlugin()
        if name in AFWPluginManager.__plugins:
            return self.__createPlugin(name)
        Warning("Could not find plugin: " + name)
        return None

    def __createPlugin(self, name):
        if name not in AFWPluginManager.__plugins:
            Error("Plugin name is not correct: " + name)
            return None
        if AFWPluginManager.__plugins[name] is not None:
            if AFWConst.PluginInstance in AFWPluginManager.__plugins[name]:
                return AFWPluginManager.__plugins[name][AFWConst.PluginInstance]
            else:
                Error("Plugin instance is missing: " + name)
                return None
        # Actually load plugin
        pluginModule = __import__(name)
        if pluginModule:
            Info("Load plugin: " + name)
            AFWPluginManager.__plugins[name] = {
                AFWConst.PluginClass: getattr(pluginModule, name),
                AFWConst.PluginInstance: None
            }
        else:
            Error("Could not load plugin: " + name)
            return None
        plugin = AFWPluginManager.__plugins[name]
        if plugin[AFWConst.PluginInstance] is None:
            plugin[AFWConst.PluginInstance] = plugin[AFWConst.PluginClass]()
        return plugin[AFWConst.PluginInstance]        

    def __loadPlugin(self):
        pluginPath = os.path.split(os.path.realpath(__file__))[0]
        pattern = re.compile(r'^Plugin[\w]+\.py$')
        for path, directories, files in os.walk(pluginPath):
            for filename in files:
                if not pattern.match(filename):
                    continue
                pluginName = os.path.splitext(filename)[0]
                # Assign to None, because plugin will be loaded only when it's needed
                self.__plugins[pluginName] = None

    # __plugins = {
    #     name: {
    #         class: pluginClass,
    #         instance: pluginInstance
    #     },
    #     ...
    # }
    __plugins = {}
