[
    {
        "Name": "UI",
        "SchemaType": "SchemaTypeDict", 
        "SchemaRule": "CheckAsTypeFromKey(AFWConst.Type)"
    },
    {
        "Name": "SubUI",
        "SchemaType": "SchemaTypeArray",
        "SchemaRule": "CheckForeachAsType(AFWConst.UI)"
    },
    {
        "Name": "Action",
        "SchemaType": "SchemaTypeDict",
        "SchemaRule": "AtLeastOneKey(AFWConst.SubAction, AFWConst.Script)"
    },
    {
        "Name": "SubAction",
        "SchemaType": "SchemaTypeArray",
        "SchemaRule": "CheckForeachAsType(AFWConst.Action)"
    },
    {
        "Name": "Script",
        "SchemaType": "SchemaTypeString",
        "SchemaRule": "NotEmpty(SchemaTypeString)"
    },
    {
        "Name": "Name",
        "SchemaType": "SchemaTypeString",
        "SchemaRule": "NotEmpty(SchemaTypeString)"
    },
    {
        "Name": "Type",
        "SchemaType": "SchemaTypeString",
        "SchemaRule": "ValueIn(AFWConst.UIType)"
    },
    {
        "Name": "Plugin",
        "SchemaType": "SchemaTypeDict",
        "SchemaRule": "KeyIn([AFWConst.PluginName, AFWConst.Proxy]), HasKey(AFWConst.PluginName)"
    },
    {
        "Name": "PluginName",
        "SchemaType": "SchemaTypeString",
        "SchemaRule": "ValueIn(AFWConst.PluginType)"
    },
    {
        "Name": "Proxy",
        "SchemaType": "SchemaTypeDict",
        "SchemaRule": "KeyIn([AFWConst.ProxyType, AFWConst.ProxyLauncher, AFWConst.PluginName]), HasKey(AFWConst.ProxyType, AFWConst.ProxyLauncher, AFWConst.PluginName)"
    },
    {
        "Name": "ProxyType",
        "SchemaType": "SchemaTypeString",
        "SchemaRule": "ValueIn([AFWConst.ProxyLocal, AFWConst.ProxyRemote])"
    },
    {
        "Name": "ProxyLauncher",
        "SchemaType": "SchemaTypeString"
    },
    {
        "Name": "Path",
        "SchemaType": "SchemaTypeString",
        "SchemaRule": "NotEmpty(SchemaTypeString)"
    },
    {
        "Name": "Browser",
        "SchemaType": "SchemaTypeString",
        "SchemaRule": "ValueIn(AFWConst.BrowserType)"
    },
    {
        "Name": "URL",
        "SchemaType": "SchemaTypeString",
        "SchemaRule": "NotEmpty(SchemaTypeString)"
    },
    {
        "Name": "BreakTime",
        "SchemaType": "SchemaTypeInteger"
    },
    {
        "Name": "Caption",
        "SchemaType": "SchemaTypeArray",
        "SchemaRule": "CheckForeachAsType(AFWConst.Name)"
    },
    {
        "Name": "Text",
        "SchemaType": "SchemaTypeArray",
        "SchemaRule": "CheckForeachAsType(AFWConst.Name)"
    },
    {
        "Name": "AttrID",
        "SchemaType": "SchemaTypeString"
    },
    {
        "Name": "AttrName",
        "SchemaType": "SchemaTypeString"
    },
    {
        "Name": "AttrClass",
        "SchemaType": "SchemaTypeString"
    },
    {
        "Name": "AttrTag",
        "SchemaType": "SchemaTypeString"
    },
    {
        "Name": "Attributes",
        "SchemaType": "SchemaTypeDict"
    }
]
