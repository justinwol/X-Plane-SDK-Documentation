---
title: "Plugin APIs"
description: "X-Plane SDK Plugin APIs documentation"
category: "XPLM_Plugin"
date: "2025-06-25T15:45:56.661425"
---

# Plugin APIs

### [Button Messages](/sdk/Button Messages/)

These messages are sent by the button to itself and then up the widget chain
when the button is clicked. (You may intercept them by providing a widget
handler for the button itself or by providing a handler in a parent widget.)

| Name | Value | Description |
| --- | --- | --- |
| [xpMsg_PushButtonPressed](/sdk/xpMsg_PushButtonPressed/) | "1300" | This
message is sent when the user completes a click and release in a button withpush
button behavior. Parameterone of the message is the widget ID of the button.
This message is dispatched up thewidget hierarchy. |
| [xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/) | "1301" | This
message is sent when a button is clicked that has radio button or check box
behaviorand its value changes. (Note that if the value changes by setting a
property you do not receivethis message!) Parameter one is the widget ID of the
button, parameter 2 is the new state value,either zero or one. This message is
dispatched up the widget hierarchy. |

### [Scroll Bar Messages](/sdk/Scroll Bar Messages/)

| Name | Value | Description |
| --- | --- | --- |
|
[xpMsg_ScrollBarSliderPositionChanged](/sdk/xpMsg_ScrollBarSliderPositionChanged/)
| "1500" | The scroll bar sends this message when the slider position changes.
It sends the message up the call chain; param1 is the scroll bar widget ID. |

### [Text Field Messages](/sdk/Text Field Messages/)

| Name | Value | Description |
| --- | --- | --- |
| [xpMsg_TextFieldChanged](/sdk/xpMsg_TextFieldChanged/) | "1400" | The text
field sends this message to itself when its text changes. It sends the message
up the call chain; param1 is the text field's widget ID. |

### [XPLMCountPlugins](/sdk/XPLMCountPlugins/)

```cpp
XPLM_API int        XPLMCountPlugins(void);

```

This routine returns the total number of plug-ins that are loaded, both disabled
and enabled.

### [XPLMDisablePlugin](/sdk/XPLMDisablePlugin/)

```cpp
XPLM_API void       XPLMDisablePlugin(
                         XPLMPluginID         inPluginID);

```

This routine disableds an enabled plug-in.

### [XPLMEnableFeature](/sdk/XPLMEnableFeature/)

```cpp
XPLM_API void       XPLMEnableFeature(
                         const char *         inFeature,
                         int                  inEnable);

```

This routine enables or disables a feature for your plugin. This will change the
running behavior of X-Plane and your plugin in some way, depending on the
feature.

### [XPLMEnablePlugin](/sdk/XPLMEnablePlugin/)

```cpp
XPLM_API int        XPLMEnablePlugin(
                         XPLMPluginID         inPluginID);

```

This routine enables a plug-in if it is not already enabled. It returns 1 if the
plugin was enabled or successfully enables itself, 0 if it does not. Plugins may
fail to enable (for example, if resources cannot be acquired) by returning 0
from their XPluginEnable callback.

### [XPLMFindPluginByPath](/sdk/XPLMFindPluginByPath/)

```cpp
XPLM_API XPLMPluginID XPLMFindPluginByPath(
                         const char *         inPath);

```

This routine returns the plug-in ID of the plug-in whose file exists at the
passed in absolute file system
path.[XPLM_NO_PLUGIN_ID](/sdk/XPLM_NO_PLUGIN_ID/)is returned if the path does
not point to a currently loaded plug-in.

### [XPLMFindPluginBySignature](/sdk/XPLMFindPluginBySignature/)

```cpp
XPLM_API XPLMPluginID XPLMFindPluginBySignature(
                         const char *         inSignature);

```

This routine returns the plug-in ID of the plug-in whose signature matches what
is passed in or[XPLM_NO_PLUGIN_ID](/sdk/XPLM_NO_PLUGIN_ID/)if no running plug-in
has this signature. Signatures are the best way to identify another plug-in as
they are independent of the file system path of a plug-in or the human-readable
plug-in name, and should be unique for all plug-ins. Use this routine to locate
another plugin that your plugin interoperates with

### [XPLMGetNthPlugin](/sdk/XPLMGetNthPlugin/)

```cpp
XPLM_API XPLMPluginID XPLMGetNthPlugin(
                         int                  inIndex);

```

This routine returns the ID of a plug-in by index. Index is 0 based from 0
to[XPLMCountPlugins](/sdk/XPLMCountPlugins/)-1, inclusive. Plugins may be
returned in any arbitrary order.

### [XPLMGetPluginInfo](/sdk/XPLMGetPluginInfo/)

```cpp
XPLM_API void       XPLMGetPluginInfo(
                         XPLMPluginID         inPlugin,
                         char *               outName,    /* Can be NULL */
                         char *               outFilePath,    /* Can be NULL */
                         char *               outSignature,    /* Can be NULL */
                         char *               outDescription);    /* Can be NULL */

```

