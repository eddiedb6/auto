import AFWConst
from AFWUI import AFWUI

class AFWAppUI(AFWUI):
    def __init__(self, manager, config, parentConfig):
        AFWUI.__init__(self, manager, config, parentConfig)

    ### Implement AFWUI ###

    def IsEnabled(self):
        return self._plugin.IsEnabled(self)