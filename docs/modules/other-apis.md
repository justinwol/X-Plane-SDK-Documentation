---
title: "Other/Miscellaneous APIs"
description: "X-Plane SDK Other/Miscellaneous APIs documentation"
category: "Other_APIs"
date: "2025-06-25T15:45:56.653424"
---

# Other/Miscellaneous APIs

### [NO_PARENT](/sdk/NO_PARENT/)

```cpp
#define NO_PARENT            -1
```

### [PARAM_PARENT](/sdk/PARAM_PARENT/)

```cpp
#define PARAM_PARENT         -2
```

### [XPDispatchMode](/sdk/XPDispatchMode/)

The dispatching modes describe how the widgets library sends out messages.
Currently there are three modes:

| Name | Value | Description |
| --- | --- | --- |
| [xpMode_Direct](/sdk/xpMode_Direct/) | "0" | The message will only be sent to
the target widget. |
| [xpMode_UpChain](/sdk/xpMode_UpChain/) | "1" | The message is sent to the
target widget, then up the chain of parents until the message ishandled or a
parentless widget is reached. |
| [xpMode_Recursive](/sdk/xpMode_Recursive/) | "2" | The message is sent to the
target widget and then all of its children recursively depth-first. |
| [xpMode_DirectAllCallbacks](/sdk/xpMode_DirectAllCallbacks/) | "3" | The
message is sent just to the target, but goes to every callback, even if it is
handled. |
| [xpMode_Once](/sdk/xpMode_Once/) | "4" | The message is only sent to the very
first handler even if it is not accepted. (This is really only useful for some
internal widget library functions.) |

### [XPElementStyle](/sdk/XPElementStyle/)

Elements are individually drawable UI things like push buttons, etc. The style
defines what kind of element you are drawing. Elements can be stretched in one
or two dimensions (depending on the element). Some elements can be lit.

In X-Plane 6 some elements must be drawn over metal. Some are scalable and some
are not. Any element can be drawn anywhere in X-Plane 7.

Scalable Axis Required Background

| Name | Value | Description |
| --- | --- | --- |
| [xpElement_TextField](/sdk/xpElement_TextField/) | "6" | x metal |
| [xpElement_CheckBox](/sdk/xpElement_CheckBox/) | "9" | none metal |
| [xpElement_CheckBoxLit](/sdk/xpElement_CheckBoxLit/) | "10" | none metal |
| [xpElement_WindowCloseBox](/sdk/xpElement_WindowCloseBox/) | "14" | none
window header |
| [xpElement_WindowCloseBoxPressed](/sdk/xpElement_WindowCloseBoxPressed/) |
"15" | none window header |
| [xpElement_PushButton](/sdk/xpElement_PushButton/) | "16" | x metal |
| [xpElement_PushButtonLit](/sdk/xpElement_PushButtonLit/) | "17" | x metal |
| [xpElement_OilPlatform](/sdk/xpElement_OilPlatform/) | "24" | none any |
| [xpElement_OilPlatformSmall](/sdk/xpElement_OilPlatformSmall/) | "25" | none
any |
| [xpElement_Ship](/sdk/xpElement_Ship/) | "26" | none any |
| [xpElement_ILSGlideScope](/sdk/xpElement_ILSGlideScope/) | "27" | none any |
| [xpElement_MarkerLeft](/sdk/xpElement_MarkerLeft/) | "28" | none any |
| [xpElement_Airport](/sdk/xpElement_Airport/) | "29" | none any |
| [xpElement_Waypoint](/sdk/xpElement_Waypoint/) | "30" | none any |
| [xpElement_NDB](/sdk/xpElement_NDB/) | "31" | none any |
| [xpElement_VOR](/sdk/xpElement_VOR/) | "32" | none any |
| [xpElement_RadioTower](/sdk/xpElement_RadioTower/) | "33" | none any |
| [xpElement_AircraftCarrier](/sdk/xpElement_AircraftCarrier/) | "34" | none any
|
| [xpElement_Fire](/sdk/xpElement_Fire/) | "35" | none any |
| [xpElement_MarkerRight](/sdk/xpElement_MarkerRight/) | "36" | none any |
| [xpElement_CustomObject](/sdk/xpElement_CustomObject/) | "37" | none any |
| [xpElement_CoolingTower](/sdk/xpElement_CoolingTower/) | "38" | none any |
| [xpElement_SmokeStack](/sdk/xpElement_SmokeStack/) | "39" | none any |
| [xpElement_Building](/sdk/xpElement_Building/) | "40" | none any |
| [xpElement_PowerLine](/sdk/xpElement_PowerLine/) | "41" | none any |
| [xpElement_CopyButtons](/sdk/xpElement_CopyButtons/) | "45" | none metal |
|
[xpElement_CopyButtonsWithEditingGrid](/sdk/xpElement_CopyButtonsWithEditingGrid/)
| "46" | none metal |
| [xpElement_EditingGrid](/sdk/xpElement_EditingGrid/) | "47" | x, y metal |
| [xpElement_ScrollBar](/sdk/xpElement_ScrollBar/) | "48" | THIS CAN PROBABLY BE
REMOVED |
| [xpElement_VORWithCompassRose](/sdk/xpElement_VORWithCompassRose/) | "49" |
none any |
| [xpElement_Zoomer](/sdk/xpElement_Zoomer/) | "51" | none metal |
| [xpElement_TextFieldMiddle](/sdk/xpElement_TextFieldMiddle/) | "52" | x, y
metal |
| [xpElement_LittleDownArrow](/sdk/xpElement_LittleDownArrow/) | "53" | none
metal |
| [xpElement_LittleUpArrow](/sdk/xpElement_LittleUpArrow/) | "54" | none metal |
| [xpElement_WindowDragBar](/sdk/xpElement_WindowDragBar/) | "61" | none metal |
| [xpElement_WindowDragBarSmooth](/sdk/xpElement_WindowDragBarSmooth/) | "62" |
none metal |

### [XPGetElementDefaultDimensions](/sdk/XPGetElementDefaultDimensions/)

```cpp
WIDGET_API void       XPGetElementDefaultDimensions(
                         XPElementStyle       inStyle,
                         int *                outWidth,    /* Can be NULL */
                         int *                outHeight,    /* Can be NULL */
                         int *                outCanBeLit);    /* Can be NULL */

```

This routine returns the recommended or minimum dimensions of a given UI
element. outCanBeLit tells whether the element has both a lit and unlit state.
Pass NULL to not receive any of these parameters.

### [XPGetTrackDefaultDimensions](/sdk/XPGetTrackDefaultDimensions/)

```cpp
WIDGET_API void       XPGetTrackDefaultDimensions(
                         XPTrackStyle         inStyle,
                         int *                outWidth,
                         int *                outCanBeLit);

```

This routine returns a track’s default smaller dimension; all tracks are
scalable in the larger dimension. It also returns whether a track can be lit.

### [XPGetTrackMetrics](/sdk/XPGetTrackMetrics/)

```cpp
WIDGET_API void       XPGetTrackMetrics(
                         int                  inX1,
                         int                  inY1,
                         int                  inX2,
                         int                  inY2,
                         int                  inMin,
                         int                  inMax,
                         int                  inValue,
                         XPTrackStyle         inTrackStyle,
                         int *                outIsVertical,
                         int *                outDownBtnSize,
                         int *                outDownPageSize,
                         int *                outThumbSize,
                         int *                outUpPageSize,
                         int *                outUpBtnSize);

```

This routine returns the metrics of a track. If you want to write UI code to
manipulate a track, this routine helps you know where the mouse locations are.
For most other elements, the rectangle the element is drawn in is enough
information. However, the scrollbar drawing routine does some automatic
placement; this routine lets you know where things ended up. You pass almost
everything you would pass to the draw routine. You get out the orientation, and
other useful stuff.

Besides orientation, you get five dimensions for the five parts of a scrollbar,
which are the down button, down area (area before the thumb), the thumb, and the
up area and button. For horizontal scrollers, the left button decreases; for
vertical scrollers, the top button decreases.

### [XPKeyState_t](/sdk/XPKeyState_t/)

When a key is pressed, a pointer to this struct is passed to your widget
function.

```cpp
typedef struct {
     // The ASCII key that was pressed.  WARNING: this may be 0 for some non-ASCII key sequences.
     char                      key;
     // The flags.  Make sure to check this if you only want key-downs!
     XPLMKeyFlags              flags;
     // The virtual key code for the key
     char                      vkey;
} XPKeyState_t;
```

### [XPLMAvionicsBrightness_f](/sdk/XPLMAvionicsBrightness_f/)

```cpp
typedef float (* XPLMAvionicsBrightness_f)(
                         float                inRheoValue,
                         float                inAmbiantBrightness,
                         float                inBusVoltsRatio,
                         void *               inRefcon);

```

This is the prototype for screen brightness callbacks for custom devices. If you
provide a callback, you can return the ratio of the screen’s maximum brightness
that the simulator should use when displaying the screen in the 3D cockpit.

inRheoValue is the current ratio value (between 0 and 1) of the instrument
brightness rheostat to which the device is bound.

inAmbientBrightness is the value (between 0 and 1) that the callback should
return for the screen to be at a usable brightness based on ambient light (if
your device has a photo cell and automatically adjusts its brightness, you can
return this and your screen will be at the optimal brightness to be readable,
but not blind the pilot).

inBusVoltsRatio is the ratio of the nominal voltage currently present on the bus
to which the device is bound, or -1 if the device is not bound to the current
aircraft.

Refcon is a unique value that you specify when creating the device, allowing you
to slip a pointer to your own data to the callback.

### [XPLMAvionicsCursor_f](/sdk/XPLMAvionicsCursor_f/)

```cpp
typedef XPLMCursorStatus (* XPLMAvionicsCursor_f)(
                         int                  x,
                         int                  y,
                         void *               inRefcon);

```

Cursor callback that decides which cursor to show when the mouse is over your
screen or (2D-popup) bezel.
Return[xplm_CursorDefault](/sdk/xplm_CursorDefault/)to let X-Plane use which
cursor to show, or other values to force the cursor to a particular one
(see[XPLMCursorStatus](/sdk/XPLMCursorStatus/)).

### [XPLMAvionicsID](/sdk/XPLMAvionicsID/)

```cpp
typedef void * XPLMAvionicsID;
```

This is an opaque identifier for an avionics display that you enhance or
replace. When you register your callbacks
(via[XPLMRegisterAvionicsCallbacksEx](/sdk/XPLMRegisterAvionicsCallbacksEx/)())
or create a new device (via XPLMCreateAvionicsDevice()), you will specify
drawing and mouse callbacks, and get back such a handle.

### [XPLMBankID](/sdk/XPLMBankID/)

These values are returned as the parameter of the
“[XPLM_MSG_FMOD_BANK_LOADED](/sdk/XPLM_MSG_FMOD_BANK_LOADED/)” and
“[XPLM_MSG_FMOD_BANK_UNLOADING](/sdk/XPLM_MSG_FMOD_BANK_UNLOADING/)” messages.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_MasterBank](/sdk/xplm_MasterBank/) | "0" | Master bank. Handles all
aircraft and environmental audio. |
| [xplm_RadioBank](/sdk/xplm_RadioBank/) | "1" | Radio bank. Handles
COM1/COM2/GND/Pilot/Copilot. |

### [XPLMCommandBegin](/sdk/XPLMCommandBegin/)

```cpp
XPLM_API void       XPLMCommandBegin(
                         XPLMCommandRef       inCommand);

```

[XPLMCommandBegin](/sdk/XPLMCommandBegin/)starts the execution of a command,
specified by its command reference. The command is “held down”
until[XPLMCommandEnd](/sdk/XPLMCommandEnd/)is called. You must balance
each[XPLMCommandBegin](/sdk/XPLMCommandBegin/)call with
an[XPLMCommandEnd](/sdk/XPLMCommandEnd/)call.

### [XPLMCommandEnd](/sdk/XPLMCommandEnd/)

```cpp
XPLM_API void       XPLMCommandEnd(
                         XPLMCommandRef       inCommand);

```

[XPLMCommandEnd](/sdk/XPLMCommandEnd/)ends the execution of a given command that
was started with[XPLMCommandBegin](/sdk/XPLMCommandBegin/). You must not
issue[XPLMCommandEnd](/sdk/XPLMCommandEnd/)for a command you did not begin.

### [XPLMCommandKeyID](/sdk/XPLMCommandKeyID/)

These enums represent all the keystrokes available within X-Plane. They can be
sent to X-Plane directly. For example, you can reverse thrust using these
enumerations.

```cpp
enum {
          xplm_key_pause=0,
          xplm_key_revthrust,
          xplm_key_jettison,
          xplm_key_brakesreg,
          xplm_key_brakesmax,
          xplm_key_gear,
          xplm_key_timedn,
          xplm_key_timeup,
          xplm_key_fadec,
          xplm_key_otto_dis,
          xplm_key_otto_atr,
          xplm_key_otto_asi,
          xplm_key_otto_hdg,
          xplm_key_otto_gps,
          xplm_key_otto_lev,
          xplm_key_otto_hnav,
          xplm_key_otto_alt,
          xplm_key_otto_vvi,
          xplm_key_otto_vnav,
          xplm_key_otto_nav1,
          xplm_key_otto_nav2,
          xplm_key_targ_dn,
          xplm_key_targ_up,
          xplm_key_hdgdn,
          xplm_key_hdgup,
          xplm_key_barodn,
          xplm_key_baroup,
          xplm_key_obs1dn,
          xplm_key_obs1up,
          xplm_key_obs2dn,
          xplm_key_obs2up,
          xplm_key_com1_1,
          xplm_key_com1_2,
          xplm_key_com1_3,
          xplm_key_com1_4,
          xplm_key_nav1_1,
          xplm_key_nav1_2,
          xplm_key_nav1_3,
          xplm_key_nav1_4,
          xplm_key_com2_1,
          xplm_key_com2_2,
          xplm_key_com2_3,
          xplm_key_com2_4,
          xplm_key_nav2_1,
          xplm_key_nav2_2,
          xplm_key_nav2_3,
          xplm_key_nav2_4,
          xplm_key_adf_1,
          xplm_key_adf_2,
          xplm_key_adf_3,
          xplm_key_adf_4,
          xplm_key_adf_5,
          xplm_key_adf_6,
          xplm_key_transpon_1,
          xplm_key_transpon_2,
          xplm_key_transpon_3,
          xplm_key_transpon_4,
          xplm_key_transpon_5,
          xplm_key_transpon_6,
          xplm_key_transpon_7,
          xplm_key_transpon_8,
          xplm_key_flapsup,
          xplm_key_flapsdn,
          xplm_key_cheatoff,
          xplm_key_cheaton,
          xplm_key_sbrkoff,
          xplm_key_sbrkon,
          xplm_key_ailtrimL,
          xplm_key_ailtrimR,
          xplm_key_rudtrimL,
          xplm_key_rudtrimR,
          xplm_key_elvtrimD,
          xplm_key_elvtrimU,
          xplm_key_forward,
          xplm_key_down,
          xplm_key_left,
          xplm_key_right,
          xplm_key_back,
          xplm_key_tower,
          xplm_key_runway,
          xplm_key_chase,
          xplm_key_free1,
          xplm_key_free2,
          xplm_key_spot,
          xplm_key_fullscrn1,
          xplm_key_fullscrn2,
          xplm_key_tanspan,
          xplm_key_smoke,
          xplm_key_map,
          xplm_key_zoomin,
          xplm_key_zoomout,
          xplm_key_cycledump,
          xplm_key_replay,
          xplm_key_tranID,
          xplm_key_max
};
typedef int XPLMCommandKeyID;
```

### [XPLMCommandKeyStroke](/sdk/XPLMCommandKeyStroke/)

```cpp
XPLM_API void       XPLMCommandKeyStroke(
                         XPLMCommandKeyID     inKey);

```

This routine simulates a command-key stroke. However, the keys are done by
function, not by actual letter, so this function works even if the user has
remapped their keyboard. Examples of things you might do with this include
pausing the simulator.

Deprecated: use[XPLMCommandOnce](/sdk/XPLMCommandOnce/)

### [XPLMCommandOnce](/sdk/XPLMCommandOnce/)

```cpp
XPLM_API void       XPLMCommandOnce(
                         XPLMCommandRef       inCommand);

```

This executes a given command momentarily, that is, the command begins and ends
immediately. This is the equivalent of
calling[XPLMCommandBegin](/sdk/XPLMCommandBegin/)()
and[XPLMCommandEnd](/sdk/XPLMCommandEnd/)() back to back.

### [XPLMCommandPhase](/sdk/XPLMCommandPhase/)

The phases of a command.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_CommandBegin](/sdk/xplm_CommandBegin/) | "0" | The command is being
started. |
| [xplm_CommandContinue](/sdk/xplm_CommandContinue/) | "1" | The command is
continuing to execute. |
| [xplm_CommandEnd](/sdk/xplm_CommandEnd/) | "2" | The command has ended. |

### [XPLMCommandRef](/sdk/XPLMCommandRef/)

```cpp
typedef void * XPLMCommandRef;
```

A command ref is an opaque identifier for an X-Plane command. Command references
stay the same for the life of your plugin but not between executions of X-Plane.
Command refs are used to execute commands, create commands, and create callbacks
for particular commands.

Note that a command is not “owned” by a particular plugin. Since many plugins
may participate in a command’s execution, the command does not go away if the
plugin that created it is unloaded.

### [XPLMCreateAvionicsEx](/sdk/XPLMCreateAvionicsEx/)

```cpp
XPLM_API XPLMAvionicsID XPLMCreateAvionicsEx(
                         XPLMCreateAvionics_t * inParams);

```

