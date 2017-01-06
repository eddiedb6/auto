import AFWConst
from AFWWebElement import AFWWebElement

class AFWWebEditBox(AFWWebElement):
    def __init__(self, manager, config, parentConfig):
        AFWWebElement.__init__(self, manager, config, parentConfig)