This routine returns information about a plug-in. Each parameter should be a
pointer to a buffer of at least 256 characters, or NULL to not receive the
information.

outName - the human-readable name of the plug-in. outFilePath - the absolute
file path to the file that contains this plug-in. outSignature - a unique string
that identifies this plug-in. outDescription - a human-readable description of
this plug-in.

### [XPLMIsFeatureEnabled](/sdk/XPLMIsFeatureEnabled/)

```cpp
XPLM_API int        XPLMIsFeatureEnabled(
                         const char *         inFeature);

```

This returns 1 if a feature is currently enabled for your plugin, or 0 if it is
not enabled. It is an error to call this routine with an unsupported feature.

### [XPLMIsPluginEnabled](/sdk/XPLMIsPluginEnabled/)

```cpp
XPLM_API int        XPLMIsPluginEnabled(
                         XPLMPluginID         inPluginID);

```

Returns whether the specified plug-in is enabled for running.

# [XPLMPlugin](/sdk/XPLMPlugin/)API

These APIs provide facilities to find and work with other plugins and manage
other plugins.

## FINDING PLUGINS

These APIs allow you to find another plugin or yourself, or iterate across all
plugins. For example, if you wrote an FMS plugin that needed to talk to an
autopilot plugin, you could use these APIs to locate the autopilot plugin.

### [XPLMGetMyID](/sdk/XPLMGetMyID/)

```cpp
XPLM_API XPLMPluginID XPLMGetMyID(void);

```

This routine returns the plugin ID of the calling plug-in. Call this to get your
own ID.

### [XPLMCountPlugins](/sdk/XPLMCountPlugins/)

```cpp
XPLM_API int        XPLMCountPlugins(void);

```

This routine returns the total number of plug-ins that are loaded, both disabled
and enabled.

### [XPLMGetNthPlugin](/sdk/XPLMGetNthPlugin/)

```cpp
XPLM_API XPLMPluginID XPLMGetNthPlugin(
                         int                  inIndex);

```

This routine returns the ID of a plug-in by index. Index is 0 based from 0
to[XPLMCountPlugins](/sdk/XPLMCountPlugins/)-1, inclusive. Plugins may be
returned in any arbitrary order.

### [XPLMFindPluginByPath](/sdk/XPLMFindPluginByPath/)

```cpp
XPLM_API XPLMPluginID XPLMFindPluginByPath(
                         const char *         inPath);

```

This routine returns the plug-in ID of the plug-in whose file exists at the
passed in absolute file system
path.[XPLM_NO_PLUGIN_ID](/sdk/XPLM_NO_PLUGIN_ID/)is returned if the path does
not point to a currently loaded plug-in.

### [XPLMFindPluginBySignature](/sdk/XPLMFindPluginBySignature/)

```cpp
XPLM_API XPLMPluginID XPLMFindPluginBySignature(
                         const char *         inSignature);

```

This routine returns the plug-in ID of the plug-in whose signature matches what
is passed in or[XPLM_NO_PLUGIN_ID](/sdk/XPLM_NO_PLUGIN_ID/)if no running plug-in
has this signature. Signatures are the best way to identify another plug-in as
they are independent of the file system path of a plug-in or the human-readable
plug-in name, and should be unique for all plug-ins. Use this routine to locate
another plugin that your plugin interoperates with

### [XPLMGetPluginInfo](/sdk/XPLMGetPluginInfo/)

```cpp
XPLM_API void       XPLMGetPluginInfo(
                         XPLMPluginID         inPlugin,
                         char *               outName,    /* Can be NULL */
                         char *               outFilePath,    /* Can be NULL */
                         char *               outSignature,    /* Can be NULL */
                         char *               outDescription);    /* Can be NULL */

```

This routine returns information about a plug-in. Each parameter should be a
pointer to a buffer of at least 256 characters, or NULL to not receive the
information.

outName - the human-readable name of the plug-in. outFilePath - the absolute
file path to the file that contains this plug-in. outSignature - a unique string
that identifies this plug-in. outDescription - a human-readable description of
this plug-in.

## ENABLING/DISABLING PLUG-INS

These routines are used to work with plug-ins and manage them. Most plugins will
not need to use these APIs.

### [XPLMIsPluginEnabled](/sdk/XPLMIsPluginEnabled/)

```cpp
XPLM_API int        XPLMIsPluginEnabled(
                         XPLMPluginID         inPluginID);

```

Returns whether the specified plug-in is enabled for running.

### [XPLMEnablePlugin](/sdk/XPLMEnablePlugin/)

```cpp
XPLM_API int        XPLMEnablePlugin(
                         XPLMPluginID         inPluginID);

```

This routine enables a plug-in if it is not already enabled. It returns 1 if the
plugin was enabled or successfully enables itself, 0 if it does not. Plugins may
fail to enable (for example, if resources cannot be acquired) by returning 0
from their XPluginEnable callback.

### [XPLMDisablePlugin](/sdk/XPLMDisablePlugin/)

```cpp
XPLM_API void       XPLMDisablePlugin(
                         XPLMPluginID         inPluginID);

```

