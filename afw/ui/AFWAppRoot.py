import AFWConst
from AFWAppUI import AFWAppUI

class AFWAppRoot(AFWAppUI):
    def __init__(self, manager, config, parentConfig):
        AFWAppUI.__init__(self, manager, config, parentConfig)
        self.__root = self._plugin.GetDesktop()
        self._native = self.__root
        if self.__root is None:
            raise Exception("Failed to get App root")
