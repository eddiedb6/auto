import AFWConst
from AFWAbility import AFWAbility

class AFWCheckable(AFWAbility):
    def __init__(self, plugin):
        AFWAbility.__init__(self, plugin)
        self._ability = AFWConst.AbilityCheckable
        self._abilityObj = self # Tricky because _abilityObj belongs to another parent

    def IsChecked(self):
        return self._uiplugin.IsChecked(self.GetID())

    def Check(self):
        if self.IsChecked():
            return True
        return self._uiplugin.Click(self.GetID())

    def Uncheck(self):
        if self.IsChecked():
            return self._uiplugin.Click(self.GetID())
        return True

