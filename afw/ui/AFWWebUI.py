import AFWConst
from AFWUI import AFWUI

class AFWWebUI(AFWUI):
    def __init__(self, manager, config):
        AFWUI.__init__(self, manager, config, None)        
