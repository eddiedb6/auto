import AFWConst
from AFWWebElement import AFWWebElement
from AFWClickable import AFWClickable

class AFWWebLink(AFWWebElement, AFWClickable):
    def __init__(self, manager, config, parentConfig):
        AFWWebElement.__init__(self, manager, config, parentConfig)
        AFWClickable.__init__(self, self._plugin)
