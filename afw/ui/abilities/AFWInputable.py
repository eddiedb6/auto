import AFWConst
from AFWAbility import AFWAbility

class AFWInputable(AFWAbility):
    def __init__(self, plugin):
        AFWAbility.__init__(self, plugin)
        self._ability = AFWConst.AbilityInputable
        self._abilityObj = self # Tricky because _abilityObj belongs to another parent

    def Input(self, text):
        return self._uiplugin.SetText(self.GetID(), text)
