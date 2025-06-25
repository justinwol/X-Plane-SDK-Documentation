---
title: "Utilities APIs"
description: "X-Plane SDK Utilities APIs documentation"
category: "XPLM_Utilities"
date: "2025-06-25T15:45:56.663423"
---

# Utilities APIs

### [XPLMAvionicsKeyboard_f](/sdk/XPLMAvionicsKeyboard_f/)

```cpp
typedef int (* XPLMAvionicsKeyboard_f)(
                         char                 inKey,
                         XPLMKeyFlags         inFlags,
                         char                 inVirtualKey,
                         void *               inRefCon,
                         int                  losingFocus);

```

Key callback called when your device is popped up and you’ve requested to
capture the keyboard. Return 1 to consume the event, or 0 to let X-Plane process
it (for stock avionics devices).

### [XPLMAvionicsMouseWheel_f](/sdk/XPLMAvionicsMouseWheel_f/)

```cpp
typedef int (* XPLMAvionicsMouseWheel_f)(
                         int                  x,
                         int                  y,
                         int                  wheel,
                         int                  clicks,
                         void *               inRefcon);

```

Mouse wheel callback for scroll actions into your screen or (2D-popup) bezel,
useful if your bezel has knobs that can be turned using the mouse wheel, or if
you want to simulate pinch-to-zoom on a touchscreen. Return 1 to consume the
event, or 0 to let X-Plane process it (for stock avionics devices). The number
of “clicks” indicates how far the wheel was turned since the last callback. The
wheel is 0 for the vertical axis or 1 for the horizontal axis (for OS/mouse
combinations that support this).

### [XPLMAvionicsMouse_f](/sdk/XPLMAvionicsMouse_f/)

```cpp
typedef int (* XPLMAvionicsMouse_f)(
                         int                  x,
                         int                  y,
                         XPLMMouseStatus      inMouse,
                         void *               inRefcon);

```

Mouse click callback for clicks into your screen or (2D-popup) bezel, useful if
the device you are making simulates a touch-screen the user can click in the 3d
cockpit, or if your pop-up’s bezel has buttons that the user can click. Return 1
to consume the event, or 0 to let X-Plane process it (for stock avionics
devices).

### [XPLMCountHotKeys](/sdk/XPLMCountHotKeys/)

```cpp
XPLM_API int        XPLMCountHotKeys(void);

```

Returns the number of current hot keys.

### [XPLMGetHotKeyInfo](/sdk/XPLMGetHotKeyInfo/)

```cpp
XPLM_API void       XPLMGetHotKeyInfo(
                         XPLMHotKeyID         inHotKey,
                         char *               outVirtualKey,    /* Can be NULL */
                         XPLMKeyFlags *       outFlags,    /* Can be NULL */
                         char *               outDescription,    /* Can be NULL */
                         XPLMPluginID *       outPlugin);    /* Can be NULL */

```

Returns information about the hot key. Return NULL for any parameter you don’t
want info about. The description should be at least 512 chars long.

### [XPLMGetLanguage](/sdk/XPLMGetLanguage/)

```cpp
XPLM_API XPLMLanguageCode XPLMGetLanguage(void);

```

This routine returns the langauge the sim is running in.

### [XPLMGetMouseLocation](/sdk/XPLMGetMouseLocation/)

```cpp
XPLM_API void       XPLMGetMouseLocation(
                         int *                outX,    /* Can be NULL */
                         int *                outY);    /* Can be NULL */

```

Deprecated in XPLM300. Modern windows should
use[XPLMGetMouseLocationGlobal](/sdk/XPLMGetMouseLocationGlobal/)() instead.

This routine returns the current mouse location in pixels relative to the main
X-Plane window. The bottom left corner of the main window is (0, 0). Pass NULL
to not receive info about either parameter.

Because this function gives the mouse position relative to the main X-Plane
window (rather than in global bounds), this function should only be used by
legacy windows. Modern windows should instead get the mouse position in global
desktop coordinates
using[XPLMGetMouseLocationGlobal](/sdk/XPLMGetMouseLocationGlobal/)().