Creates a new cockpit device to be used in the 3D cockpit. You can call this at
any time: if an aircraft referencing your device is loaded before your plugin,
the simulator will make sure to retroactively map your display into it.

```cpp
        When you are done with the device, and at least before your plugin is unloaded, you should destroy the device using XPLMDestroyAvionics().

```

### [XPLMCreateAvionics_t](/sdk/XPLMCreateAvionics_t/)

The[XPLMCreateAvionics_t](/sdk/XPLMCreateAvionics_t/)structure defines all of
the parameters used to generate your own glass cockpit device by
using[XPLMCreateAvionicsEx](/sdk/XPLMCreateAvionicsEx/)(). The structure will be
expanded in future SDK APIs to include more features. Always set the structSize
member to the size of your struct in bytes!

```cpp
typedef struct {
     // Used to inform XPLMCreateAvionicsEx() of the SDK version you compiled against; should always be set to sizeof(XPLMCreateAvionics_t)
     int                       structSize;
     // Width of the device's screen in pixels.
     int                       screenWidth;
     // Height of the device's screen in pixels.
     int                       screenHeight;
     // Width of the bezel around your device's screen for 2D pop-ups.
     int                       bezelWidth;
     // Height of the bezel around your device's screen for 2D pop-ups.
     int                       bezelHeight;
     // The screen's lateral offset into the bezel for 2D pop-ups.
     int                       screenOffsetX;
     // The screen's vertical offset into the bezel for 2D pop-ups.
     int                       screenOffsetY;
     // If set to true (1), X-Plane won't call your plugin to re-render the device's screen every frame. Instead, you should tell X-Plane you want to refresh your screen with XPLMAvionicsNeedsDrawing(), and X-Plane will call you before rendering the next simulator frame.
     int                       drawOnDemand;
     // The draw callback you will use to draw the 2D-popup bezel. This is called only when the popup window is visible, and X-Plane is about to draw the bezel in it.
     XPLMAvionicsBezelCallback_f bezelDrawCallback;
     // The draw callback you will be using to draw into the device's screen framebuffer.
     XPLMAvionicsScreenCallback_f drawCallback;
     // The mouse click callback that is called when the user clicks onto your bezel.
     XPLMAvionicsMouse_f       bezelClickCallback;
     // The mouse click callback that is called when the user clicks onto your bezel.
     XPLMAvionicsMouse_f       bezelRightClickCallback;
     // The callback that is called when the users uses the scroll wheel over your avionics' bezel.
     XPLMAvionicsMouseWheel_f  bezelScrollCallback;
     // The callback that lets you determine what cursor should be shown when the mouse is over your device's bezel.
     XPLMAvionicsCursor_f      bezelCursorCallback;
     // The mouse click callback that is called when the user clicks onto your screen.
     XPLMAvionicsMouse_f       screenTouchCallback;
     // The right mouse click callback that is called when the user clicks onto your screen.
     XPLMAvionicsMouse_f       screenRightTouchCallback;
     // The callback that is called when the users uses the scroll wheel over your avionics' screen.
     XPLMAvionicsMouseWheel_f  screenScrollCallback;
     // The callback that lets you determine what cursor should be shown when the mouse is over your device's screen.
     XPLMAvionicsCursor_f      screenCursorCallback;
     // The key callback that is called when the user types in your popup.
     XPLMAvionicsKeyboard_f    keyboardCallback;
     // The callback that is called to determine the absolute brightness of the device's screen. Set to NULL to use X-Plane's default behaviour.
     XPLMAvionicsBrightness_f  brightnessCallback;
     // A null-terminated string of maximum 64 characters to uniquely identify your cockpit device. This must be unique (you cannot re-use an ID that X-Plane or another plugin provides), and it must not contain spaces. This is the string the OBJ file must reference when marking polygons with ATTR_cockpit_device. The string is copied when you call XPLMCreateAvionicsEx, so you don't need to hold this string in memory after the call.
     char *                    deviceID;
     // A null-terminated string to give a user-readable name to your device, which can be presented in UI dialogs.
     char *                    deviceName;
     // A reference which will be passed into your draw and mouse callbacks. Use this to pass information to yourself as needed.
     void *                    refcon;
} XPLMCreateAvionics_t;
```

### [XPLMCreateCommand](/sdk/XPLMCreateCommand/)

```cpp
XPLM_API XPLMCommandRef XPLMCreateCommand(
                         const char *         inName,
                         const char *         inDescription);

```

[XPLMCreateCommand](/sdk/XPLMCreateCommand/)creates a new command for a given
string. If the command already exists, the existing command reference is
returned. The description may appear in user interface contexts, such as the
joystick configuration screen.

### [XPLMCursorStatus](/sdk/XPLMCursorStatus/)

[XPLMCursorStatus](/sdk/XPLMCursorStatus/)describes how you would like X-Plane
to manage the cursor. See[XPLMHandleCursor_f](/sdk/XPLMHandleCursor_f/)for more
info.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_CursorDefault](/sdk/xplm_CursorDefault/) | "0" | X-Plane manages the
cursor normally, plugin does not affect the cusrsor. |
| [xplm_CursorHidden](/sdk/xplm_CursorHidden/) | "1" | X-Plane hides the cursor.
|
| [xplm_CursorArrow](/sdk/xplm_CursorArrow/) | "2" | X-Plane shows the cursor as
the default arrow. |
| [xplm_CursorCustom](/sdk/xplm_CursorCustom/) | "3" | X-Plane shows the cursor
but lets you select an OS cursor. |

### [XPLMCustomizeAvionics_t](/sdk/XPLMCustomizeAvionics_t/)

The[XPLMCustomizeAvionics_t](/sdk/XPLMCustomizeAvionics_t/)structure defines all
of the parameters used to replace or enhance built-in simulator avionics devices
using[XPLMRegisterAvionicsCallbacksEx](/sdk/XPLMRegisterAvionicsCallbacksEx/)().
The structure will be expanded in future SDK APIs to include more features.
Always set the structSize member to the size of your struct in bytes!

```cpp
typedef struct {
     // Used to inform XPLMRegisterAvionicsCallbacksEx() of the SDK version you compiled against; should always be set to sizeof(XPLMCustomizeAvionics_t)
     int                       structSize;
     // The built-in avionics device to which you want your drawing applied.
     XPLMDeviceID              deviceId;
     // The draw callback to be called before X-Plane draws.
     XPLMAvionicsCallback_f    drawCallbackBefore;
     // The draw callback to be called after X-Plane has drawn.
     XPLMAvionicsCallback_f    drawCallbackAfter;
     // The mouse click callback that is called when the user clicks onto the device's bezel.
     XPLMAvionicsMouse_f       bezelClickCallback;
     // The mouse click callback that is called when the user clicks onto the device's bezel.
     XPLMAvionicsMouse_f       bezelRightClickCallback;
     // The callback that is called when the users uses the scroll wheel over the device's bezel.
     XPLMAvionicsMouseWheel_f  bezelScrollCallback;
     // The callback that lets you determine what cursor should be shown when the mouse is over the device's bezel.
     XPLMAvionicsCursor_f      bezelCursorCallback;
     // The mouse click callback that is called when the user clicks onto the device's screen.
     XPLMAvionicsMouse_f       screenTouchCallback;
     // The right mouse click callback that is called when the user clicks onto the device's screen.
     XPLMAvionicsMouse_f       screenRightTouchCallback;
     // The callback that is called when the users uses the scroll wheel over the device's screen.
     XPLMAvionicsMouseWheel_f  screenScrollCallback;
     // The callback that lets you determine what cursor should be shown when the mouse is over the device's screen.
     XPLMAvionicsCursor_f      screenCursorCallback;
     // The key callback that is called when the user types in the device's popup.
     XPLMAvionicsKeyboard_f    keyboardCallback;
     // A reference which will be passed into each of your draw callbacks. Use this to pass information to yourself as needed.
     void *                    refcon;
} XPLMCustomizeAvionics_t;
```

### [XPLMDebugString](/sdk/XPLMDebugString/)

```cpp
XPLM_API void       XPLMDebugString(
                         const char *         inString);

```

This routine outputs a C-style string to the Log.txt file. The file is
immediately flushed so you will not lose data. (This does cause a performance
penalty.)

Please do*not*leave routine diagnostic logging enabled in your shipping plugin.
The X-Plane Log file is shared by X-Plane and every plugin in the system, and
plugins that (when functioning normally) print verbose log output make it
difficult for developers to find error conditions from other parts of the
system.

# [XPLMDefs](/sdk/XPLMDefs/)API

This file is contains the cross-platform and basic definitions for the X-Plane
SDK.

The preprocessor macros APL, LIN and IBM must be defined to specify the
compilation target; define APL to 1 to compile on Mac, IBM to 1 to compile on
Windows and LIN to 1 to compile on Linux. Only one compilation target may be
used at a time. You must specify these macro definitions before
including[XPLMDefs](/sdk/XPLMDefs/).h or any other XPLM headers. You can do this
using the -D command line option or a preprocessor header.

## DLL Definitions

These definitions control the importing and exporting of functions within the
DLL.

You can prefix your five required callbacks with the PLUGIN_API macro to declare
them as exported C functions. The XPLM_API macro identifies functions that are
provided to you via the plugin SDK. (Link against XPLM.lib to use these
functions.)

## GLOBAL DEFINITIONS

These definitions are used in all parts of the SDK.

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

### [XPLM_NO_PLUGIN_ID](/sdk/XPLM_NO_PLUGIN_ID/)

```cpp
#define XPLM_NO_PLUGIN_ID    (-1)
```

No plugin.

### [XPLM_PLUGIN_XPLANE](/sdk/XPLM_PLUGIN_XPLANE/)

```cpp
#define XPLM_PLUGIN_XPLANE   (0)
```

X-Plane itself

### [kXPLM_Version](/sdk/kXPLM_Version/)

```cpp
#define kXPLM_Version        (411)
```

The current XPLM revision is 4.1.1 (411).

### [XPLMKeyFlags](/sdk/XPLMKeyFlags/)

These bitfields define modifier keys in a platform independent way. When a key
is pressed, a series of messages are sent to your plugin. The down flag is set
in the first of these messages, and the up flag in the last. While the key is
held down, messages are sent with neither flag set to indicate that the key is
being held down as a repeated character.

The control flag is mapped to the control flag on Macintosh and PC. Generally
X-Plane uses the control key and not the command key on Macintosh, providing a
consistent interface across platforms that does not necessarily match the
Macintosh user interface guidelines. There is not yet a way for plugins to
access the Macintosh control keys without using #ifdefed code.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_ShiftFlag](/sdk/xplm_ShiftFlag/) | "1" | The shift key is down |
| [xplm_OptionAltFlag](/sdk/xplm_OptionAltFlag/) | "2" | The option or alt key
is down |
| [xplm_ControlFlag](/sdk/xplm_ControlFlag /) | "4" | The control key is down |
| [xplm_DownFlag](/sdk/xplm_DownFlag/) | "8" | The key is being pressed down |
| [xplm_UpFlag](/sdk/xplm_UpFlag/) | "16" | The key is being released |

## ASCII CONTROL KEY CODES

These definitions define how various control keys are mapped to ASCII key codes.
Not all key presses generate an ASCII value, so plugin code should be prepared
to see null characters come from the keyboard…this usually represents a key
stroke that has no equivalent ASCII, like a page-down press. Use virtual key
codes to find these key strokes.

ASCII key codes take into account modifier keys; shift keys will affect capitals
and punctuation; control key combinations may have no vaild ASCII and produce
NULL. To detect control-key combinations, use virtual key codes, not ASCII keys.

### [XPLM_KEY_RETURN](/sdk/XPLM_KEY_RETURN/)

```cpp
#define XPLM_KEY_RETURN      13
```

### [XPLM_KEY_ESCAPE](/sdk/XPLM_KEY_ESCAPE/)

```cpp
#define XPLM_KEY_ESCAPE      27
```

### [XPLM_KEY_TAB](/sdk/XPLM_KEY_TAB/)

```cpp
#define XPLM_KEY_TAB         9
```

### [XPLM_KEY_DELETE](/sdk/XPLM_KEY_DELETE/)

```cpp
#define XPLM_KEY_DELETE      8
```

### [XPLM_KEY_LEFT](/sdk/XPLM_KEY_LEFT/)

```cpp
#define XPLM_KEY_LEFT        28
```

### [XPLM_KEY_RIGHT](/sdk/XPLM_KEY_RIGHT/)

```cpp
#define XPLM_KEY_RIGHT       29
```

### [XPLM_KEY_UP](/sdk/XPLM_KEY_UP/)

```cpp
#define XPLM_KEY_UP          30
```

### [XPLM_KEY_DOWN](/sdk/XPLM_KEY_DOWN/)

```cpp
#define XPLM_KEY_DOWN        31
```

### [XPLM_KEY_0](/sdk/XPLM_KEY_0/)

```cpp
#define XPLM_KEY_0           48
```

### [XPLM_KEY_1](/sdk/XPLM_KEY_1/)

```cpp
#define XPLM_KEY_1           49
```

### [XPLM_KEY_2](/sdk/XPLM_KEY_2/)

```cpp
#define XPLM_KEY_2           50
```

### [XPLM_KEY_3](/sdk/XPLM_KEY_3/)

```cpp
#define XPLM_KEY_3           51
```

### [XPLM_KEY_4](/sdk/XPLM_KEY_4/)

```cpp
#define XPLM_KEY_4           52
```

### [XPLM_KEY_5](/sdk/XPLM_KEY_5/)

```cpp
#define XPLM_KEY_5           53
```

### [XPLM_KEY_6](/sdk/XPLM_KEY_6/)

```cpp
#define XPLM_KEY_6           54
```

### [XPLM_KEY_7](/sdk/XPLM_KEY_7/)

```cpp
#define XPLM_KEY_7           55
```

### [XPLM_KEY_8](/sdk/XPLM_KEY_8/)

```cpp
#define XPLM_KEY_8           56
```

### [XPLM_KEY_9](/sdk/XPLM_KEY_9/)

```cpp
#define XPLM_KEY_9           57
```

### [XPLM_KEY_DECIMAL](/sdk/XPLM_KEY_DECIMAL/)

```cpp
#define XPLM_KEY_DECIMAL     46
```

## VIRTUAL KEY CODES

These are cross-platform defines for every distinct keyboard press on the
computer. Every physical key on the keyboard has a virtual key code. So the
“two” key on the top row of the main keyboard has a different code from the
“two” key on the numeric key pad. But the ‘w’ and ‘W’ character are
indistinguishable by virtual key code because they are the same physical key
(one with and one without the shift key).

Use virtual key codes to detect keystrokes that do not have ASCII equivalents,
allow the user to map the numeric keypad separately from the main keyboard, and
detect control key and other modifier-key combinations that generate ASCII
control key sequences (many of which are not available directly via character
keys in the SDK).

To assign virtual key codes we started with the Microsoft set but made some
additions and changes. A few differences:

1. Modifier keys are not available as virtual key codes. You cannot get distinct modifier press and release messages. Please do not try to use modifier keys as regular keys; doing so will almost certainly interfere with users' abilities to use the native X-Plane key bindings.
2. Some keys that do not exist on both Mac and PC keyboards are removed.
3. Do not assume that the values of these keystrokes are interchangeable with MS v-keys.

### [XPLM_VK_BACK](/sdk/XPLM_VK_BACK/)

```cpp
#define XPLM_VK_BACK         0x08
```

### [XPLM_VK_TAB](/sdk/XPLM_VK_TAB/)

```cpp
#define XPLM_VK_TAB          0x09
```

### [XPLM_VK_CLEAR](/sdk/XPLM_VK_CLEAR/)

```cpp
#define XPLM_VK_CLEAR        0x0C
```

### [XPLM_VK_RETURN](/sdk/XPLM_VK_RETURN/)

```cpp
#define XPLM_VK_RETURN       0x0D
```

### [XPLM_VK_ESCAPE](/sdk/XPLM_VK_ESCAPE/)

```cpp
#define XPLM_VK_ESCAPE       0x1B
```

### [XPLM_VK_SPACE](/sdk/XPLM_VK_SPACE/)

```cpp
#define XPLM_VK_SPACE        0x20
```

### [XPLM_VK_PRIOR](/sdk/XPLM_VK_PRIOR/)

```cpp
#define XPLM_VK_PRIOR        0x21
```

### [XPLM_VK_NEXT](/sdk/XPLM_VK_NEXT/)

```cpp
#define XPLM_VK_NEXT         0x22
```

### [XPLM_VK_END](/sdk/XPLM_VK_END/)

```cpp
#define XPLM_VK_END          0x23
```

### [XPLM_VK_HOME](/sdk/XPLM_VK_HOME/)

```cpp
#define XPLM_VK_HOME         0x24
```

### [XPLM_VK_LEFT](/sdk/XPLM_VK_LEFT/)

```cpp
#define XPLM_VK_LEFT         0x25
```

### [XPLM_VK_UP](/sdk/XPLM_VK_UP/)

```cpp
#define XPLM_VK_UP           0x26
```

### [XPLM_VK_RIGHT](/sdk/XPLM_VK_RIGHT/)

```cpp
#define XPLM_VK_RIGHT        0x27
```

### [XPLM_VK_DOWN](/sdk/XPLM_VK_DOWN/)

```cpp
#define XPLM_VK_DOWN         0x28
```

### [XPLM_VK_SELECT](/sdk/XPLM_VK_SELECT/)

```cpp
#define XPLM_VK_SELECT       0x29
```

### [XPLM_VK_PRINT](/sdk/XPLM_VK_PRINT/)

```cpp
#define XPLM_VK_PRINT        0x2A
```

### [XPLM_VK_EXECUTE](/sdk/XPLM_VK_EXECUTE/)

