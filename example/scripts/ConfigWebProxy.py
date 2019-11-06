{
    AFWConst.Name: "Web",
    AFWConst.Type: AFWConst.UIBrowser,
    AFWConst.Plugin: {
        AFWConst.PluginName: AFWConst.PluginProxyWeb,
        AFWConst.Proxy: {
            AFWConst.ProxyType: AFWConst.ProxyLocal,
            AFWConst.ProxyLauncher: "python",
            AFWConst.PluginName: "PluginSelenium"
        }
    },
    AFWConst.Browser: AFWConst.BrowserFireFox,
    AFWConst.SubUI: [
        ImportFile("ConfigWebBaidu.py")
    ]
}
