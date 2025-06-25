---
title: "Display APIs"
description: "X-Plane SDK Display APIs documentation"
category: "XPLM_Display"
date: "2025-06-25T15:45:56.657425"
---

# Display APIs

### [Main Window Properties](/sdk/Main Window Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_MainWindowType](/sdk/xpProperty_MainWindowType/) | "1100" | This
property specifies the type of window. Set to one of the main window types
above. |
| [xpProperty_MainWindowHasCloseBoxes](/sdk/xpProperty_MainWindowHasCloseBoxes/)
| "1200" | This property specifies whether the main window has close boxes in
its corners. |

### [Main Window Type Values](/sdk/Main Window Type Values/)

These type values are used to control the appearance of a main window.

| Name | Value | Description |
| --- | --- | --- |
| [xpMainWindowStyle_MainWindow](/sdk/xpMainWindowStyle_MainWindow/) | "0" | The
standard main window; pin stripes on XP7, metal frame on XP 6. |
| [xpMainWindowStyle_Translucent](/sdk/xpMainWindowStyle_Translucent/) | "1" | A
translucent dark gray window. |

### [MainWindow Messages](/sdk/MainWindow Messages/)

| Name | Value | Description |
| --- | --- | --- |
| [xpMessage_CloseButtonPushed](/sdk/xpMessage_CloseButtonPushed/) | "1200" |
This message is sent when the close buttons for your window are pressed. |

### [SubWindow Properties](/sdk/SubWindow Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_SubWindowType](/sdk/xpProperty_SubWindowType/) | "1200" | This
property specifies the type of window. Set to one of the subwindow types above.
|

### [SubWindow Type Values](/sdk/SubWindow Type Values/)

These values control the appearance of the subwindow.

| Name | Value | Description |
| --- | --- | --- |
| [xpSubWindowStyle_SubWindow](/sdk/xpSubWindowStyle_SubWindow/) | "0" | A panel
that sits inside a main window. |
| [xpSubWindowStyle_Screen](/sdk/xpSubWindowStyle_Screen/) | "2" | A screen that
sits inside a panel for showing text information. |
| [xpSubWindowStyle_ListView](/sdk/xpSubWindowStyle_ListView/) | "3" | A list
view for scrolling lists. |

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

### [XPGetWidgetUnderlyingWindow](/sdk/XPGetWidgetUnderlyingWindow/)

```cpp
WIDGET_API XPLMWindowID XPGetWidgetUnderlyingWindow(
                         XPWidgetID           inWidget);

```

Returns the window (from the[XPLMDisplay](/sdk/XPLMDisplay/)API) that backs your
widget window. If you have opted in to modern windows, via a call
to[XPLMEnableFeature](/sdk/XPLMEnableFeature/)(“XPLM_USE_NATIVE_WIDGET_WINDOWS”,
1), you can use the returned window ID for display APIs
like[XPLMSetWindowPositioningMode](/sdk/XPLMSetWindowPositioningMode/)(),
allowing you to pop the widget window out into a real OS window, or move it into
VR.

### [XPGetWindowDefaultDimensions](/sdk/XPGetWindowDefaultDimensions/)

```cpp
WIDGET_API void       XPGetWindowDefaultDimensions(
                         XPWindowStyle        inStyle,
                         int *                outWidth,    /* Can be NULL */
                         int *                outHeight);    /* Can be NULL */

```

This routine returns the default dimensions for a window. Output is either a
minimum or fixed value depending on whether the window is scalable.

### [XPLMAvionicsNeedsDrawing](/sdk/XPLMAvionicsNeedsDrawing/)

```cpp
XPLM_API void       XPLMAvionicsNeedsDrawing(
                         XPLMAvionicsID       inHandle);

```

Tells X-Plane that your device’s screen needs to be re-drawn. If your device is
marked for on-demand drawing, X-Plane will call your screen drawing callback
before drawing the next simulator frame. If your device is already drawn every
frame, this has no effect.

### [XPLMAvionicsScreenCallback_f](/sdk/XPLMAvionicsScreenCallback_f/)

```cpp
typedef void (* XPLMAvionicsScreenCallback_f)(
                         void *               inRefcon);

```

This is the prototype for drawing callbacks for custom devices' screens. Refcon
is a unique value that you specify when creating the device, allowing you to
slip a pointer to your own data to the callback.

Upon entry the OpenGL context will be correctly set up for you and OpenGL will
be in panel coordinates for 2d drawing. The OpenGL state (texturing, etc.) will
be unknown. X-Plane does not clear your screen for you between calls - this
means you can re-use portions to save drawing, but otherwise you must call
glClear() to erase the screen’s contents.

### [XPLMBindTexture2d](/sdk/XPLMBindTexture2d/)

```cpp
XPLM_API void       XPLMBindTexture2d(
                         int                  inTextureNum,
                         int                  inTextureUnit);

```

[XPLMBindTexture2d](/sdk/XPLMBindTexture2d/)changes what texture is bound to the
2d texturing target. This routine caches the current 2d texture across all
texturing units in the sim and plug-ins, preventing extraneous binding. For
example, consider several plug-ins running in series; if they all use the
‘general interface’ bitmap to do UI, calling this function will skip the
rebinding of the general interface texture on all but the first plug-in, which
can provide better frame rates on some graphics cards.

inTextureID is the ID of the texture object to bind; inTextureUnit is a
zero-based texture unit (e.g. 0 for the first one), up to a maximum of 4 units.
(This number may increase in future versions of X-Plane.)

Use this routine instead of glBindTexture(GL_TEXTURE_2D, ….);

### [XPLMBringWindowToFront](/sdk/XPLMBringWindowToFront/)

```cpp
XPLM_API void       XPLMBringWindowToFront(
                         XPLMWindowID         inWindow);

```

This routine brings the window to the front of the Z-order for its layer.
Windows are brought to the front automatically when they are created. Beyond
that, you should make sure you are front before handling mouse clicks.

Note that this only brings your window to the front of its layer
([XPLMWindowLayer](/sdk/XPLMWindowLayer/)). Thus, if you have a window in the
floating window layer
([xplm_WindowLayerFloatingWindows](/sdk/xplm_WindowLayerFloatingWindows/)), but
there is a modal window (in
layer[xplm_WindowLayerModal](/sdk/xplm_WindowLayerModal/)) above you, you would
still not be the true frontmost window after calling this. (After all, the
window layers are strictly ordered, and no window in a lower layer can ever be
above any window in a higher one.)

### [XPLMCreateWindow](/sdk/XPLMCreateWindow/)

```cpp
XPLM_API XPLMWindowID XPLMCreateWindow(
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom,
                         int                  inIsVisible,
                         XPLMDrawWindow_f     inDrawCallback,
                         XPLMHandleKey_f      inKeyCallback,
                         XPLMHandleMouseClick_f inMouseCallback,
                         void *               inRefcon);

```

Deprecated as of XPLM300.

This routine creates a new legacy window. Unlike modern windows (created
via[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)()), legacy windows do not have
access to X-Plane 11 features like automatic scaling for high-DPI screens,
native window styles, or support for being “popped out” into first-class
operating system windows.

Pass in the dimensions and offsets to the window’s bottom left corner from the
bottom left of the screen. You can specify whether the window is initially
visible or not. Also, you pass in three callbacks to run the window and a
refcon. This function returns a window ID you can use to refer to the new
window.

