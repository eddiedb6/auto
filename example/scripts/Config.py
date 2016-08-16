{
    AFWConst.UI: {
        AFWConst.Name: "App",
        AFWConst.Type: AFWConst.UIApp,
        AFWConst.Path: "C:/Windows/System32/calc.exe",
        AFWConst.SubUI: [
        {    
            AFWConst.Name: "Desktop",
            AFWConst.Type: AFWConst.AppRoot,
            AFWConst.SubUI: [
            {
                AFWConst.Name: "Main",
                AFWConst.Type: AFWConst.AppForm,
                AFWConst.Caption: "Calculator",
                AFWConst.BreakTime: 2000,
                AFWConst.SubUI: [
                {
                    AFWConst.Name: "1",
                    AFWConst.Type: AFWConst.AppButton,
                    AFWConst.Text: "1"
                },
                {
                    AFWConst.Name: "2",
                    AFWConst.Type: AFWConst.AppButton,
                    AFWConst.Text: "2"
                },
                {
                    AFWConst.Name: "3",
                    AFWConst.Type: AFWConst.AppButton,
                    AFWConst.Text: "3"
                }]
            }]
        }]
    },

    AFWConst.Action: {
        AFWConst.SubAction: [
        {
            AFWConst.Script: "scripts/Test.py"
        }]
    }
}
