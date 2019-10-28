class AFWPlugin:
    def __init__(self, pluginConfig, uiConfigPool):
        self.__configPool = uiConfigPool
        self.__nativePool = {}

    ### Need to be implement ###
        
    def GetElement(self, configID, parentConfigID):
        return None

    def GetDynamicElement(self, parentID, config):
        return None

    def SetFocus(self, uiID):
        return False

    def Click(self, uiID):
        return False

    def Select(self, uiID, itemValue):
        return False

    def IsChecked(self, uiID):
        return False

    def IsEnabled(self, uiID):
        return False

    def PressKey(self, uiID, key):
        return False

    def ReleaseKey(self, uiID, key):
        return False

    def SetText(self, uiID, text):
        return False

    def GetText(self, uiID):
        return None

    def GetCellText(self, uiID, row, column):
        return None

    def GetAttribute(self, uiID, name):
        return ""

    def DumpUI(self, uiID):
        if uiID in self.__nativePool:
            del self.__nativePool[uiID]
            return True
        return False
    
    ### Protected ###
    
    def _getConfig(self, configID):
        return self.__configPool.GetConfig(configID)

    def _getNative(self, nativeID):
        if nativeID not in self.__nativePool:
            raise Exception("No native ID exsists: " + nativeID)
        return self.__nativePool[nativeID]

    def _addNative(self, nativeID, native):
        if nativeID in self.__nativePool:
            raise Exception("Native ID exsists already: " + nativeID)
        self.__nativePool[nativeID] = native