```cpp
#define XPLM_VK_EXECUTE      0x2B
```

### [XPLM_VK_SNAPSHOT](/sdk/XPLM_VK_SNAPSHOT/)

```cpp
#define XPLM_VK_SNAPSHOT     0x2C
```

### [XPLM_VK_INSERT](/sdk/XPLM_VK_INSERT/)

```cpp
#define XPLM_VK_INSERT       0x2D
```

### [XPLM_VK_DELETE](/sdk/XPLM_VK_DELETE/)

```cpp
#define XPLM_VK_DELETE       0x2E
```

### [XPLM_VK_HELP](/sdk/XPLM_VK_HELP/)

```cpp
#define XPLM_VK_HELP         0x2F
```

### [XPLM_VK_0](/sdk/XPLM_VK_0/)

```cpp
#define XPLM_VK_0            0x30
```

[XPLM_VK_0](/sdk/XPLM_VK_0/)thru[XPLM_VK_9](/sdk/XPLM_VK_9/)are the same as
ASCII ‘0’ thru ‘9’ (0x30 - 0x39)

### [XPLM_VK_1](/sdk/XPLM_VK_1/)

```cpp
#define XPLM_VK_1            0x31
```

### [XPLM_VK_2](/sdk/XPLM_VK_2/)

```cpp
#define XPLM_VK_2            0x32
```

### [XPLM_VK_3](/sdk/XPLM_VK_3/)

```cpp
#define XPLM_VK_3            0x33
```

### [XPLM_VK_4](/sdk/XPLM_VK_4/)

```cpp
#define XPLM_VK_4            0x34
```

### [XPLM_VK_5](/sdk/XPLM_VK_5/)

```cpp
#define XPLM_VK_5            0x35
```

### [XPLM_VK_6](/sdk/XPLM_VK_6/)

```cpp
#define XPLM_VK_6            0x36
```

### [XPLM_VK_7](/sdk/XPLM_VK_7/)

```cpp
#define XPLM_VK_7            0x37
```

### [XPLM_VK_8](/sdk/XPLM_VK_8/)

```cpp
#define XPLM_VK_8            0x38
```

### [XPLM_VK_9](/sdk/XPLM_VK_9/)

```cpp
#define XPLM_VK_9            0x39
```

### [XPLM_VK_A](/sdk/XPLM_VK_A/)

```cpp
#define XPLM_VK_A            0x41
```

[XPLM_VK_A](/sdk/XPLM_VK_A/)thru[XPLM_VK_Z](/sdk/XPLM_VK_Z/)are the same as
ASCII ‘A’ thru ‘Z’ (0x41 - 0x5A)

### [XPLM_VK_B](/sdk/XPLM_VK_B/)

```cpp
#define XPLM_VK_B            0x42
```

### [XPLM_VK_C](/sdk/XPLM_VK_C/)

```cpp
#define XPLM_VK_C            0x43
```

### [XPLM_VK_D](/sdk/XPLM_VK_D/)

```cpp
#define XPLM_VK_D            0x44
```

### [XPLM_VK_E](/sdk/XPLM_VK_E/)

```cpp
#define XPLM_VK_E            0x45
```

### [XPLM_VK_F](/sdk/XPLM_VK_F/)

```cpp
#define XPLM_VK_F            0x46
```

### [XPLM_VK_G](/sdk/XPLM_VK_G/)

```cpp
#define XPLM_VK_G            0x47
```

### [XPLM_VK_H](/sdk/XPLM_VK_H/)

```cpp
#define XPLM_VK_H            0x48
```

### [XPLM_VK_I](/sdk/XPLM_VK_I/)

```cpp
#define XPLM_VK_I            0x49
```

### [XPLM_VK_J](/sdk/XPLM_VK_J/)

```cpp
#define XPLM_VK_J            0x4A
```

### [XPLM_VK_K](/sdk/XPLM_VK_K/)

```cpp
#define XPLM_VK_K            0x4B
```

### [XPLM_VK_L](/sdk/XPLM_VK_L/)

```cpp
#define XPLM_VK_L            0x4C
```

### [XPLM_VK_M](/sdk/XPLM_VK_M/)

```cpp
#define XPLM_VK_M            0x4D
```

### [XPLM_VK_N](/sdk/XPLM_VK_N/)

```cpp
#define XPLM_VK_N            0x4E
```

### [XPLM_VK_O](/sdk/XPLM_VK_O/)

```cpp
#define XPLM_VK_O            0x4F
```

### [XPLM_VK_P](/sdk/XPLM_VK_P/)

```cpp
#define XPLM_VK_P            0x50
```

### [XPLM_VK_Q](/sdk/XPLM_VK_Q/)

```cpp
#define XPLM_VK_Q            0x51
```

### [XPLM_VK_R](/sdk/XPLM_VK_R/)

```cpp
#define XPLM_VK_R            0x52
```

### [XPLM_VK_S](/sdk/XPLM_VK_S/)

```cpp
#define XPLM_VK_S            0x53
```

### [XPLM_VK_T](/sdk/XPLM_VK_T/)

```cpp
#define XPLM_VK_T            0x54
```

### [XPLM_VK_U](/sdk/XPLM_VK_U/)

```cpp
#define XPLM_VK_U            0x55
```

### [XPLM_VK_V](/sdk/XPLM_VK_V/)

```cpp
#define XPLM_VK_V            0x56
```

### [XPLM_VK_W](/sdk/XPLM_VK_W/)

```cpp
#define XPLM_VK_W            0x57
```

### [XPLM_VK_X](/sdk/XPLM_VK_X/)

```cpp
#define XPLM_VK_X            0x58
```

### [XPLM_VK_Y](/sdk/XPLM_VK_Y/)

```cpp
#define XPLM_VK_Y            0x59
```

### [XPLM_VK_Z](/sdk/XPLM_VK_Z/)

```cpp
#define XPLM_VK_Z            0x5A
```

### [XPLM_VK_NUMPAD0](/sdk/XPLM_VK_NUMPAD0/)

```cpp
#define XPLM_VK_NUMPAD0      0x60
```

### [XPLM_VK_NUMPAD1](/sdk/XPLM_VK_NUMPAD1/)

```cpp
#define XPLM_VK_NUMPAD1      0x61
```

### [XPLM_VK_NUMPAD2](/sdk/XPLM_VK_NUMPAD2/)

```cpp
#define XPLM_VK_NUMPAD2      0x62
```

### [XPLM_VK_NUMPAD3](/sdk/XPLM_VK_NUMPAD3/)

```cpp
#define XPLM_VK_NUMPAD3      0x63
```

### [XPLM_VK_NUMPAD4](/sdk/XPLM_VK_NUMPAD4/)

```cpp
#define XPLM_VK_NUMPAD4      0x64
```

### [XPLM_VK_NUMPAD5](/sdk/XPLM_VK_NUMPAD5/)

```cpp
#define XPLM_VK_NUMPAD5      0x65
```

### [XPLM_VK_NUMPAD6](/sdk/XPLM_VK_NUMPAD6/)

```cpp
#define XPLM_VK_NUMPAD6      0x66
```

### [XPLM_VK_NUMPAD7](/sdk/XPLM_VK_NUMPAD7/)

```cpp
#define XPLM_VK_NUMPAD7      0x67
```

### [XPLM_VK_NUMPAD8](/sdk/XPLM_VK_NUMPAD8/)

```cpp
#define XPLM_VK_NUMPAD8      0x68
```

### [XPLM_VK_NUMPAD9](/sdk/XPLM_VK_NUMPAD9/)

```cpp
#define XPLM_VK_NUMPAD9      0x69
```

### [XPLM_VK_MULTIPLY](/sdk/XPLM_VK_MULTIPLY/)

```cpp
#define XPLM_VK_MULTIPLY     0x6A
```

### [XPLM_VK_ADD](/sdk/XPLM_VK_ADD/)

```cpp
#define XPLM_VK_ADD          0x6B
```

### [XPLM_VK_SEPARATOR](/sdk/XPLM_VK_SEPARATOR/)

```cpp
#define XPLM_VK_SEPARATOR    0x6C
```

### [XPLM_VK_SUBTRACT](/sdk/XPLM_VK_SUBTRACT/)

```cpp
#define XPLM_VK_SUBTRACT     0x6D
```

### [XPLM_VK_DECIMAL](/sdk/XPLM_VK_DECIMAL/)

```cpp
#define XPLM_VK_DECIMAL      0x6E
```

### [XPLM_VK_DIVIDE](/sdk/XPLM_VK_DIVIDE/)

```cpp
#define XPLM_VK_DIVIDE       0x6F
```

### [XPLM_VK_F1](/sdk/XPLM_VK_F1/)

```cpp
#define XPLM_VK_F1           0x70
```

### [XPLM_VK_F2](/sdk/XPLM_VK_F2/)

```cpp
#define XPLM_VK_F2           0x71
```

### [XPLM_VK_F3](/sdk/XPLM_VK_F3/)

```cpp
#define XPLM_VK_F3           0x72
```

### [XPLM_VK_F4](/sdk/XPLM_VK_F4/)

```cpp
#define XPLM_VK_F4           0x73
```

### [XPLM_VK_F5](/sdk/XPLM_VK_F5/)

```cpp
#define XPLM_VK_F5           0x74
```

### [XPLM_VK_F6](/sdk/XPLM_VK_F6/)

```cpp
#define XPLM_VK_F6           0x75
```

### [XPLM_VK_F7](/sdk/XPLM_VK_F7/)

```cpp
#define XPLM_VK_F7           0x76
```

### [XPLM_VK_F8](/sdk/XPLM_VK_F8/)

```cpp
#define XPLM_VK_F8           0x77
```

### [XPLM_VK_F9](/sdk/XPLM_VK_F9/)

```cpp
#define XPLM_VK_F9           0x78
```

### [XPLM_VK_F10](/sdk/XPLM_VK_F10/)

```cpp
#define XPLM_VK_F10          0x79
```

### [XPLM_VK_F11](/sdk/XPLM_VK_F11/)

```cpp
#define XPLM_VK_F11          0x7A
```

### [XPLM_VK_F12](/sdk/XPLM_VK_F12/)

```cpp
#define XPLM_VK_F12          0x7B
```

### [XPLM_VK_F13](/sdk/XPLM_VK_F13/)

```cpp
#define XPLM_VK_F13          0x7C
```

### [XPLM_VK_F14](/sdk/XPLM_VK_F14/)

```cpp
#define XPLM_VK_F14          0x7D
```

### [XPLM_VK_F15](/sdk/XPLM_VK_F15/)

```cpp
#define XPLM_VK_F15          0x7E
```

### [XPLM_VK_F16](/sdk/XPLM_VK_F16/)

```cpp
#define XPLM_VK_F16          0x7F
```

### [XPLM_VK_F17](/sdk/XPLM_VK_F17/)

```cpp
#define XPLM_VK_F17          0x80
```

### [XPLM_VK_F18](/sdk/XPLM_VK_F18/)

```cpp
#define XPLM_VK_F18          0x81
```

### [XPLM_VK_F19](/sdk/XPLM_VK_F19/)

```cpp
#define XPLM_VK_F19          0x82
```

### [XPLM_VK_F20](/sdk/XPLM_VK_F20/)

```cpp
#define XPLM_VK_F20          0x83
```

### [XPLM_VK_F21](/sdk/XPLM_VK_F21/)

```cpp
#define XPLM_VK_F21          0x84
```

### [XPLM_VK_F22](/sdk/XPLM_VK_F22/)

```cpp
#define XPLM_VK_F22          0x85
```

### [XPLM_VK_F23](/sdk/XPLM_VK_F23/)

```cpp
#define XPLM_VK_F23          0x86
```

### [XPLM_VK_F24](/sdk/XPLM_VK_F24/)

```cpp
#define XPLM_VK_F24          0x87
```

### [XPLM_VK_EQUAL](/sdk/XPLM_VK_EQUAL/)

```cpp
#define XPLM_VK_EQUAL        0xB0
```

The following definitions are extended and are not based on the Microsoft key
set.

### [XPLM_VK_MINUS](/sdk/XPLM_VK_MINUS/)

```cpp
#define XPLM_VK_MINUS        0xB1
```

### [XPLM_VK_RBRACE](/sdk/XPLM_VK_RBRACE/)

```cpp
#define XPLM_VK_RBRACE       0xB2
```

### [XPLM_VK_LBRACE](/sdk/XPLM_VK_LBRACE/)

```cpp
#define XPLM_VK_LBRACE       0xB3
```

### [XPLM_VK_QUOTE](/sdk/XPLM_VK_QUOTE/)

```cpp
#define XPLM_VK_QUOTE        0xB4
```

### [XPLM_VK_SEMICOLON](/sdk/XPLM_VK_SEMICOLON/)

```cpp
#define XPLM_VK_SEMICOLON    0xB5
```

### [XPLM_VK_BACKSLASH](/sdk/XPLM_VK_BACKSLASH/)

```cpp
#define XPLM_VK_BACKSLASH    0xB6
```

### [XPLM_VK_COMMA](/sdk/XPLM_VK_COMMA/)

```cpp
#define XPLM_VK_COMMA        0xB7
```

### [XPLM_VK_SLASH](/sdk/XPLM_VK_SLASH/)

```cpp
#define XPLM_VK_SLASH        0xB8
```

### [XPLM_VK_PERIOD](/sdk/XPLM_VK_PERIOD/)

```cpp
#define XPLM_VK_PERIOD       0xB9
```

### [XPLM_VK_BACKQUOTE](/sdk/XPLM_VK_BACKQUOTE/)

```cpp
#define XPLM_VK_BACKQUOTE    0xBA
```

### [XPLM_VK_ENTER](/sdk/XPLM_VK_ENTER/)

```cpp
#define XPLM_VK_ENTER        0xBB
```

### [XPLM_VK_NUMPAD_ENT](/sdk/XPLM_VK_NUMPAD_ENT/)

```cpp
#define XPLM_VK_NUMPAD_ENT   0xBC
```

### [XPLM_VK_NUMPAD_EQ](/sdk/XPLM_VK_NUMPAD_EQ/)

```cpp
#define XPLM_VK_NUMPAD_EQ    0xBD
```

### [XPLMFixedString150_t](/sdk/XPLMFixedString150_t/)

A container for a fixed-size string buffer of 150 characters.

```cpp
typedef struct {
     // The size of the struct.
     char                      buffer[150];
} XPLMFixedString150_t;
```

### [XPLMCursorStatus](/sdk/XPLMCursorStatus/)

[XPLMCursorStatus](/sdk/XPLMCursorStatus/)describes how you would like X-Plane
to manage the cursor. See[XPLMHandleCursor_f](/sdk/XPLMHandleCursor_f/)for more
info.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_CursorDefault](/sdk/xplm_CursorDefault/) | "0" | X-Plane manages the
cursor normally, plugin does not affect the cusrsor. |
| [xplm_CursorHidden](/sdk/xplm_CursorHidden/) | "1" | X-Plane hides the cursor.
|
| [xplm_CursorArrow](/sdk/xplm_CursorArrow/) | "2" | X-Plane shows the cursor as
the default arrow. |
| [xplm_CursorCustom](/sdk/xplm_CursorCustom/) | "3" | X-Plane shows the cursor
but lets you select an OS cursor. |

### [XPLMMouseStatus](/sdk/XPLMMouseStatus/)

```cpp
When the mouse is clicked, your mouse click routine is called repeatedly.  It is first called with the
mouse down message.  It is then called zero or more times with the mouse-drag message, and finally it
is called once with the mouse up message.  All of these messages will be directed to the same window;
you are guaranteed to not receive a drag or mouse-up event without first receiving the corresponding mouse-down.

```

| Name | Value | Description |
| --- | --- | --- |
| [xplm_MouseDown](/sdk/xplm_MouseDown/) | "1" |
| [xplm_MouseDrag](/sdk/xplm_MouseDrag/) | "2" |
| [xplm_MouseUp](/sdk/xplm_MouseUp/) | "3" |

### [XPLMDestroyAvionics](/sdk/XPLMDestroyAvionics/)

```cpp
XPLM_API void       XPLMDestroyAvionics(
                         XPLMAvionicsID       inHandle);

```

Destroys the cockpit device and deallocates its screen’s memory. You should only
ever call this for devices that you created
using[XPLMCreateAvionicsEx](/sdk/XPLMCreateAvionicsEx/)(), not X-Plane'
built-ine devices you have customised.

### [XPLMDeviceID](/sdk/XPLMDeviceID/)

