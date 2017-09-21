import AFWConst

from AFWWebUI import AFWWebUI

class AFWWebPage(AFWWebUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWWebUI.__init__(self, manager, configID, parentConfigID)
        if self.GetParentConfig()[AFWConst.Type] != AFWConst.UIWeb:
            raise Exception("Web page parent is not browser")
        pageID = self._plugin.GetWebPage(parentConfigID, configID)
        if pageID is None:
            raise Exception("Failed to get web page: " + self.GetConfig(configID)[AFWConst.Name])
        
