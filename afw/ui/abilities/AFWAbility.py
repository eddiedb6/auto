import AFWConst

class AFWAbility:
    def __init__(self, plugin):
        self._uiplugin = plugin
        self._ability = AFWConst.AbilityNone

    def Get(self):
        return self._ability

class AFWAbilityChecker:
    def __init__(self, ability):
        self._ability = ability

    def IsClickable(self):
        return (self._ability.Get() & AFWConst.AbilityClickable)

    def IsCheckable(self):
        return (self._ability.Get() & AFWConst.AbilityCheckable)

    def IsInputable(self):
        return (self._ability.Get() & AFWConst.AbilityInputable)

    def IsSelectable(self):
        return (self._ability.Get() & AFWConst.AbilitySelectable)
