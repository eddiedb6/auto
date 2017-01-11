{
    SchemaConfigRoot: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.UI, AFWConst.Action)
        ]
    },
    
### Schema key schema start ###
    AFWConst.UI: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            CheckAsTypeFromKey(AFWConst.Type)
        ],
    },
    AFWConst.SubUI: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType(AFWConst.UI)
        ],
    },
    AFWConst.Action: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            AtLeastOneKey(AFWConst.SubAction, AFWConst.Script)
        ],
    },
    AFWConst.SubAction: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType(AFWConst.Action)
        ],
    },
    AFWConst.Script: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ],
    },
    AFWConst.Name: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ],
    },
    AFWConst.Type: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.UIType)
        ],
    },
    AFWConst.Plugin: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.PluginType)
        ],
    },
    AFWConst.Path: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ],
    },
    AFWConst.Browser: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.BrowserType)
        ],
    },
    AFWConst.URL: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            NotEmpty(SchemaTypeString)
        ],
    },
    AFWConst.BreakTime: {
        SchemaType: SchemaTypeInteger
    },
    AFWConst.Caption: {
        SchemaType: SchemaTypeString
    },
    AFWConst.Text: {
        SchemaType: SchemaTypeString
    },
    AFWConst.AttrID: {
        SchemaType: SchemaTypeString
    },
    AFWConst.AttrName: {
        SchemaType: SchemaTypeString
    },
### Schema key schema end ###

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
    AFWConst.WebLink: {
        SchemaType: SchemaTypeDict
    },
    AFWConst.WebButton: {
        SchemaType: SchemaTypeDict
    },
### App types schema end ###

    AFWConst.UIRoot: {
        SchemaType: SchemaTypeDict
    }
}
