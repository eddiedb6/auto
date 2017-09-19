import AFWConst

from AFWWebUI import AFWWebUI

class AFWWebPage(AFWWebUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebUI.__init__(self, manager, configID, parentConfigID)
        if self.GetParentConfig()[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web page parent is not browser")
        parentUI = manager.GetUI(self._parentId)
        if parentUI is None:
            raise Exception("Web page parent is not bound")
        self._nativeId = parentUI.GetNativeUIID()
        if self._nativeId is None:
            raise Exception("Browser is not open")