This constant indicates the device we want to override or enhance. We can get a
callback before or after each item.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_device_GNS430_1](/sdk/xplm_device_GNS430_1/) | "0" | GNS430, pilot side.
|
| [xplm_device_GNS430_2](/sdk/xplm_device_GNS430_2/) | "1" | GNS430, copilot
side. |
| [xplm_device_GNS530_1](/sdk/xplm_device_GNS530_1/) | "2" | GNS530, pilot side.
|
| [xplm_device_GNS530_2](/sdk/xplm_device_GNS530_2/) | "3" | GNS530, copilot
side. |
| [xplm_device_CDU739_1](/sdk/xplm_device_CDU739_1/) | "4" | generic airliner
CDU, pilot side. |
| [xplm_device_CDU739_2](/sdk/xplm_device_CDU739_2/) | "5" | generic airliner
CDU, copilot side. |
| [xplm_device_G1000_PFD_1](/sdk/xplm_device_G1000_PFD_1/) | "6" | G1000 Primary
Flight Display, pilot side. |
| [xplm_device_G1000_MFD](/sdk/xplm_device_G1000_MFD/) | "7" | G1000
Multifunction Display. |
| [xplm_device_G1000_PFD_2](/sdk/xplm_device_G1000_PFD_2/) | "8" | G1000 Primary
Flight Display, copilot side. |
| [xplm_device_CDU815_1](/sdk/xplm_device_CDU815_1/) | "9" | Primus CDU, pilot
side. |
| [xplm_device_CDU815_2](/sdk/xplm_device_CDU815_2/) | "10" | Primus CDU,
copilot side. |
| [xplm_device_Primus_PFD_1](/sdk/xplm_device_Primus_PFD_1/) | "11" | Primus
Primary Flight Display, pilot side. |
| [xplm_device_Primus_PFD_2](/sdk/xplm_device_Primus_PFD_2/) | "12" | Primus
Primary Flight Display, copilot side. |
| [xplm_device_Primus_MFD_1](/sdk/xplm_device_Primus_MFD_1/) | "13" | Primus
Multifunction Display, pilot side. |
| [xplm_device_Primus_MFD_2](/sdk/xplm_device_Primus_MFD_2/) | "14" | Primus
Multifunction Display, copilot side. |
| [xplm_device_Primus_MFD_3](/sdk/xplm_device_Primus_MFD_3/) | "15" | Primus
Multifunction Display, central. |
| [xplm_device_Primus_RMU_1](/sdk/xplm_device_Primus_RMU_1/) | "16" | Primus
Radio Management Unit, pilot side. |
| [xplm_device_Primus_RMU_2](/sdk/xplm_device_Primus_RMU_2/) | "17" | Primus
Radio Management Unit, copilot side. |
| [xplm_device_MCDU_1](/sdk/xplm_device_MCDU_1/) | "18" | Airbus MCDU, pilot
side. |
| [xplm_device_MCDU_2](/sdk/xplm_device_MCDU_2/) | "19" | Airbus MCDU, copilot
side. |

### [XPLMError_f](/sdk/XPLMError_f/)

```cpp
typedef void (* XPLMError_f)(
                         const char *         inMessage);

```

An XPLM error callback is a function that you provide to receive debugging
information from the plugin SDK.
See[XPLMSetErrorCallback](/sdk/XPLMSetErrorCallback/)for more information. NOTE:
for the sake of debugging, your error callback will be called even if your
plugin is not enabled, allowing you to receive debug info in your XPluginStart
and XPluginStop callbacks. To avoid causing logic errors in the management code,
do not call any other plugin routines from your error callback - it is only
meant for catching errors in the debugging.

### [XPLMExtractFileAndPath](/sdk/XPLMExtractFileAndPath/)

```cpp
XPLM_API char *     XPLMExtractFileAndPath(
                         char *               inFullPath);

```

Given a full path to a file, this routine separates the path from the file. If
the path is a partial directory (e.g. ends in : or / ) the trailing directory
separator is removed. This routine works in-place; a pointer to the file part of
the buffer is returned; the original buffer still starts with the path and is
null terminated with no trailing separator.

### [XPLMFeatureEnumerator_f](/sdk/XPLMFeatureEnumerator_f/)

```cpp
typedef void (* XPLMFeatureEnumerator_f)(
                         const char *         inFeature,
                         void *               inRef);

```

You pass an[XPLMFeatureEnumerator_f](/sdk/XPLMFeatureEnumerator_f/)to get a list
of all features supported by a given version running version of X-Plane. This
routine is called once for each feature.

### [XPLMFindCommand](/sdk/XPLMFindCommand/)

```cpp
XPLM_API XPLMCommandRef XPLMFindCommand(
                         const char *         inName);

```

[XPLMFindCommand](/sdk/XPLMFindCommand/)looks up a command by name, and returns
its command reference or NULL if the command does not exist.

### [XPLMFindSymbol](/sdk/XPLMFindSymbol/)

```cpp
XPLM_API void *     XPLMFindSymbol(
                         const char *         inString);

```

This routine will attempt to find the symbol passed in the inString parameter.
If the symbol is found a pointer the function is returned, othewise the function
will return NULL.

You can use[XPLMFindSymbol](/sdk/XPLMFindSymbol/)to utilize newer SDK API
features without requiring newer versions of the SDK (and X-Plane) as your
minimum X-Plane version as follows:

- Define the XPLMnnn macro to the minimum required XPLM version you will ship with
  (e.g. XPLM210 for X-Plane 10 compatibility).
- Use[XPLMGetVersions](/sdk/XPLMGetVersions/)and[XPLMFindSymbol](/sdk/XPLMFindSymbol/)to
  detect that the host sim is new enough to use new functions and resolve function
  pointers.
- Conditionally use the new functions if and only
  if[XPLMFindSymbol](/sdk/XPLMFindSymbol/)only returns a non- NULL pointer.

Warning: you should always check the XPLM API version as well as the results
of[XPLMFindSymbol](/sdk/XPLMFindSymbol/)to determine if funtionality is safe to
use.

To use functionality via[XPLMFindSymbol](/sdk/XPLMFindSymbol/)you will need to
copy your own definitions of the X-Plane API prototypes and cast the returned
pointer to the correct type.

### [XPLMFixedString150_t](/sdk/XPLMFixedString150_t/)

A container for a fixed-size string buffer of 150 characters.

```cpp
typedef struct {
     // The size of the struct.
     char                      buffer[150];
} XPLMFixedString150_t;
```

### [XPLMFontID](/sdk/XPLMFontID/)

X-Plane features some fixed-character fonts. Each font may have its own metrics.

WARNING: Some of these fonts are no longer supported or may have changed
geometries. For maximum copmatibility, see the comments below.

Note: X-Plane 7 supports proportional-spaced fonts. Since no measuring routine
is available yet, the SDK will normally draw using a fixed-width font. You can
use a dataref to enable proportional font drawing on XP7 if you want to.

| Name | Value | Description |
| --- | --- | --- |
| [xplmFont_Basic](/sdk/xplmFont_Basic/) | "0" | Mono-spaced font for user
interface. Available in all versions of the SDK. |
| [xplmFont_Menus](/sdk/xplmFont_Menus/) | "1" | Deprecated, do not use. |
| [xplmFont_Metal](/sdk/xplmFont_Metal /) | "2" | Deprecated, do not use. |
| [xplmFont_Led](/sdk/xplmFont_Led/) | "3" | Deprecated, do not use. |
| [xplmFont_LedWide](/sdk/xplmFont_LedWide/) | "4" | Deprecated, do not use. |
| [xplmFont_PanelHUD](/sdk/xplmFont_PanelHUD/) | "5" | Deprecated, do not use. |
| [xplmFont_PanelEFIS](/sdk/xplmFont_PanelEFIS/) | "6" | Deprecated, do not use.
|
| [xplmFont_PanelGPS](/sdk/xplmFont_PanelGPS/) | "7" | Deprecated, do not use. |
| [xplmFont_RadiosGA](/sdk/xplmFont_RadiosGA/) | "8" | Deprecated, do not use. |
| [xplmFont_RadiosBC](/sdk/xplmFont_RadiosBC/) | "9" | Deprecated, do not use. |
| [xplmFont_RadiosHM](/sdk/xplmFont_RadiosHM/) | "10" | Deprecated, do not use.
|
| [xplmFont_RadiosGANarrow](/sdk/xplmFont_RadiosGANarrow/) | "11" | Deprecated,
do not use. |
| [xplmFont_RadiosBCNarrow](/sdk/xplmFont_RadiosBCNarrow/) | "12" | Deprecated,
do not use. |
| [xplmFont_RadiosHMNarrow](/sdk/xplmFont_RadiosHMNarrow/) | "13" | Deprecated,
do not use. |
| [xplmFont_Timer](/sdk/xplmFont_Timer /) | "14" | Deprecated, do not use. |
| [xplmFont_FullRound](/sdk/xplmFont_FullRound/) | "15" | Deprecated, do not
use. |
| [xplmFont_SmallRound](/sdk/xplmFont_SmallRound/) | "16" | Deprecated, do not
use. |
| [xplmFont_Menus_Localized](/sdk/xplmFont_Menus_Localized /) | "17" |
Deprecated, do not use. |
| [xplmFont_Proportional](/sdk/xplmFont_Proportional/) | "18" | Proportional UI
font. |

### [XPLMGetAllMonitorBoundsOS](/sdk/XPLMGetAllMonitorBoundsOS/)

```cpp
XPLM_API void       XPLMGetAllMonitorBoundsOS(
                         XPLMReceiveMonitorBoundsOS_f inMonitorBoundsCallback,
                         void *               inRefcon);

```

This routine immediately calls you back with the bounds (in pixels) of each
monitor within the operating system’s global desktop space. Note that
unlike[XPLMGetAllMonitorBoundsGlobal](/sdk/XPLMGetAllMonitorBoundsGlobal/)(),
this may include monitors that have no X-Plane window on them.

Note that this function’s monitor indices match those provided
by[XPLMGetAllMonitorBoundsGlobal](/sdk/XPLMGetAllMonitorBoundsGlobal/)(), but
the coordinates are different (since the X-Plane global desktop may not match
the operating system’s global desktop, and one X-Plane boxel may be larger than
one pixel).

### [XPLMGetAvionicsBrightnessRheo](/sdk/XPLMGetAvionicsBrightnessRheo/)

```cpp
XPLM_API float      XPLMGetAvionicsBrightnessRheo(
                         XPLMAvionicsID       inHandle);

```

Returns the brightness setting value, between 0 and 1, for the screen of the
cockpit device with the given handle.

```cpp
    If the device is bound to the current aircraft, this is a shortcut to getting the brightness rheostat value from the `sim/cockpit2/switches/instrument_brightness_ratio[]` dataref; this gets the slot in the `instrument_brightness_ratio` array to which the device is bound.

    If the device is not currently bound, this returns the device's own brightness rheostat value.

```

### [XPLMGetAvionicsBusVoltsRatio](/sdk/XPLMGetAvionicsBusVoltsRatio/)

```cpp
XPLM_API float      XPLMGetAvionicsBusVoltsRatio(
                         XPLMAvionicsID       inHandle);

```

Returns the ratio of the nominal voltage (1.0 means full nominal voltage) of the
electrical bus to which the given avionics device is bound, or -1 if the device
is not bound to the current aircraft.

### [XPLMGetAvionicsGeometry](/sdk/XPLMGetAvionicsGeometry/)

```cpp
XPLM_API void       XPLMGetAvionicsGeometry(
                         XPLMAvionicsID       inHandle,
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

Returns the bounds of a cockpit device’s popup window in the X-Plane coordinate
system.

### [XPLMGetAvionicsGeometryOS](/sdk/XPLMGetAvionicsGeometryOS/)

```cpp
XPLM_API void       XPLMGetAvionicsGeometryOS(
                         XPLMAvionicsID       inHandle,
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

Returns the bounds of a cockpit device’s popped-out window.

### [XPLMGetAvionicsHandle](/sdk/XPLMGetAvionicsHandle/)

```cpp
XPLM_API XPLMAvionicsID XPLMGetAvionicsHandle(
                         XPLMDeviceID         inDeviceID);

```

This routine registers no callbacks for a built-in cockpit device, but returns a
handle which allows you to interact with it using the Avionics Device API. Use
this if you do not wish to intercept drawing, clicks and touchscreen calls to a
device, but want to interact with its popup programmatically. This is equivalent
to calling XPLMRegisterAvionicsCallbackEx() with NULL for all callbacks.

### [XPLMGetCycleNumber](/sdk/XPLMGetCycleNumber/)

```cpp
XPLM_API int        XPLMGetCycleNumber(void);

```

This routine returns a counter starting at zero for each sim cycle
computed/video frame rendered.

### [XPLMGetDirectoryContents](/sdk/XPLMGetDirectoryContents/)

```cpp
XPLM_API int        XPLMGetDirectoryContents(
                         const char *         inDirectoryPath,
                         int                  inFirstReturn,
                         char *               outFileNames,
                         int                  inFileNameBufSize,
                         char **              outIndices,    /* Can be NULL */
                         int                  inIndexCount,
                         int *                outTotalFiles,    /* Can be NULL */
                         int *                outReturnedFiles);    /* Can be NULL */

```

This routine returns a list of files in a directory (specified by a full path,
no trailing : or / ). The output is returned as a list of NULL terminated
strings. An index array (if specified) is filled with pointers into the strings.
The last file is indicated by a zero-length string (and NULL in the indices).
This routine will return 1 if you had capacity for all files or 0 if you did
not. You can also skip a given number of files.

- inDirectoryPath - a null terminated C string containing the full path to the
  directory with no trailing directory char.
- inFirstReturn - the zero-based index of the first file in the directory to
  return. (Usually zero to fetch all in one pass.)
- outFileNames - a buffer to receive a series of sequential null terminated
  C-string file names. A zero-length C string will be appended to the very end.
- inFileNameBufSize - the size of the file name buffer in bytes.
- outIndices - a pointer to an array of character pointers that will become an
  index into the directory. The last file will be followed by a NULL value. Pass
  NULL if you do not want indexing information.
- inIndexCount - the max size of the index in entries.
- outTotalFiles - if not NULL, this is filled in with the number of files in the
  directory.
- outReturnedFiles - if not NULL, the number of files returned by this iteration.

Return value: 1 if all info could be returned, 0 if there was a buffer overrun.

WARNING: Before X-Plane 7 this routine did not properly iterate through
directories. If X-Plane 6 compatibility is needed, use your own code to iterate
directories.

### [XPLMGetDirectorySeparator](/sdk/XPLMGetDirectorySeparator/)

```cpp
XPLM_API const char * XPLMGetDirectorySeparator(void);

```

This routine returns a string with one char and a null terminator that is the
directory separator for the current platform. This allows you to write code that
concatenates directory paths without having to #ifdef for platform. The
character returned will reflect the current file path mode.

### [XPLMGetElapsedTime](/sdk/XPLMGetElapsedTime/)

```cpp
XPLM_API float      XPLMGetElapsedTime(void);

```

This routine returns the elapsed time since the sim started up in decimal
seconds. This is a wall timer; it keeps counting upward even if the sim is
pasued.

**WARNING**:[XPLMGetElapsedTime](/sdk/XPLMGetElapsedTime/)is not a very good
timer! It lacks precision in both its data type and its source. Do not attempt
to use it for timing critical applications like network multiplayer.

### [XPLMGetFontDimensions](/sdk/XPLMGetFontDimensions/)

```cpp
XPLM_API void       XPLMGetFontDimensions(
                         XPLMFontID           inFontID,
                         int *                outCharWidth,    /* Can be NULL */
                         int *                outCharHeight,    /* Can be NULL */
                         int *                outDigitsOnly);    /* Can be NULL */

```

This routine returns the width and height of a character in a given font. It
also tells you if the font only supports numeric digits. Pass NULL if you don’t
need a given field. Note that for a proportional font the width will be an
arbitrary, hopefully average width.

### [XPLMGetVirtualKeyDescription](/sdk/XPLMGetVirtualKeyDescription/)

```cpp
XPLM_API const char * XPLMGetVirtualKeyDescription(
                         char                 inVirtualKey);

```

Given a virtual key code (as defined in[XPLMDefs](/sdk/XPLMDefs/).h) this
routine returns a human-readable string describing the character. This routine
is provided for showing users what keyboard mappings they have set up. The
string may read ‘unknown’ or be a blank or NULL string if the virtual key is
unknown.

### [XPLMHandleCursor_f](/sdk/XPLMHandleCursor_f/)

```cpp
typedef XPLMCursorStatus (* XPLMHandleCursor_f)(
                         XPLMWindowID         inWindowID,
                         int                  x,
                         int                  y,
                         void *               inRefcon);

```

The SDK calls your cursor status callback when the mouse is over your plugin
window. Return a cursor status code to indicate how you would like X-Plane to
manage the cursor. If you return[xplm_CursorDefault](/sdk/xplm_CursorDefault/),
the SDK will try lower-Z-order plugin windows, then let the sim manage the
cursor.

Note: you should never show or hide the cursor yourself—these APIs are typically
reference-counted and thus cannot safely and predictably be used by the SDK.
Instead return one of[xplm_CursorHidden](/sdk/xplm_CursorHidden/)to hide the
cursor or xplm_CursorArrow/xplm_CursorCustom to show the cursor.

If you want to implement a custom cursor by drawing a cursor in OpenGL,
use[xplm_CursorHidden](/sdk/xplm_CursorHidden/)to hide the OS cursor and draw
the cursor using a 2-d drawing callback
(after[xplm_Phase_Window](/sdk/xplm_Phase_Window/)is probably a good choice, but
see deprecation warnings on the drawing APIs!). If you want to use a custom
OS-based cursor, use[xplm_CursorCustom](/sdk/xplm_CursorCustom/)to ask X-Plane
to show the cursor but not affect its image. You can then use an OS specific
call like SetThemeCursor (Mac) or SetCursor/LoadCursor (Windows).

The units for x and y values match the units used in your window. Thus, for
“modern” windows (those created
via[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)() and compiled against the
XPLM300 library), the units are boxels, while legacy windows will get pixels.
Legacy windows have their origin in the lower left of the main X-Plane window,
while modern windows have their origin in the lower left of the global desktop
space. In both cases, x increases as you move right, and y increases as you move
up.

### [XPLMHandleKey_f](/sdk/XPLMHandleKey_f/)

```cpp
typedef void (* XPLMHandleKey_f)(
                         XPLMWindowID         inWindowID,
                         char                 inKey,
                         XPLMKeyFlags         inFlags,
                         char                 inVirtualKey,
                         void *               inRefcon,
                         int                  losingFocus);

```

This function is called when a key is pressed or keyboard focus is taken away
from your window. If losingFocus is 1, you are losing the keyboard focus,
otherwise a key was pressed and inKey contains its character.

The window ID passed in will be your window for key presses, or the other window
taking focus when losing focus. Note that in the modern plugin system, often
focus is taken by the window manager itself; for this resaon, the window ID may
be zero when losing focus, and you should not write code that depends onit.

The refcon passed in will be the one from registration, for both key presses and
losing focus.

Warning: this API declares virtual keys as a signed character; however the VKEY
#define macros in[XPLMDefs](/sdk/XPLMDefs/).h define the vkeys using unsigned
values (that is 0x80 instead of -0x80). So you may need to cast the incoming
vkey to an unsigned char to get correct comparisons in C.

### [XPLMHasFeature](/sdk/XPLMHasFeature/)

```cpp
XPLM_API int        XPLMHasFeature(
                         const char *         inFeature);

```

This returns 1 if the given installation of X-Plane supports a feature, or 0 if
it does not.

### [XPLMHostApplicationID](/sdk/XPLMHostApplicationID/)

While the plug-in SDK is only accessible to plugins running inside X-Plane, the
original authors considered extending the API to other applications that shared
basic infrastructure with X-Plane. These enumerations are hold-overs from that
original roadmap; all values other than X-Plane are deprecated. Your plugin
should never need this enumeration.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_Host_Unknown](/sdk/xplm_Host_Unknown/) | "0" |
| [xplm_Host_XPlane](/sdk/xplm_Host_XPlane/) | "1" |
| [xplm_Host_PlaneMaker](/sdk/xplm_Host_PlaneMaker/) | "2" |
| [xplm_Host_WorldMaker](/sdk/xplm_Host_WorldMaker/) | "3" |
| [xplm_Host_Briefer](/sdk/xplm_Host_Briefer/) | "4" |
| [xplm_Host_PartMaker](/sdk/xplm_Host_PartMaker/) | "5" |
| [xplm_Host_YoungsMod](/sdk/xplm_Host_YoungsMod/) | "6" |
| [xplm_Host_XAuto](/sdk/xplm_Host_XAuto/) | "7" |
| [xplm_Host_Xavion](/sdk/xplm_Host_Xavion/) | "8" |
| [xplm_Host_Control_Pad](/sdk/xplm_Host_Control_Pad/) | "9" |
| [xplm_Host_PFD_Map](/sdk/xplm_Host_PFD_Map/) | "10" |
| [xplm_Host_RADAR](/sdk/xplm_Host_RADAR/) | "11" |