This routine disableds an enabled plug-in.

### [XPLMReloadPlugins](/sdk/XPLMReloadPlugins/)

```cpp
XPLM_API void       XPLMReloadPlugins(void);

```

This routine reloads all plug-ins. Once this routine is called and you return
from the callback you were within (e.g. a menu select callback) you will receive
your XPluginDisable and XPluginStop callbacks and your DLL will be unloaded,
then the start process happens as if the sim was starting up.

## INTERPLUGIN MESSAGING

Plugin messages are defined as 32-bit integers. Messages below 0x00FFFFFF are
reserved for X-Plane and the plugin SDK.

Messages come with a pointer parameter; the meaning of this pointer depends on
the message itself. In some messages, the pointer parameter contains an actual
typed pointer to data that can be inspected in the plugin; in these cases the
documentation will state that the parameter “points to” information.

in other cases, the value of the pointer is actually an integral number stuffed
into the pointer’s storage. In these second cases, the pointer parameter needs
to be cast, not dereferenced. In these caess, the documentation will state that
the parameter “contains” a value, which will always be an integral type.

Some messages don’t use the pointer parameter - in this case your plugin should
ignore it.

Messages have two conceptual uses: notifications and commands. Commands are sent
from one plugin to another to induce behavior; notifications are sent from one
plugin to all others for informational purposes. It is important that commands
and notifications not have the same values because this could cause a
notification sent by one plugin to accidentally induce a command in another.

By convention, plugin-defined notifications should have the high bit set (e.g.
be greater or equal to unsigned 0x8000000) while commands should have this bit
be cleared.

The following messages are sent to your plugin by X-Plane.

### [XPLM_MSG_PLANE_CRASHED](/sdk/XPLM_MSG_PLANE_CRASHED/)

```cpp
#define XPLM_MSG_PLANE_CRASHED 101
```

This message is sent to your plugin whenever the user’s plane crashes. The
parameter is ignored.

### [XPLM_MSG_PLANE_LOADED](/sdk/XPLM_MSG_PLANE_LOADED/)

```cpp
#define XPLM_MSG_PLANE_LOADED 102
```

This message is sent to your plugin whenever a new plane is loaded. The
parameter contains the index number of the plane being loaded; 0 indicates the
user’s plane.

### [XPLM_MSG_AIRPORT_LOADED](/sdk/XPLM_MSG_AIRPORT_LOADED/)

```cpp
#define XPLM_MSG_AIRPORT_LOADED 103
```

This messages is sent whenever the user’s plane is positioned at a new airport.
The parameter is ignored.

### [XPLM_MSG_SCENERY_LOADED](/sdk/XPLM_MSG_SCENERY_LOADED/)

```cpp
#define XPLM_MSG_SCENERY_LOADED 104
```

This message is sent whenever new scenery is loaded. Use datarefs to determine
the new scenery files that were loaded. The parameter is ignored.

### [XPLM_MSG_AIRPLANE_COUNT_CHANGED](/sdk/XPLM_MSG_AIRPLANE_COUNT_CHANGED/)

```cpp
#define XPLM_MSG_AIRPLANE_COUNT_CHANGED 105
```

This message is sent whenever the user adjusts the number of X-Plane aircraft
models. You must use XPLMCountPlanes to find out how many planes are now
available. This message will only be sent in XP7 and higher because in XP6 the
number of aircraft is not user-adjustable. The parameter is ignored.

### [XPLM_MSG_PLANE_UNLOADED](/sdk/XPLM_MSG_PLANE_UNLOADED/)

```cpp
#define XPLM_MSG_PLANE_UNLOADED 106
```

This message is sent to your plugin whenever a plane is unloaded. The parameter
contains the index number of the plane being unloaded; 0 indicates the user’s
plane. The parameter is of type int, passed as the value of the pointer. (That
is: the parameter is an int, not a pointer to an int.)

### [XPLM_MSG_WILL_WRITE_PREFS](/sdk/XPLM_MSG_WILL_WRITE_PREFS/)

```cpp
#define XPLM_MSG_WILL_WRITE_PREFS 107
```

This message is sent to your plugin right before X-Plane writes its preferences
file. You can use this for two purposes: to write your own preferences, and to
modify any datarefs to influence preferences output. For example, if your plugin
temporarily modifies saved preferences, you can put them back to their default
values here to avoid having the tweaks be persisted if your plugin is not loaded
on the next invocation of X-Plane. The parameter is ignored.

### [XPLM_MSG_LIVERY_LOADED](/sdk/XPLM_MSG_LIVERY_LOADED/)

```cpp
#define XPLM_MSG_LIVERY_LOADED 108
```

This message is sent to your plugin right after a livery is loaded for an
airplane. You can use this to check the new livery (via datarefs) and react
accordingly. The parameter contains the index number of the aircraft whose
livery is changing.

### [XPLM_MSG_ENTERED_VR](/sdk/XPLM_MSG_ENTERED_VR/)

```cpp
#define XPLM_MSG_ENTERED_VR  109
```

