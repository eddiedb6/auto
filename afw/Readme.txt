1. Data Structure
    [Config Object] Loaded from config files, lives in UI manager
     `[UI Object] AFWUI instance, defines kinds of UI operations and lives in UI manager
        `[Native Object] Native object created from plugin, which implements AFWUI operations and lives in plugin
    * The three objects shared the same GUID, so could use one ID to find any of them

    a. Configure Object
        * Configure objects are defined as dictionary in config file
        * The entry key in config file is "AFWConst.UI"
        * When loaded to UI manager, there will be an uuid generated for each configure object and saved in map "AFWUIManager.__configPool" using the uuid as key
        * Meanwhile, the sub configure objects (which are defined as array) in parent configure object will be replaced as map using uuid as key
        * The UI parent children structure is saved in the configure objects level

    b. UI Object
        * When call "AFWUIManager.TryToFindUI", the configure object pool is searched
        * Whe the configure object is found, corresponding UI object is created
        * When UI object is saved in "AFWUIManager.__uiPool" as map using the uuid as key
        * When call "AFWUIManager.DumpUI", the UI object will be removed from the pool including its uuid
        * When call "AFWUI.Dump", the UI object and all its children will be dumped, including corresponding native object in plugin

    c. Native Object
        * Native object will be created in UI object constructure

2. How to add new UI type?
    Refer to AFWConst.py comments

3. How to add new plugin?
    Refer to AFWConst.py comments

4. How to write execution script?
    a. "afw" is the default variable name of AFWUIManagerWrapper instance
    b. User "afw" instance variable to execuete AFWUIManager operations, e.g. "afw.StartApp"
    c. When get AFWUI instance successfully, call its operations defined by AFWUI or its subclass

5. Plugin
    a. Plugin is named as "^Plugin[\w]+\.py$" and saved in plugin folder which is the same one as AFWPluginManager.py
    b. Plugin will be loaded and created only in following UI object constructor:
        AFWApp
        AFWAppRoot
        AFWWeb
    c. Proxy
    
[APIs]

AFW
    Load(path) -> bool
    Destroy()
    Execute() -> bool
    @LogLevel
    @BreakTime

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
    DumpUI(uiID) -> bool

AFWUI
 |  GetID() -> id
 |  GetParentID() -> id
 |  GetChildID(index) -> id
 |  GetConfig() -> dict
 |  GetParentConfig() -> dict
 |  GetChildConfig(index) -> dict	
 |  GetChildCount() -> int
 |  GetType() -> string
 |  GetName() -> string
 |  TryToFindSubUI(name) -> AFWUI
 |  FindSubUI(name) -> AFWUI, exception
 |  Dump() -> bool
 |  SetFocus() -> bool
 |  IsEnabled() -> bool
 |  PressKey(key) -> bool
 |  ReleaseKey(key) -> bool
 |  InputText(text) -> bool
 |  GetText() -> string
 `-AFWWebBase
    `-AFWWeb
       |  GetCurrentURL() -> string
       |  OpenURL(name) -> bool
       |  Quit() -> bool
       `-AFWWebUI
          `-AFWWebElement
	     `-AFWWebTable
	           GetCellText(row, column) -> string    

AFWAbility
 |-AFWClickable
 |  |  Click() -> bool
 |  `-AFWCheckable
 |        IsChecked() -> bool
 `-AFWSelectable
       Select(itemValue) -> bool

AFWPlugin
 |  GetElement(configID, parentConfigID) -> obj
 |  SetFocus(uiID) -> bool
 |  Click(uiID) -> bool
 |  Select(uiID, itemValue) -> bool
 |  IsChecked(uiID) -> bool
 |  IsEnabled(uiID) -> bool
 |  PressKey(uiID, key) -> bool
 |  ReleaseKey(uiID, key) -> bool
 |  GetText(uiID) -> string
 |  GetCellText(uiID, row, column) -> string
 |  DumpUI(uiID) -> bool
 |-AFWPluginApp
 |     StartApp(path, configID) -> id
 |     GetDesktop(configID) -> id
 |     GetForm(configID) -> id
 `-AFWPluginWeb
       OpenBrowser(name, configID) -> id
       CloseBrowser(browserID) -> bool
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
    |-AFWWebEntry (WebEntry)
    `-AFWWebUI
       |-AFWWebPage (WebPage)
       `-AFWWebElement (WebElement)
          |-AFWClickableElement (WebClickableElement)
          |-AFWWebPanel (WebPanel)
	  |-AFWWebTable (WebTable)
          |-AFWWebEditBox (WebEditBox)
	  |-AFWWebLink (WebLink)
	  |-AFWWebButton (WebButton)
	  `-AFWWebCombobox (WebCombobox)

AFWPlugin
 |-AFWPluginApp
 |  |-PluginMSApp
 |  `-PluginSocketApp
 `-AFWPluginWeb
    |-PluginSelenium
    `-PluginSocketWeb

[Messages]
MsgNameRegisterClient
    MsgParam1: guid
MsgNameCloseClient
MsgNameGetConfig
    MsgParam1: configID
MsgNameGetElement
    MsgParam1: configID
    MsgParam2: parentConfigID
MsgNameSetFocus
    MsgParam1: uiID
MsgNameClick
    MsgParam1: uiID
MsgNameSelect
    MsgParam1: uiID
    MsgParam2: item
MsgNameIsChecked
    MsgParam1: uiID
MsgNameIsEnabled
    MsgParam1: uiID
MsgNamePressKey
    MsgParam1: uiID
    MsgParam2: key
MsgNameReleaseKey
    MsgParam1: uiID
    MsgParam2: key
MsgNameGetText
    MsgParam1: uiID
MsgNameGetCellText
    MsgParam1: uiID
    MsgParam2: row
    MsgParam3: column
MsgNameDumpUI
    MsgParam1: uiID
MsgNameOpenBrowser
    MsgParam1: name
    MsgParam2: configID
MsgNameCloseBrowser
    MsgParam1: browserID
MsgNameOpenWebURL
    MsgParam1: browserID
    MsgParam2: url
    MsgParam3: configID
MsgNameGetCurrentURL
    MsgParam1: browserID
MsgNameGetWebPage
    MsgParam1: browserID
    MsgParam2: configID
MsgNameSendKeys
    MsgParam1: uiID
    MsgParam2: keys
MsgNameStartApp
    MsgParam1: path
    MsgParam2: configID
MsgNameGetDesktop
    MsgParam1: configID
MsgNameGetForm
    MsgParam1: configID
