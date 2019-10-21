import AFWConst
from AFWAbility import AFWAbility

class AFWSelectable(AFWAbility):
    def __init__(self, plugin):
        AFWAbility.__init__(self, plugin)
        self._ability = AFWConst.AbilitySelectable
        self._abilityObj = self # Tricky because _abilityObj belongs to another parent

    def Select(self, itemValue):
        return self._uiplugin.Select(self.GetID(), itemValue)