Sent to your plugin right before X-Plane enters virtual reality mode (at which
time any windows that are not positioned in VR mode will no longer be visible to
the user). The parameter is unused and should be ignored.

### [XPLM_MSG_EXITING_VR](/sdk/XPLM_MSG_EXITING_VR/)

```cpp
#define XPLM_MSG_EXITING_VR  110
```

Sent to your plugin right before X-Plane leaves virtual reality mode (at which
time you may want to clean up windows that are positioned in VR mode). The
parameter is unused and should be ignored.

### [XPLM_MSG_RELEASE_PLANES](/sdk/XPLM_MSG_RELEASE_PLANES/)

```cpp
#define XPLM_MSG_RELEASE_PLANES 111
```

Sent to your plugin if another plugin wants to take over AI planes. If you are a
synthetic traffic provider, that probably means a plugin for an online network
has connected and wants to supply aircraft flown by real humans and you should
cease to provide synthetic traffic. If however you are providing online traffic
from real humans, you probably don’t want to disconnect, in which case you just
ignore this message. The sender is the plugin ID of the plugin asking for
control of the planes now. You can use it to find out who is requesting and
whether you should yield to them. Synthetic traffic providers should always
yield to online networks. The parameter is unused and should be ignored.

### [XPLM_MSG_FMOD_BANK_LOADED](/sdk/XPLM_MSG_FMOD_BANK_LOADED/)

```cpp
#define XPLM_MSG_FMOD_BANK_LOADED 112
```

Sent to your plugin after FMOD sound banks are loaded. The parameter is
the[XPLMBankID](/sdk/XPLMBankID/)enum in[XPLMSound](/sdk/XPLMSound/).h, 0 for
the master bank and 1 for the radio bank.

### [XPLM_MSG_FMOD_BANK_UNLOADING](/sdk/XPLM_MSG_FMOD_BANK_UNLOADING/)

```cpp
#define XPLM_MSG_FMOD_BANK_UNLOADING 113
```

Sent to your plugin before FMOD sound banks are unloaded. Any associated
resources should be cleaned up at this point. The parameter is
the[XPLMBankID](/sdk/XPLMBankID/)enum in[XPLMSound](/sdk/XPLMSound/).h, 0 for
the master bank and 1 for the radio bank.

### [XPLM_MSG_DATAREFS_ADDED](/sdk/XPLM_MSG_DATAREFS_ADDED/)

```cpp
#define XPLM_MSG_DATAREFS_ADDED 114
```

Sent to your plugin per-frame (at-most) when/if datarefs are added. It will
include the new data ref total count so that your plugin can keep a local cache
of the total, see what’s changed and know which ones to inquire about if it
cares.

This message is only sent to plugins that enable the
XPLM_WANTS_DATAREF_NOTIFICATIONS feature.

### [XPLMSendMessageToPlugin](/sdk/XPLMSendMessageToPlugin/)

```cpp
XPLM_API void       XPLMSendMessageToPlugin(
                         XPLMPluginID         inPlugin,
                         int                  inMessage,
                         void *               inParam);

```

This function sends a message to another plug-in or X-Plane.
Pass[XPLM_NO_PLUGIN_ID](/sdk/XPLM_NO_PLUGIN_ID/)to broadcast to all plug-ins.
Only enabled plug-ins with a message receive function receive the message.

## Plugin Features API

The plugin features API allows your plugin to “sign up” for additional
capabilities and plugin system features that are normally disabled for backward
compatibility or performance. This allows advanced plugins to “opt-in” to new
behavior.

Each feature is defined by a permanent string name. The feature string names
will vary with the particular installation of X-Plane, so plugins should not
expect a feature to be guaranteed present.

## XPLM_WANTS_REFLECTIONS

Available in the SDK 2.0 and later for X-Plane 9, enabling this capability
causes your plugin to receive drawing hook callbacks when X-Plane builds its
off-screen reflection and shadow rendering passes. Plugins should enable this
and examine the dataref sim/graphics/view/plane_render_type to determine whether
the drawing callback is for a reflection, shadow calculation, or the main
screen. Rendering can be simlified or omitted for reflections, and non-solid
drawing should be skipped for shadow calculations.

**Note**: direct drawing via draw callbacks is not recommended; use
the[XPLMInstance](/sdk/XPLMInstance/)API to create object models instead.

## XPLM_USE_NATIVE_PATHS

available in the SDK 2.1 and later for X-Plane 10, this modifies the plugin
system to use Unix-style paths on all operating systems. With this enabled:

- OS X paths will match the native OS X Unix.
- Windows will use forward slashes but preserve C:\ or another drive letter when using complete file paths.
- Linux uses its native file system path scheme.

Without this enabled:

- OS X will use CFM file paths separated by a colon.
- Windows will use back-slashes and conventional DOS paths.
- Linux uses its native file system path scheme.

All plugins should enable this feature on OS X to access the native file system.

## XPLM_USE_NATIVE_WIDGET_WINDOWS

