{
    AFWConst.UI: {
        AFWConst.Name: "Root",
        AFWConst.Type: AFWConst.UIRoot,
        AFWConst.SubUI: [
            ImportFile("ConfigApp.py"),
            ImportFile("ConfigWeb.py")
        ]
    },

    AFWConst.Action: {
        AFWConst.SubAction: [
        {
            AFWConst.Script: "TestScript.py"
        }]
    }
}
