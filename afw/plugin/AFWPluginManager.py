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
        plugin = AFWPluginManager.__plugins[name]
        if plugin[AFWConst.PluginInstance] is None:
            plugin[AFWConst.PluginInstance] = plugin[AFWConst.PluginClass]()
        return plugin[AFWConst.PluginInstance]        

    def __loadPlugin(self):
        pluginPath = os.path.split(os.path.realpath(__file__))[0]
        pattern = re.compile(r'^Plugin[\w]+\.py$')
        for path,directories, files in os.walk(pluginPath):
            for filename in files:
                if not pattern.match(filename):
                    continue
                pluginName = os.path.splitext(filename)[0]
                pluginModule = __import__(pluginName)
                if pluginModule:
                    Info("Load plugin: " + pluginName)
                    self.__plugins[pluginName] = {
                        AFWConst.PluginClass: getattr(pluginModule, pluginName),
                        AFWConst.PluginInstance: None
                    }
                else:
                    Error("Could not load plugin: " + pluginName)

    # __plugins = {
    #     name: {
    #         class: pluginClass,
    #         instance: pluginInstance
    #     },
    #     ...
    # }
    __plugins = {}
