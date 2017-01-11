[
    {
        # Application
        "Name": "UIApp",
        "Class": "AFWApp",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Path, AFWConst.Plugin)"
    },
    {
        # Desktop
        "Name": "AppRoot",
        "Class": "AFWAppRoot",
        "Parent": "AFWAppUI",
    },
    {
        # Windows Form
        "Name": "AppForm",
        "Class": "AFWAppForm",
        "Parent": "AFWAppUI",
    },
    {
        # Popup Dialog
        "Name": "AppSubForm",
        "Class": "AFWAppSubForm",
        "Parent": "AFWAppUI"
    },
    {
        "Name": "AppTab",
        "Class": "AFWAppTab",
        "Parent": "AFWAppElement",
        "SchemaRule": "HasKey(AFWConst.SubUI)"
    },
    {
        "Name": "AppTabPage",
        "Class": "AFWAppTabPage",
        "Parent": "AFWAppElement",
    },
    {
        "Name": "AppButton",
        "Class": "AFWAppButton",
        "Parent": "AFWAppElement",
        "Abilities": [
            "AFWClickable"
        ]
    },
    {
        "Name": "AppCheckbox",
        "Class": "AFWAppCheckbox",
        "Parent": "AFWAppElement",
        "Abilities": [
            "AFWCheckable"
        ]
    },
    {
        "Name": "AppEditBox",
        "Class": "AFWAppEditBox",
        "Parent": "AFWAppElement"
    },
    {
        # Browser
        "Name": "UIWeb",
        "Class": "AFWWeb",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Browser, AFWConst.Plugin)"
    },
    {
        # Web Page
        "Name": "WebPage",
        "Class": "AFWWebPage",
        "Parent": "AFWWebUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.URL)"
    },
    {
        "Name": "WebEditBox",
        "Class": "AFWWebEditBox",
        "Parent": "AFWWebElement"
    },
    {
        "Name": "WebLink",
        "Class": "AFWWebLink",
        "Parent": "AFWWebElement",
        "Abilities": [
            "AFWClickable"
        ]
    },
    {
        "Name": "WebButton",
        "Class": "AFWWebButton",
        "Parent": "AFWWebElement",
        "Abilities": [
            "AFWClickable"
        ]
    }
]
