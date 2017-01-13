[
    {
        # Application
        "Name": "UIApp",
        "Class": "AFWApp",
        "Parent": "AFWAppBase",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Path, AFWConst.Plugin)"
    },
    {
        # Desktop
        "Name": "AppRoot",
        "Class": "AFWAppRoot",
        "Parent": "AFWAppUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        # Windows Form
        "Name": "AppForm",
        "Class": "AFWAppForm",
        "Parent": "AFWAppUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        # Popup Dialog
        "Name": "AppSubForm",
        "Class": "AFWAppSubForm",
        "Parent": "AFWAppUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "AppTab",
        "Class": "AFWAppTab",
        "Parent": "AFWAppElement",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.SubUI)"
    },
    {
        "Name": "AppTabPage",
        "Class": "AFWAppTabPage",
        "Parent": "AFWAppElement",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "AppButton",
        "Class": "AFWAppButton",
        "Parent": "AFWAppElement",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)",
        "Abilities": [
            "AFWClickable"
        ]
    },
    {
        "Name": "AppCheckbox",
        "Class": "AFWAppCheckbox",
        "Parent": "AFWAppElement",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)",
        "Abilities": [
            "AFWCheckable"
        ]
    },
    {
        "Name": "AppEditBox",
        "Class": "AFWAppEditBox",
        "Parent": "AFWAppElement",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        # Browser
        "Name": "UIWeb",
        "Class": "AFWWeb",
        "Parent": "AFWWebBase",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Browser, AFWConst.Plugin)"
    },
    {
        # Web Page
        "Name": "WebPage",
        "Class": "AFWWebPage",
        "Parent": "AFWWebUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "WebElement",
        "Class": "AFWWebElement",
        "Parent": "AFWWebUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "WebEditBox",
        "Class": "AFWWebEditBox",
        "Parent": "AFWWebElement",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "WebLink",
        "Class": "AFWWebLink",
        "Parent": "AFWWebElement",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)",
        "Abilities": [
            "AFWClickable"
        ]
    },
    {
        "Name": "WebButton",
        "Class": "AFWWebButton",
        "Parent": "AFWWebElement",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)",
        "Abilities": [
            "AFWClickable"
        ]
    },
    {
        "Name": "WebURL",
        "Class": "AFWWebURL",
        "Parent": "AFWWebBase",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.URL)"
    }
]
