class AFWPlugin:
    def __init__(self):
        pass

    def GetElement(self, config, parentConfig):
        return None
    
    def SetFocus(self, ui):
        return False

    def Click(self, ui):
        return False

    def IsCheckboxChecked(self, ui):
        return False

    def IsEnabled(self, ui):
        return False

    def PressKey(self, ui, key):
        return False

    def ReleaseKey(self, ui, key):
        return False

    def GetText(self, ui):
        return None
