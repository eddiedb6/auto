1. Data Structure
    [Config Object] Loaded from config files, lives in UI manager
     `[UI Object] AFWUI instance, defines kinds of UI operations and lives in UI manager
        `[Native Object] Native object created from plugin, which implements AFWUI operations and lives in plugin
    * The three objects shared the same GUID, so could use one ID to find any of them

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
    FindWinForm(name) -> AFWAppForm, exception
    OpenWebBrowser(name) -> AFWWeb, exception
    
AFWUIManager
    GetConfig(configID) -> dict, exception
    GetUI(uiID) -> obj, exception
    TryToFindUI(name, parentUI) -> AFWUI
    StartApp(name) -> AFWApp, exception
    FindWinForm(name) -> AFWAppForm, exception	
    OpenWebBrowser(name) -> AFWWeb, exception
    GetBreakTime() -> int

AFWUI
 |  GetID() -> id
 |  GetParentID() -> id
 |  GetConfig() -> dict
 |  GetParentConfig() -> dict
 |  GetType() -> string
 |  GetName() -> string
 |  GetChildConfigCount() -> int
 |  GetChildConfig(index) -> dict
 |  TryToFindSubUI(name) -> AFWUI
 |  FindSubUI(name) -> AFWUI, exception
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
 `-AFWClickable
    |  Click() -> bool
    `-AFWCheckable
          IsChecked() -> bool

AFWPlugin
 |  GetElement(configID, parentConfigID) -> obj
 |  SetFocus(uiID) -> bool
 |  Click(uiID) -> bool
 |  IsChecked(uiID) -> bool
 |  IsEnabled(uiID) -> bool
 |  PressKey(uiID, key) -> bool
 |  ReleaseKey(uiID, key) -> bool
 |  GetText(uiID) -> string
 |-AFWPluginApp
 |     StartApp(path, configID) -> id
 |     GetDesktop(configID) -> id
 |     GetForm(configID) -> id
 `-AFWPluginWeb
       OpenBrowser(name, configID) -> id
       OpenWebURL(browserID, url, configID) -> bool
       GetCurrentURL(browserID) -> string
       GetWebPage(browserID, configID) -> id	
       SendKeys(uiID, keys) -> bool

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
       `-AFWWebElement (WebElement) 
          |-AFWWebEditBox (WebEditBox)
	  |-AFWWebLink (WebLink)
	  `-AFWWebButton (WebButton)

AFWPlugin
 |-AFWPluginApp
 |  |-PluginMSApp
 |  `-PluginSocketApp
 `-AFWPluginWeb
    |-PluginSelenium
    `-PluginSocketWeb
