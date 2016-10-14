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
    FindUI(name)
    TryToFindUI(name)
    StartApp(name)
    TryToStartApp(name)
    GetBreakTime()

AFWUI
    GetType()
    GetName()
    GetConfig()
    GetParentConfig()
    GetChildrenCount()
    GetChild(index)
    GetNativeUI()
    IsEditable()
    IsEnabled()

AFWAppElement: AFWAppUI: AFWUI
    Click()

AFWPlugin
    SetFocus(ui)
    Click(ui)
    IsCheckboxChecked(ui)
    IsEnabled(ui)
    PressKey(ui, key)
    ReleaseKey(ui, key)

AFWPluginApp: AFWPlugin
    StartApp(path)
    GetDesktop()
    GetForm(config)
    GetElement(config, parentConfig)
    