Note that
unlike[XPLMGetMouseLocationGlobal](/sdk/XPLMGetMouseLocationGlobal/)(), if the
mouse goes outside the user’s main monitor (for instance, to a pop out window or
a secondary monitor), this function will not reflect it.

### [XPLMGetMyID](/sdk/XPLMGetMyID/)

```cpp
XPLM_API XPLMPluginID XPLMGetMyID(void);

```

This routine returns the plugin ID of the calling plug-in. Call this to get your
own ID.

### [XPLMGetNthHotKey](/sdk/XPLMGetNthHotKey/)

```cpp
XPLM_API XPLMHotKeyID XPLMGetNthHotKey(
                         int                  inIndex);

```

Returns a hot key by index, for iteration on all hot keys.

### [XPLMGetPrefsPath](/sdk/XPLMGetPrefsPath/)

```cpp
XPLM_API void       XPLMGetPrefsPath(
                         char *               outPrefsPath);

```

This routine returns a full path to a file that is within X-Plane’s preferences
directory. (You should remove the file name back to the last directory separator
to get the preferences directory
using[XPLMExtractFileAndPath](/sdk/XPLMExtractFileAndPath/)).

The buffer you pass should be at least 512 characters long. The path is returned
using the current native or OS path conventions.

### [XPLMGetSystemPath](/sdk/XPLMGetSystemPath/)

```cpp
XPLM_API void       XPLMGetSystemPath(
                         char *               outSystemPath);

```

This function returns the full path to the X-System folder. Note that this is a
directory path, so it ends in a trailing : or / .

The buffer you pass should be at least 512 characters long. The path is returned
using the current native or OS path conventions.

### [XPLMGetVersions](/sdk/XPLMGetVersions/)

```cpp
XPLM_API void       XPLMGetVersions(
                         int *                outXPlaneVersion,
                         int *                outXPLMVersion,
                         XPLMHostApplicationID * outHostID);

```

This routine returns the revision of both X-Plane and the XPLM DLL. All versions
are at least three-digit decimal numbers (e.g. 606 for version 6.06 of X-Plane);
the current revision of the XPLM is 400 (4.00). This routine also returns the
host ID of the app running us.

The most common use of this routine is to special-case around X-Plane
version-specific behavior.

### [XPLMHandleMouseClick_f](/sdk/XPLMHandleMouseClick_f/)

```cpp
typedef int (* XPLMHandleMouseClick_f)(
                         XPLMWindowID         inWindowID,
                         int                  x,
                         int                  y,
                         XPLMMouseStatus      inMouse,
                         void *               inRefcon);

```

You receive this call for one of three events:

- when the user clicks the mouse button down
- (optionally) when the user drags the mouse after a down-click, but before the up-click
- when the user releases the down-clicked mouse button.

You receive the x and y of the click, your window, and a refcon. Return 1 to
consume the click, or 0 to pass it through.

WARNING: passing clicks through windows (as of this writing) causes mouse
tracking problems in X-Plane; do not use this feature!

The units for x and y values match the units used in your window. Thus, for
“modern” windows (those created
via[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)() and compiled against the
XPLM300 library), the units are boxels, while legacy windows will get pixels.
Legacy windows have their origin in the lower left of the main X-Plane window,
while modern windows have their origin in the lower left of the global desktop
space. In both cases, x increases as you move right, and y increases as you move
up.

### [XPLMHandleMouseWheel_f](/sdk/XPLMHandleMouseWheel_f/)

```cpp
typedef int (* XPLMHandleMouseWheel_f)(
                         XPLMWindowID         inWindowID,
                         int                  x,
                         int                  y,
                         int                  wheel,
                         int                  clicks,
                         void *               inRefcon);

```