NOTE: Legacy windows do not have “frames”; you are responsible for drawing the
background and frame of the window. Higher level libraries have routines which
make this easy.

### [XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)

```cpp
XPLM_API XPLMWindowID XPLMCreateWindowEx(
                         XPLMCreateWindow_t * inParams);

```

This routine creates a new “modern” window. You pass in
an[XPLMCreateWindow_t](/sdk/XPLMCreateWindow_t/)structure with all of the fields
set in. You must set the structSize of the structure to the size of the actual
structure you used. Also, you must provide functions for every callback—you may
not leave them null! (If you do not support the cursor or mouse wheel, use
functions that return the default values.)

### [XPLMCreateWindow_t](/sdk/XPLMCreateWindow_t/)

The XPMCreateWindow_t structure defines all of the parameters used to create a
modern window using[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)(). The
structure will be expanded in future SDK APIs to include more features. Always
set the structSize member to the size of your struct in bytes!

All windows created by this function in the XPLM300 version of the API are
created with the new X-Plane 11 GUI features. This means your plugin will get to
“know” about the existence of X-Plane windows other than the main window. All
drawing and mouse callbacks for your window will occur in “boxels,” giving your
windows automatic support for high-DPI scaling in X-Plane. In addition, your
windows can opt-in to decoration with the X-Plane 11 window styling, and you can
use the[XPLMSetWindowPositioningMode](/sdk/XPLMSetWindowPositioningMode/)() API
to make your window “popped out” into a first-class operating system window.

Note that this requires dealing with your window’s bounds in “global desktop”
positioning units, rather than the traditional panel coordinate system. In
global desktop coordinates, the main X-Plane window may not have its origin at
coordinate (0, 0), and your own window may have negative coordinates. Assuming
you don’t implicitly assume (0, 0) as your origin, the only API change you
should need is to start
using[XPLMGetMouseLocationGlobal](/sdk/XPLMGetMouseLocationGlobal/)() rather
than[XPLMGetMouseLocation](/sdk/XPLMGetMouseLocation/)(),
and[XPLMGetScreenBoundsGlobal](/sdk/XPLMGetScreenBoundsGlobal/)() instead
of[XPLMGetScreenSize](/sdk/XPLMGetScreenSize/)().

If you ask to be decorated as a floating window, you’ll get the blue window
control bar and blue backing that you see in X-Plane 11’s normal “floating”
windows (like the map).

```cpp
typedef struct {
     // Used to inform XPLMCreateWindowEx() of the SDK version you compiled against; should always be set to sizeof(XPLMCreateWindow_t)
     int                       structSize;
     // Left bound, in global desktop boxels
     int                       left;
     // Top bound, in global desktop boxels
     int                       top;
     // Right bound, in global desktop boxels
     int                       right;
     // Bottom bound, in global desktop boxels
     int                       bottom;
     int                       visible;
     XPLMDrawWindow_f          drawWindowFunc;
     // A callback to handle the user left-clicking within your window (or NULL to ignore left clicks)
     XPLMHandleMouseClick_f    handleMouseClickFunc;
     XPLMHandleKey_f           handleKeyFunc;
     XPLMHandleCursor_f        handleCursorFunc;
     XPLMHandleMouseWheel_f    handleMouseWheelFunc;
     // A reference which will be passed into each of your window callbacks. Use this to pass information to yourself as needed.
     void *                    refcon;
     // Specifies the type of X-Plane 11-style "wrapper" you want around your window, if any
     XPLMWindowDecoration      decorateAsFloatingWindow;
     XPLMWindowLayer           layer;
     // A callback to handle the user right-clicking within your window (or NULL to ignore right clicks)
     XPLMHandleMouseClick_f    handleRightClickFunc;
} XPLMCreateWindow_t;
```

### [XPLMDestroyWindow](/sdk/XPLMDestroyWindow/)

```cpp
XPLM_API void       XPLMDestroyWindow(
                         XPLMWindowID         inWindowID);

```

This routine destroys a window. The window’s callbacks are not called after this
call. Keyboard focus is removed from the window before destroying it.

### [XPLMDrawAircraft](/sdk/XPLMDrawAircraft/)

```cpp
XPLM_API void       XPLMDrawAircraft(
                         int                  inPlaneIndex,
                         float                inX,
                         float                inY,
                         float                inZ,
                         float                inPitch,
                         float                inRoll,
                         float                inYaw,
                         int                  inFullDraw,
                         XPLMPlaneDrawState_t * inDrawStateInfo);

```

WARNING: Aircraft drawing via this API is deprecated and WILL NOT WORK in future
versions of X-Plane. Use[XPLMInstance](/sdk/XPLMInstance/)for 3-d drawing of
custom aircraft models.

This routine draws an aircraft. It can only be called from a 3-d drawing
callback. Pass in the position of the plane in OpenGL local coordinates and the
orientation of the plane. A 1 for full drawing indicates that the whole plane
must be drawn; a 0 indicates you only need the nav lights drawn. (This saves
rendering time when planes are far away.)

### [XPLMDrawCallback_f](/sdk/XPLMDrawCallback_f/)

```cpp
typedef int (* XPLMDrawCallback_f)(
                         XPLMDrawingPhase     inPhase,
                         int                  inIsBefore,
                         void *               inRefcon);

```

This is the prototype for a low level drawing callback. You are passed in the
phase and whether it is before or after. If you are before the phase, return 1
to let X-Plane draw or 0 to suppress X-Plane drawing. If you are after the phase
the return value is ignored.

Refcon is a unique value that you specify when registering the callback,
allowing you to slip a pointer to your own data to the callback.

Upon entry the OpenGL context will be correctly set up for you and OpenGL will
be in ‘local’ coordinates for 3d drawing and panel coordinates for 2d drawing.
The OpenGL state (texturing, etc.) will be unknown.

### [XPLMDrawInfo_t](/sdk/XPLMDrawInfo_t/)

The[XPLMDrawInfo_t](/sdk/XPLMDrawInfo_t/)structure contains positioning info for
one object that is to be drawn. Be sure to set structSize to the size of the
structure for future expansion.

```cpp
typedef struct {
     // Set this to the size of this structure!
     int                       structSize;
     // X location of the object in local coordinates.
     float                     x;
     // Y location of the object in local coordinates.
     float                     y;
     // Z location of the object in local coordinates.
     float                     z;
     // Pitch in degres to rotate the object, positive is up.
     float                     pitch;
     // Heading in local coordinates to rotate the object, clockwise.
     float                     heading;
     // Roll to rotate the object.
     float                     roll;
} XPLMDrawInfo_t;
```

### [XPLMDrawMapIconFromSheet](/sdk/XPLMDrawMapIconFromSheet/)

```cpp
XPLM_API void       XPLMDrawMapIconFromSheet(
                         XPLMMapLayerID       layer,
                         const char *         inPngPath,
                         int                  s,
                         int                  t,
                         int                  ds,
                         int                  dt,
                         float                mapX,
                         float                mapY,
                         XPLMMapOrientation   orientation,
                         float                rotationDegrees,
                         float                mapWidth);

```

