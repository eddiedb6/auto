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

    ### Plugin ###
    AFWConst.Plugin: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.PluginType)
        ]
    },

### App types schema start ###
    AFWConst.UIApp: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Path, AFWConst.Plugin)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppRoot: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppForm: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppSubForm: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppTab: {
        SchemaRule: [
            HasKey(AFWConst.SubUI)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppTabPage: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppButton: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppCheckbox: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppEditBox: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIWeb: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Browser, AFWConst.Plugin)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.WebPage: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.URL)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.WebEditBox: {
        SchemaType: SchemaTypeDict
    },
### App types schema end ###

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
