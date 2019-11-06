import AFWConst
from AFWAbility import AFWAbility

class AFWExecutable(AFWAbility):
    def __init__(self, plugin):
        AFWAbility.__init__(self, plugin)
        self._ability = AFWConst.AbilityExecutable
        self._abilityObj = self # Tricky because _abilityObj belongs to another parent

    def ExecuteScript(self, script):
        return self._uiplugin.ExecuteScript(self.GetID(), script)