Available in the SDK 3.0.2 SDK, this capability tells the widgets library to use
new, modern X-Plane backed[XPLMDisplay](/sdk/XPLMDisplay/)windows to anchor all
widget trees. Without it, widgets will always use legacy windows.

Plugins should enable this to allow their widget hierarchies to respond to the
user’s UI size settings and to map widget-based windwos to a VR HMD.

Before enabling this, make sure any custom widget code in your plugin is
prepared to cope with the UI coordinate system not being th same as the OpenGL
window coordinate system.

## XPLM_WANTS_DATAREF_NOTIFICATIONS

Available in the SDK 4.0.0, this capability tells X-Plane to to send the
enabling plugin the
new[XPLM_MSG_DATAREFS_ADDED](/sdk/XPLM_MSG_DATAREFS_ADDED/)message any time new
datarefs are added. The SDK will coalesce consecutive dataref registrations to
minimize the number of messages sent.

### [XPLMFeatureEnumerator_f](/sdk/XPLMFeatureEnumerator_f/)

```cpp
typedef void (* XPLMFeatureEnumerator_f)(
                         const char *         inFeature,
                         void *               inRef);

```

You pass an[XPLMFeatureEnumerator_f](/sdk/XPLMFeatureEnumerator_f/)to get a list
of all features supported by a given version running version of X-Plane. This
routine is called once for each feature.

### [XPLMHasFeature](/sdk/XPLMHasFeature/)

```cpp
XPLM_API int        XPLMHasFeature(
                         const char *         inFeature);

```

This returns 1 if the given installation of X-Plane supports a feature, or 0 if
it does not.

### [XPLMIsFeatureEnabled](/sdk/XPLMIsFeatureEnabled/)

```cpp
XPLM_API int        XPLMIsFeatureEnabled(
                         const char *         inFeature);

```

This returns 1 if a feature is currently enabled for your plugin, or 0 if it is
not enabled. It is an error to call this routine with an unsupported feature.

### [XPLMEnableFeature](/sdk/XPLMEnableFeature/)

```cpp
XPLM_API void       XPLMEnableFeature(
                         const char *         inFeature,
                         int                  inEnable);

```

This routine enables or disables a feature for your plugin. This will change the
running behavior of X-Plane and your plugin in some way, depending on the
feature.

### [XPLMEnumerateFeatures](/sdk/XPLMEnumerateFeatures/)

```cpp
XPLM_API void       XPLMEnumerateFeatures(
                         XPLMFeatureEnumerator_f inEnumerator,
                         void *               inRef);

```

This routine calls your enumerator callback once for each feature that this
running version of X-Plane supports. Use this routine to determine all of the
features that X-Plane can support.

### [XPLMPluginID](/sdk/XPLMPluginID/)

```cpp
typedef int XPLMPluginID;
```

Each plug-in is identified by a unique integer ID. This ID can be used to
disable or enable a plug-in, or discover what plug-in is ‘running’ at the time.
A plug-in ID is unique within the currently running instance of X-Plane unless
plug-ins are reloaded. Plug-ins may receive a different unique ID each time they
are loaded. This includes the unloading and reloading of plugins that are part
of the user’s aircraft.

For persistent identification of plug-ins,
use[XPLMFindPluginBySignature](/sdk/XPLMFindPluginBySignature/)in
XPLMUtiltiies.h .

-1 indicates no plug-in.

### [XPLMReloadPlugins](/sdk/XPLMReloadPlugins/)

```cpp
XPLM_API void       XPLMReloadPlugins(void);

```

This routine reloads all plug-ins. Once this routine is called and you return
from the callback you were within (e.g. a menu select callback) you will receive
your XPluginDisable and XPluginStop callbacks and your DLL will be unloaded,
then the start process happens as if the sim was starting up.

### [XPLMSendMessageToPlugin](/sdk/XPLMSendMessageToPlugin/)

```cpp
XPLM_API void       XPLMSendMessageToPlugin(
                         XPLMPluginID         inPlugin,
                         int                  inMessage,
                         void *               inParam);

```

This function sends a message to another plug-in or X-Plane.
Pass[XPLM_NO_PLUGIN_ID](/sdk/XPLM_NO_PLUGIN_ID/)to broadcast to all plug-ins.
Only enabled plug-ins with a message receive function receive the message.

### [XPLM_NO_PLUGIN_ID](/sdk/XPLM_NO_PLUGIN_ID/)

```cpp
#define XPLM_NO_PLUGIN_ID    (-1)
```

No plugin.

### [XPSendMessageToWidget](/sdk/XPSendMessageToWidget/)

```cpp
WIDGET_API int        XPSendMessageToWidget(
                         XPWidgetID           inWidget,
                         XPWidgetMessage      inMessage,
                         XPDispatchMode       inMode,
                         intptr_t             inParam1,
                         intptr_t             inParam2);

```

This sends any message to a widget. You should probably not go around simulating
the predefined messages that the widgets library defines for you. You may
however define custom messages for your widgets and send them with this method.

This method supports several dispatching patterns;
see[XPDispatchMode](/sdk/XPDispatchMode/)for more info. The function returns 1
if the message was handled, 0 if it was not.

