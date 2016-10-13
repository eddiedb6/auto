import AFWConst
from AFWAppElement import AFWAppElement

class AFWAppEditBox(AFWAppElement):
    def __init__(self, manager, config, parentConfig):
        AFWAppElement.__init__(self, manager, config, parentConfig)

    ### Implement AFWUI ###

    def IsEditable(self):
        return True
