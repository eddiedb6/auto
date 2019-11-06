from AFWConfigPool import AFWConfigPool

class AFWLocalConfigPool(AFWConfigPool):
    def __init__(self, uiManager):
        self.__uiManager = uiManager

    ### Implements AFWConfigPool ###

    def GetConfig(self, configID):
        return self.__uiManager.GetConfig(configID)

    def GetConfigDirty(self):
        return self.__uiManager.GetConfigDirty()