For each widget that receives the message (see the dispatching modes), each
widget function from the most recently installed to the oldest one receives the
message in order until it is handled.

### [XPWidgetMessage](/sdk/XPWidgetMessage/)

Widgets receive 32-bit messages indicating what action is to be taken or
notifications of events. The list of messages may be expanded.

| Name | Value | Description |
| --- | --- | --- |
| [xpMsg_None](/sdk/xpMsg_None/) | "0" | No message, should not be sent. |
| [xpMsg_Create](/sdk/xpMsg_Create/) | "1" | The create message is sent once per
widget that is created with your widget function and oncefor any widget that has
your widget function attached.Dispatching: DirectParam 1: 1 if you are being
added as a subclass, 0 if the widget is first being created. |
| [xpMsg_Destroy](/sdk/xpMsg_Destroy/) | "2" | The destroy message is sent once
for each message that is destroyed that has your widget function.Dispatching:
Direct for allParam 1: 1 if being deleted by a recursive delete to the parent, 0
for explicit deletion. |
| [xpMsg_Paint](/sdk/xpMsg_Paint/) | "3" | The paint message is sent to your
widget to draw itself. The paint message is the bare-bonesmessage; in response
you must draw yourself, draw your children, set up clipping and culling,check
for visibility, etc. If you don't want to do all of this, ignore the paint
message anda draw message (see below) will be sent to you.Dispatching: Direct |
| [xpMsg_Draw](/sdk/xpMsg_Draw/) | "4" | The draw message is sent to your widget
when it is time to draw yourself. OpenGL will be set upto draw in 2-d global
screen coordinates, but you should use the XPLM to set up OpenGL
state.Dispatching: Direct |
| [xpMsg_KeyPress](/sdk/xpMsg_KeyPress/) | "5" | The key press message is sent
once per key that is pressed. The first parameter is the type of keycode
(integer or char) and the second is the code itself. By handling this event, you
consume thekey stroke.Handling this message 'consumes' the keystroke; not
handling it passes it to your parent widget.Dispatching: Up ChainParam 1: A
pointer to an[XPKeyState_t](/sdk/XPKeyState_t/)structure with the keystroke. |
| [xpMsg_KeyTakeFocus](/sdk/xpMsg_KeyTakeFocus/) | "6" | Keyboard focus is being
given to you. By handling this message you accept keyboard focus. Thefirst
parameter will be one if a child of yours gave up focus to you, 0 if someone set
focus onyou explicitly.Handling this message accepts focus; not handling refuses
focus.Dispatching: directParam 1: 1 if you are gaining focus because your child
is giving it up, 0 if someone is explicitlygiving you focus. |
| [xpMsg_KeyLoseFocus](/sdk/xpMsg_KeyLoseFocus/) | "7" | Keyboard focus is being
taken away from you. The first parameter will be 1 if you are losingfocus
because another widget is taking it, or 0 if someone called the API to make you
lose focusexplicitly.Dispatching: DirectParam 1: 1 if focus is being taken by
another widget, 0 if code requested to remove focus. |
| [xpMsg_MouseDown](/sdk/xpMsg_MouseDown/) | "8" | You receive one mousedown
event per click with a mouse-state structure pointed to by parameter 1.By
accepting this you eat the click, otherwise your parent gets it. You will not
receive drag andmouse up messages if you do not accept the down message.Handling
this message consumes the mouse click, not handling it passes it to the next
widget.You can act 'transparent' as a window by never handling moues clicks to
certain areas.Dispatching: Up chain NOTE: Technically this is direct dispatched,
but the widgets library will shipit to each widget until one consumes the click,
making it effectively "up chain".Param 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |
| [xpMsg_MouseDrag](/sdk/xpMsg_MouseDrag/) | "9" | You receive a series of mouse
drag messages (typically one per frame in the sim) as the mouse ismoved once you
have accepted a mouse down message. Parameter one points to a mouse-state
structuredescribing the mouse location. You will continue to receive these until
the mouse button isreleased.You may receive multiple mouse state messages with
the same mouse position. You will receive mousedrag events even if the mouse is
dragged out of your current or original bounds at the time of themouse
down.Dispatching: DirectParam 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |
| [xpMsg_MouseUp](/sdk/xpMsg_MouseUp/) | "10" | The mouseup event is sent once
when the mouse button is released after a drag or click. You onlyreceive this
message if you accept the mouseDown message. Parameter one points to a mouse
statestructure.Dispatching: DirectParam 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |
| [xpMsg_Reshape](/sdk/xpMsg_Reshape/) | "11" | Your geometry or a child's
geometry is being changed.Dispatching: Up chainParam 1: The widget ID of the
original reshaped target.Param 2: A pointer to
a[XPWidgetGeometryChange_t](/sdk/XPWidgetGeometryChange_t/)struct describing the
change. |
| [xpMsg_ExposedChanged](/sdk/xpMsg_ExposedChanged/) | "12" | Your exposed area
has changed.Dispatching: Direct |
| [xpMsg_AcceptChild](/sdk/xpMsg_AcceptChild/) | "13" | A child has been added
to you. The child's ID is passed in parameter one.Dispatching: DirectParam 1:
The Widget ID of the child being added. |
| [xpMsg_LoseChild](/sdk/xpMsg_LoseChild/) | "14" | A child has been removed
from you. The child's ID is passed in parameter one.Dispatching: DirectParam 1:
The Widget ID of the child being removed. |
| [xpMsg_AcceptParent](/sdk/xpMsg_AcceptParent/) | "15" | You now have a new
parent, or have no parent. The parent's ID is passed in, or 0 for no
parent.Dispatching: DirectParam 1: The Widget ID of your parent |
| [xpMsg_Shown](/sdk/xpMsg_Shown/) | "16" | You or a child has been shown. Note
that this does not include you being shown because your parentwas shown, you
were put in a new parent, your root was shown, etc.Dispatching: Up chainParam 1:
The widget ID of the shown widget. |
| [xpMsg_Hidden](/sdk/xpMsg_Hidden/) | "17" | You have been hidden. See
limitations above.Dispatching: Up chainParam 1: The widget ID of the hidden
widget. |
| [xpMsg_DescriptorChanged](/sdk/xpMsg_DescriptorChanged/) | "18" | Your
descriptor has changed.Dispatching: Direct |
| [xpMsg_PropertyChanged](/sdk/xpMsg_PropertyChanged/) | "19" | A property has
changed. Param 1 contains the property ID.Dispatching: DirectParam 1: The
Property ID being changed.Param 2: The new property value |
| [xpMsg_MouseWheel](/sdk/xpMsg_MouseWheel/) | "20" | The mouse wheel has
moved.Return 1 to consume the mouse wheel move, or 0 to pass the message to a
parent.Dispatching: Up chainParam 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |
| [xpMsg_CursorAdjust](/sdk/xpMsg_CursorAdjust/) | "21" | The cursor is over
your widget. If you consume this message, change
the[XPLMCursorStatus](/sdk/XPLMCursorStatus/)value to indicate the desired
result, with the same rules as in[XPLMDisplay](/sdk/XPLMDisplay/).h.Return 1 to
consume this message, 0 to pass it on.Dispatching: Up chainParam 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)struct containing the mouse status.Param
2: A pointer to a[XPLMCursorStatus](/sdk/XPLMCursorStatus/)- set this to the
cursor result you desire. |
| [xpMsg_UserStart](/sdk/xpMsg_UserStart/) | "10000" | NOTE: Message IDs 1000 -
9999 are allocated to the standard widget classes provided with the librarywith
1000 - 1099 for widget class 0, 1100 - 1199 for widget class 1, etc. Message IDs
10,000 andbeyond are for plugin use. |

