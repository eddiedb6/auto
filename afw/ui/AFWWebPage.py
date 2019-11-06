import AFWConst

from AFWUI import AFWUI

class AFWWebPage(AFWUI):
    def __init__(self, manager, configID, parentConfigID):
        AFWUI.__init__(self, manager, configID, parentConfigID)
        if self.GetParentConfig()[AFWConst.Type] != AFWConst.UIWebEntry:
            raise Exception("Web page parent is not browser entry")
        pageID = self._plugin.GetWebPage(parentConfigID, configID)
        if pageID is None:
            raise Exception("Failed to get web page: " + self.GetConfig()[AFWConst.Name])
        