The SDK calls your mouse wheel callback when one of the mouse wheels is scrolled
within your window. Return 1 to consume the mouse wheel movement or 0 to pass
them on to a lower window. (If your window appears opaque to the user, you
should consume mouse wheel scrolling even if it does nothing.) The number of
“clicks” indicates how far the wheel was turned since the last callback. The
wheel is 0 for the vertical axis or 1 for the horizontal axis (for OS/mouse
combinations that support this).

The units for x and y values match the units used in your window. Thus, for
“modern” windows (those created
via[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)() and compiled against the
XPLM300 library), the units are boxels, while legacy windows will get pixels.
Legacy windows have their origin in the lower left of the main X-Plane window,
while modern windows have their origin in the lower left of the global desktop
space. In both cases, x increases as you move right, and y increases as you move
up.

### [XPLMHasAvionicsKeyboardFocus](/sdk/XPLMHasAvionicsKeyboardFocus/)

```cpp
XPLM_API int        XPLMHasAvionicsKeyboardFocus(
                         XPLMAvionicsID       inHandle);

```

Returns true (1) if the popup window for a cockpit device has keyboard focus.

### [XPLMHasKeyboardFocus](/sdk/XPLMHasKeyboardFocus/)

```cpp
XPLM_API int        XPLMHasKeyboardFocus(
                         XPLMWindowID         inWindow);

```

Returns true (1) if the indicated window has keyboard focus. Pass a window ID of
0 to see if no plugin window has focus, and all keystrokes will go directly to
X-Plane.

### [XPLMHotKeyID](/sdk/XPLMHotKeyID/)

```cpp
typedef void * XPLMHotKeyID;
```

An opaque ID used to identify a hot key.

### [XPLMHotKey_f](/sdk/XPLMHotKey_f/)

```cpp
typedef void (* XPLMHotKey_f)(
                         void *               inRefcon);

```

Your hot key callback simply takes a pointer of your choosing.

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

### [XPLMRegisterHotKey](/sdk/XPLMRegisterHotKey/)

```cpp
XPLM_API XPLMHotKeyID XPLMRegisterHotKey(
                         char                 inVirtualKey,
                         XPLMKeyFlags         inFlags,
                         const char *         inDescription,
                         XPLMHotKey_f         inCallback,
                         void *               inRefcon);

```

This routine registers a hot key. You specify your preferred key stroke virtual
key/flag combination, a description of what your callback does (so other
plug-ins can describe the plug-in to the user for remapping) and a callback
function and opaque pointer to pass in). A new hot key ID is returned. During
execution, the actual key associated with your hot key may change, but you are
insulated from this.

### [XPLMSetHotKeyCombination](/sdk/XPLMSetHotKeyCombination/)

```cpp
XPLM_API void       XPLMSetHotKeyCombination(
                         XPLMHotKeyID         inHotKey,
                         char                 inVirtualKey,
                         XPLMKeyFlags         inFlags);

```

Remaps a hot key’s keystrokes. You may remap another plugin’s keystrokes.

### [XPLMTakeAvionicsKeyboardFocus](/sdk/XPLMTakeAvionicsKeyboardFocus/)

```cpp
XPLM_API void       XPLMTakeAvionicsKeyboardFocus(
                         XPLMAvionicsID       inHandle);

```

This routine gives keyboard focus to the popup window of a custom cockpit
device, if it is visible.

### [XPLMTakeKeyboardFocus](/sdk/XPLMTakeKeyboardFocus/)

```cpp
XPLM_API void       XPLMTakeKeyboardFocus(
                         XPLMWindowID         inWindow);

```

This routine gives a specific window keyboard focus. Keystrokes will be sent to
that window. Pass a window ID of 0 to remove keyboard focus from any
plugin-created windows and instead pass keyboard strokes directly to X-Plane.

### [XPLMUnregisterHotKey](/sdk/XPLMUnregisterHotKey/)

```cpp
XPLM_API void       XPLMUnregisterHotKey(
                         XPLMHotKeyID         inHotKey);

```

Unregisters a hot key. You can only unregister your own hot keys.

