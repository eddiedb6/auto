########################
# Consigure Schema Key #
########################

# To add a new key:
#     *. There is keygen.py script to help 

### Schema key definition start ###
UI = "ui"
SubUI = "subui"
Action = "action"
SubAction = "subaction"
Script = "script"
Name = "name"
Type = "type"
Plugin = "plugin"
PluginName = "pluginname"
Proxy = "proxy"
ProxyType = "proxytype"
ProxyLauncher = "proxylauncher"
Path = "path"
Browser = "browser"
URL = "url"
BreakTime = "breaktime"
Caption = "caption"
Text = "text"
AttrID = "attrid"
AttrName = "attrname"
AttrClass = "attrclass"
AttrTag = "attrtag"
Attributes = "attributes"
UICacheIndex = "uicacheindex"
IsDynamic = "isdynamic"
### Schema key definition end ###

######################
# AFW UI Type Define #
######################

# To add a new UI type:
#     1. Define here
#     2. Add new type to UIType collection in this file
#     3. Add new type class in afw/ui folder
#     4. Add new type to __uiFactory in AFWUIManager and import new py file in this manager
#     5. Add new type to AFWSchema
#     6. Update Readme description
#     *. There is uigen.py script to help except #6

UIRoot = "uiroot"

### UI types definition start ###
UIApp = "uiapp"
UIDesktop = "uidesktop"
UIForm = "uiform"
UIAppDialog = "uiappdialog"
UIAppTab = "uiapptab"
UIAppTabPage = "uiapptabpage"
UIBrowser = "uibrowser"
UIWebEntry = "uiwebentry"
UIWebPage = "uiwebpage"
UIWebTable = "uiwebtable"
UIWebLink = "uiweblink"
UIClickable = "uiclickable"
UICheckable = "uicheckable"
UIInputable = "uiinputable"
UISelectable = "uiselectable"
UIEditBox = "uieditbox"
UICommon = "uicommon"
### UI types definition end ###

UIType = [
### UI types collection start ###
    UIApp,
    UIDesktop,
    UIForm,
    UIAppDialog,
    UIAppTab,
    UIAppTabPage,
    UIBrowser,
    UIWebEntry,
    UIWebPage,
    UIWebTable,
    UIWebLink,
    UIClickable,
    UICheckable,
    UIInputable,
    UISelectable,
    UIEditBox,
    UICommon,
### UI types collection end ###
    UIRoot
]

AbilityNone = 0x00
AbilityClickable = 0x01
AbilityCheckable = 0x02
AbilityInputable = 0x04
AbilitySelectable = 0x08

###########
# Browser #
###########

# To add a new browser type:
#     1. Define here
#     2. Add new type to BrowserType collection in this file

### Browser type definition start ###
BrowserChrome = "browserchrome"
BrowserIE = "browserie"
BrowserFireFox = "browserfirefox"
### Browser type definition end ###

BrowserType = [
    BrowserChrome,
    BrowserIE,
    BrowserFireFox
]

##############
#   Plugin   #
##############

# To add a new plugin type:
#     1. Define here
#     2. Add new type to PluginType collection in this file
#     3. Add new plugin in afw/plugin folder

### Plugin type definition start ###
PluginMSApp = "PluginMSApp"
PluginSelenium = "PluginSelenium"
PluginProxyApp = "PluginProxyApp"
PluginProxyWeb = "PluginProxyWeb"
### Plugin type definition end ###

PluginType = [
    PluginMSApp,
    PluginSelenium,
    PluginProxyApp,
    PluginProxyWeb
]

#########
# Proxy #
#########

ProxyLocal = "proxylocal"
ProxyRemote = "proxyremote"

ProxyLocalEntry = "AFWProxyLocalClient.py"

ProxyHostPort = 51783
ProxyGUID = "proxyguid"

###########
# Message #
###########

MsgLength = 65495

MsgName = "msgname"
MsgParam1 = "msgparam1"
MsgParam2 = "msgparam2"
MsgParam3 = "msgparam3"
MsgParam4 = "msgparam4"
MsgParam5 = "msgparam5"
MsgParam6 = "msgparam6"
MsgParam7 = "msgparam7"
MsgParam8 = "msgparam8"
MsgParam9 = "msgparam9"
MsgResult = "msgresult"

MsgNameRegisterClient = "registerclient"
MsgNameCloseClient = "closeclient"

