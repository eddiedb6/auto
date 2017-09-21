from AFWAbility import AFWAbility

class AFWClickable(AFWAbility):
    def __init__(self, plugin):
        AFWAbility.__init__(self, plugin)
    
    def Click(self):
        return self._uiplugin.Click(self.GetID())
