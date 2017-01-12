import AFWConst
from AFWUI import AFWUI
import AFWUIHelper

class AFWAppBase(AFWUI):
    def __init__(self, manager, config, parentConfig):
        AFWUI.__init__(self, manager, config, parentConfig)

    ### Implement AFWUI ###

    def InputText(self, text):
        for char in text:
            key, needShift = AFWUIHelper.GetKeyFromChar(char)
            if key is None:
                continue
            if needShift:
                self.PressKey(AFWConst.AFWKeyShift)
            self.PressKey(key)
            self.ReleaseKey(key)
            if needShift:
                self.ReleaseKey(AFWConst.AFWKeyShift)
        return True
