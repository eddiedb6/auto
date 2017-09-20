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