Enables plugin-created map layers to draw PNG icons using X-Plane’s built-in
icon drawing functionality. Only valid from within an XPLMIconDrawingCallback_t
(but you can request an arbitrary number of icons to be drawn from within your
callback).

X-Plane will automatically manage the memory for your texture so that it only
has to be loaded from disk once as long as you continue drawing it per-frame.
(When you stop drawing it, the memory may purged in a “garbage collection” pass,
require a load from disk in the future.)

Instead of having X-Plane draw a full PNG, this method allows you to use UV
coordinates to request a portion of the image to be drawn. This allows you to
use a single texture load (of an icon sheet, for example) to draw many icons.
Doing so is much more efficient than drawing a dozen different small PNGs.

The UV coordinates used here treat the texture you load as being comprised of a
number of identically sized “cells”. You specify the width and height in cells
(ds and dt, respectively), as well as the coordinates within the cell grid for
the sub-image you’d like to draw.

Note that you can use different ds and dt values in subsequent calls with the
same texture sheet. This enables you to use icons of different sizes in the same
sheet if you arrange them properly in the PNG.

This function is only valid from within an XPLMIconDrawingCallback_t (but you
can request an arbitrary number of icons to be drawn from within your callback).

### [XPLMDrawMapLabel](/sdk/XPLMDrawMapLabel/)

```cpp
XPLM_API void       XPLMDrawMapLabel(
                         XPLMMapLayerID       layer,
                         const char *         inText,
                         float                mapX,
                         float                mapY,
                         XPLMMapOrientation   orientation,
                         float                rotationDegrees);

```

Enables plugin-created map layers to draw text labels using X-Plane’s built-in
labeling functionality. Only valid from within
an[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/)(but you
can request an arbitrary number of text labels to be drawn from within your
callback).

### [XPLMDrawNumber](/sdk/XPLMDrawNumber/)

```cpp
XPLM_API void       XPLMDrawNumber(
                         float *              inColorRGB,
                         int                  inXOffset,
                         int                  inYOffset,
                         double               inValue,
                         int                  inDigits,
                         int                  inDecimals,
                         int                  inShowSign,
                         XPLMFontID           inFontID);

```

This routine draws a number similar to the digit editing fields in PlaneMaker
and data output display in X-Plane. Pass in a color, a position, a floating
point value, and formatting info. Specify how many integer and how many decimal
digits to show and whether to show a sign, as well as a character set. This
routine returns the xOffset plus width of the string drawn.

### [XPLMDrawObjects](/sdk/XPLMDrawObjects/)

```cpp
XPLM_API void       XPLMDrawObjects(
                         XPLMObjectRef        inObject,
                         int                  inCount,
                         XPLMDrawInfo_t *     inLocations,
                         int                  lighting,
                         int                  earth_relative);

```

**Deprecation Warning**: use XPLMInstancing to draw 3-d objects by creating
instances, rather than these APIs from draw callbacks.

[XPLMDrawObjects](/sdk/XPLMDrawObjects/)draws an object from an OBJ file one or
more times. You pass in the object and an array
of[XPLMDrawInfo_t](/sdk/XPLMDrawInfo_t/)structs, one for each place you would
like the object to be drawn.

X-Plane will attempt to cull the objects based on LOD and visibility, and will
pick the appropriate LOD.

Lighting is a boolean; pass 1 to show the night version of object with
night-only lights lit up. Pass 0 to show the daytime version of the object.

earth_relative controls the coordinate system. If this is 1, the rotations you
specify are applied to the object after its coordinate system is transformed
from local to earth-relative coordinates – that is, an object with no rotations
will point toward true north and the Y axis will be up against gravity. If this
is 0, the object is drawn with your rotations from local coordanates – that is,
an object with no rotations is drawn pointing down the -Z axis and the Y axis of
the object matches the local coordinate Y axis.

### [XPLMDrawString](/sdk/XPLMDrawString/)

```cpp
XPLM_API void       XPLMDrawString(
                         float *              inColorRGB,
                         int                  inXOffset,
                         int                  inYOffset,
                         const char *         inChar,
                         int *                inWordWrapWidth,    /* Can be NULL */
                         XPLMFontID           inFontID);

```

This routine draws a NULL terminated string in a given font. Pass in the lower
left pixel that the character is to be drawn onto. Also pass the character and
font ID. This function returns the x offset plus the width of all drawn
characters. The color to draw in is specified as a pointer to an array of three
floating point colors, representing RGB intensities from 0.0 to 1.0.

### [XPLMDrawTranslucentDarkBox](/sdk/XPLMDrawTranslucentDarkBox/)

```cpp
XPLM_API void       XPLMDrawTranslucentDarkBox(
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

This routine draws a translucent dark box, partially obscuring parts of the
screen but making text easy to read. This is the same graphics primitive used by
X-Plane to show text files.

### [XPLMDrawWindow_f](/sdk/XPLMDrawWindow_f/)

```cpp
typedef void (* XPLMDrawWindow_f)(
                         XPLMWindowID         inWindowID,
                         void *               inRefcon);

