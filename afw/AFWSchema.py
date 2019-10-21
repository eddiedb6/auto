{
    SchemaConfigRoot: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            HasKey(AFWConst.UI, AFWConst.Action)
        ]
    },
    AFWConst.UIRoot: {
        SchemaType: SchemaTypeDict
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
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            KeyIn([AFWConst.PluginName, AFWConst.Proxy]), HasKey(AFWConst.PluginName)
        ],
    },
    AFWConst.PluginName: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn(AFWConst.PluginType)
        ],
    },
    AFWConst.Proxy: {
        SchemaType: SchemaTypeDict,
        SchemaRule: [
            KeyIn([AFWConst.ProxyType, AFWConst.ProxyLauncher, AFWConst.PluginName]), HasKey(AFWConst.ProxyType, AFWConst.ProxyLauncher, AFWConst.PluginName)
        ],
    },
    AFWConst.ProxyType: {
        SchemaType: SchemaTypeString,
        SchemaRule: [
            ValueIn([AFWConst.ProxyLocal, AFWConst.ProxyRemote])
        ],
    },
    AFWConst.ProxyLauncher: {
        SchemaType: SchemaTypeString
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
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType(AFWConst.Name)
        ],
    },
    AFWConst.Text: {
        SchemaType: SchemaTypeArray,
        SchemaRule: [
            CheckForeachAsType(AFWConst.Name)
        ],
    },
    AFWConst.AttrID: {
        SchemaType: SchemaTypeString
    },
    AFWConst.AttrName: {
        SchemaType: SchemaTypeString
    },
    AFWConst.AttrClass: {
        SchemaType: SchemaTypeString
    },
    AFWConst.AttrTag: {
        SchemaType: SchemaTypeString
    },
    AFWConst.Attributes: {
        SchemaType: SchemaTypeDict
    },
### Schema key schema end ###

### App types schema start ###
    AFWConst.UIApp: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Path, AFWConst.Plugin)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIDesktop: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIForm: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIAppDialog: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIAppTab: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.SubUI)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIAppTabPage: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIBrowser: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Browser, AFWConst.Plugin)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIWebEntry: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type, AFWConst.URL)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIWebPage: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIWebTable: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIWebLink: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIClickable: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UICheckable: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIInputable: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UISelectable: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UIEditBox: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
    AFWConst.UICommon: {
        SchemaRule: [
            HasKey(AFWConst.Name, AFWConst.Type)
        ],
        SchemaType: SchemaTypeDict
    },
### App types schema end ###

    # Schema for key in attributes
    SchemaAnyOther: {
        SchemaType: SchemaTypeString
    }
}
