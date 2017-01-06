import sys
import time
import platform

# afw, default variable name for UI manager

if platform.system() == "Linux":
    web = afw.OpenWebBrowser("Web")
    page = web.FindSubUI("Baidu")

if platform.system() == "Windows":
    app = afw.StartApp("App")
    form = app.FindSubUI("Main")
    button1 = form.FindSubUI("1")

    # 1
    button1.Click()
    time.sleep(0.5)

    # +
    form.PressKey(AFWConst.AFWKeyShift)
    form.PressKey(AFWConst.AFWKeyPlus)
    form.ReleaseKey(AFWConst.AFWKeyPlus)
    form.ReleaseKey(AFWConst.AFWKeyShift)
    time.sleep(0.5)

    # 1
    button1.Click()
    time.sleep(0.5)
    
    # =
    form.PressKey(AFWConst.AFWKeyPlus)
    form.ReleaseKey(AFWConst.AFWKeyPlus)
