from AFWAbility import AFWAbility

class AFWClickable(AFWAbility):
    def __init__(self, plugin):
        AFWAbility.__init__(self, plugin)
        self._ability = AFWConst.AbilityClickable
        self._abilityObj = self # Tricky because _abilityObj belongs to another parent

    def Click(self):
        return self._uiplugin.Click(self.GetID())
