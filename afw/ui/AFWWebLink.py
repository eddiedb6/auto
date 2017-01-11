import AFWConst
from AFWWebElement import AFWWebElement

class AFWWebLink(AFWWebElement):
    def __init__(self, manager, config, parentConfig):
        AFWWebElement.__init__(self, manager, config, parentConfig)

    ### Implement AFWUI ###

    def Click(self):
        return self._plugin.Click(self)
