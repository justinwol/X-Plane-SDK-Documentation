---
title: "Graphics APIs"
description: "X-Plane SDK Graphics APIs documentation"
category: "XPLM_Graphics"
date: "2025-06-24T17:34:11.201013"
---

# Graphics APIs

### [General Graphics Properties](/sdk/General Graphics Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_GeneralGraphicsType](/sdk/xpProperty_GeneralGraphicsType/) |
"1700" | This property controls the type of icon that is drawn. |

### [General Graphics Types Values](/sdk/General Graphics Types Values/)

These define the icon for the general graphics.

| Name | Value | Description |
| --- | --- | --- |
| [xpShip](/sdk/xpShip/) | "4" |
| [xpILSGlideScope](/sdk/xpILSGlideScope/) | "5" |
| [xpMarkerLeft](/sdk/xpMarkerLeft/) | "6" |
| [xp_Airport](/sdk/xp_Airport/) | "7" |
| [xpNDB](/sdk/xpNDB/) | "8" |
| [xpVOR](/sdk/xpVOR/) | "9" |
| [xpRadioTower](/sdk/xpRadioTower/) | "10" |
| [xpAircraftCarrier](/sdk/xpAircraftCarrier/) | "11" |
| [xpFire](/sdk/xpFire/) | "12" |
| [xpMarkerRight](/sdk/xpMarkerRight/) | "13" |
| [xpCustomObject](/sdk/xpCustomObject/) | "14" |
| [xpCoolingTower](/sdk/xpCoolingTower/) | "15" |
| [xpSmokeStack](/sdk/xpSmokeStack/) | "16" |
| [xpBuilding](/sdk/xpBuilding/) | "17" |
| [xpPowerLine](/sdk/xpPowerLine/) | "18" |
| [xpVORWithCompassRose](/sdk/xpVORWithCompassRose/) | "19" |
| [xpOilPlatform](/sdk/xpOilPlatform/) | "21" |
| [xpOilPlatformSmall](/sdk/xpOilPlatformSmall/) | "22" |
| [xpWayPoint](/sdk/xpWayPoint/) | "23" |

### [XPLMGetAllMonitorBoundsGlobal](/sdk/XPLMGetAllMonitorBoundsGlobal/)

```cpp
XPLM_API void       XPLMGetAllMonitorBoundsGlobal(
                         XPLMReceiveMonitorBoundsGlobal_f inMonitorBoundsCallback,
                         void *               inRefcon);

```

This routine immediately calls you back with the bounds (in boxels) of each
full-screen X-Plane window within the X-Plane global desktop space. Note that if
a monitor is*not*covered by an X-Plane window, you cannot get its bounds this
way. Likewise, monitors with only an X-Plane window (not in full-screen mode)
will not be included.

If X-Plane is running in full-screen and your monitors are of the same size and
configured contiguously in the OS, then the combined global bounds of all
full-screen monitors will match the total global desktop bounds, as returned
by[XPLMGetScreenBoundsGlobal](/sdk/XPLMGetScreenBoundsGlobal/)(). (Of course, if
X-Plane is running in windowed mode, this will not be the case. Likewise, if you
have differently sized monitors, the global desktop space will include wasted
space.)

Note that this function’s monitor indices match those provided
by[XPLMGetAllMonitorBoundsOS](/sdk/XPLMGetAllMonitorBoundsOS/)(), but the
coordinates are different (since the X-Plane global desktop may not match the
operating system’s global desktop, and one X-Plane boxel may be larger than one
pixel due to 150% or 200% scaling).

### [XPLMGetMouseLocationGlobal](/sdk/XPLMGetMouseLocationGlobal/)

```cpp
XPLM_API void       XPLMGetMouseLocationGlobal(
                         int *                outX,    /* Can be NULL */
                         int *                outY);    /* Can be NULL */

```

Returns the current mouse location in global desktop boxels.
Unlike[XPLMGetMouseLocation](/sdk/XPLMGetMouseLocation/)(), the bottom left of
the main X-Plane window is not guaranteed to be (0, 0)—instead, the origin is
the lower left of the entire global desktop space. In addition, this routine
gives the real mouse location when the mouse goes to X-Plane windows other than
the primary display. Thus, it can be used with both pop-out windows and
secondary monitors.

