1. Data Structure
    [Config Object] Loaded from config files
     `[UI Object] AFWUI instance, defines kinds of UI operations 
        `[Native Object] Native object created from plugin, which implements AFWUI operations

2. How to add new UI type?
    Refer to AFWConst.py comments

3. How to add new plugin?
    Refer to AFWConst.py comments

4. How to write execution script?
    a. "afw" is the default variable name of AFWUIManager instance
    b. User "afw" instance variable to execuete AFWUIManager operations to get AFWUI instance, e.g. "afw.FindUI"
    c. When get AFWUI instance successfully, call its operations defined by AFWUI or its subclass

[APIs]

AFWUIManager
    FindUI(name) -> obj, exception
    TryToFindUI(name) -> obj
    StartApp(name) -> obj, exception
    TryToStartApp(name) -> obj
    OpenWebSite(name) -> obj, exception
    TryToOpenWebSite(name) -> obj
    GetBreakTime() -> int

AFWUI
    GetType() -> string
    GetName() -> string
    GetConfig() -> obj
    GetParentConfig() -> obj
    GetChildrenCount() -> int
    GetChild(index) -> obj
    GetNativeUI() -> obj
    IsEditable() -> bool
    IsEnabled() -> bool
    SetFocus() -> bool
    PressKey(key) -> bool
    ReleaseKey(key) -> bool
    InputText(text) -> bool
    GetText() -> string
    Click() -> bool

AFWPlugin
    SetFocus(ui) -> bool
    Click(ui) -> bool
    IsCheckboxChecked(ui) -> bool
    IsEnabled(ui) -> bool
    PressKey(ui, key) -> bool
    ReleaseKey(ui, key) -> bool
    GetText(ui) -> string

AFWPluginApp: AFWPlugin
    StartApp(path) -> obj
    GetDesktop() -> obj
    GetForm(config) -> obj
    GetElement(config, parentConfig) -> obj

AFWPluginWeb: AFWPlugin
    OpenBrowser(name) -> obj
    OpenWebSite(browser, url) -> bool

[Classes]

AFWUI
 |-AFWApp (UIApp)
 |-AFWAppUI
 |  |-AFWAppRoot (AppRoot) 
 |  |-AFWAppForm (AppForm)
 |  |-AFWAppSubForm (AppSubForm)
 |  `-AFWAppElement
 |     |-AFWAppTab (AppTab)
 |     |-AFWAppTabPage (AppTabPage)
 |     |-AFWAppEditBox (AppEditBox)
 |     |-AFWAppCheckbox (AppCheckbox)
 |     `-AFWAppButton (AppButton)
 |-AFWWeb (UIWeb)
 |-AFWWebSite (WebSite)
 `-AFWWebUI
    
    