### [XPLoseKeyboardFocus](/sdk/XPLoseKeyboardFocus/)

```cpp
WIDGET_API void       XPLoseKeyboardFocus(
                         XPWidgetID           inWidget);

```

This causes the specified widget to lose focus; focus is passed to its parent,
or the next parent that will accept it. This routine does nothing if this widget
does not have focus.

### [XPMouseState_t](/sdk/XPMouseState_t/)

When the mouse is clicked or dragged, a pointer to this structure is passed to
your widget function.

```cpp
typedef struct {
     int                       x;
     int                       y;
     // Mouse button number, left = 0 (right button not yet supported.
     int                       button;
     // Scroll wheel delta (button in this case would be the wheel axis number).
     int                       delta;
} XPMouseState_t;
```

### [XPSetKeyboardFocus](/sdk/XPSetKeyboardFocus/)

```cpp
WIDGET_API XPWidgetID XPSetKeyboardFocus(
                         XPWidgetID           inWidget);

```

Controls which widget will receive keystrokes. Pass the widget ID of the widget
to get the keys. Note that if the widget does not care about keystrokes, they
will go to the parent widget, and if no widget cares about them, they go to
X-Plane.

If you set the keyboard focus to widget ID 0, X-Plane gets keyboard focus.

This routine returns the widget ID that ended up with keyboard focus, or 0 for
X-Plane.

Keyboard focus is not changed if the new widget will not accept it. For setting
to X-Plane, keyboard focus is always accepted.

### [XPUDefocusKeyboard](/sdk/XPUDefocusKeyboard/)

```cpp
WIDGET_API int        XPUDefocusKeyboard(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2,
                         int                  inEatClick);

```

This causes the widget to send keyboard focus back to X-Plane. This stops
editing of any text fields, etc.

| |  |
| --- | --- | --- |
| [xpMsg_MouseDown](/sdk/xpMsg_MouseDown/) | "8" | You receive one mousedown event per click with a mouse-state structure pointed to by parameter 1.By accepting this you eat the click, otherwise your parent gets it. You will not receive drag andmouse up messages if you do not accept the down message.Handling this message consumes the mouse click, not handling it passes it to the next widget.You can act 'transparent' as a window by never handling moues clicks to certain areas.Dispatching: Up chain NOTE: Technically this is direct dispatched, but the widgets library will shipit to each widget until one consumes the click, making it effectively "up chain".Param 1: A pointer to an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |

| |  |
| --- | --- | --- |
| [xpMsg_MouseDrag](/sdk/xpMsg_MouseDrag/) | "9" | You receive a series of mouse drag messages (typically one per frame in the sim) as the mouse ismoved once you have accepted a mouse down message. Parameter one points to a mouse-state structuredescribing the mouse location. You will continue to receive these until the mouse button isreleased.You may receive multiple mouse state messages with the same mouse position. You will receive mousedrag events even if the mouse is dragged out of your current or original bounds at the time of themouse down.Dispatching: DirectParam 1: A pointer to an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |

| |  |
| --- | --- | --- |
| [xpMsg_MouseUp](/sdk/xpMsg_MouseUp/) | "10" | The mouseup event is sent once when the mouse button is released after a drag or click. You onlyreceive this message if you accept the mouseDown message. Parameter one points to a mouse statestructure.Dispatching: DirectParam 1: A pointer to an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |

| |  |
| --- | --- | --- |
| [xpMsg_MouseWheel](/sdk/xpMsg_MouseWheel/) | "20" | The mouse wheel has moved.Return 1 to consume the mouse wheel move, or 0 to pass the message to a parent.Dispatching: Up chainParam 1: A pointer to an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |

| |
| --- | --- |
| [xplm_MouseDown](/sdk/xplm_MouseDown/) | "1" |

| |
| --- | --- |
| [xplm_MouseDrag](/sdk/xplm_MouseDrag/) | "2" |

| |
| --- | --- |
| [xplm_MouseUp](/sdk/xplm_MouseUp/) | "3" |