### [XPLMInitialized](/sdk/XPLMInitialized/)

```cpp
XPLM_API int        XPLMInitialized(void);

```

Deprecated: This function returns 1 if X-Plane has properly initialized the
plug-in system. If this routine returns 0, many XPLM functions will not work.

NOTE: because plugins are always called from within the XPLM, there is no need
to check for initialization; it will always return 1. This routine is deprecated
- you do not need to check it before continuing within your plugin.

### [XPLMIsAvionicsBound](/sdk/XPLMIsAvionicsBound/)

```cpp
XPLM_API int        XPLMIsAvionicsBound(
                         XPLMAvionicsID       inHandle);

```

Returns true (1) if the cockpit device with the given handle is used by the
current aircraft.

### [XPLMIsAvionicsPoppedOut](/sdk/XPLMIsAvionicsPoppedOut/)

```cpp
XPLM_API int        XPLMIsAvionicsPoppedOut(
                         XPLMAvionicsID       inHandle);

```

Returns true (1) if the popup window for a cockpit device is popped out.

### [XPLMIsAvionicsPopupVisible](/sdk/XPLMIsAvionicsPopupVisible/)

```cpp
XPLM_API int        XPLMIsAvionicsPopupVisible(
                         XPLMAvionicsID       inHandle);

```

Returns true (1) if the popup window for a cockpit device is visible.

### [XPLMIsCursorOverAvionics](/sdk/XPLMIsCursorOverAvionics/)

```cpp
XPLM_API int        XPLMIsCursorOverAvionics(
                         XPLMAvionicsID       inHandle,
                         int *                outX,    /* Can be NULL */
                         int *                outY);    /* Can be NULL */

```

Returns true (1) if the mouse is currently over the screen of cockpit device
with the given handle. If they are not NULL, the optional x and y arguments are
filled with the co-ordinates of the mouse cursor in device co-ordinates.

### [XPLMKeyFlags](/sdk/XPLMKeyFlags/)

These bitfields define modifier keys in a platform independent way. When a key
is pressed, a series of messages are sent to your plugin. The down flag is set
in the first of these messages, and the up flag in the last. While the key is
held down, messages are sent with neither flag set to indicate that the key is
being held down as a repeated character.

The control flag is mapped to the control flag on Macintosh and PC. Generally
X-Plane uses the control key and not the command key on Macintosh, providing a
consistent interface across platforms that does not necessarily match the
Macintosh user interface guidelines. There is not yet a way for plugins to
access the Macintosh control keys without using #ifdefed code.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_ShiftFlag](/sdk/xplm_ShiftFlag/) | "1" | The shift key is down |
| [xplm_OptionAltFlag](/sdk/xplm_OptionAltFlag/) | "2" | The option or alt key
is down |
| [xplm_ControlFlag](/sdk/xplm_ControlFlag /) | "4" | The control key is down |
| [xplm_DownFlag](/sdk/xplm_DownFlag/) | "8" | The key is being pressed down |
| [xplm_UpFlag](/sdk/xplm_UpFlag/) | "16" | The key is being released |

### [XPLMKeySniffer_f](/sdk/XPLMKeySniffer_f/)

```cpp
typedef int (* XPLMKeySniffer_f)(
                         char                 inChar,
                         XPLMKeyFlags         inFlags,
                         char                 inVirtualKey,
                         void *               inRefcon);

```

This is the prototype for a low level key-sniffing function. Window-based
UI*should not use this*! The windowing system provides high-level mediated
keyboard access, via the callbacks you attach to
your[XPLMCreateWindow_t](/sdk/XPLMCreateWindow_t/). By comparison, the key
sniffer provides low level keyboard access.

Key sniffers are provided to allow libraries to provide non-windowed user
interaction. For example, the MUI library uses a key sniffer to do pop-up text
entry.

Return 1 to pass the key on to the next sniffer, the window manager, X-Plane, or
whomever is down stream. Return 0 to consume the key.

Warning: this API declares virtual keys as a signed character; however the VKEY
#define macros in[XPLMDefs](/sdk/XPLMDefs/).h define the vkeys using unsigned
values (that is 0x80 instead of -0x80). So you may need to cast the incoming
vkey to an unsigned char to get correct comparisons in C.

### [XPLMLanguageCode](/sdk/XPLMLanguageCode/)

These enums define what language the sim is running in. These enumerations do
not imply that the sim can or does run in all of these languages; they simply
provide a known encoding in the event that a given sim version is localized to a
certain language.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_Language_Unknown](/sdk/xplm_Language_Unknown/) | "0" |
| [xplm_Language_English](/sdk/xplm_Language_English/) | "1" |
| [xplm_Language_French](/sdk/xplm_Language_French/) | "2" |
| [xplm_Language_German](/sdk/xplm_Language_German/) | "3" |
| [xplm_Language_Italian](/sdk/xplm_Language_Italian/) | "4" |
| [xplm_Language_Spanish](/sdk/xplm_Language_Spanish/) | "5" |
| [xplm_Language_Korean](/sdk/xplm_Language_Korean/) | "6" |
| [xplm_Language_Russian](/sdk/xplm_Language_Russian/) | "7" |
| [xplm_Language_Greek](/sdk/xplm_Language_Greek/) | "8" |
| [xplm_Language_Japanese](/sdk/xplm_Language_Japanese/) | "9" |
| [xplm_Language_Chinese](/sdk/xplm_Language_Chinese/) | "10" |
| [xplm_Language_Ukrainian](/sdk/xplm_Language_Ukrainian/) | "11" |

### [XPLMLibraryEnumerator_f](/sdk/XPLMLibraryEnumerator_f/)

```cpp
typedef void (* XPLMLibraryEnumerator_f)(
                         const char *         inFilePath,
                         void *               inRef);

```

An[XPLMLibraryEnumerator_f](/sdk/XPLMLibraryEnumerator_f/)is a callback you
provide that is called once for each library element that is located. The
returned paths will be relative to the X-System folder.

### [XPLMLoadDataFile](/sdk/XPLMLoadDataFile/)

```cpp
XPLM_API int        XPLMLoadDataFile(
                         XPLMDataFileType     inFileType,
                         const char *         inFilePath);    /* Can be NULL */

```

Loads a data file of a given type. Paths must be relative to the X-System
folder. To clear the replay, pass a NULL file name (this is only valid with
replay movies, not sit files).

### [XPLMLocalToWorld](/sdk/XPLMLocalToWorld/)

```cpp
XPLM_API void       XPLMLocalToWorld(
                         double               inX,
                         double               inY,
                         double               inZ,
                         double *             outLatitude,
                         double *             outLongitude,
                         double *             outAltitude);

```

This routine translates a local coordinate triplet back into latitude,
longitude, and altitude. Latitude and longitude are in decimal degrees, and
altitude is in meters MSL (mean sea level). The XYZ coordinates are in meters in
the local OpenGL coordinate system.

NOTE: world coordinates are less precise than local coordinates; you should try
to avoid round tripping from local to world and back.

### [XPLMMeasureString](/sdk/XPLMMeasureString/)

```cpp
XPLM_API float      XPLMMeasureString(
                         XPLMFontID           inFontID,
                         const char *         inChar,
                         int                  inNumChars);

```

This routine returns the width in pixels of a string using a given font. The
string is passed as a pointer plus length (and does not need to be null
terminated); this is used to allow for measuring substrings. The return value is
floating point; it is possible that future font drawing may allow for fractional
pixels.

### [XPLMPCMComplete_f](/sdk/XPLMPCMComplete_f/)

```cpp
typedef void (* XPLMPCMComplete_f)(
                         void *               inRefcon,
                         FMOD_RESULT          status);

```

If you use[XPLMPlayPCMOnBus](/sdk/XPLMPlayPCMOnBus/)() you may use this optional
callback to find out when the FMOD::Channel is complete, if you need to
deallocate memory for example.

### [XPLMPlaceUserAtLocation](/sdk/XPLMPlaceUserAtLocation/)

```cpp
XPLM_API void       XPLMPlaceUserAtLocation(
                         double               latitudeDegrees,
                         double               longitudeDegrees,
                         float                elevationMetersMSL,
                         float                headingDegreesTrue,
                         float                speedMetersPerSecond);

```

Places the user at a specific location after performing any necessary scenery
loads.

As with in-air starts initiated from the X-Plane user interface, the aircraft
will always start with its engines running, regardless of the user’s preferences
(i.e., regardless of what the dataref`sim/operation/prefs/startup_running`says).

### [XPLMPlayPCMOnBus](/sdk/XPLMPlayPCMOnBus/)

```cpp
XPLM_API FMOD_CHANNEL* XPLMPlayPCMOnBus(
                         void *               audioBuffer,
                         uint32_t             bufferSize,
                         FMOD_SOUND_FORMAT    soundFormat,
                         int                  freqHz,
                         int                  numChannels,
                         int                  loop,
                         XPLMAudioBus         audioType,
                         XPLMPCMComplete_f    inCallback,
                         void *               inRefcon);    /* Can be NULL */

```

Play an in-memory audio buffer on a given audio bus. The resulting FMOD channel
is returned. PAY ATTENTION TO THE CALLBACK - when the sample completes or is
stopped by X-Plane, the channel will go away. It’s up to you to listen for the
callback and invalidate any copy of the channel pointer you have lying around.
The callback is optional because if you have no intention of interacting with
the sound after it’s launched, then you don’t need to keep the channel pointer
at all. The sound is not started instantly. Instead, it will be started the next
time X-Plane refreshes the sound system, typically at the start of the next
frame. This allows you to set the initial position for the sound, if required.
The callback will be called on the main thread, and will be called only once per
sound. If the call fails and you provide a callback function, you will get a
callback with an FMOD status code.

### [XPLMPopOutAvionics](/sdk/XPLMPopOutAvionics/)

```cpp
XPLM_API void       XPLMPopOutAvionics(
                         XPLMAvionicsID       inHandle);

```

Pops out the window for a cockpit device.

### [XPLMReceiveMonitorBoundsOS_f](/sdk/XPLMReceiveMonitorBoundsOS_f/)

```cpp
typedef void (* XPLMReceiveMonitorBoundsOS_f)(
                         int                  inMonitorIndex,
                         int                  inLeftPx,
                         int                  inTopPx,
                         int                  inRightPx,
                         int                  inBottomPx,
                         void *               inRefcon);

```

This function is informed of the global bounds (in pixels) of a particular
monitor within the operating system’s global desktop space. Note that a monitor
index being passed to you here does not indicate that X-Plane is running in full
screen on this monitor, or even that any X-Plane windows exist on this monitor.

### [XPLMRegisterCommandHandler](/sdk/XPLMRegisterCommandHandler/)

```cpp
XPLM_API void       XPLMRegisterCommandHandler(
                         XPLMCommandRef       inComand,
                         XPLMCommandCallback_f inHandler,
                         int                  inBefore,
                         void *               inRefcon);

```

[XPLMRegisterCommandHandler](/sdk/XPLMRegisterCommandHandler/)registers a
callback to be called when a command is executed. You provide a callback with a
reference pointer.

If inBefore is true, your command handler callback will be executed before
X-Plane executes the command, and returning 0 from your callback will disable
X-Plane’s processing of the command. If inBefore is false, your callback will
run after X-Plane. (You can register a single callback both before and after a
command.)

### [XPLMRegisterDataAccessor](/sdk/XPLMRegisterDataAccessor/)

```cpp
XPLM_API XPLMDataRef XPLMRegisterDataAccessor(
                         const char *         inDataName,
                         XPLMDataTypeID       inDataType,
                         int                  inIsWritable,
                         XPLMGetDatai_f       inReadInt,
                         XPLMSetDatai_f       inWriteInt,
                         XPLMGetDataf_f       inReadFloat,
                         XPLMSetDataf_f       inWriteFloat,
                         XPLMGetDatad_f       inReadDouble,
                         XPLMSetDatad_f       inWriteDouble,
                         XPLMGetDatavi_f      inReadIntArray,
                         XPLMSetDatavi_f      inWriteIntArray,
                         XPLMGetDatavf_f      inReadFloatArray,
                         XPLMSetDatavf_f      inWriteFloatArray,
                         XPLMGetDatab_f       inReadData,
                         XPLMSetDatab_f       inWriteData,
                         void *               inReadRefcon,
                         void *               inWriteRefcon);

```

This routine creates a new item of data that can be read and written. Pass in
the data’s full name for searching, the type(s) of the data for accessing, and
whether the data can be written to. For each data type you support, pass in a
read accessor function and a write accessor function if necessary. Pass NULL for
data types you do not support or write accessors if you are read-only.

You are returned a dataref for the new item of data created. You can use this
dataref to unregister your data later or read or write from it.

### [XPLMRegisterKeySniffer](/sdk/XPLMRegisterKeySniffer/)

```cpp
XPLM_API int        XPLMRegisterKeySniffer(
                         XPLMKeySniffer_f     inCallback,
                         int                  inBeforeWindows,
                         void *               inRefcon);

```

This routine registers a key sniffing callback. You specify whether you want to
sniff before the window system, or only sniff keys the window system does not
consume. You should ALMOST ALWAYS sniff non-control keys after the window
system. When the window system consumes a key, it is because the user has
“focused” a window. Consuming the key or taking action based on the key will
produce very weird results. Returns 1 if successful.

### [XPLMSaveDataFile](/sdk/XPLMSaveDataFile/)

```cpp
XPLM_API int        XPLMSaveDataFile(
                         XPLMDataFileType     inFileType,
                         const char *         inFilePath);

```

Saves the current situation or replay; paths are relative to the X-System
folder.

### [XPLMSetAvionicsBrightnessRheo](/sdk/XPLMSetAvionicsBrightnessRheo/)

```cpp
XPLM_API void       XPLMSetAvionicsBrightnessRheo(
                         XPLMAvionicsID       inHandle,
                         float                brightness);

```

Sets the brightness setting’s value, between 0 and 1, for the screen of the
cockpit device with the given handle.

If the device is bound to the current aircraft, this is a shortcut to setting
the brightness rheostat value using
the`sim/cockpit2/switches/instrument_brightness_ratio[]`dataref; this sets the
slot in the`instrument_brightness_ratio`array to which the device is bound.

If the device is not currently bound, the device keeps track of its own screen
brightness rheostat, allowing you to control the brightness even though it isn’t
connected to the`instrument_brightness_ratio`dataref.

### [XPLMSetAvionicsGeometry](/sdk/XPLMSetAvionicsGeometry/)

