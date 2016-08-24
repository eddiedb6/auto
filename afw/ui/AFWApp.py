import AFWConst
from AFWUI import AFWUI

class AFWApp(AFWUI):
    def __init__(self, config):
        AFWUI.__init__(self, config, None)
        self.__plugin = self.GetPlugin(config[AFWConst.Plugin]) # TODO
