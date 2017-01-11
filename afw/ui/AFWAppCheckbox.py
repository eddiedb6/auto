import AFWConst
from AFWAppElement import AFWAppElement
from AFWCheckable import AFWCheckable

class AFWAppCheckbox(AFWAppElement, AFWCheckable):
    def __init__(self, manager, config, parentConfig):
        AFWAppElement.__init__(self, manager, config, parentConfig)
        AFWCheckable.__init__(self, self._plugin)