```

A callback to handle 2-D drawing of your window. You are passed in your window
and its refcon. Draw the window. You can use other XPLM functions from this
header to find the current dimensions of your window, etc. When this callback is
called, the OpenGL context will be set properly for 2-D window drawing.

**Note**: Because you are drawing your window over a background, you can make a
translucent window easily by simply not filling in your entire window’s bounds.

### [XPLMDrawingPhase](/sdk/XPLMDrawingPhase/)

This constant indicates which part of drawing we are in. Drawing is done from
the back to the front. We get a callback before or after each item. Metaphases
provide access to the beginning and end of the 3d (scene) and 2d (cockpit)
drawing in a manner that is independent of new phases added via X-Plane
implementation.

**NOTE**: As of XPLM302 the legacy 3D drawing phases
([xplm_Phase_FirstScene](/sdk/xplm_Phase_FirstScene/)to[xplm_Phase_LastScene](/sdk/xplm_Phase_LastScene/))
are deprecated. When running under X-Plane 11.50 with the modern Vulkan or Metal
backend, X-Plane will no longer call these drawing phases. There is a new
drawing phase,[xplm_Phase_Modern3D](/sdk/xplm_Phase_Modern3D/), which is
supported under OpenGL and Vulkan which is called out roughly where the old
before[xplm_Phase_Airplanes](/sdk/xplm_Phase_Airplanes/)phase was for blending.
This phase is*NOT*supported under Metal and comes with potentially substantial
performance overhead. Please do*NOT*opt into this phase if you don’t do any
actual drawing that requires the depth buffer in some way!

**WARNING**: As X-Plane’s scenery evolves, some drawing phases may cease to
exist and new ones may be invented. If you need a particularly specific use of
these codes, consult Austin and/or be prepared to revise your code as X-Plane
evolves.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_Phase_FirstScene](/sdk/xplm_Phase_FirstScene/) | "0" | Deprecated as of
XPLM302. This is the earliest point at which you can draw in 3-d. |
| [xplm_Phase_Terrain](/sdk/xplm_Phase_Terrain/) | "5" | Deprecated as of
XPLM302. Drawing of land and water. |
| [xplm_Phase_Airports](/sdk/xplm_Phase_Airports/) | "10" | Deprecated as of
XPLM302. Drawing runways and other airport detail. |
| [xplm_Phase_Vectors](/sdk/xplm_Phase_Vectors/) | "15" | Deprecated as of
XPLM302. Drawing roads, trails, trains, etc. |
| [xplm_Phase_Objects](/sdk/xplm_Phase_Objects/) | "20" | Deprecated as of
XPLM302. 3-d objects (houses, smokestacks, etc. |
| [xplm_Phase_Airplanes](/sdk/xplm_Phase_Airplanes/) | "25" | Deprecated as of
XPLM302. External views of airplanes, both yours and the AI aircraft. |
| [xplm_Phase_LastScene](/sdk/xplm_Phase_LastScene/) | "30" | Deprecated as of
XPLM302. This is the last point at which you can draw in 3-d. |
| [xplm_Phase_Modern3D](/sdk/xplm_Phase_Modern3D/) | "31" | A chance to do
modern 3D drawing. |
| [xplm_Phase_FirstCockpit](/sdk/xplm_Phase_FirstCockpit/) | "35" | This is the
first phase where you can draw in 2-d. |
| [xplm_Phase_Panel](/sdk/xplm_Phase_Panel/) | "40" | The non-moving parts of
the aircraft panel. |
| [xplm_Phase_Gauges](/sdk/xplm_Phase_Gauges/) | "45" | The moving parts of the
aircraft panel. |
| [xplm_Phase_Window](/sdk/xplm_Phase_Window/) | "50" | Floating windows from
plugins. |
| [xplm_Phase_LastCockpit](/sdk/xplm_Phase_LastCockpit/) | "55" | The last
chance to draw in 2d. |
| [xplm_Phase_LocalMap3D](/sdk/xplm_Phase_LocalMap3D/) | "100" | Removed as of
XPLM300; Use the full-blown[XPLMMap](/sdk/XPLMMap/)API instead. |
| [xplm_Phase_LocalMap2D](/sdk/xplm_Phase_LocalMap2D/) | "101" | Removed as of
XPLM300; Use the full-blown[XPLMMap](/sdk/XPLMMap/)API instead. |
| [xplm_Phase_LocalMapProfile](/sdk/xplm_Phase_LocalMapProfile/) | "102" |
Removed as of XPLM300; Use the full-blown[XPLMMap](/sdk/XPLMMap/)API instead. |

### [XPLMGenerateTextureNumbers](/sdk/XPLMGenerateTextureNumbers/)

```cpp
XPLM_API void       XPLMGenerateTextureNumbers(
                         int *                outTextureIDs,
                         int                  inCount);

