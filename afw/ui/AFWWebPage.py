import AFWConst

from AFWWebUI import AFWWebUI

class AFWWebPage(AFWWebUI):
    def __init__(self, manager, config, parentConfig):
        AFWWebUI.__init__(self, manager, config, parentConfig)
        if parentConfig[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web page parent is not browser")
        self._native = parentConfig[AFWConst.UIObj].GetNativeUI()
        if self._native is None:
            raise Exception("Browser is not open")
