import AFWConst
import AFWUIUtil
from AFWUI import AFWUI


class AFWAppBase(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)

    ### Implement AFWUI ###

    def InputText(self, text):
        for char in text:
            key, needShift = AFWUIUtil.GetKeyFromChar(char)
            if key is None:
                continue
            if needShift:
                self.PressKey(AFWConst.AFWKeyShift)
            self.PressKey(key)
            self.ReleaseKey(key)
            if needShift:
                self.ReleaseKey(AFWConst.AFWKeyShift)
        return True