```cpp
XPLM_API void       XPLMSetAvionicsGeometry(
                         XPLMAvionicsID       inHandle,
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

Sets the size and position of a cockpit device’s popup window in the X-Plane
coordinate system.

### [XPLMSetAvionicsGeometryOS](/sdk/XPLMSetAvionicsGeometryOS/)

```cpp
XPLM_API void       XPLMSetAvionicsGeometryOS(
                         XPLMAvionicsID       inHandle,
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

Sets the size and position of a cockpit device’s popped-out window.

### [XPLMSetAvionicsPopupVisible](/sdk/XPLMSetAvionicsPopupVisible/)

```cpp
XPLM_API void       XPLMSetAvionicsPopupVisible(
                         XPLMAvionicsID       inHandle,
                         int                  inVisible);

```

Shows or hides the popup window for a cockpit device.

### [XPLMShareData](/sdk/XPLMShareData/)

```cpp
XPLM_API int        XPLMShareData(
                         const char *         inDataName,
                         XPLMDataTypeID       inDataType,
                         XPLMDataChanged_f    inNotificationFunc,
                         void *               inNotificationRefcon);

```

This routine connects a plug-in to shared data, creating the shared data if
necessary. inDataName is a standard path for the dataref, and inDataType
specifies the type. This function will create the data if it does not exist. If
the data already exists but the type does not match, an error is returned, so it
is important that plug-in authors collaborate to establish public standards for
shared data.

If a notificationFunc is passed in and is not NULL, that notification function
will be called whenever the data is modified. The notification refcon will be
passed to it. This allows your plug-in to know which shared data was changed if
multiple shared data are handled by one callback, or if the plug-in does not use
global variables.

A one is returned for successfully creating or finding the shared data; a zero
if the data already exists but is of the wrong type.

### [XPLMSimulateKeyPress](/sdk/XPLMSimulateKeyPress/)

```cpp
XPLM_API void       XPLMSimulateKeyPress(
                         int                  inKeyType,
                         int                  inKey);

```

This function simulates a key being pressed for X-Plane. The keystroke goes
directly to X-Plane; it is never sent to any plug-ins. However, since this is a
raw key stroke it may be mapped by the keys file or enter text into a field.

Deprecated: use[XPLMCommandOnce](/sdk/XPLMCommandOnce/)

### [XPLMSpeakString](/sdk/XPLMSpeakString/)

```cpp
XPLM_API void       XPLMSpeakString(
                         const char *         inString);

```

This function displays the string in a translucent overlay over the current
display and also speaks the string if text-to-speech is enabled. The string is
spoken asynchronously, this function returns immediately. This function may not
speak or print depending on user preferences.

### [XPLMUnregisterCommandHandler](/sdk/XPLMUnregisterCommandHandler/)

```cpp
XPLM_API void       XPLMUnregisterCommandHandler(
                         XPLMCommandRef       inComand,
                         XPLMCommandCallback_f inHandler,
                         int                  inBefore,
                         void *               inRefcon);

```

[XPLMUnregisterCommandHandler](/sdk/XPLMUnregisterCommandHandler/)removes a
command callback registered
with[XPLMRegisterCommandHandler](/sdk/XPLMRegisterCommandHandler/).

### [XPLMUnregisterDataAccessor](/sdk/XPLMUnregisterDataAccessor/)

```cpp
XPLM_API void       XPLMUnregisterDataAccessor(
                         XPLMDataRef          inDataRef);

```

Use this routine to unregister any data accessors you may have registered. You
unregister a dataref by the[XPLMDataRef](/sdk/XPLMDataRef/)you get back from
registration. Once you unregister a dataref, your function pointer will not be
called anymore.

### [XPLMUnregisterKeySniffer](/sdk/XPLMUnregisterKeySniffer/)

```cpp
XPLM_API int        XPLMUnregisterKeySniffer(
                         XPLMKeySniffer_f     inCallback,
                         int                  inBeforeWindows,
                         void *               inRefcon);

```

This routine unregisters a key sniffer. You must unregister a key sniffer for
every time you register one with the exact same signature. Returns 1 if
successful.

### [XPLMUnshareData](/sdk/XPLMUnshareData/)

```cpp
XPLM_API int        XPLMUnshareData(
                         const char *         inDataName,
                         XPLMDataTypeID       inDataType,
                         XPLMDataChanged_f    inNotificationFunc,
                         void *               inNotificationRefcon);

```

This routine removes your notification function for shared data. Call it when
done with the data to stop receiving change notifications. Arguments must
match[XPLMShareData](/sdk/XPLMShareData/). The actual memory will not
necessarily be freed, since other plug-ins could be using it.

### [XPLMWorldToLocal](/sdk/XPLMWorldToLocal/)

```cpp
XPLM_API void       XPLMWorldToLocal(
                         double               inLatitude,
                         double               inLongitude,
                         double               inAltitude,
                         double *             outX,
                         double *             outY,
                         double *             outZ);

```

This routine translates coordinates from latitude, longitude, and altitude to
local scene coordinates. Latitude and longitude are in decimal degrees, and
altitude is in meters MSL (mean sea level). The XYZ coordinates are in meters in
the local OpenGL coordinate system.

### [XPLM_KEY_0](/sdk/XPLM_KEY_0/)

```cpp
#define XPLM_KEY_0           48
```

### [XPLM_KEY_1](/sdk/XPLM_KEY_1/)

```cpp
#define XPLM_KEY_1           49
```

### [XPLM_KEY_2](/sdk/XPLM_KEY_2/)

```cpp
#define XPLM_KEY_2           50
```

### [XPLM_KEY_3](/sdk/XPLM_KEY_3/)

```cpp
#define XPLM_KEY_3           51
```

### [XPLM_KEY_4](/sdk/XPLM_KEY_4/)

```cpp
#define XPLM_KEY_4           52
```

### [XPLM_KEY_5](/sdk/XPLM_KEY_5/)

```cpp
#define XPLM_KEY_5           53
```

### [XPLM_KEY_6](/sdk/XPLM_KEY_6/)

```cpp
#define XPLM_KEY_6           54
```

### [XPLM_KEY_7](/sdk/XPLM_KEY_7/)

```cpp
#define XPLM_KEY_7           55
```

### [XPLM_KEY_8](/sdk/XPLM_KEY_8/)

```cpp
#define XPLM_KEY_8           56
```

### [XPLM_KEY_9](/sdk/XPLM_KEY_9/)

```cpp
#define XPLM_KEY_9           57
```

### [XPLM_KEY_DECIMAL](/sdk/XPLM_KEY_DECIMAL/)

```cpp
#define XPLM_KEY_DECIMAL     46
```

### [XPLM_KEY_DELETE](/sdk/XPLM_KEY_DELETE/)

```cpp
#define XPLM_KEY_DELETE      8
```

### [XPLM_KEY_DOWN](/sdk/XPLM_KEY_DOWN/)

```cpp
#define XPLM_KEY_DOWN        31
```

### [XPLM_KEY_ESCAPE](/sdk/XPLM_KEY_ESCAPE/)

```cpp
#define XPLM_KEY_ESCAPE      27
```

### [XPLM_KEY_LEFT](/sdk/XPLM_KEY_LEFT/)

```cpp
#define XPLM_KEY_LEFT        28
```

### [XPLM_KEY_RETURN](/sdk/XPLM_KEY_RETURN/)

```cpp
#define XPLM_KEY_RETURN      13
```

### [XPLM_KEY_RIGHT](/sdk/XPLM_KEY_RIGHT/)

```cpp
#define XPLM_KEY_RIGHT       29
```

### [XPLM_KEY_TAB](/sdk/XPLM_KEY_TAB/)

```cpp
#define XPLM_KEY_TAB         9
```

### [XPLM_KEY_UP](/sdk/XPLM_KEY_UP/)

```cpp
#define XPLM_KEY_UP          30
```

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

### [XPLM_MSG_LIVERY_LOADED](/sdk/XPLM_MSG_LIVERY_LOADED/)

```cpp
#define XPLM_MSG_LIVERY_LOADED 108
```

This message is sent to your plugin right after a livery is loaded for an
airplane. You can use this to check the new livery (via datarefs) and react
accordingly. The parameter contains the index number of the aircraft whose
livery is changing.

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

### [XPLM_VK_0](/sdk/XPLM_VK_0/)

```cpp
#define XPLM_VK_0            0x30
```

[XPLM_VK_0](/sdk/XPLM_VK_0/)thru[XPLM_VK_9](/sdk/XPLM_VK_9/)are the same as
ASCII ‘0’ thru ‘9’ (0x30 - 0x39)

### [XPLM_VK_1](/sdk/XPLM_VK_1/)

```cpp
#define XPLM_VK_1            0x31
```

### [XPLM_VK_2](/sdk/XPLM_VK_2/)

```cpp
#define XPLM_VK_2            0x32
```

### [XPLM_VK_3](/sdk/XPLM_VK_3/)

```cpp
#define XPLM_VK_3            0x33
```

### [XPLM_VK_4](/sdk/XPLM_VK_4/)

```cpp
#define XPLM_VK_4            0x34
```

### [XPLM_VK_5](/sdk/XPLM_VK_5/)

```cpp
#define XPLM_VK_5            0x35
```

### [XPLM_VK_6](/sdk/XPLM_VK_6/)

```cpp
#define XPLM_VK_6            0x36
```

### [XPLM_VK_7](/sdk/XPLM_VK_7/)

```cpp
#define XPLM_VK_7            0x37
```

### [XPLM_VK_8](/sdk/XPLM_VK_8/)

```cpp
#define XPLM_VK_8            0x38
```

### [XPLM_VK_9](/sdk/XPLM_VK_9/)

```cpp
#define XPLM_VK_9            0x39
```

### [XPLM_VK_A](/sdk/XPLM_VK_A/)

```cpp
#define XPLM_VK_A            0x41
```

[XPLM_VK_A](/sdk/XPLM_VK_A/)thru[XPLM_VK_Z](/sdk/XPLM_VK_Z/)are the same as
ASCII ‘A’ thru ‘Z’ (0x41 - 0x5A)

### [XPLM_VK_ADD](/sdk/XPLM_VK_ADD/)

```cpp
#define XPLM_VK_ADD          0x6B
```

### [XPLM_VK_B](/sdk/XPLM_VK_B/)

```cpp
#define XPLM_VK_B            0x42
```

### [XPLM_VK_BACK](/sdk/XPLM_VK_BACK/)

```cpp
#define XPLM_VK_BACK         0x08
```

### [XPLM_VK_BACKQUOTE](/sdk/XPLM_VK_BACKQUOTE/)

```cpp
#define XPLM_VK_BACKQUOTE    0xBA
```

### [XPLM_VK_BACKSLASH](/sdk/XPLM_VK_BACKSLASH/)

```cpp
#define XPLM_VK_BACKSLASH    0xB6
```

### [XPLM_VK_C](/sdk/XPLM_VK_C/)

```cpp
#define XPLM_VK_C            0x43
```

### [XPLM_VK_CLEAR](/sdk/XPLM_VK_CLEAR/)

```cpp
#define XPLM_VK_CLEAR        0x0C
```

### [XPLM_VK_COMMA](/sdk/XPLM_VK_COMMA/)

```cpp
#define XPLM_VK_COMMA        0xB7
```

### [XPLM_VK_D](/sdk/XPLM_VK_D/)

```cpp
#define XPLM_VK_D            0x44
```

### [XPLM_VK_DECIMAL](/sdk/XPLM_VK_DECIMAL/)

```cpp
#define XPLM_VK_DECIMAL      0x6E
```

### [XPLM_VK_DELETE](/sdk/XPLM_VK_DELETE/)

```cpp
#define XPLM_VK_DELETE       0x2E
```

### [XPLM_VK_DIVIDE](/sdk/XPLM_VK_DIVIDE/)

```cpp
#define XPLM_VK_DIVIDE       0x6F
```

### [XPLM_VK_DOWN](/sdk/XPLM_VK_DOWN/)

```cpp
#define XPLM_VK_DOWN         0x28
```

### [XPLM_VK_E](/sdk/XPLM_VK_E/)

```cpp
#define XPLM_VK_E            0x45
```

### [XPLM_VK_END](/sdk/XPLM_VK_END/)

```cpp
#define XPLM_VK_END          0x23
```

### [XPLM_VK_ENTER](/sdk/XPLM_VK_ENTER/)

```cpp
#define XPLM_VK_ENTER        0xBB
```

### [XPLM_VK_EQUAL](/sdk/XPLM_VK_EQUAL/)

```cpp
#define XPLM_VK_EQUAL        0xB0
```

The following definitions are extended and are not based on the Microsoft key
set.

### [XPLM_VK_ESCAPE](/sdk/XPLM_VK_ESCAPE/)

```cpp
#define XPLM_VK_ESCAPE       0x1B
```

### [XPLM_VK_EXECUTE](/sdk/XPLM_VK_EXECUTE/)

```cpp
#define XPLM_VK_EXECUTE      0x2B
```

### [XPLM_VK_F](/sdk/XPLM_VK_F/)

```cpp
#define XPLM_VK_F            0x46
```

### [XPLM_VK_F1](/sdk/XPLM_VK_F1/)

```cpp
#define XPLM_VK_F1           0x70
```

### [XPLM_VK_F10](/sdk/XPLM_VK_F10/)

```cpp
#define XPLM_VK_F10          0x79
```

### [XPLM_VK_F11](/sdk/XPLM_VK_F11/)

```cpp
#define XPLM_VK_F11          0x7A
```

### [XPLM_VK_F12](/sdk/XPLM_VK_F12/)

```cpp
#define XPLM_VK_F12          0x7B
```

### [XPLM_VK_F13](/sdk/XPLM_VK_F13/)

```cpp
#define XPLM_VK_F13          0x7C
```

### [XPLM_VK_F14](/sdk/XPLM_VK_F14/)

```cpp
#define XPLM_VK_F14          0x7D
```

### [XPLM_VK_F15](/sdk/XPLM_VK_F15/)

```cpp
#define XPLM_VK_F15          0x7E
```

### [XPLM_VK_F16](/sdk/XPLM_VK_F16/)

```cpp
#define XPLM_VK_F16          0x7F
```

### [XPLM_VK_F17](/sdk/XPLM_VK_F17/)

```cpp
#define XPLM_VK_F17          0x80
```

### [XPLM_VK_F18](/sdk/XPLM_VK_F18/)

```cpp
#define XPLM_VK_F18          0x81
```

### [XPLM_VK_F19](/sdk/XPLM_VK_F19/)

```cpp
#define XPLM_VK_F19          0x82
```

### [XPLM_VK_F2](/sdk/XPLM_VK_F2/)

```cpp
#define XPLM_VK_F2           0x71
```

### [XPLM_VK_F20](/sdk/XPLM_VK_F20/)

```cpp
#define XPLM_VK_F20          0x83
```

### [XPLM_VK_F21](/sdk/XPLM_VK_F21/)

```cpp
#define XPLM_VK_F21          0x84
```

### [XPLM_VK_F22](/sdk/XPLM_VK_F22/)

```cpp
#define XPLM_VK_F22          0x85
```

### [XPLM_VK_F23](/sdk/XPLM_VK_F23/)

```cpp
#define XPLM_VK_F23          0x86
```

### [XPLM_VK_F24](/sdk/XPLM_VK_F24/)

```cpp
#define XPLM_VK_F24          0x87
```

### [XPLM_VK_F3](/sdk/XPLM_VK_F3/)

```cpp
#define XPLM_VK_F3           0x72
```

### [XPLM_VK_F4](/sdk/XPLM_VK_F4/)

```cpp
#define XPLM_VK_F4           0x73
```

### [XPLM_VK_F5](/sdk/XPLM_VK_F5/)

```cpp
#define XPLM_VK_F5           0x74
```

### [XPLM_VK_F6](/sdk/XPLM_VK_F6/)

```cpp
#define XPLM_VK_F6           0x75
```

### [XPLM_VK_F7](/sdk/XPLM_VK_F7/)

```cpp
#define XPLM_VK_F7           0x76
```

### [XPLM_VK_F8](/sdk/XPLM_VK_F8/)

```cpp
#define XPLM_VK_F8           0x77
```

### [XPLM_VK_F9](/sdk/XPLM_VK_F9/)

```cpp
#define XPLM_VK_F9           0x78
```

### [XPLM_VK_G](/sdk/XPLM_VK_G/)

```cpp
#define XPLM_VK_G            0x47
```

### [XPLM_VK_H](/sdk/XPLM_VK_H/)

```cpp
#define XPLM_VK_H            0x48
```

### [XPLM_VK_HELP](/sdk/XPLM_VK_HELP/)

```cpp
#define XPLM_VK_HELP         0x2F
```

### [XPLM_VK_HOME](/sdk/XPLM_VK_HOME/)

```cpp
#define XPLM_VK_HOME         0x24
```

### [XPLM_VK_I](/sdk/XPLM_VK_I/)

```cpp
#define XPLM_VK_I            0x49
```

### [XPLM_VK_INSERT](/sdk/XPLM_VK_INSERT/)

```cpp
#define XPLM_VK_INSERT       0x2D
```

### [XPLM_VK_J](/sdk/XPLM_VK_J/)

```cpp
#define XPLM_VK_J            0x4A
```

### [XPLM_VK_K](/sdk/XPLM_VK_K/)

```cpp
#define XPLM_VK_K            0x4B
```

### [XPLM_VK_L](/sdk/XPLM_VK_L/)

```cpp
#define XPLM_VK_L            0x4C
```

### [XPLM_VK_LBRACE](/sdk/XPLM_VK_LBRACE/)

```cpp
#define XPLM_VK_LBRACE       0xB3
```

### [XPLM_VK_LEFT](/sdk/XPLM_VK_LEFT/)

```cpp
#define XPLM_VK_LEFT         0x25
```

### [XPLM_VK_M](/sdk/XPLM_VK_M/)

```cpp
#define XPLM_VK_M            0x4D
```

### [XPLM_VK_MINUS](/sdk/XPLM_VK_MINUS/)

```cpp
#define XPLM_VK_MINUS        0xB1
```

### [XPLM_VK_MULTIPLY](/sdk/XPLM_VK_MULTIPLY/)

```cpp
#define XPLM_VK_MULTIPLY     0x6A
```

### [XPLM_VK_N](/sdk/XPLM_VK_N/)

```cpp
#define XPLM_VK_N            0x4E
```

### [XPLM_VK_NEXT](/sdk/XPLM_VK_NEXT/)

```cpp
#define XPLM_VK_NEXT         0x22
```

### [XPLM_VK_NUMPAD0](/sdk/XPLM_VK_NUMPAD0/)

```cpp
#define XPLM_VK_NUMPAD0      0x60
```

### [XPLM_VK_NUMPAD1](/sdk/XPLM_VK_NUMPAD1/)

```cpp
#define XPLM_VK_NUMPAD1      0x61
```

### [XPLM_VK_NUMPAD2](/sdk/XPLM_VK_NUMPAD2/)

```cpp
#define XPLM_VK_NUMPAD2      0x62
```

### [XPLM_VK_NUMPAD3](/sdk/XPLM_VK_NUMPAD3/)

```cpp
#define XPLM_VK_NUMPAD3      0x63
```

### [XPLM_VK_NUMPAD4](/sdk/XPLM_VK_NUMPAD4/)

```cpp
#define XPLM_VK_NUMPAD4      0x64
```

### [XPLM_VK_NUMPAD5](/sdk/XPLM_VK_NUMPAD5/)

```cpp
#define XPLM_VK_NUMPAD5      0x65
```

### [XPLM_VK_NUMPAD6](/sdk/XPLM_VK_NUMPAD6/)

```cpp
#define XPLM_VK_NUMPAD6      0x66
```

### [XPLM_VK_NUMPAD7](/sdk/XPLM_VK_NUMPAD7/)

```cpp
#define XPLM_VK_NUMPAD7      0x67
```

### [XPLM_VK_NUMPAD8](/sdk/XPLM_VK_NUMPAD8/)

```cpp
#define XPLM_VK_NUMPAD8      0x68
```

### [XPLM_VK_NUMPAD9](/sdk/XPLM_VK_NUMPAD9/)

```cpp
#define XPLM_VK_NUMPAD9      0x69
```

### [XPLM_VK_NUMPAD_ENT](/sdk/XPLM_VK_NUMPAD_ENT/)

```cpp
#define XPLM_VK_NUMPAD_ENT   0xBC
```

### [XPLM_VK_NUMPAD_EQ](/sdk/XPLM_VK_NUMPAD_EQ/)

```cpp
#define XPLM_VK_NUMPAD_EQ    0xBD
```

### [XPLM_VK_O](/sdk/XPLM_VK_O/)

```cpp
#define XPLM_VK_O            0x4F
```

### [XPLM_VK_P](/sdk/XPLM_VK_P/)

```cpp
#define XPLM_VK_P            0x50
```

### [XPLM_VK_PERIOD](/sdk/XPLM_VK_PERIOD/)

```cpp
#define XPLM_VK_PERIOD       0xB9
```

### [XPLM_VK_PRINT](/sdk/XPLM_VK_PRINT/)

```cpp
#define XPLM_VK_PRINT        0x2A
```

### [XPLM_VK_PRIOR](/sdk/XPLM_VK_PRIOR/)

```cpp
#define XPLM_VK_PRIOR        0x21
```

### [XPLM_VK_Q](/sdk/XPLM_VK_Q/)

```cpp
#define XPLM_VK_Q            0x51
```

### [XPLM_VK_QUOTE](/sdk/XPLM_VK_QUOTE/)

```cpp
#define XPLM_VK_QUOTE        0xB4
```

### [XPLM_VK_R](/sdk/XPLM_VK_R/)

```cpp
#define XPLM_VK_R            0x52
```

### [XPLM_VK_RBRACE](/sdk/XPLM_VK_RBRACE/)

```cpp
#define XPLM_VK_RBRACE       0xB2
```

### [XPLM_VK_RETURN](/sdk/XPLM_VK_RETURN/)

```cpp
#define XPLM_VK_RETURN       0x0D
```

### [XPLM_VK_RIGHT](/sdk/XPLM_VK_RIGHT/)

```cpp
#define XPLM_VK_RIGHT        0x27
```

### [XPLM_VK_S](/sdk/XPLM_VK_S/)

```cpp
#define XPLM_VK_S            0x53
```

### [XPLM_VK_SELECT](/sdk/XPLM_VK_SELECT/)

```cpp
#define XPLM_VK_SELECT       0x29
```

### [XPLM_VK_SEMICOLON](/sdk/XPLM_VK_SEMICOLON/)

```cpp
#define XPLM_VK_SEMICOLON    0xB5
```

### [XPLM_VK_SEPARATOR](/sdk/XPLM_VK_SEPARATOR/)

```cpp
#define XPLM_VK_SEPARATOR    0x6C
```

### [XPLM_VK_SLASH](/sdk/XPLM_VK_SLASH/)

```cpp
#define XPLM_VK_SLASH        0xB8
```

### [XPLM_VK_SNAPSHOT](/sdk/XPLM_VK_SNAPSHOT/)

```cpp
#define XPLM_VK_SNAPSHOT     0x2C
```

### [XPLM_VK_SPACE](/sdk/XPLM_VK_SPACE/)

```cpp
#define XPLM_VK_SPACE        0x20
```

### [XPLM_VK_SUBTRACT](/sdk/XPLM_VK_SUBTRACT/)

```cpp
#define XPLM_VK_SUBTRACT     0x6D
```

### [XPLM_VK_T](/sdk/XPLM_VK_T/)

```cpp
#define XPLM_VK_T            0x54
```

### [XPLM_VK_TAB](/sdk/XPLM_VK_TAB/)

```cpp
#define XPLM_VK_TAB          0x09
```

### [XPLM_VK_U](/sdk/XPLM_VK_U/)

```cpp
#define XPLM_VK_U            0x55
```

### [XPLM_VK_UP](/sdk/XPLM_VK_UP/)

```cpp
#define XPLM_VK_UP           0x26
```

### [XPLM_VK_V](/sdk/XPLM_VK_V/)

```cpp
#define XPLM_VK_V            0x56
```

### [XPLM_VK_W](/sdk/XPLM_VK_W/)

```cpp
#define XPLM_VK_W            0x57
```

### [XPLM_VK_X](/sdk/XPLM_VK_X/)

```cpp
#define XPLM_VK_X            0x58
```

### [XPLM_VK_Y](/sdk/XPLM_VK_Y/)

```cpp
#define XPLM_VK_Y            0x59
```

### [XPLM_VK_Z](/sdk/XPLM_VK_Z/)

```cpp
#define XPLM_VK_Z            0x5A
```

### [XPTrackStyle](/sdk/XPTrackStyle/)

A track is a UI element that displays a value vertically or horizontally.
X-Plane has three kinds of tracks: scroll bars, sliders, and progress bars.
Tracks can be displayed either horizontally or vertically; tracks will choose
their own layout based on the larger dimension of their dimensions (e.g. they
know if they are tall or wide). Sliders may be lit or unlit (showing the user
manipulating them).

- ScrollBar: this is a standard scroll bar with arrows and a thumb to drag.
- Slider: this is a simple track with a ball in the middle that can be slid.
- Progress: this is a progress indicator showing how a long task is going.

| Name | Value | Description |
| --- | --- | --- |
| [xpTrack_ScrollBar](/sdk/xpTrack_ScrollBar/) | "0" | not over metal can be lit
can be rotated |
| [xpTrack_Slider](/sdk/xpTrack_Slider/) | "1" | over metal can be lit can be
rotated |
| [xpTrack_Progress](/sdk/xpTrack_Progress/) | "2" | over metal cannot be lit
cannot be rotated |

### [XPUFixedLayout](/sdk/XPUFixedLayout/)

```cpp
WIDGET_API int        XPUFixedLayout(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2);

```

This function causes the widget to maintain its children in fixed position
relative to itself as it is resized. Use this on the top level ‘window’ widget
for your window.

### [XPUSelectIfNeeded](/sdk/XPUSelectIfNeeded/)

```cpp
WIDGET_API int        XPUSelectIfNeeded(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2,
                         int                  inEatClick);

```

This causes the widget to bring its window to the foreground if it is not
already. inEatClick specifies whether clicks in the background should be
consumed by bringing the window to the foreground.

### [kXPLM_Version](/sdk/kXPLM_Version/)

```cpp
#define kXPLM_Version        (411)
```

The current XPLM revision is 4.1.1 (411).

| |
| --- | --- |
| [xpBuilding](/sdk/xpBuilding/) | "17" |

| |
| --- | --- |
| [xpCoolingTower](/sdk/xpCoolingTower/) | "15" |

| |  |
| --- | --- | --- |
| [xpElement_Building](/sdk/xpElement_Building/) | "40" | none any |

| |  |
| --- | --- | --- |
| [xpElement_CoolingTower](/sdk/xpElement_CoolingTower/) | "38" | none any |

| |  |
| --- | --- | --- |
| [xpElement_EditingGrid](/sdk/xpElement_EditingGrid/) | "47" | x, y metal |

| |  |
| --- | --- | --- |
| [xpElement_Fire](/sdk/xpElement_Fire/) | "35" | none any |

| |  |
| --- | --- | --- |
| [xpElement_LittleDownArrow](/sdk/xpElement_LittleDownArrow/) | "53" | none metal |

| |  |
| --- | --- | --- |
| [xpElement_LittleUpArrow](/sdk/xpElement_LittleUpArrow/) | "54" | none metal |

| |  |
| --- | --- | --- |
| [xpElement_MarkerLeft](/sdk/xpElement_MarkerLeft/) | "28" | none any |

| |  |
| --- | --- | --- |
| [xpElement_MarkerRight](/sdk/xpElement_MarkerRight/) | "36" | none any |

| |  |
| --- | --- | --- |
| [xpElement_NDB](/sdk/xpElement_NDB/) | "31" | none any |

| |  |
| --- | --- | --- |
| [xpElement_OilPlatform](/sdk/xpElement_OilPlatform/) | "24" | none any |

| |  |
| --- | --- | --- |
| [xpElement_OilPlatformSmall](/sdk/xpElement_OilPlatformSmall/) | "25" | none any |

| |  |
| --- | --- | --- |
| [xpElement_PowerLine](/sdk/xpElement_PowerLine/) | "41" | none any |

| |  |
| --- | --- | --- |
| [xpElement_RadioTower](/sdk/xpElement_RadioTower/) | "33" | none any |

| |  |
| --- | --- | --- |
| [xpElement_Ship](/sdk/xpElement_Ship/) | "26" | none any |

| |  |
| --- | --- | --- |
| [xpElement_SmokeStack](/sdk/xpElement_SmokeStack/) | "39" | none any |

| |  |
| --- | --- | --- |
| [xpElement_VOR](/sdk/xpElement_VOR/) | "32" | none any |

| |  |
| --- | --- | --- |
| [xpElement_VORWithCompassRose](/sdk/xpElement_VORWithCompassRose/) | "49" | none any |

| |  |
| --- | --- | --- |
| [xpElement_Zoomer](/sdk/xpElement_Zoomer/) | "51" | none metal |

| |
| --- | --- |
| [xpFire](/sdk/xpFire/) | "12" |

| |  |
| --- | --- | --- |
| [xpLittleDownArrow](/sdk/xpLittleDownArrow/) | "5" | A small down arrow. |

| |  |
| --- | --- | --- |
| [xpLittleUpArrow](/sdk/xpLittleUpArrow/) | "6" | A small up arrow. |

| |
| --- | --- |
| [xpMarkerLeft](/sdk/xpMarkerLeft/) | "6" |

| |
| --- | --- |
| [xpMarkerRight](/sdk/xpMarkerRight/) | "13" |

| |  |
| --- | --- | --- |
| [xpMode_Direct](/sdk/xpMode_Direct/) | "0" | The message will only be sent to the target widget. |

| |  |
| --- | --- | --- |
| [xpMode_Once](/sdk/xpMode_Once/) | "4" | The message is only sent to the very first handler even if it is not accepted. (This is really only useful for some internal widget library functions.) |

| |  |
| --- | --- | --- |
| [xpMode_Recursive](/sdk/xpMode_Recursive/) | "2" | The message is sent to the target widget and then all of its children recursively depth-first. |

| |  |
| --- | --- | --- |
| [xpMode_UpChain](/sdk/xpMode_UpChain/) | "1" | The message is sent to the target widget, then up the chain of parents until the message ishandled or a parentless widget is reached. |

| |  |
| --- | --- | --- |
| [xpMsg_AcceptChild](/sdk/xpMsg_AcceptChild/) | "13" | A child has been added to you. The child's ID is passed in parameter one.Dispatching: DirectParam 1: The Widget ID of the child being added. |

| |  |
| --- | --- | --- |
| [xpMsg_AcceptParent](/sdk/xpMsg_AcceptParent/) | "15" | You now have a new parent, or have no parent. The parent's ID is passed in, or 0 for no parent.Dispatching: DirectParam 1: The Widget ID of your parent |

| |  |
| --- | --- | --- |
| [xpMsg_Create](/sdk/xpMsg_Create/) | "1" | The create message is sent once per widget that is created with your widget function and oncefor any widget that has your widget function attached.Dispatching: DirectParam 1: 1 if you are being added as a subclass, 0 if the widget is first being created. |

| |  |
| --- | --- | --- |
| [xpMsg_CursorAdjust](/sdk/xpMsg_CursorAdjust/) | "21" | The cursor is over your widget. If you consume this message, change the[XPLMCursorStatus](/sdk/XPLMCursorStatus/)value to indicate the desired result, with the same rules as in[XPLMDisplay](/sdk/XPLMDisplay/).h.Return 1 to consume this message, 0 to pass it on.Dispatching: Up chainParam 1: A pointer to an[XPMouseState_t](/sdk/XPMouseState_t/)struct containing the mouse status.Param 2: A pointer to a[XPLMCursorStatus](/sdk/XPLMCursorStatus/)- set this to the cursor result you desire. |

| |  |
| --- | --- | --- |
| [xpMsg_DescriptorChanged](/sdk/xpMsg_DescriptorChanged/) | "18" | Your descriptor has changed.Dispatching: Direct |

| |  |
| --- | --- | --- |
| [xpMsg_Destroy](/sdk/xpMsg_Destroy/) | "2" | The destroy message is sent once for each message that is destroyed that has your widget function.Dispatching: Direct for allParam 1: 1 if being deleted by a recursive delete to the parent, 0 for explicit deletion. |

| |  |
| --- | --- | --- |
| [xpMsg_ExposedChanged](/sdk/xpMsg_ExposedChanged/) | "12" | Your exposed area has changed.Dispatching: Direct |

| |  |
| --- | --- | --- |
| [xpMsg_Hidden](/sdk/xpMsg_Hidden/) | "17" | You have been hidden. See limitations above.Dispatching: Up chainParam 1: The widget ID of the hidden widget. |

| |  |
| --- | --- | --- |
| [xpMsg_KeyLoseFocus](/sdk/xpMsg_KeyLoseFocus/) | "7" | Keyboard focus is being taken away from you. The first parameter will be 1 if you are losingfocus because another widget is taking it, or 0 if someone called the API to make you lose focusexplicitly.Dispatching: DirectParam 1: 1 if focus is being taken by another widget, 0 if code requested to remove focus. |

| |  |
| --- | --- | --- |
| [xpMsg_KeyPress](/sdk/xpMsg_KeyPress/) | "5" | The key press message is sent once per key that is pressed. The first parameter is the type of keycode (integer or char) and the second is the code itself. By handling this event, you consume thekey stroke.Handling this message 'consumes' the keystroke; not handling it passes it to your parent widget.Dispatching: Up ChainParam 1: A pointer to an[XPKeyState_t](/sdk/XPKeyState_t/)structure with the keystroke. |

| |  |
| --- | --- | --- |
| [xpMsg_KeyTakeFocus](/sdk/xpMsg_KeyTakeFocus/) | "6" | Keyboard focus is being given to you. By handling this message you accept keyboard focus. Thefirst parameter will be one if a child of yours gave up focus to you, 0 if someone set focus onyou explicitly.Handling this message accepts focus; not handling refuses focus.Dispatching: directParam 1: 1 if you are gaining focus because your child is giving it up, 0 if someone is explicitlygiving you focus. |

| |  |
| --- | --- | --- |
| [xpMsg_LoseChild](/sdk/xpMsg_LoseChild/) | "14" | A child has been removed from you. The child's ID is passed in parameter one.Dispatching: DirectParam 1: The Widget ID of the child being removed. |

| |  |
| --- | --- | --- |
| [xpMsg_None](/sdk/xpMsg_None/) | "0" | No message, should not be sent. |

| |  |
| --- | --- | --- |
| [xpMsg_Paint](/sdk/xpMsg_Paint/) | "3" | The paint message is sent to your widget to draw itself. The paint message is the bare-bonesmessage; in response you must draw yourself, draw your children, set up clipping and culling,check for visibility, etc. If you don't want to do all of this, ignore the paint message anda draw message (see below) will be sent to you.Dispatching: Direct |

| |  |
| --- | --- | --- |
| [xpMsg_PropertyChanged](/sdk/xpMsg_PropertyChanged/) | "19" | A property has changed. Param 1 contains the property ID.Dispatching: DirectParam 1: The Property ID being changed.Param 2: The new property value |

| |  |
| --- | --- | --- |
| [xpMsg_Reshape](/sdk/xpMsg_Reshape/) | "11" | Your geometry or a child's geometry is being changed.Dispatching: Up chainParam 1: The widget ID of the original reshaped target.Param 2: A pointer to a[XPWidgetGeometryChange_t](/sdk/XPWidgetGeometryChange_t/)struct describing the change. |

| |  |
| --- | --- | --- |
| [xpMsg_Shown](/sdk/xpMsg_Shown/) | "16" | You or a child has been shown. Note that this does not include you being shown because your parentwas shown, you were put in a new parent, your root was shown, etc.Dispatching: Up chainParam 1: The widget ID of the shown widget. |

| |  |
| --- | --- | --- |
| [xpMsg_UserStart](/sdk/xpMsg_UserStart/) | "10000" | NOTE: Message IDs 1000 - 9999 are allocated to the standard widget classes provided with the librarywith 1000 - 1099 for widget class 0, 1100 - 1199 for widget class 1, etc. Message IDs 10,000 andbeyond are for plugin use. |

| |
| --- | --- |
| [xpNDB](/sdk/xpNDB/) | "8" |

| |
| --- | --- |
| [xpOilPlatform](/sdk/xpOilPlatform/) | "21" |

| |
| --- | --- |
| [xpOilPlatformSmall](/sdk/xpOilPlatformSmall/) | "22" |

| |
| --- | --- |
| [xpPowerLine](/sdk/xpPowerLine/) | "18" |

| |  |
| --- | --- | --- |
| [xpProperty_ActiveEditSide](/sdk/xpProperty_ActiveEditSide/) | "1408" | This is the active side of the insert selection. (Internal) |

| |  |
| --- | --- | --- |
| [xpProperty_Clip](/sdk/xpProperty_Clip/) | "6" | If this property is 1, the widget package will use OpenGL to restrict drawing to the Widget's exposed rectangle. |

| |
| --- | --- |
| [xpProperty_DragXOff](/sdk/xpProperty_DragXOff/) | "2" |

| |
| --- | --- |
| [xpProperty_DragYOff](/sdk/xpProperty_DragYOff/) | "3" |

| |  |
| --- | --- | --- |
| [xpProperty_Dragging](/sdk/xpProperty_Dragging/) | "1" | These properties are used by the utilities to implement dragging. |

| |  |
| --- | --- | --- |
| [xpProperty_EditFieldSelDragStart](/sdk/xpProperty_EditFieldSelDragStart/) | "1402" | This is the character position a drag was started at if the user is dragging to select text, or -1 if a drag is not in progress. |

| |  |
| --- | --- | --- |
| [xpProperty_EditFieldSelEnd](/sdk/xpProperty_EditFieldSelEnd/) | "1401" | This is the character position of the end of the selection. |

| |  |
| --- | --- | --- |
| [xpProperty_EditFieldSelStart](/sdk/xpProperty_EditFieldSelStart/) | "1400" | This is the character position the selection starts at, zero based.If it is the same as the end insertion point, the insertion pointis not a selection. |

| |  |
| --- | --- | --- |
| [xpProperty_Font](/sdk/xpProperty_Font/) | "1407" | The font to draw the field's text with. (An[XPLMFontID](/sdk/XPLMFontID/).) |

| |  |
| --- | --- | --- |
| [xpProperty_Hilited](/sdk/xpProperty_Hilited/) | "4" | Is the widget highlighted? (For widgets that support this kind of thing.) |

| |  |
| --- | --- | --- |
| [xpProperty_MaxCharacters](/sdk/xpProperty_MaxCharacters/) | "1405" | The max number of characters you can enter, if limited. Zero means unlimited. |

| |  |
| --- | --- | --- |
| [xpProperty_PasswordMode](/sdk/xpProperty_PasswordMode/) | "1404" | Set this property to 1 to password protect the field. Characters will be drawn as *s even though the descriptor will contain plain-text. |

| |  |
| --- | --- | --- |
| [xpProperty_Refcon](/sdk/xpProperty_Refcon/) | "0" | A window's refcon is an opaque value used by client code to find other data based on it. |

| |  |
| --- | --- | --- |
| [xpProperty_ScrollPosition](/sdk/xpProperty_ScrollPosition/) | "1406" | The first visible character on the left. This effectively scrolls the text field. |

| |  |
| --- | --- | --- |
| [xpProperty_UserStart](/sdk/xpProperty_UserStart/) | "10000" | NOTE: Property IDs 1 - 999 are reserved for the widgets library.NOTE: Property IDs 1000 - 9999 are allocated to the standard widget classes provided with the library.Properties 1000 - 1099 are for widget class 0, 1100 - 1199 for widget class 1, etc. |

| |
| --- | --- |
| [xpRadioTower](/sdk/xpRadioTower/) | "10" |

| |
| --- | --- |
| [xpShip](/sdk/xpShip/) | "4" |

| |
| --- | --- |
| [xpSmokeStack](/sdk/xpSmokeStack/) | "16" |

| |  |
| --- | --- | --- |
| [xpTextTranslucent](/sdk/xpTextTranslucent/) | "4" | A translucent edit field, dark gray. |

| |  |
| --- | --- | --- |
| [xpTextTransparent](/sdk/xpTextTransparent/) | "3" | A transparent text field. The user can type and the text is drawn, but no background is drawn.You can draw your own background by adding a widget handler and prehandling the draw message. |

| |  |
| --- | --- | --- |
| [xpTrack_Slider](/sdk/xpTrack_Slider/) | "1" | over metal can be lit can be rotated |

| |
| --- | --- |
| [xpVOR](/sdk/xpVOR/) | "9" |

| |
| --- | --- |
| [xpVORWithCompassRose](/sdk/xpVORWithCompassRose/) | "19" |

| |  |
| --- | --- | --- |
| [xplmFont_Basic](/sdk/xplmFont_Basic/) | "0" | Mono-spaced font for user interface. Available in all versions of the SDK. |

| |  |
| --- | --- | --- |
| [xplmFont_FullRound](/sdk/xplmFont_FullRound/) | "15" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_Led](/sdk/xplmFont_Led/) | "3" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_LedWide](/sdk/xplmFont_LedWide/) | "4" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_Metal](/sdk/xplmFont_Metal /) | "2" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_PanelEFIS](/sdk/xplmFont_PanelEFIS/) | "6" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_PanelHUD](/sdk/xplmFont_PanelHUD/) | "5" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_Proportional](/sdk/xplmFont_Proportional/) | "18" | Proportional UI font. |