This is the mouse location function to use with modern windows (i.e., those
created by[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)()).

Pass NULL to not receive info about either parameter.

### [XPLMReceiveMonitorBoundsGlobal_f](/sdk/XPLMReceiveMonitorBoundsGlobal_f/)

```cpp
typedef void (* XPLMReceiveMonitorBoundsGlobal_f)(
                         int                  inMonitorIndex,
                         int                  inLeftBx,
                         int                  inTopBx,
                         int                  inRightBx,
                         int                  inBottomBx,
                         void *               inRefcon);

```

This function is informed of the global bounds (in boxels) of a particular
monitor within the X-Plane global desktop space. Note that X-Plane must be
running in full screen on a monitor in order for that monitor to be passed to
you in this callback.

### [XPLMSetGraphicsState](/sdk/XPLMSetGraphicsState/)

```cpp
XPLM_API void       XPLMSetGraphicsState(
                         int                  inEnableFog,
                         int                  inNumberTexUnits,
                         int                  inEnableLighting,
                         int                  inEnableAlphaTesting,
                         int                  inEnableAlphaBlending,
                         int                  inEnableDepthTesting,
                         int                  inEnableDepthWriting);

```

[XPLMSetGraphicsState](/sdk/XPLMSetGraphicsState/)changes OpenGL’s fixed
function pipeline state. You are not responsible for restoring any state that is
accessed via[XPLMSetGraphicsState](/sdk/XPLMSetGraphicsState/), but you are
responsible for not accessing this state directly.

- inEnableFog - enables or disables fog, equivalent to: glEnable(GL_FOG);
- inNumberTexUnits - enables or disables a number of multitexturing units. If the number is 0, 2d texturing is disabled entirely, as in glDisable(GL_TEXTURE_2D); Otherwise, 2d texturing is enabled, and a number of multitexturing units are enabled sequentially, starting with unit 0, e.g. glActiveTextureARB(GL_TEXTURE0_ARB); glEnable (GL_TEXTURE_2D);
- inEnableLighting - enables or disables OpenGL lighting, e.g. glEnable(GL_LIGHTING); glEnable(GL_LIGHT0);
- inEnableAlphaTesting - enables or disables the alpha test per pixel, e.g. glEnable(GL_ALPHA_TEST);
- inEnableAlphaBlending - enables or disables alpha blending per pixel, e.g. glEnable(GL_BLEND);
- inEnableDepthTesting - enables per pixel depth testing, as in glEnable(GL_DEPTH_TEST);
- inEnableDepthWriting - enables writing back of depth information to the depth buffer, as in glDepthMask(GL_TRUE);

The purpose of this function is to change OpenGL state while keeping X-Plane
aware of the state changes; this keeps X-Plane from getting surprised by OGL
state changes, and prevents X-Plane and plug-ins from having to set all state
before all draws;[XPLMSetGraphicsState](/sdk/XPLMSetGraphicsState/)internally
skips calls to change state that is already properly enabled.

X-Plane does not have a ‘default’ OGL state for plug-ins with respect to the
above state vector; plug-ins should totally set OGL state using this API before
drawing. Use[XPLMSetGraphicsState](/sdk/XPLMSetGraphicsState/)instead of any of
the above OpenGL calls.

WARNING: Any routine that performs drawing
(e.g.[XPLMDrawString](/sdk/XPLMDrawString/)or widget code) may change X-Plane’s
state. Always set state before drawing after unknown code has executed.

*Deprecation Warnings*: X-Plane’s lighting and fog environment is significantly
more complex than the fixed function pipeline can express; do not assume that
lighting and fog state is a good approximation for 3-d drawing. Prefer to use
XPLMInstancing to draw objects. All calls
to[XPLMSetGraphicsState](/sdk/XPLMSetGraphicsState/)should have no fog or
lighting.

# [XPUIGraphics](/sdk/XPUIGraphics/)API

## UI GRAPHICS

### [XPWindowStyle](/sdk/XPWindowStyle/)

There are a few built-in window styles in X-Plane that you can use.

Note that X-Plane 6 does not offer real shadow-compositing; you must make sure
to put a window on top of another window of the right style to make the shadows
work, etc. This applies to elements with insets and shadows. The rules are:

