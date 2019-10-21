from AFWAbility import AFWAbility

class AFWInputable(AFWAbility):
    def __init__(self, plugin):
        AFWAbility.__init__(self, plugin)

    def Input(self, text):
        return self._uiplugin.SetText(self.GetID(), text)