| |  |
| --- | --- | --- |
| [xplmFont_RadiosBC](/sdk/xplmFont_RadiosBC/) | "9" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_RadiosBCNarrow](/sdk/xplmFont_RadiosBCNarrow/) | "12" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_RadiosGA](/sdk/xplmFont_RadiosGA/) | "8" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_RadiosGANarrow](/sdk/xplmFont_RadiosGANarrow/) | "11" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_RadiosHM](/sdk/xplmFont_RadiosHM/) | "10" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_RadiosHMNarrow](/sdk/xplmFont_RadiosHMNarrow/) | "13" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_SmallRound](/sdk/xplmFont_SmallRound/) | "16" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmType_Data](/sdk/xplmType_Data/) | "32" | A variable block of data. |

| |  |
| --- | --- | --- |
| [xplmType_Double](/sdk/xplmType_Double/) | "4" | A single 8-byte double, native endian. |

| |  |
| --- | --- | --- |
| [xplmType_Float](/sdk/xplmType_Float/) | "2" | A single 4-byte float, native endian. |

| |  |
| --- | --- | --- |
| [xplmType_FloatArray](/sdk/xplmType_FloatArray/) | "8" | An array of 4-byte floats, native endian. |

| |  |
| --- | --- | --- |
| [xplmType_Int](/sdk/xplmType_Int/) | "1" | A single 4-byte integer, native endian. |