## Available APIs

- [[XPLMCamera](/sdk/XPLMCamera/)](/sdk/XPLMCamera/)
- [[XPLMDataAccess](/sdk/XPLMDataAccess/)](/sdk/XPLMDataAccess/)
- [[XPLMDefs](/sdk/XPLMDefs/)](/sdk/XPLMDefs/)
- [[XPLMDisplay](/sdk/XPLMDisplay/)](/sdk/XPLMDisplay/)
- [[XPLMGraphics](/sdk/XPLMGraphics/)](/sdk/XPLMGraphics/)
- [[XPLMInstance](/sdk/XPLMInstance/)](/sdk/XPLMInstance/)
- [[XPLMMap](/sdk/XPLMMap/)](/sdk/XPLMMap/)
- [[XPLMMenus](/sdk/XPLMMenus/)](/sdk/XPLMMenus/)
- [[XPLMNavigation](/sdk/XPLMNavigation/)](/sdk/XPLMNavigation/)
- [[XPLMPlanes](/sdk/XPLMPlanes/)](/sdk/XPLMPlanes/)
- [[XPLMPlugin](/sdk/XPLMPlugin/)](/sdk/XPLMPlugin/)
- [[XPLMProcessing](/sdk/XPLMProcessing/)](/sdk/XPLMProcessing/)
- [[XPLMScenery](/sdk/XPLMScenery/)](/sdk/XPLMScenery/)
- [[XPLMSound](/sdk/XPLMSound/)](/sdk/XPLMSound/)
- [[XPLMUtilities](/sdk/XPLMUtilities/)](/sdk/XPLMUtilities/)
- [[XPLMWeather](/sdk/XPLMWeather/)](/sdk/XPLMWeather/)
- [[XPStandardWidgets](/sdk/XPStandardWidgets/)](/sdk/XPStandardWidgets/)
- [[XPUIGraphics](/sdk/XPUIGraphics/)](/sdk/XPUIGraphics/)
- [[XPWidgetDefs](/sdk/XPWidgetDefs/)](/sdk/XPWidgetDefs/)
- [[XPWidgets](/sdk/XPWidgets/)](/sdk/XPWidgets/)
- [[XPWidgetUtils](/sdk/XPWidgetUtils/)](/sdk/XPWidgetUtils/)

## General Documentation