Sub windows must go on top of main windows, and screens and list views on top of
subwindows. Only help and main windows can be over the main screen.

With X-Plane 7 any window or element may be placed over any other element.

Some windows are scaled by stretching, some by repeating. The drawing routines
know which scaling method to use. The list view cannot be rescaled in X-Plane 6
because it has both a repeating pattern and a gradient in one element. All other
elements can be rescaled.

| Name | Value | Description |
| --- | --- | --- |
| [xpWindow_Help](/sdk/xpWindow_Help/) | "0" | An LCD screen that shows help. |
| [xpWindow_MainWindow](/sdk/xpWindow_MainWindow/) | "1" | A dialog box window.
|
| [xpWindow_SubWindow](/sdk/xpWindow_SubWindow/) | "2" | A panel or frame within
a dialog box window. |
| [xpWindow_Screen](/sdk/xpWindow_Screen/) | "4" | An LCD screen within a panel
to hold text displays. |
| [xpWindow_ListView](/sdk/xpWindow_ListView/) | "5" | A list view within a
panel for scrolling file names, etc. |

### [XPDrawWindow](/sdk/XPDrawWindow/)

```cpp
WIDGET_API void       XPDrawWindow(
                         int                  inX1,
                         int                  inY1,
                         int                  inX2,
                         int                  inY2,
                         XPWindowStyle        inStyle);

```

This routine draws a window of the given dimensions at the given offset on the
virtual screen in a given style. The window is automatically scaled as
appropriate using a bitmap scaling technique (scaling or repeating) as
appropriate to the style.

### [XPGetWindowDefaultDimensions](/sdk/XPGetWindowDefaultDimensions/)

```cpp
WIDGET_API void       XPGetWindowDefaultDimensions(
                         XPWindowStyle        inStyle,
                         int *                outWidth,    /* Can be NULL */
                         int *                outHeight);    /* Can be NULL */

```

This routine returns the default dimensions for a window. Output is either a
minimum or fixed value depending on whether the window is scalable.

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

### [XPDrawElement](/sdk/XPDrawElement/)

```cpp
WIDGET_API void       XPDrawElement(
                         int                  inX1,
                         int                  inY1,
                         int                  inX2,
                         int                  inY2,
                         XPElementStyle       inStyle,
                         int                  inLit);

```

[XPDrawElement](/sdk/XPDrawElement/)draws a given element at an offset on the
virtual screen in set dimensions. Even if the element is not scalable, it will
be scaled if the width and height do not match the preferred dimensions; it’ll
just look ugly. Pass inLit to see the lit version of the element; if the element
cannot be lit this is ignored.

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

### [XPDrawTrack](/sdk/XPDrawTrack/)

```cpp
WIDGET_API void       XPDrawTrack(
                         int                  inX1,
                         int                  inY1,
                         int                  inX2,
                         int                  inY2,
                         int                  inMin,
                         int                  inMax,
                         int                  inValue,
                         XPTrackStyle         inTrackStyle,
                         int                  inLit);

```

This routine draws a track. You pass in the track dimensions and size; the track
picks the optimal orientation for these dimensions. Pass in the track’s minimum
current and maximum values; the indicator will be positioned appropriately. You
can also specify whether the track is lit or not.

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

| |  |
| --- | --- | --- |
| [xpElement_ILSGlideScope](/sdk/xpElement_ILSGlideScope/) | "27" | none any |

| |
| --- | --- |
| [xpILSGlideScope](/sdk/xpILSGlideScope/) | "5" |

| |  |
| --- | --- | --- |
| [xpProperty_GeneralGraphicsType](/sdk/xpProperty_GeneralGraphicsType/) | "1700" | This property controls the type of icon that is drawn. |

### [xpWidgetClass_GeneralGraphics](/sdk/xpWidgetClass_GeneralGraphics/)

```cpp
#define xpWidgetClass_GeneralGraphics 7
```

| |
| --- | --- |
| [xplm_Language_English](/sdk/xplm_Language_English/) | "1" |

| |
| --- | --- |
| [xplm_Nav_GlideSlope](/sdk/xplm_Nav_GlideSlope/) | "32" |

