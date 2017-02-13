class AFWPlugin:
    def __init__(self):
        pass

    def GetElement(self, config, parentConfig):
        return None
    
    def SetFocus(self, ui):
        return False

    def Click(self, ui):
        return False

    def IsChecked(self, ui):
        return False

    def IsEnabled(self, ui):
        return False

    def PressKey(self, ui, key):
        return False

    def ReleaseKey(self, ui, key):
        return False

    def GetText(self, ui):
        return None

    def _loopTextArray(self, textArray, op):
        result = None
        for text in textArray:
            result = op(text)
            if result is not None:
                return result
        return None
