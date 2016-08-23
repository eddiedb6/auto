#############
#    Key    #
#############

UI = "UI"
Action = "action"

Name = "name"
Type = "type"
Path = "path"

SubUI = "subui"
SubAction = "subaction"

Caption = "caption"
Text = "text"
Script = "script"

BreakTime = "breaktime"

############
# UI Value #
############

# To add a new UI type:
#     1. Define here
#     2. Add new type to UIType collection in this file
#     3. Add new type class in afw/ui folder
#     4. Add new type to __uiFactory in AFWUIManager

# UI types definition #

UIRoot = "uiroot"
UIApp = "uiapp"
UIWeb = "uiweb"

AppRoot = "approot"
AppButton = "appbutton"
AppForm = "appform"

# UI types definition end #

UIType = [
    UIRoot,
    UIApp,
    UIWeb,

    AppRoot,
    AppButton,
    AppForm
]

##############
#   Plugin   #
##############

# To add a new plugin type:
#     1. Define here
#     2. Add new type to PluginType collection in this file
#     3. Add new plugin in afw/plugin folder
#     4. Add new plugin to __pluginFactory in AFWUIManager

Plugin = "plugin"

# Plugin type definition #
PluginMS = "pluginms"
PluginSelenium = "pluginselenium"
# Plugin type definition end #

PluginType = [
    PluginMS,
    PluginSelenium
]

##############
#  AFW ONLY  #
##############
UIObj = "uiobj"

