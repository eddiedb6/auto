from AFWClickable import AFWClickable

class AFWCheckable(AFWClickable):
    def __init__(self, plugin):
        AFWClickable.__init__(self, plugin)

    def IsChecked(self):
        return self._uiplugin.IsChecked(self.GetID())
