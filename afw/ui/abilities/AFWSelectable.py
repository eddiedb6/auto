from AFWAbility import AFWAbility

class AFWSelectable(AFWAbility):
    def __init__(self, plugin):
        AFWAbility.__init__(self, plugin)
    
    def Select(self, itemValue):
        return self._uiplugin.Select(self.GetID(), itemValue)
