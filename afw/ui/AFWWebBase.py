from AFWUI import AFWUI

class AFWWebBase(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
