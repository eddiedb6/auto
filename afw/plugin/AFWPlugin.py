class AFWPlugin:
    def __init__(self, pluginConfig, uiConfigPool):
        self._configPool = uiConfigPool
        self._nativePool = {}

    def GetNative(self, nativeID):
        if nativeID not in self._nativePool:
            raise Exception("No native ID exsists: " + nativeID)
        return self._nativePool[nativeID]

    def AddNative(self, nativeID, native):
        if nativeID in self._nativePool:
            raise Exception("Native ID exsists already: " + nativeID)
        self._nativePool[nativeID] = native

    def GetElement(self, configID, parentConfigID):
        return None
    
    def SetFocus(self, uiID):
        return False

    def Click(self, uiID):
        return False

    def IsChecked(self, uiID):
        return False

    def IsEnabled(self, uiID):
        return False

    def PressKey(self, uiID, key):
        return False

    def ReleaseKey(self, uiID, key):
        return False

    def GetText(self, uiID):
        return None