```

Use this routine instead of glGenTextures to generate new texture object IDs.
This routine historically ensured that plugins don’t use texure IDs that X-Plane
is reserving for its own use.

### [XPLMGetScreenBoundsGlobal](/sdk/XPLMGetScreenBoundsGlobal/)

```cpp
XPLM_API void       XPLMGetScreenBoundsGlobal(
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

This routine returns the bounds of the “global” X-Plane desktop, in boxels.
Unlike the non-global version[XPLMGetScreenSize](/sdk/XPLMGetScreenSize/)(),
this is multi-monitor aware. There are three primary consequences of
multimonitor awareness.

First, if the user is running X-Plane in full-screen on two or more monitors
(typically configured using one full-screen window per monitor), the global
desktop will be sized to include all X-Plane windows.

Second, the origin of the screen coordinates is not guaranteed to be (0, 0).
Suppose the user has two displays side-by-side, both running at 1080p. Suppose
further that they’ve configured their OS to make the left display their
“primary” monitor, and that X-Plane is running in full-screen on their right
monitor only. In this case, the global desktop bounds would be the rectangle
from (1920, 0) to (3840, 1080). If the user later asked X-Plane to draw on their
primary monitor as well, the bounds would change to (0, 0) to (3840, 1080).

Finally, if the usable area of the virtual desktop is not a perfect rectangle
(for instance, because the monitors have different resolutions or because one
monitor is configured in the operating system to be above and to the right of
the other), the global desktop will include any wasted space. Thus, if you have
two 1080p monitors, and monitor 2 is configured to have its bottom left touch
monitor 1’s upper right, your global desktop area would be the rectangle from
(0, 0) to (3840, 2160).

Note that popped-out windows (windows drawn in their own operating system
windows, rather than “floating” within X-Plane) are not included in these
bounds.

### [XPLMGetScreenSize](/sdk/XPLMGetScreenSize/)

```cpp
XPLM_API void       XPLMGetScreenSize(
                         int *                outWidth,    /* Can be NULL */
                         int *                outHeight);    /* Can be NULL */

```

This routine returns the size of the main X-Plane OpenGL window in pixels. This
number can be used to get a rough idea of the amount of detail the user will be
able to see when drawing in 3-d.

### [XPLMGetTexture](/sdk/XPLMGetTexture/)

```cpp
XPLM_API int        XPLMGetTexture(
                         XPLMTextureID        inTexture);

```

[XPLMGetTexture](/sdk/XPLMGetTexture/)returns the OpenGL texture ID of an
X-Plane texture based on a generic identifying code. For example, you can get
the texture for X-Plane’s UI bitmaps.

### [XPLMGetWindowGeometry](/sdk/XPLMGetWindowGeometry/)

```cpp
XPLM_API void       XPLMGetWindowGeometry(
                         XPLMWindowID         inWindowID,
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

This routine returns the position and size of a window. The units and coordinate
system vary depending on the type of window you have.

If this is a legacy window (one compiled against a pre-XPLM300 version of the
SDK, or an XPLM300 window that was not created
using[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)()), the units are pixels
relative to the main X-Plane display.

If, on the other hand, this is a new X-Plane 11-style window (compiled against
the XPLM300 SDK and created
using[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)()), the units are global
desktop boxels.

Pass NULL to not receive any paramter.

### [XPLMGetWindowGeometryOS](/sdk/XPLMGetWindowGeometryOS/)

```cpp
XPLM_API void       XPLMGetWindowGeometryOS(
                         XPLMWindowID         inWindowID,
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

This routine returns the position and size of a “popped out” window (i.e., a
window whose positioning mode is[xplm_WindowPopOut](/sdk/xplm_WindowPopOut/)),
in operating system pixels. Pass NULL to not receive any parameter.

### [XPLMGetWindowGeometryVR](/sdk/XPLMGetWindowGeometryVR/)

```cpp
XPLM_API void       XPLMGetWindowGeometryVR(
                         XPLMWindowID         inWindowID,
                         int *                outWidthBoxels,    /* Can be NULL */
                         int *                outHeightBoxels);    /* Can be NULL */

```

Returns the width and height, in boxels, of a window in VR. Note that you are
responsible for ensuring your window is in VR
(using[XPLMWindowIsInVR](/sdk/XPLMWindowIsInVR/)()).

### [XPLMGetWindowIsVisible](/sdk/XPLMGetWindowIsVisible/)

```cpp
XPLM_API int        XPLMGetWindowIsVisible(
                         XPLMWindowID         inWindowID);

```

Returns true (1) if the specified window is visible.

### [XPLMGetWindowRefCon](/sdk/XPLMGetWindowRefCon/)

```cpp
XPLM_API void *     XPLMGetWindowRefCon(
                         XPLMWindowID         inWindowID);

```

Returns a window’s reference constant, the unique value you can use for your own
purposes.

### [XPLMIsWindowInFront](/sdk/XPLMIsWindowInFront/)

```cpp
XPLM_API int        XPLMIsWindowInFront(
                         XPLMWindowID         inWindow);

```

This routine returns true if the window you passed in is the frontmost visible
window in its layer ([XPLMWindowLayer](/sdk/XPLMWindowLayer/)).

Thus, if you have a window at the front of the floating window layer
([xplm_WindowLayerFloatingWindows](/sdk/xplm_WindowLayerFloatingWindows/)), this
will return true even if there is a modal window (in
layer[xplm_WindowLayerModal](/sdk/xplm_WindowLayerModal/)) above you. (Not to
worry, though: in such a case, X-Plane will not pass clicks or keyboard input
down to your layer until the window above stops “eating” the input.)

Note that legacy windows are always placed in
layer[xplm_WindowLayerFlightOverlay](/sdk/xplm_WindowLayerFlightOverlay/), while
modern-style windows default
to[xplm_WindowLayerFloatingWindows](/sdk/xplm_WindowLayerFloatingWindows/). This
means it’s perfectly consistent to have two different plugin-created windows
(one legacy, one modern)*both*be in the front (of their different layers!) at
the same time.

### [XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/)

```cpp
typedef void (* XPLMMapDrawingCallback_f)(
                         XPLMMapLayerID       inLayer,
                         const float *        inMapBoundsLeftTopRightBottom,
                         float                zoomRatio,
                         float                mapUnitsPerUserInterfaceUnit,
                         XPLMMapStyle         mapStyle,
                         XPLMMapProjectionID  projection,
                         void *               inRefcon);

```

This is the OpenGL map drawing callback for plugin-created map layers. You can
perform arbitrary OpenGL drawing from this callback, with one exception: changes
to the Z-buffer are not permitted, and will result in map drawing errors.

All drawing done from within this callback appears beneath all built-in X-Plane
icons and labels, but above the built-in “fill” layers (layers providing major
details, like terrain and water). Note, however, that the relative ordering
between the drawing callbacks of different plugins is not guaranteed.

### [XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/)

```cpp
typedef void (* XPLMMapIconDrawingCallback_f)(
                         XPLMMapLayerID       inLayer,
                         const float *        inMapBoundsLeftTopRightBottom,
                         float                zoomRatio,
                         float                mapUnitsPerUserInterfaceUnit,
                         XPLMMapStyle         mapStyle,
                         XPLMMapProjectionID  projection,
                         void *               inRefcon);

```

This is the icon drawing callback that enables plugin-created map layers to draw
icons using X-Plane’s built-in icon drawing functionality. You can request an
arbitrary number of PNG icons to be drawn
via[XPLMDrawMapIconFromSheet](/sdk/XPLMDrawMapIconFromSheet/)() from within this
callback, but you may not perform any OpenGL drawing here.

Icons enqueued by this function will appear above all OpenGL drawing (performed
by your optional[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/)), and
above all built-in X-Plane map icons of the same layer type (“fill” or
“markings,” as determined by the[XPLMMapLayerType](/sdk/XPLMMapLayerType/)in
your[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)). Note, however, that the
relative ordering between the drawing callbacks of different plugins is not
guaranteed.

### [XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/)

```cpp
typedef void (* XPLMMapLabelDrawingCallback_f)(
                         XPLMMapLayerID       inLayer,
                         const float *        inMapBoundsLeftTopRightBottom,
                         float                zoomRatio,
                         float                mapUnitsPerUserInterfaceUnit,
                         XPLMMapStyle         mapStyle,
                         XPLMMapProjectionID  projection,
                         void *               inRefcon);

```

This is the label drawing callback that enables plugin-created map layers to
draw text labels using X-Plane’s built-in labeling functionality. You can
request an arbitrary number of text labels to be drawn
via[XPLMDrawMapLabel](/sdk/XPLMDrawMapLabel/)() from within this callback, but
you may not perform any OpenGL drawing here.

Labels enqueued by this function will appear above all OpenGL drawing (performed
by your optional[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/)), and
above all built-in map icons and labels of the same layer type (“fill” or
“markings,” as determined by the[XPLMMapLayerType](/sdk/XPLMMapLayerType/)in
your[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)). Note, however, that the
relative ordering between the drawing callbacks of different plugins is not
guaranteed.

### [XPLMPlaneDrawState_t](/sdk/XPLMPlaneDrawState_t/)

This structure contains additional plane parameter info to be passed to draw
plane. Make sure to fill in the size of the structure field with
sizeof(XPLMDrawPlaneState_t) so that the XPLM can tell how many fields you knew
about when compiling your plugin (since more fields may be added later).

Most of these fields are ratios from 0 to 1 for control input. X-Plane
calculates what the actual controls look like based on the .acf file for that
airplane. Note for the yoke inputs, this is what the pilot of the plane has
commanded (post artificial stability system if there were one) and affects
ailerons, rudder, etc. It is not necessarily related to the actual position of
the plane’s surfaces!

```cpp
typedef struct {
     // The size of the draw state struct.
     int                       structSize;
     // A ratio from [0..1] describing how far the landing gear is extended.
     float                     gearPosition;
     // Ratio of flap deployment, 0 = up, 1 = full deploy.
     float                     flapRatio;
     // Ratio of spoiler deployment, 0 = none, 1 = full deploy.
     float                     spoilerRatio;
     // Ratio of speed brake deployment, 0 = none, 1 = full deploy.
     float                     speedBrakeRatio;
     // Ratio of slat deployment, 0 = none, 1 = full deploy.
     float                     slatRatio;
     // Wing sweep ratio, 0 = forward, 1 = swept.
     float                     wingSweep;
     // Thrust power, 0 = none, 1 = full fwd, -1 = full reverse.
     float                     thrust;
     // Total pitch input for this plane.
     float                     yokePitch;
     // Total Heading input for this plane.
     float                     yokeHeading;
     // Total Roll input for this plane.
     float                     yokeRoll;
} XPLMPlaneDrawState_t;
```

### [XPLMRegisterDrawCallback](/sdk/XPLMRegisterDrawCallback/)

```cpp
XPLM_API int        XPLMRegisterDrawCallback(
                         XPLMDrawCallback_f   inCallback,
                         XPLMDrawingPhase     inPhase,
                         int                  inWantsBefore,
                         void *               inRefcon);

```

This routine registers a low level drawing callback. Pass in the phase you want
to be called for and whether you want to be called before or after. This routine
returns 1 if the registration was successful, or 0 if the phase does not exist
in this version of X-Plane. You may register a callback multiple times for the
same or different phases as long as the refcon is unique each time.

Note that this function will likely be removed during the X-Plane 11 run as part
of the transition to Vulkan/Metal/etc. See
the[XPLMInstance](/sdk/XPLMInstance/)API for future-proof drawing of 3-D
objects.

### [XPLMSetWindowGeometry](/sdk/XPLMSetWindowGeometry/)

```cpp
XPLM_API void       XPLMSetWindowGeometry(
                         XPLMWindowID         inWindowID,
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

This routine allows you to set the position and size of a window.

The units and coordinate system match those
of[XPLMGetWindowGeometry](/sdk/XPLMGetWindowGeometry/)(). That is, modern
windows use global desktop boxel coordinates, while legacy windows use pixels
relative to the main X-Plane display.

Note that this only applies to “floating” windows (that is, windows that are
drawn within the X-Plane simulation windows, rather than being “popped out” into
their own first-class operating system windows). To set the position of windows
whose positioning mode is[xplm_WindowPopOut](/sdk/xplm_WindowPopOut/), you’ll
need to instead use[XPLMSetWindowGeometryOS](/sdk/XPLMSetWindowGeometryOS/)().

### [XPLMSetWindowGeometryOS](/sdk/XPLMSetWindowGeometryOS/)

```cpp
XPLM_API void       XPLMSetWindowGeometryOS(
                         XPLMWindowID         inWindowID,
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

This routine allows you to set the position and size, in operating system pixel
coordinates, of a popped out window (that is, a window whose positioning mode
is[xplm_WindowPopOut](/sdk/xplm_WindowPopOut/), which exists outside the X-Plane
simulation window, in its own first-class operating system window).

Note that you are responsible for ensuring both that your window is popped out
(using[XPLMWindowIsPoppedOut](/sdk/XPLMWindowIsPoppedOut/)()) and that a monitor
really exists at the OS coordinates you provide
(using[XPLMGetAllMonitorBoundsOS](/sdk/XPLMGetAllMonitorBoundsOS/)()).

### [XPLMSetWindowGeometryVR](/sdk/XPLMSetWindowGeometryVR/)

```cpp
XPLM_API void       XPLMSetWindowGeometryVR(
                         XPLMWindowID         inWindowID,
                         int                  widthBoxels,
                         int                  heightBoxels);

```

This routine allows you to set the size, in boxels, of a window in VR (that is,
a window whose positioning mode is[xplm_WindowVR](/sdk/xplm_WindowVR/)).

Note that you are responsible for ensuring your window is in VR
(using[XPLMWindowIsInVR](/sdk/XPLMWindowIsInVR/)()).

### [XPLMSetWindowGravity](/sdk/XPLMSetWindowGravity/)

```cpp
XPLM_API void       XPLMSetWindowGravity(
                         XPLMWindowID         inWindowID,
                         float                inLeftGravity,
                         float                inTopGravity,
                         float                inRightGravity,
                         float                inBottomGravity);

```

A window’s “gravity” controls how the window shifts as the whole X-Plane window
resizes. A gravity of 1 means the window maintains its positioning relative to
the right or top edges, 0 the left/bottom, and 0.5 keeps it centered.

Default gravity is (0, 1, 0, 1), meaning your window will maintain its position
relative to the top left and will not change size as its containing window
grows.

If you wanted, say, a window that sticks to the top of the screen (with a
constant height), but which grows to take the full width of the window, you
would pass (0, 1, 1, 1). Because your left and right edges would maintain their
positioning relative to their respective edges of the screen, the whole width of
your window would change with the X-Plane window.

Only applies to modern windows. (Windows created using the
deprecated[XPLMCreateWindow](/sdk/XPLMCreateWindow/)(), or windows compiled
against a pre-XPLM300 version of the SDK will simply get the default gravity.)

### [XPLMSetWindowIsVisible](/sdk/XPLMSetWindowIsVisible/)

```cpp
XPLM_API void       XPLMSetWindowIsVisible(
                         XPLMWindowID         inWindowID,
                         int                  inIsVisible);

```

This routine shows or hides a window.

### [XPLMSetWindowPositioningMode](/sdk/XPLMSetWindowPositioningMode/)

```cpp
XPLM_API void       XPLMSetWindowPositioningMode(
                         XPLMWindowID         inWindowID,
                         XPLMWindowPositioningMode inPositioningMode,
                         int                  inMonitorIndex);

```

Sets the policy for how X-Plane will position your window.

Some positioning modes apply to a particular monitor. For those modes, you can
pass a negative monitor index to position the window on the main X-Plane monitor
(the screen with the X-Plane menu bar at the top). Or, if you have a specific
monitor you want to position your window on, you can pass a real monitor index
as received from,
e.g.,[XPLMGetAllMonitorBoundsOS](/sdk/XPLMGetAllMonitorBoundsOS/)().

Only applies to modern windows. (Windows created using the
deprecated[XPLMCreateWindow](/sdk/XPLMCreateWindow/)(), or windows compiled
against a pre-XPLM300 version of the SDK will always
use[xplm_WindowPositionFree](/sdk/xplm_WindowPositionFree/).)

### [XPLMSetWindowRefCon](/sdk/XPLMSetWindowRefCon/)

```cpp
XPLM_API void       XPLMSetWindowRefCon(
                         XPLMWindowID         inWindowID,
                         void *               inRefcon);

```

Sets a window’s reference constant. Use this to pass data to yourself in the
callbacks.

### [XPLMSetWindowResizingLimits](/sdk/XPLMSetWindowResizingLimits/)

```cpp
XPLM_API void       XPLMSetWindowResizingLimits(
                         XPLMWindowID         inWindowID,
                         int                  inMinWidthBoxels,
                         int                  inMinHeightBoxels,
                         int                  inMaxWidthBoxels,
                         int                  inMaxHeightBoxels);

```

Sets the minimum and maximum size of the client rectangle of the given window.
(That is, it does not include any window styling that you might have asked
X-Plane to apply on your behalf.) All resizing operations are constrained to
these sizes.

Only applies to modern windows. (Windows created using the
deprecated[XPLMCreateWindow](/sdk/XPLMCreateWindow/)(), or windows compiled
against a pre-XPLM300 version of the SDK will have no minimum or maximum size.)

### [XPLMSetWindowTitle](/sdk/XPLMSetWindowTitle/)

```cpp
XPLM_API void       XPLMSetWindowTitle(
                         XPLMWindowID         inWindowID,
                         const char *         inWindowTitle);

```

Sets the name for a window. This only applies to windows that opted-in to
styling as an X-Plane 11 floating window (i.e., with styling
mode[xplm_WindowDecorationRoundRectangle](/sdk/xplm_WindowDecorationRoundRectangle/))
when they were created using[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)().

### [XPLMTextureID](/sdk/XPLMTextureID/)

XPLM Texture IDs name well-known textures in the sim for you to use. This allows
you to recycle textures from X-Plane, saving VRAM.

*Warning*: do not use these enums. The only remaining use they have is to access
the legacy compatibility v10 UI texture; if you need this, get it via the
Widgets library.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_Tex_GeneralInterface](/sdk/xplm_Tex_GeneralInterface/) | "0" | The
bitmap that contains window outlines, button outlines, fonts, etc. |
| [xplm_Tex_AircraftPaint](/sdk/xplm_Tex_AircraftPaint/) | "1" | The exterior
paint for the user's aircraft (daytime). |
| [xplm_Tex_AircraftLiteMap](/sdk/xplm_Tex_AircraftLiteMap/) | "2" | The
exterior light map for the user's aircraft. |

### [XPLMUnregisterDrawCallback](/sdk/XPLMUnregisterDrawCallback/)

```cpp
XPLM_API int        XPLMUnregisterDrawCallback(
                         XPLMDrawCallback_f   inCallback,
                         XPLMDrawingPhase     inPhase,
                         int                  inWantsBefore,
                         void *               inRefcon);

```

This routine unregisters a draw callback. You must unregister a callback for
each time you register a callback if you have registered it multiple times with
different refcons. The routine returns 1 if it can find the callback to
unregister, 0 otherwise.

Note that this function will likely be removed during the X-Plane 11 run as part
of the transition to Vulkan/Metal/etc. See
the[XPLMInstance](/sdk/XPLMInstance/)API for future-proof drawing of 3-D
objects.

### [XPLMWindowDecoration](/sdk/XPLMWindowDecoration/)

[XPLMWindowDecoration](/sdk/XPLMWindowDecoration/)describes how “modern” windows
will be displayed. This impacts both how X-Plane draws your window as well as
certain mouse handlers.

Your window’s decoration can only be specified when you create the window (in
the[XPLMCreateWindow_t](/sdk/XPLMCreateWindow_t/)you pass
to[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)()).

| Name | Value | Description |
| --- | --- | --- |
| [xplm_WindowDecorationNone](/sdk/xplm_WindowDecorationNone/) | "0" | X-Plane
will draw no decoration for your window, and apply no automatic click handlers.
The window will not stop click from passing through its bounds. This is suitable
for "windows" which request, say, the full screen bounds, then only draw in a
small portion of the available area. |
|
[xplm_WindowDecorationRoundRectangle](/sdk/xplm_WindowDecorationRoundRectangle/)
| "1" | The default decoration for "native" windows, like the map. Provides a
solid background, as well as click handlers for resizing and dragging the
window. |
| [xplm_WindowDecorationSelfDecorated](/sdk/xplm_WindowDecorationSelfDecorated/)
| "2" | X-Plane will draw no decoration for your window, nor will it provide
resize handlers for your window edges, but it will stop clicks from passing
through your windows bounds. |
|
[xplm_WindowDecorationSelfDecoratedResizable](/sdk/xplm_WindowDecorationSelfDecoratedResizable/)
| "3" | Like self-decorated, but with resizing; X-Plane will draw no decoration
for your window, but it will stop clicks from passing through your windows
bounds, and provide automatic mouse handlers for resizing. |

### [XPLMWindowID](/sdk/XPLMWindowID/)

```cpp
typedef void * XPLMWindowID;
```

This is an opaque identifier for a window. You use it to control your window.
When you create a window (via either[XPLMCreateWindow](/sdk/XPLMCreateWindow/)()
or[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)()), you will specify callbacks
to handle drawing, mouse interaction, etc.

### [XPLMWindowIsInVR](/sdk/XPLMWindowIsInVR/)

```cpp
XPLM_API int        XPLMWindowIsInVR(
                         XPLMWindowID         inWindowID);

```

True if this window has been moved to the virtual reality (VR) headset, which in
turn is true if and only if you have set the window’s positioning mode
to[xplm_WindowVR](/sdk/xplm_WindowVR/).

Only applies to modern windows. (Windows created using the
deprecated[XPLMCreateWindow](/sdk/XPLMCreateWindow/)(), or windows compiled
against a pre-XPLM301 version of the SDK cannot be moved to VR.)

### [XPLMWindowIsPoppedOut](/sdk/XPLMWindowIsPoppedOut/)

```cpp
XPLM_API int        XPLMWindowIsPoppedOut(
                         XPLMWindowID         inWindowID);

```

True if this window has been popped out (making it a first-class window in the
operating system), which in turn is true if and only if you have set the
window’s positioning mode to[xplm_WindowPopOut](/sdk/xplm_WindowPopOut/).

Only applies to modern windows. (Windows created using the
deprecated[XPLMCreateWindow](/sdk/XPLMCreateWindow/)(), or windows compiled
against a pre-XPLM300 version of the SDK cannot be popped out.)

### [XPLMWindowLayer](/sdk/XPLMWindowLayer/)

[XPLMWindowLayer](/sdk/XPLMWindowLayer/)describes where in the ordering of
windows X-Plane should place a particular window. Windows in higher layers cover
windows in lower layers. So, a given window might be at the top of its
particular layer, but it might still be obscured by a window in a higher layer.
(This happens frequently when floating windows, like X-Plane’s map, are covered
by a modal alert.)

Your window’s layer can only be specified when you create the window (in
the[XPLMCreateWindow_t](/sdk/XPLMCreateWindow_t/)you pass
to[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)()). For this reason, layering
only applies to windows created with new X-Plane 11 GUI features. (Windows
created using the older[XPLMCreateWindow](/sdk/XPLMCreateWindow/)(), or windows
compiled against a pre-XPLM300 version of the SDK will simply be placed in the
flight overlay window layer.)

| Name | Value | Description |
| --- | --- | --- |
| [xplm_WindowLayerFlightOverlay](/sdk/xplm_WindowLayerFlightOverlay/) | "0" |
The lowest layer, used for HUD-like displays while flying. |
| [xplm_WindowLayerFloatingWindows](/sdk/xplm_WindowLayerFloatingWindows/) | "1"
| Windows that "float" over the sim, like the X-Plane 11 map does. If you are
not sure which layer to create your window in, choose floating. |
| [xplm_WindowLayerModal](/sdk/xplm_WindowLayerModal/) | "2" | An interruptive
modal that covers the sim with a transparent black overlay to draw the user's
focus to the alert |
| [xplm_WindowLayerGrowlNotifications](/sdk/xplm_WindowLayerGrowlNotifications/)
| "3" | "Growl"-style notifications that are visible in a corner of the screen,
even over modals |

### [XPLMWindowPositioningMode](/sdk/XPLMWindowPositioningMode/)

XPLMWindowPositionMode describes how X-Plane will position your window on the
user’s screen. X-Plane will maintain this positioning mode even as the user
resizes their window or adds/removes full-screen monitors.

Positioning mode can only be set for “modern” windows (that is, windows created
using[XPLMCreateWindowEx](/sdk/XPLMCreateWindowEx/)() and compiled against the
XPLM300 SDK). Windows created using the
deprecated[XPLMCreateWindow](/sdk/XPLMCreateWindow/)(), or windows compiled
against a pre-XPLM300 version of the SDK will simply get the “free” positioning
mode.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_WindowPositionFree](/sdk/xplm_WindowPositionFree/) | "0" | The default
positioning mode. Set the window geometry and its future position will be
determined by its window gravity, resizing limits, and user interactions. |
| [xplm_WindowCenterOnMonitor](/sdk/xplm_WindowCenterOnMonitor/) | "1" | Keep
the window centered on the monitor you specify |
| [xplm_WindowFullScreenOnMonitor](/sdk/xplm_WindowFullScreenOnMonitor/) | "2" |
Keep the window full screen on the monitor you specify |
| [xplm_WindowFullScreenOnAllMonitors](/sdk/xplm_WindowFullScreenOnAllMonitors/)
| "3" | Like gui_window_full_screen_on_monitor, but stretches over *all*
monitors and popout windows. This is an obscure one... unless you have a very
good reason to need it, you probably don't! |
| [xplm_WindowPopOut](/sdk/xplm_WindowPopOut/) | "4" | A first-class window in
the operating system, completely separate from the X-Plane window(s) |
| [xplm_WindowVR](/sdk/xplm_WindowVR/) | "5" | A floating window visible on the
VR headset |

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

| |  |
| --- | --- | --- |
| [xpElement_WindowCloseBox](/sdk/xpElement_WindowCloseBox/) | "14" | none window header |

| |  |
| --- | --- | --- |
| [xpElement_WindowCloseBoxPressed](/sdk/xpElement_WindowCloseBoxPressed/) | "15" | none window header |

| |  |
| --- | --- | --- |
| [xpElement_WindowDragBar](/sdk/xpElement_WindowDragBar/) | "61" | none metal |

| |  |
| --- | --- | --- |
| [xpElement_WindowDragBarSmooth](/sdk/xpElement_WindowDragBarSmooth/) | "62" | none metal |

| |  |
| --- | --- | --- |
| [xpMainWindowStyle_MainWindow](/sdk/xpMainWindowStyle_MainWindow/) | "0" | The standard main window; pin stripes on XP7, metal frame on XP 6. |

| |  |
| --- | --- | --- |
| [xpMainWindowStyle_Translucent](/sdk/xpMainWindowStyle_Translucent/) | "1" | A translucent dark gray window. |

| |  |
| --- | --- | --- |
| [xpMsg_Draw](/sdk/xpMsg_Draw/) | "4" | The draw message is sent to your widget when it is time to draw yourself. OpenGL will be set upto draw in 2-d global screen coordinates, but you should use the XPLM to set up OpenGL state.Dispatching: Direct |

| |  |
| --- | --- | --- |
| [xpProperty_MainWindowHasCloseBoxes](/sdk/xpProperty_MainWindowHasCloseBoxes/) | "1200" | This property specifies whether the main window has close boxes in its corners. |

| |  |
| --- | --- | --- |
| [xpProperty_MainWindowType](/sdk/xpProperty_MainWindowType/) | "1100" | This property specifies the type of window. Set to one of the main window types above. |

| |  |
| --- | --- | --- |
| [xpProperty_SubWindowType](/sdk/xpProperty_SubWindowType/) | "1200" | This property specifies the type of window. Set to one of the subwindow types above. |

| |  |
| --- | --- | --- |
| [xpSubWindowStyle_Screen](/sdk/xpSubWindowStyle_Screen/) | "2" | A screen that sits inside a panel for showing text information. |

| |  |
| --- | --- | --- |
| [xpSubWindowStyle_SubWindow](/sdk/xpSubWindowStyle_SubWindow/) | "0" | A panel that sits inside a main window. |

### [xpWidgetClass_MainWindow](/sdk/xpWidgetClass_MainWindow/)

```cpp
#define xpWidgetClass_MainWindow 1
```

### [xpWidgetClass_SubWindow](/sdk/xpWidgetClass_SubWindow/)

```cpp
#define xpWidgetClass_SubWindow 2
```

| |  |
| --- | --- | --- |
| [xpWindowCloseBox](/sdk/xpWindowCloseBox/) | "3" | A window close box. |

| |  |
| --- | --- | --- |
| [xpWindow_Help](/sdk/xpWindow_Help/) | "0" | An LCD screen that shows help. |

| |  |
| --- | --- | --- |
| [xpWindow_MainWindow](/sdk/xpWindow_MainWindow/) | "1" | A dialog box window. |

| |  |
| --- | --- | --- |
| [xpWindow_Screen](/sdk/xpWindow_Screen/) | "4" | An LCD screen within a panel to hold text displays. |

| |  |
| --- | --- | --- |
| [xpWindow_SubWindow](/sdk/xpWindow_SubWindow/) | "2" | A panel or frame within a dialog box window. |

| |  |
| --- | --- | --- |
| [xplm_Phase_Window](/sdk/xplm_Phase_Window/) | "50" | Floating windows from plugins. |

| |  |
| --- | --- | --- |
| [xplm_WindowCenterOnMonitor](/sdk/xplm_WindowCenterOnMonitor/) | "1" | Keep the window centered on the monitor you specify |

| |  |
| --- | --- | --- |
| [xplm_WindowDecorationNone](/sdk/xplm_WindowDecorationNone/) | "0" | X-Plane will draw no decoration for your window, and apply no automatic click handlers. The window will not stop click from passing through its bounds. This is suitable for "windows" which request, say, the full screen bounds, then only draw in a small portion of the available area. |

| |  |
| --- | --- | --- |
| [xplm_WindowDecorationRoundRectangle](/sdk/xplm_WindowDecorationRoundRectangle/) | "1" | The default decoration for "native" windows, like the map. Provides a solid background, as well as click handlers for resizing and dragging the window. |

| |  |
| --- | --- | --- |
| [xplm_WindowDecorationSelfDecorated](/sdk/xplm_WindowDecorationSelfDecorated/) | "2" | X-Plane will draw no decoration for your window, nor will it provide resize handlers for your window edges, but it will stop clicks from passing through your windows bounds. |

| |  |
| --- | --- | --- |
| [xplm_WindowDecorationSelfDecoratedResizable](/sdk/xplm_WindowDecorationSelfDecoratedResizable/) | "3" | Like self-decorated, but with resizing; X-Plane will draw no decoration for your window, but it will stop clicks from passing through your windows bounds, and provide automatic mouse handlers for resizing. |

| |  |
| --- | --- | --- |
| [xplm_WindowFullScreenOnAllMonitors](/sdk/xplm_WindowFullScreenOnAllMonitors/) | "3" | Like gui_window_full_screen_on_monitor, but stretches over *all* monitors and popout windows. This is an obscure one... unless you have a very good reason to need it, you probably don't! |

| |  |
| --- | --- | --- |
| [xplm_WindowFullScreenOnMonitor](/sdk/xplm_WindowFullScreenOnMonitor/) | "2" | Keep the window full screen on the monitor you specify |

| |  |
| --- | --- | --- |
| [xplm_WindowLayerFlightOverlay](/sdk/xplm_WindowLayerFlightOverlay/) | "0" | The lowest layer, used for HUD-like displays while flying. |

| |  |
| --- | --- | --- |
| [xplm_WindowLayerFloatingWindows](/sdk/xplm_WindowLayerFloatingWindows/) | "1" | Windows that "float" over the sim, like the X-Plane 11 map does. If you are not sure which layer to create your window in, choose floating. |

| |  |
| --- | --- | --- |
| [xplm_WindowLayerGrowlNotifications](/sdk/xplm_WindowLayerGrowlNotifications/) | "3" | "Growl"-style notifications that are visible in a corner of the screen, even over modals |

| |  |
| --- | --- | --- |
| [xplm_WindowLayerModal](/sdk/xplm_WindowLayerModal/) | "2" | An interruptive modal that covers the sim with a transparent black overlay to draw the user's focus to the alert |

| |  |
| --- | --- | --- |
| [xplm_WindowPopOut](/sdk/xplm_WindowPopOut/) | "4" | A first-class window in the operating system, completely separate from the X-Plane window(s) |

| |  |
| --- | --- | --- |
| [xplm_WindowPositionFree](/sdk/xplm_WindowPositionFree/) | "0" | The default positioning mode. Set the window geometry and its future position will be determined by its window gravity, resizing limits, and user interactions. |

| |  |
| --- | --- | --- |
| [xplm_WindowVR](/sdk/xplm_WindowVR/) | "5" | A floating window visible on the VR headset |

