1. Data Structure
    [Config Object] Loaded from config files
     `[UI Object] AFWUI instance, defines kinds of UI operations 
        `[Native Object] Native object created from plugin, which implements AFWUI operations

2. How to add new UI type?
    Refer to AFWConst.py comments

3. How to add new plugin?
    Refer to AFWConst.py comments

4. How to write execution script?
    a. "afw" is the default variable name of AFWUIManagerWrapper instance
    b. User "afw" instance variable to execuete AFWUIManager operations, e.g. "afw.StartApp"
    c. When get AFWUI instance successfully, call its operations defined by AFWUI or its subclass

[APIs]

AFWUIManagerWrapper
    StartApp(name) -> AFWApp, exception
    OpenWebBrowser(name) -> AFWWeb, exception
    
AFWUIManager
    StartApp(name) -> AFWApp, exception
    OpenWebBrowser(name) -> AFWWeb, exception
    GetUIConfigPath(name) -> bool, list
    IsUIObjCreated(config) -> bool
    CreateUIObj(config, parentConfig) -> AFWUI
    GetBreakTime() -> int

AFWUI
 |  GetType() -> string
 |  GetName() -> string
 |  GetConfig() -> dict
 |  GetParentConfig() -> dict
 |  GetChildConfig(index) -> dict
 |  GetChildConfigCount() -> int
 |  GetNativeUI() -> obj
 |  FindSubUI(name) -> AFWUI, exception
 |  TryToFindSubUI(name) -> AFWUI
 |  SetFocus() -> bool
 |  IsEnabled() -> bool
 |  PressKey(key) -> bool
 |  ReleaseKey(key) -> bool
 |  InputText(text) -> bool
 |  GetText() -> string
 `-AFWWeb
       GetCurrentURL() -> string
       OpenURL(name) -> bool

AFWAbility
 `-AFWCickable
    |  Click() -> bool
    `-AFWCheckable
          IsChecked() -> bool

AFWPlugin
 |  GetElement(config, parentConfig) -> obj
 |  SetFocus(ui) -> bool
 |  Click(ui) -> bool
 |  IsChecked(ui) -> bool
 |  IsEnabled(ui) -> bool
 |  PressKey(ui, key) -> bool
 |  ReleaseKey(ui, key) -> bool
 |  GetText(ui) -> string
 |-AFWPluginApp
 |     StartApp(path) -> obj
 |     GetDesktop() -> obj
 |     GetForm(config) -> obj
 `-AFWPluginWeb
       OpenBrowser(name) -> obj
       OpenWebPage(browser, url) -> bool
       GetCurrentURL(browser) -> string
       SendKeys(ui, keys) -> bool

[Classes]

AFWUI
 |-AFWAppBase
 |  |-AFWApp (UIApp)
 |  `-AFWAppUI
 |     |-AFWAppRoot (AppRoot) 
 |     |-AFWAppForm (AppForm)
 |     |-AFWAppSubForm (AppSubForm)
 |     `-AFWAppElement
 |        |-AFWAppTab (AppTab)
 |        |-AFWAppTabPage (AppTabPage)
 |        |-AFWAppEditBox (AppEditBox)
 |        |-AFWAppCheckbox (AppCheckbox)
 |        `-AFWAppButton (AppButton)
 `-AFWWebBase
    |-AFWWeb (UIWeb)
    |-AFWWebURL (WebURL)
    `-AFWWebUI
       |-AFWWebPage (WebPage)
       `-AFWWebElement
          |-AFWWebEditBox (WebEditBox)
	  |-AFWWebLink (WebLink)
	  `-AFWWebButton (WebButton)
