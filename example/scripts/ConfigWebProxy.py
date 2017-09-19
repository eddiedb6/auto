{
    AFWConst.Name: "Web",
    AFWConst.Type: AFWConst.UIWeb,
    AFWConst.Plugin: {
        AFWConst.PluginName: AFWConst.PluginProxyWeb,
        AFWConst.Proxy: {
            AFWConst.ProxyType: AFWConst.ProxyLocal,
            AFWConst.ProxyLauncher: "python",
            AFWConst.PluginName: "PluginSelenium"
        }
    },
    AFWConst.Browser: AFWConst.BrowserChrome,
    AFWConst.SubUI: [
        ImportFile("ConfigWebBaidu.py")
    ]
}
