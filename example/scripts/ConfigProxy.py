{
    AFWConst.UI: {
        AFWConst.Name: "Root",
        AFWConst.Type: AFWConst.UIRoot,
        AFWConst.SubUI: [
            ImportFile("ConfigAppProxy.py"),
            ImportFile("ConfigWebProxy.py")
        ]
    },

    AFWConst.Action: {
        AFWConst.SubAction: [
        {
            AFWConst.Script: "TestScript.py"
        }]
    }
}
