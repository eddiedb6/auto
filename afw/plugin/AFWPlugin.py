class AFWPlugin:
    def __init__(self):
        self._uiPool = {}

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

    def _loopTextArray(self, textArray, op):
        result = None
        for text in textArray:
            result = op(text)
            if result is not None:
                return result
        return None