MsgNameCheckConfigDirty = "msgnamecheckconfigdirty"
MsgNameGetConfig = "msgnamegetconfig"
MsgNameGetElement = "msgnamegetelement"
MsgNameSetFocus = "msgnamesetfocus"
MsgNameClick = "msgnameclick"
MsgNameSelect = "msgnameselect"
MsgNameIsChecked = "msgnameischecked"
MsgNameIsEnabled = "msgnameisenabled"
MsgNamePressKey = "msgnamepresskey"
MsgNameReleaseKey = "msgnamereleasekey"
MsgNameGetText = "msgnamegettext"
MsgNameGetCellText = "msgnamegetcelltext"
MsgNameGetDynamicElement = "msgnamegetdynamicelement"
MsgNameGetAttribute = "msgnamegetattribute"
MsgNameDumpUI = "msgnamedumpui"
MsgNameOpenBrowser = "msgnameopenbrowser"
MsgNameCloseBrowser = "msgnameclosebrowser"
MsgNameOpenWebURL = "msgnameopenweburl"
MsgNameGetCurrentURL = "msgnamegetcurrenturl"
MsgNameGetWebPage = "msgnamegetwebpage"
MsgNameSendKeys = "msgnamesettext"
MsgNameStartApp = "msgnamestartapp"
MsgNameGetDesktop = "msgnamegetdesktop"
MsgNameGetForm = "msgnamegetform"
MsgNameSetText = "msgnamesettext"

################
# AFW Keyboard #
################

AFWKeyBackspace = 0x08
AFWKeyTab =       0x09
AFWKeyEnter =     0x0D

AFWKeyShift = 0x10
AFWKeyCtrl =  0x11
AFWKeyAlt =   0x12

AFWKeyCaps =  0x14
AFWKeyEsc =   0x1B
AFWKeySpace = 0x20
	
AFWKeyPageUp =   0x21
AFWKeyPageDown = 0x22
AFWKeyEnd =      0x23
AFWKeyHome =     0x24
AFWKeyLeft =     0x25
AFWKeyUp =       0x26
AFWKeyRight =    0x27
AFWKeyDown =     0x28
	
AFWKeyIns = 0x2D
AFWKeyDel = 0x2E
	
AFWKey0 = 0x30
AFWKey1 = 0x31
AFWKey2 = 0x32
AFWKey3 = 0x33
AFWKey4 = 0x34
AFWKey5 = 0x35
AFWKey6 = 0x36
AFWKey7 = 0x37
AFWKey8 = 0x38
AFWKey9 = 0x39

AFWKeyA = 0x41
AFWKeyB = 0x42
AFWKeyC = 0x43
AFWKeyD = 0x44
AFWKeyE = 0x45
AFWKeyF = 0x46
AFWKeyG = 0x47
AFWKeyH = 0x48
AFWKeyI = 0x49
AFWKeyJ = 0x4A
AFWKeyK = 0x4B
AFWKeyL = 0x4C
AFWKeyM = 0x4D
AFWKeyN = 0x4E
AFWKeyO = 0x4F
AFWKeyP = 0x50
AFWKeyQ = 0x51
AFWKeyR = 0x52
AFWKeyS = 0x53
AFWKeyT = 0x54
AFWKeyU = 0x55
AFWKeyV = 0x56
AFWKeyW = 0x57
AFWKeyX = 0x58
AFWKeyY = 0x59
AFWKeyZ = 0x5A
	
AFWKeyF1 =  0x70
AFWKeyF2 =  0x71
AFWKeyF3 =  0x72
AFWKeyF4 =  0x73
AFWKeyF5 =  0x74
AFWKeyF6 =  0x75
AFWKeyF7 =  0x76
AFWKeyF8 =  0x77
AFWKeyF9 =  0x78
AFWKeyF10 = 0x79
AFWKeyF11 = 0x7A
AFWKeyF12 = 0x7B

AFWKeySemicolon = 0xBA # ":"
AFWKeyPlus =      0xBB # "+"
AFWKeyComma =     0xBC # ","
AFWKeyMinus =     0xBD # "-"
AFWKeyPeriod =    0xBE # "."
AFWKeySlash =     0xBF # "/"
AFWKeyTidle =     0xC0 # "~"

AFWKeyBracketLeft =  0xDB # "["
AFWKeyBackslash =    0xDC # "\"
AFWKeyBracketRight = 0xDD # "]"
AFWKeyQuote =        0xDE # "'"

############
# HTML TAG #
############
TagDiv = "div"
TagA = "a"

##############
#  AFW ONLY  #
##############
UIObj = "uiobj"
PluginClass = "pluginclass"
PluginInstance = "plugininstance"


	