| |  |
| --- | --- | --- |
| [xplmType_IntArray](/sdk/xplmType_IntArray/) | "16" | An array of 4-byte integers, native endian. |

| |  |
| --- | --- | --- |
| [xplmType_Unknown](/sdk/xplmType_Unknown/) | "0" | Data of a type the current XPLM doesn't do. |

| |  |
| --- | --- | --- |
| [xplm_CommandBegin](/sdk/xplm_CommandBegin/) | "0" | The command is being started. |

| |  |
| --- | --- | --- |
| [xplm_CommandContinue](/sdk/xplm_CommandContinue/) | "1" | The command is continuing to execute. |

| |  |
| --- | --- | --- |
| [xplm_CommandEnd](/sdk/xplm_CommandEnd/) | "2" | The command has ended. |

| |  |
| --- | --- | --- |
| [xplm_ControlFlag](/sdk/xplm_ControlFlag /) | "4" | The control key is down |

| |  |
| --- | --- | --- |
| [xplm_CursorArrow](/sdk/xplm_CursorArrow/) | "2" | X-Plane shows the cursor as the default arrow. |

| |  |
| --- | --- | --- |
| [xplm_CursorCustom](/sdk/xplm_CursorCustom/) | "3" | X-Plane shows the cursor but lets you select an OS cursor. |

| |  |
| --- | --- | --- |
| [xplm_CursorDefault](/sdk/xplm_CursorDefault/) | "0" | X-Plane manages the cursor normally, plugin does not affect the cusrsor. |

| |  |
| --- | --- | --- |
| [xplm_CursorHidden](/sdk/xplm_CursorHidden/) | "1" | X-Plane hides the cursor. |

| |  |
| --- | --- | --- |
| [xplm_DataFile_ReplayMovie](/sdk/xplm_DataFile_ReplayMovie/) | "2" | A situation movie (.smo) file, which replays a past flight. |

| |  |
| --- | --- | --- |
| [xplm_DataFile_Situation](/sdk/xplm_DataFile_Situation/) | "1" | A situation (.sit) file, which starts off a flight in a given configuration. |

| |  |
| --- | --- | --- |
| [xplm_DownFlag](/sdk/xplm_DownFlag/) | "8" | The key is being pressed down |

| |
| --- | --- |
| [xplm_Fpl_CoPilot_Approach](/sdk/xplm_Fpl_CoPilot_Approach/) | "3" |

| |
| --- | --- |
| [xplm_Fpl_CoPilot_Primary](/sdk/xplm_Fpl_CoPilot_Primary/) | "1" |

| |
| --- | --- |
| [xplm_Fpl_CoPilot_Temporary](/sdk/xplm_Fpl_CoPilot_Temporary/) | "5" |

| |
| --- | --- |
| [xplm_Fpl_Pilot_Approach](/sdk/xplm_Fpl_Pilot_Approach/) | "2" |

| |
| --- | --- |
| [xplm_Fpl_Pilot_Primary](/sdk/xplm_Fpl_Pilot_Primary/) | "0" |

| |
| --- | --- |
| [xplm_Fpl_Pilot_Temporary](/sdk/xplm_Fpl_Pilot_Temporary/) | "4" |

| |
| --- | --- |
| [xplm_Host_Briefer](/sdk/xplm_Host_Briefer/) | "4" |

| |
| --- | --- |
| [xplm_Host_Control_Pad](/sdk/xplm_Host_Control_Pad/) | "9" |

| |
| --- | --- |
| [xplm_Host_PartMaker](/sdk/xplm_Host_PartMaker/) | "5" |

| |
| --- | --- |
| [xplm_Host_RADAR](/sdk/xplm_Host_RADAR/) | "11" |

| |
| --- | --- |
| [xplm_Host_Unknown](/sdk/xplm_Host_Unknown/) | "0" |

| |
| --- | --- |
| [xplm_Host_WorldMaker](/sdk/xplm_Host_WorldMaker/) | "3" |

| |
| --- | --- |
| [xplm_Host_XAuto](/sdk/xplm_Host_XAuto/) | "7" |

| |
| --- | --- |
| [xplm_Host_Xavion](/sdk/xplm_Host_Xavion/) | "8" |

| |
| --- | --- |
| [xplm_Host_YoungsMod](/sdk/xplm_Host_YoungsMod/) | "6" |

| |
| --- | --- |
| [xplm_Language_Chinese](/sdk/xplm_Language_Chinese/) | "10" |

| |
| --- | --- |
| [xplm_Language_French](/sdk/xplm_Language_French/) | "2" |

| |
| --- | --- |
| [xplm_Language_German](/sdk/xplm_Language_German/) | "3" |

| |
| --- | --- |
| [xplm_Language_Greek](/sdk/xplm_Language_Greek/) | "8" |

| |
| --- | --- |
| [xplm_Language_Italian](/sdk/xplm_Language_Italian/) | "4" |

| |
| --- | --- |
| [xplm_Language_Japanese](/sdk/xplm_Language_Japanese/) | "9" |

| |
| --- | --- |
| [xplm_Language_Korean](/sdk/xplm_Language_Korean/) | "6" |

| |
| --- | --- |
| [xplm_Language_Russian](/sdk/xplm_Language_Russian/) | "7" |

| |
| --- | --- |
| [xplm_Language_Spanish](/sdk/xplm_Language_Spanish/) | "5" |

| |
| --- | --- |
| [xplm_Language_Ukrainian](/sdk/xplm_Language_Ukrainian/) | "11" |

| |
| --- | --- |
| [xplm_Language_Unknown](/sdk/xplm_Language_Unknown/) | "0" |

| |  |
| --- | --- | --- |
| [xplm_Master](/sdk/xplm_Master/) | "10" | Master bus. Not normally to be used directly. |

| |  |
| --- | --- | --- |
| [xplm_MasterBank](/sdk/xplm_MasterBank/) | "0" | Master bank. Handles all aircraft and environmental audio. |

| |  |
| --- | --- | --- |
| [xplm_OptionAltFlag](/sdk/xplm_OptionAltFlag/) | "2" | The option or alt key is down |

| |  |
| --- | --- | --- |
| [xplm_Phase_FirstCockpit](/sdk/xplm_Phase_FirstCockpit/) | "35" | This is the first phase where you can draw in 2-d. |

| |  |
| --- | --- | --- |
| [xplm_Phase_FirstScene](/sdk/xplm_Phase_FirstScene/) | "0" | Deprecated as of XPLM302. This is the earliest point at which you can draw in 3-d. |

| |  |
| --- | --- | --- |
| [xplm_Phase_Gauges](/sdk/xplm_Phase_Gauges/) | "45" | The moving parts of the aircraft panel. |

| |  |
| --- | --- | --- |
| [xplm_Phase_LastCockpit](/sdk/xplm_Phase_LastCockpit/) | "55" | The last chance to draw in 2d. |

| |  |
| --- | --- | --- |
| [xplm_Phase_LastScene](/sdk/xplm_Phase_LastScene/) | "30" | Deprecated as of XPLM302. This is the last point at which you can draw in 3-d. |

| |  |
| --- | --- | --- |
| [xplm_Phase_Modern3D](/sdk/xplm_Phase_Modern3D/) | "31" | A chance to do modern 3D drawing. |

| |  |
| --- | --- | --- |
| [xplm_Phase_Panel](/sdk/xplm_Phase_Panel/) | "40" | The non-moving parts of the aircraft panel. |

| |  |
| --- | --- | --- |
| [xplm_Phase_Vectors](/sdk/xplm_Phase_Vectors/) | "15" | Deprecated as of XPLM302. Drawing roads, trails, trains, etc. |

| |  |
| --- | --- | --- |
| [xplm_RadioBank](/sdk/xplm_RadioBank/) | "1" | Radio bank. Handles COM1/COM2/GND/Pilot/Copilot. |

| |  |
| --- | --- | --- |
| [xplm_ShiftFlag](/sdk/xplm_ShiftFlag/) | "1" | The shift key is down |

| |  |
| --- | --- | --- |
| [xplm_Tex_GeneralInterface](/sdk/xplm_Tex_GeneralInterface/) | "0" | The bitmap that contains window outlines, button outlines, fonts, etc. |

| |  |
| --- | --- | --- |
| [xplm_UpFlag](/sdk/xplm_UpFlag/) | "16" | The key is being released |

| |  |
| --- | --- | --- |
| [xplm_device_CDU739_1](/sdk/xplm_device_CDU739_1/) | "4" | generic airliner CDU, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_CDU739_2](/sdk/xplm_device_CDU739_2/) | "5" | generic airliner CDU, copilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_CDU815_1](/sdk/xplm_device_CDU815_1/) | "9" | Primus CDU, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_CDU815_2](/sdk/xplm_device_CDU815_2/) | "10" | Primus CDU, copilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_G1000_MFD](/sdk/xplm_device_G1000_MFD/) | "7" | G1000 Multifunction Display. |

| |  |
| --- | --- | --- |
| [xplm_device_G1000_PFD_1](/sdk/xplm_device_G1000_PFD_1/) | "6" | G1000 Primary Flight Display, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_G1000_PFD_2](/sdk/xplm_device_G1000_PFD_2/) | "8" | G1000 Primary Flight Display, copilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_GNS430_1](/sdk/xplm_device_GNS430_1/) | "0" | GNS430, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_GNS430_2](/sdk/xplm_device_GNS430_2/) | "1" | GNS430, copilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_GNS530_1](/sdk/xplm_device_GNS530_1/) | "2" | GNS530, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_GNS530_2](/sdk/xplm_device_GNS530_2/) | "3" | GNS530, copilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_MCDU_1](/sdk/xplm_device_MCDU_1/) | "18" | Airbus MCDU, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_MCDU_2](/sdk/xplm_device_MCDU_2/) | "19" | Airbus MCDU, copilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_Primus_MFD_1](/sdk/xplm_device_Primus_MFD_1/) | "13" | Primus Multifunction Display, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_Primus_MFD_2](/sdk/xplm_device_Primus_MFD_2/) | "14" | Primus Multifunction Display, copilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_Primus_MFD_3](/sdk/xplm_device_Primus_MFD_3/) | "15" | Primus Multifunction Display, central. |

| |  |
| --- | --- | --- |
| [xplm_device_Primus_PFD_1](/sdk/xplm_device_Primus_PFD_1/) | "11" | Primus Primary Flight Display, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_Primus_PFD_2](/sdk/xplm_device_Primus_PFD_2/) | "12" | Primus Primary Flight Display, copilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_Primus_RMU_1](/sdk/xplm_device_Primus_RMU_1/) | "16" | Primus Radio Management Unit, pilot side. |

| |  |
| --- | --- | --- |
| [xplm_device_Primus_RMU_2](/sdk/xplm_device_Primus_RMU_2/) | "17" | Primus Radio Management Unit, copilot side. |

