[
    ### APP ###

    {
        # Application
        "Name": "UIApp",
        "Class": "AFWApp",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Path, AFWConst.Plugin)"
    },
    {
        # Desktop
        "Name": "UIDesktop",
        "Class": "AFWDesktop",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        # Windows Form
        "Name": "UIForm",
        "Class": "AFWForm",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        # Popup Dialog
        "Name": "UIAppDialog",
        "Class": "AFWAppDialog",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "UIAppTab",
        "Class": "AFWAppTab",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.SubUI)"
    },
    {
        "Name": "UIAppTabPage",
        "Class": "AFWAppTabPage",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },

    #### WEB ###

    {
        # Browser
        "Name": "UIBrowser",
        "Class": "AFWBrowser",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.Browser, AFWConst.Plugin)",
        "Abilities": [
            "AFWExecutable"
        ]
    },
    {
        "Name": "UIWebEntry",
        "Class": "AFWWebEntry",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type, AFWConst.URL)"
    },
    {
        # Web Page
        "Name": "UIWebPage",
        "Class": "AFWWebPage",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "UIWebTable",
        "Class": "AFWWebTable",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "UIWebLink",
        "Class": "AFWWebLink",
        "Parent": "AFWClickableUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },

    #### Common ###
    
    {
        "Name": "UIClickable",
        "Class": "AFWClickableUI",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)",
        "Abilities": [
            "AFWClickable"
        ]
    },
    {
        "Name": "UICheckable",
        "Class": "AFWCheckableUI",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)",
        "Abilities": [
            "AFWCheckable"
        ]
    },
    {
        "Name": "UIInputable",
        "Class": "AFWInputableUI",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)",
        "Abilities": [
            "AFWInputable"
        ]
    },
    {
        "Name": "UISelectable",
        "Class": "AFWSelectableUI",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)",
        "Abilities": [
            "AFWSelectable"
        ]
    },
    {
        "Name": "UIEditBox",
        "Class": "AFWEditBox",
        "Parent": "AFWInputableUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    },
    {
        "Name": "UICommon",
        "Class": "AFWCommon",
        "Parent": "AFWUI",
        "SchemaRule": "HasKey(AFWConst.Name, AFWConst.Type)"
    }
]
