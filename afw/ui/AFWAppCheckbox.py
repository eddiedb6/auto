import AFWConst
from AFWAppElement import AFWAppElement

class AFWAppCheckbox(AFWAppElement):
    def __init__(self, manager, config, parentConfig):
        AFWAppElement.__init__(self, manager, config, parentConfig)

    def IsChecked(self):
        return self._plugin.IsCheckboxChecked(self)