| Title | Updated | Description |
| --- | --- | --- |
| [Plugin compatibility guide for X-Plane 11.50](https://developer.x-plane.com/article/plugin-compatibility-guide-for-x-plane-11-50/) | 12 Oct 2021 | X-Plane 11.50 and newer contains to option to run in Vulkan, Metal or OpenGL. This guide explains what's compatible and what needs to update for plugin authors. |
| [Plugin Guidance for OpenGL Drawing](https://developer.x-plane.com/article/plugin-guidance-for-opengl-drawing/) | 12 Oct 2021 | Guidelines for using OpenGL to draw from X-Plane plugins running inside X-Plane’s process. Plugin-drawing is supported only via OpenGL. |
| [Testing in X-Plane](https://developer.x-plane.com/article/testing-in-x-plane/) | 16 Mar 2021 | This document outlines how to test X-Plane via CLI commands and telnet. It explains key commands, debugging, and provides a sample test script text file. |
| [Building and Installing Plugins](https://developer.x-plane.com/article/building-and-installing-plugins/) | 7 May 2019 | Discusses platform-specific considerations for compiling & distributing plugins on Windows, macOS, and Linux. |
| [Developing Plugins](https://developer.x-plane.com/article/developing-plugins/) | 13 Feb 2019 | An introduction to the plug-in system, including the basics of how to set up plugins. |

## Tech Notes

### Aircraft

| Title | Updated | Description |
| --- | --- | --- |
| [Helicopter governor and correlator configuration](https://developer.x-plane.com/article/helicopter-governor-and-correlator-configuration/) | 20 Nov 2023 | X-Plane 12 revises the interaction of collective and throttle control in helicopters. Existing helicopters retain the default behavior of X-Plane 11 until modified in Plane Maker 12 to opt into one of the new governor systems. The joystick control assignments for collective and throttle don't change, but there's a new joystick curve available for Robinson-style throttle control. |
| [Moving the Plane](https://developer.x-plane.com/article/movingtheplane/) | 12 Jul 2018 | This tech note describes how to position the user's aircraft or multiplayer aircraft in X-Plane. |

### Data Access

| Title | Updated | Description |
| --- | --- | --- |
| [Datarefs for the CDU screen](https://developer.x-plane.com/article/datarefs-for-the-cdu-screen/) | 29 Jun 2022 | Datarefs to read the contents of the X-Plane default FMS Control and Display Unit (CDU) screen. |
| [Plugin Traffic Wake Turbulence](https://developer.x-plane.com/article/plugin-traffic-wake-turbulence/) | 27 Feb 2022 |
| [Overriding TCAS and providing traffic information](https://developer.x-plane.com/article/overriding-tcas-and-providing-traffic-information/) | 4 Jan 2022 | With X-Plane 11.50, plugins that display traffic in X-Plane, whether auto-generated or from an online multiplayer network, have to use the[XPLMInstance](/sdk/XPLMInstance/)API to draw these aircraft in X-Plane's world. |
| [SDKRawData](https://developer.x-plane.com/article/sdkrawdata/) | 11 Jan 2018 | This guide contains some of the raw data used to generate the SDK. It is probably not of general interest, but may be useful to programmers working with lots of datarefs, or adapting plugins to other APIs. |

### General

| Title | Updated | Description |
| --- | --- | --- |
| [LuaJIT](https://developer.x-plane.com/article/luajit/) | 24 May 2021 | This tech note describes the integration issues between X-Plane 10.20 64-bit and LuaJIT. |
| [Deferred Initialization](https://developer.x-plane.com/article/deferredinitialization/) | 12 Jul 2018 | This article explains limitations on plugins due to loading early in the X-Plane init sequence. |

### Graphics

| Title | Updated | Description |
| --- | --- | --- |
| [Drawing Rules](https://developer.x-plane.com/article/drawingrules/) | 12 Jul 2018 | A tech note with guidelines on plugin drawing in X-Plane. |
| [Screen Coordinates](https://developer.x-plane.com/article/screencoordinates/) | 12 Jul 2018 | This tech-note describes the various coordinate systems in X-Plane. |
| [Plugins and Objects](https://developer.x-plane.com/article/pluginsandobjects/) | 12 Jul 2018 | This tech note describes how plugins can interact with objects. |
| [OpenGL State](https://developer.x-plane.com/article/openglstate/) | 12 Jul 2018 | This note covers the differences between the 3 OpenGL states and how to handle them in your plugin. |

### Sound

| Title | Updated | Description |
| --- | --- | --- |
| [OpenAL](https://developer.x-plane.com/article/openal/) | 11 Jan 2018 | This tech note explains how to use OpenAL in an X-Plane Plugin. |

### User Interface

| |  |
| --- | --- | --- |
| [xpMessage_CloseButtonPushed](/sdk/xpMessage_CloseButtonPushed/) | "1200" | This message is sent when the close buttons for your window are pressed. |

| |  |
| --- | --- | --- |
| [xpProperty_Enabled](/sdk/xpProperty_Enabled/) | "7" | Is this widget enabled (for those that have a disabled state too)? |

