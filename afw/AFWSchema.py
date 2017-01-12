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
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppForm: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppSubForm: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppTab: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.SubUI)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppTabPage: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppButton: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppCheckbox: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.AppEditBox: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
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
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.WebEditBox: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.WebLink: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.WebButton: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.WebURL: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.URL)
        ],
        SchemaType: SchemaTypeDict
    },
### App types schema end ###

    AFWConst.UIRoot: {
        SchemaType: SchemaTypeDict
    }
}
