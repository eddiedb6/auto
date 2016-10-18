{
    SchemaConfigRoot: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.UI, AFWConst.Action)
        ]
    },

    ### Root ###
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
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Path, AFWConst.Plugin)
        ]
    },
    AFWConst.UIWeb: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Plugin, AFWConst.Browser)
        ]
    },

    ### Plugin ###
    AFWConst.Plugin: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.PluginType)
        ]
    },

    ### App Types ###
    AFWConst.AppRoot: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppForm: {
        SchemaInherit: AFWConst.AppRoot
    },
    AFWConst.AppSubForm: {
        SchemaInherit: AFWConst.AppRoot
    },
    AFWConst.AppTab: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.SubUI)
        ]
    },
    AFWConst.AppTabPage: {
        SchemaInherit: AFWConst.AppRoot
    },
    AFWConst.AppButton: {
        SchemaInherit: AFWConst.AppRoot
    },
    AFWConst.AppCheckbox: {
        SchemaInherit: AFWConst.AppRoot
    },
    AFWConst.AppEditBox: {
        SchemaInherit: AFWConst.AppRoot
    },

    ### Web Types ###
    AFWConst.WebSite: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.URL)
        ]
    },

    ### Properties ###
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

    AFWConst.URL: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ]
    },
    AFWConst.Browser: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.BrowserType)
        ]
    },
    
    ### Action ###
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
