{
    AFWConst.Name: "App",
    AFWConst.Type: AFWConst.UIApp,
    AFWConst.Path: "C:/Windows/System32/calc.exe",
    AFWConst.Plugin: {
        AFWConst.PluginName: AFWConst.PluginProxyApp,
        AFWConst.Proxy: {
            AFWConst.ProxyType: AFWConst.ProxyLocal,
            AFWConst.ProxyLauncher: "c:/App/IronPython-2.7.5/ipy.exe",
            AFWConst.PluginName: "PluginMSApp"
        }
    },
    AFWConst.SubUI: [
        ImportFile("ConfigAppDesktop.py")
    ]
}
