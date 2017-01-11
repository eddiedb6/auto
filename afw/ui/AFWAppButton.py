import AFWConst
from AFWAppElement import AFWAppElement
from AFWClickable import AFWClickable

class AFWAppButton(AFWAppElement, AFWClickable):
    def __init__(self, manager, config, parentConfig):
        AFWAppElement.__init__(self, manager, config, parentConfig)
        AFWClickable.__init__(self, self._plugin)
