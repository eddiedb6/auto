import AFWConst
from AFWUI import AFWUI

class AFWAppRoot(AFWUI):
    def __init__(self, manager, config, parent):
        AFWUI.__init__(self, manager, config, parent)
        self.__root = self._plugin.GetDesktop()
        if not self.__root:
            raise Exception("Failed to get App root")
