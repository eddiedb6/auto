{
    SchemaConfigRoot: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.UI, AFWConst.Action)
        ]
    },
    AFWConst.UI: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type),
            CheckAsTypeFromKey(AFWConst.Type)
        ]
    },
    AFWConst.UIRoot: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIApp: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.Path)
        ]
    },
    AFWConst.UIWeb: {
        SchemaInherit: AFWConst.UIApp
    },
    AFWConst.Plugin: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.PluginType)
        ]
    },
    AFWConst.AppRoot: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppButton: {
        SchemaInherit: AFWConst.AppRoot
    },
    AFWConst.AppForm: {
        SchemaInherit: AFWConst.AppRoot
    },
    AFWConst.Path: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ]
    },
    AFWConst.Name: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ]
    },
    AFWConst.Type: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.UIType)
        ]
    },
    AFWConst.SubUI: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType(AFWConst.UI)
        ]
    },
    AFWConst.Caption: {
        SchemaType: SchemaTypeString
    },
    AFWConst.BreakTime: {
        SchemaType: SchemaTypeInteger
    },
    AFWConst.Text: {
        SchemaType: SchemaTypeString
    },
    AFWConst.Script: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ]
    },
    AFWConst.Action: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            AtLeastOneKey(AFWConst.SubAction, AFWConst.Script)
        ]
    },
    AFWConst.SubAction: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType(AFWConst.Action)
        ]
    }
}
