---
title: "Map APIs"
description: "X-Plane SDK Map APIs documentation"
category: "XPLM_Map"
date: "2025-06-25T15:45:56.659424"
---

# Map APIs

### [XPLMAppendMenuItem](/sdk/XPLMAppendMenuItem/)

```cpp
XPLM_API int        XPLMAppendMenuItem(
                         XPLMMenuID           inMenu,
                         const char *         inItemName,
                         void *               inItemRef,
                         int                  inDeprecatedAndIgnored);

```

This routine appends a new menu item to the bottom of a menu and returns its
index. Pass in the menu to add the item to, the items name, and a void * ref for
this item.

Returns a negative index if the append failed (due to an invalid parent menu
argument).

Note that all menu indices returned are relative to your plugin’s menus only; if
your plugin creates two sub-menus in the Plugins menu at different times, it
doesn’t matter how many other plugins also create sub-menus of Plugins in the
intervening time: your sub-menus will be given menu indices 0 and 1. (The SDK
does some work in the back-end to filter out menus that are irrelevant to your
plugin in order to deliver this consistency for each plugin.)

### [XPLMAppendMenuItemWithCommand](/sdk/XPLMAppendMenuItemWithCommand/)

```cpp
XPLM_API int        XPLMAppendMenuItemWithCommand(
                         XPLMMenuID           inMenu,
                         const char *         inItemName,
                         XPLMCommandRef       inCommandToExecute);

```

Like[XPLMAppendMenuItem](/sdk/XPLMAppendMenuItem/)(), but instead of the new
menu item triggering the[XPLMMenuHandler_f](/sdk/XPLMMenuHandler_f/)of the
containiner menu, it will simply execute the command you pass in. Using a
command for your menu item allows the user to bind a keyboard shortcut to the
command and see that shortcut represented in the menu.

Returns a negative index if the append failed (due to an invalid parent menu
argument).

Like[XPLMAppendMenuItem](/sdk/XPLMAppendMenuItem/)(), all menu indices are
relative to your plugin’s menus only.

### [XPLMAppendMenuSeparator](/sdk/XPLMAppendMenuSeparator/)

```cpp
XPLM_API void       XPLMAppendMenuSeparator(
                         XPLMMenuID           inMenu);

```

This routine adds a separator to the end of a menu.

Returns a negative index if the append failed (due to an invalid parent menu
argument).

### [XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)

```cpp
XPLM_API XPLMMapLayerID XPLMCreateMapLayer(
                         XPLMCreateMapLayer_t * inParams);

```

This routine creates a new map layer. You pass in
an[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)structure with all of the
fields defined. You must set the structSize of the structure to the size of the
actual structure you used.

Returns NULL if the layer creation failed. This happens most frequently because
the map you specified in
your[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)::mapToCreateLayerIn field
doesn’t exist (that is, if[XPLMMapExists](/sdk/XPLMMapExists/)() returns 0 for
the specified map). You can
use[XPLMRegisterMapCreationHook](/sdk/XPLMRegisterMapCreationHook/)() to get a
notification each time a new map is opened in X-Plane, at which time you can
create layers in it.

### [XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)

This structure defines all of the parameters used to create a map layer
using[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/). The structure will be
expanded in future SDK APIs to include more features. Always set the structSize
member to the size of your struct in bytes!

Each layer must be associated with exactly one map instance in X-Plane. That
map, and that map alone, will call your callbacks. Likewise, when that map is
deleted, your layer will be as well.

```cpp
typedef struct {
     // Used to inform XPLMCreateMapLayer() of the SDK version you compiled against; should always be set to sizeof(XPLMCreateMapLayer_t)
     int                       structSize;
     // Globally unique string identifying the map you want this layer to appear in. As of XPLM300, this is limited to one of XPLM_MAP_USER_INTERFACE or XPLM_MAP_IOS
     const char *              mapToCreateLayerIn;
     // The type of layer you are creating, used to determine draw order (all plugin-created markings layers are drawn above all plugin-created fill layers)
     XPLMMapLayerType          layerType;
     // Optional callback to inform you this layer is being deleted (due to its owning map being destroyed)
     XPLMMapWillBeDeletedCallback_f willBeDeletedCallback;
     // Optional callback you want to use to prepare your draw cache when the map bounds change (set to NULL if you don't want this callback)
     XPLMMapPrepareCacheCallback_f prepCacheCallback;
     // Optional callback you want to use for arbitrary OpenGL drawing, which goes beneath all icons in the map's layering system (set to NULL if you don't want this callback)
     XPLMMapDrawingCallback_f  drawCallback;
     // Optional callback you want to use for drawing icons, which go above all built-in X-Plane icons (except the aircraft) in the map's layering system (set to NULL if you don't want this callback)
     XPLMMapIconDrawingCallback_f iconCallback;
     // Optional callback you want to use for drawing map labels, which go above all built-in X-Plane icons and labels (except those of aircraft) in the map's layering system (set to NULL if you don't want this callback)
     XPLMMapLabelDrawingCallback_f labelCallback;
     // True if you want a checkbox to be created in the map UI to toggle this layer on and off; false if the layer should simply always be enabled
     int                       showUiToggle;
     // Short label to use for this layer in the user interface
     const char *              layerName;
     // A reference to arbitrary data that will be passed to your callbacks
     void *                    refcon;
} XPLMCreateMapLayer_t;
```

### [XPLMDestroyMapLayer](/sdk/XPLMDestroyMapLayer/)

```cpp
XPLM_API int        XPLMDestroyMapLayer(
                         XPLMMapLayerID       inLayer);

```

Destroys a map layer you created (calling
your[XPLMMapWillBeDeletedCallback_f](/sdk/XPLMMapWillBeDeletedCallback_f/)if
applicable). Returns true if a deletion took place.

# [XPLMMap](/sdk/XPLMMap/)API

This API allows you to create new layers within X-Plane maps. Your layers can
draw arbitrary OpenGL, but they conveniently also have access to X-Plane’s
built-in icon and label drawing functions.

As of X-Plane 11, map drawing happens in three stages:

1. backgrounds and “fill”,
2. icons, and
3. labels.

Thus, all background drawing gets layered beneath all icons, which likewise get
layered beneath all labels. Within each stage, the map obeys a consistent layer
ordering, such that “fill” layers (layers that cover a large amount of map area,
like the terrain and clouds) appear beneath “markings” layers (like airport
icons). This ensures that layers with fine details don’t get obscured by layers
with larger details.

The XPLM map API reflects both aspects of this draw layering: you can register a
layer as providing either markings or fill, and X-Plane will draw your fill
layers beneath your markings layers (regardless of registration order).
Likewise, you are guaranteed that your layer’s icons (added from within an icon
callback) will go above your layer’s OpenGL drawing, and your labels will go
above your icons.

The XPLM guarantees that all plugin-created fill layers go on top of all native
X-Plane fill layers, and all plugin-created markings layers go on top of all
X-Plane markings layers (with the exception of the aircraft icons). It also
guarantees that the draw order of your own plugin’s layers will be consistent.
But, for layers created by different plugins, the only guarantee is that we will
draw all of one plugin’s layers of each type (fill, then markings), then all of
the others'; we don’t guarantee which plugin’s fill and markings layers go on
top of the other’s.

As of X-Plane 11, maps use true cartographic projections for their drawing, and
different maps may use different projections. For that reason, all drawing calls
include an opaque handle for the projection you should use to do the drawing.
Any time you would draw at a particular latitude/longitude, you’ll need to ask
the projection to translate that position into “map coordinates.” (Note that the
projection is guaranteed not to change between calls to your prepare-cache hook,
so if you cache your map coordinates ahead of time, there’s no need to
re-project them when you actually draw.)

In addition to mapping normal latitude/longitude locations into map coordinates,
the projection APIs also let you know the current heading for north. (Since
X-Plane 11 maps can rotate to match the heading of the user’s aircraft, it’s not
safe to assume that north is at zero degrees rotation.)

## DRAWING CALLBACKS

When you create a new map layer
(using[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)), you can provide any or
all of these callbacks. They allow you to insert your own OpenGL drawing, text
labels, and icons into the X-Plane map at the appropriate places, allowing your
layer to behave as similarly to X-Plane’s built-in layers as possible.

### [XPLMMapLayerID](/sdk/XPLMMapLayerID/)

```cpp
typedef void * XPLMMapLayerID;
```

This is an opaque handle for a plugin-created map layer. Pass it to the map
drawing APIs from an appropriate callback to draw in the layer you created.

### [XPLMMapProjectionID](/sdk/XPLMMapProjectionID/)

```cpp
typedef void * XPLMMapProjectionID;
```

This is an opaque handle for a map projection. Pass it to the projection APIs to
translate between map coordinates and latitude/longitudes.

### [XPLMMapStyle](/sdk/XPLMMapStyle/)

Indicates the visual style being drawn by the map. In X-Plane, the user can
choose between a number of map types, and different map types may have use a
different visual representation for the same elements (for instance, the visual
style of the terrain layer changes drastically between the VFR and IFR layers),
or certain layers may be disabled entirely in some map types (e.g., localizers
are only visible in the IFR low-enroute style).

| Name | Value | Description |
| --- | --- | --- |
| [xplm_MapStyle_VFR_Sectional](/sdk/xplm_MapStyle_VFR_Sectional/) | "0" |
| [xplm_MapStyle_IFR_LowEnroute](/sdk/xplm_MapStyle_IFR_LowEnroute/) | "1" |
| [xplm_MapStyle_IFR_HighEnroute](/sdk/xplm_MapStyle_IFR_HighEnroute/) | "2" |

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

## LAYER MANAGEMENT CALLBACKS

These are various “bookkeeping” callbacks that your map layer can receive (if
you provide the callback in
your[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)). They allow you to
manage the lifecycle of your layer, as well as cache any
computationally-intensive preparation you might need for drawing.

### [XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/)

```cpp
typedef void (* XPLMMapPrepareCacheCallback_f)(
                         XPLMMapLayerID       inLayer,
                         const float *        inTotalMapBoundsLeftTopRightBottom,
                         XPLMMapProjectionID  projection,
                         void *               inRefcon);

```

A callback used to allow you to cache whatever information your layer needs to
draw in the current map area.

This is called each time the map’s total bounds change. This is typically
triggered by new DSFs being loaded, such that X-Plane discards old, now-distant
DSFs and pulls in new ones. At that point, the available bounds of the map also
change to match the new DSF area.

By caching just the information you need to draw in this area, your future draw
calls can be made faster, since you’ll be able to simply “splat” your
precomputed information each frame.

We guarantee that the map projection will not change between successive prepare
cache calls, nor will any draw call give you bounds outside these total map
bounds. So, if you cache the projected map coordinates of all the items you
might want to draw in the total map area, you can be guaranteed that no draw
call will be asked to do any new work.

### [XPLMMapWillBeDeletedCallback_f](/sdk/XPLMMapWillBeDeletedCallback_f/)

```cpp
typedef void (* XPLMMapWillBeDeletedCallback_f)(
                         XPLMMapLayerID       inLayer,
                         void *               inRefcon);

```

Called just before your map layer gets deleted. Because SDK-created map layers
have the same lifetime as the X-Plane map that contains them, if the map gets
unloaded from memory, your layer will too.

## MAP LAYER CREATION AND DESTRUCTION

Enables the creation of new map layers. Layers are created for a particular
instance of the X-Plane map. For instance, if you want your layer to appear in
both the normal map interface and the Instructor Operator Station (IOS), you
would need two separate calls
to[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)(), with two different values
for your[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)::layer_name.

Your layer’s lifetime will be determined by the lifetime of the map it is
created in. If the map is destroyed (on the X-Plane side), your layer will be
too, and you’ll receive a callback to
your[XPLMMapWillBeDeletedCallback_f](/sdk/XPLMMapWillBeDeletedCallback_f/).

### [XPLMMapLayerType](/sdk/XPLMMapLayerType/)

Indicates the type of map layer you are creating. Fill layers will always be
drawn beneath markings layers.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_MapLayer_Fill](/sdk/xplm_MapLayer_Fill/) | "0" | A layer that draws
"fill" graphics, like weather patterns, terrain, etc. Fill layers frequently
cover a large portion of the visible map area. |
| [xplm_MapLayer_Markings](/sdk/xplm_MapLayer_Markings/) | "1" | A layer that
provides markings for particular map features, like NAVAIDs, airports, etc. Even
dense markings layers cover a small portion of the total map area. |

### [XPLM_MAP_USER_INTERFACE](/sdk/XPLM_MAP_USER_INTERFACE/)

```cpp
#define XPLM_MAP_USER_INTERFACE "XPLM_MAP_USER_INTERFACE"
```

Globally unique identifier for X-Plane’s Map window, used as the
mapToCreateLayerIn parameter
in[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)

### [XPLM_MAP_IOS](/sdk/XPLM_MAP_IOS/)

```cpp
#define XPLM_MAP_IOS         "XPLM_MAP_IOS"
```

Globally unique identifier for X-Plane’s Instructor Operator Station window,
used as the mapToCreateLayerIn parameter
in[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)

### [XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)

This structure defines all of the parameters used to create a map layer
using[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/). The structure will be
expanded in future SDK APIs to include more features. Always set the structSize
member to the size of your struct in bytes!

Each layer must be associated with exactly one map instance in X-Plane. That
map, and that map alone, will call your callbacks. Likewise, when that map is
deleted, your layer will be as well.

```cpp
typedef struct {
     // Used to inform XPLMCreateMapLayer() of the SDK version you compiled against; should always be set to sizeof(XPLMCreateMapLayer_t)
     int                       structSize;
     // Globally unique string identifying the map you want this layer to appear in. As of XPLM300, this is limited to one of XPLM_MAP_USER_INTERFACE or XPLM_MAP_IOS
     const char *              mapToCreateLayerIn;
     // The type of layer you are creating, used to determine draw order (all plugin-created markings layers are drawn above all plugin-created fill layers)
     XPLMMapLayerType          layerType;
     // Optional callback to inform you this layer is being deleted (due to its owning map being destroyed)
     XPLMMapWillBeDeletedCallback_f willBeDeletedCallback;
     // Optional callback you want to use to prepare your draw cache when the map bounds change (set to NULL if you don't want this callback)
     XPLMMapPrepareCacheCallback_f prepCacheCallback;
     // Optional callback you want to use for arbitrary OpenGL drawing, which goes beneath all icons in the map's layering system (set to NULL if you don't want this callback)
     XPLMMapDrawingCallback_f  drawCallback;
     // Optional callback you want to use for drawing icons, which go above all built-in X-Plane icons (except the aircraft) in the map's layering system (set to NULL if you don't want this callback)
     XPLMMapIconDrawingCallback_f iconCallback;
     // Optional callback you want to use for drawing map labels, which go above all built-in X-Plane icons and labels (except those of aircraft) in the map's layering system (set to NULL if you don't want this callback)
     XPLMMapLabelDrawingCallback_f labelCallback;
     // True if you want a checkbox to be created in the map UI to toggle this layer on and off; false if the layer should simply always be enabled
     int                       showUiToggle;
     // Short label to use for this layer in the user interface
     const char *              layerName;
     // A reference to arbitrary data that will be passed to your callbacks
     void *                    refcon;
} XPLMCreateMapLayer_t;
```

### [XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)

```cpp
XPLM_API XPLMMapLayerID XPLMCreateMapLayer(
                         XPLMCreateMapLayer_t * inParams);

```

This routine creates a new map layer. You pass in
an[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)structure with all of the
fields defined. You must set the structSize of the structure to the size of the
actual structure you used.

Returns NULL if the layer creation failed. This happens most frequently because
the map you specified in
your[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)::mapToCreateLayerIn field
doesn’t exist (that is, if[XPLMMapExists](/sdk/XPLMMapExists/)() returns 0 for
the specified map). You can
use[XPLMRegisterMapCreationHook](/sdk/XPLMRegisterMapCreationHook/)() to get a
notification each time a new map is opened in X-Plane, at which time you can
create layers in it.

### [XPLMDestroyMapLayer](/sdk/XPLMDestroyMapLayer/)

```cpp
XPLM_API int        XPLMDestroyMapLayer(
                         XPLMMapLayerID       inLayer);

```

Destroys a map layer you created (calling
your[XPLMMapWillBeDeletedCallback_f](/sdk/XPLMMapWillBeDeletedCallback_f/)if
applicable). Returns true if a deletion took place.

### [XPLMMapCreatedCallback_f](/sdk/XPLMMapCreatedCallback_f/)

```cpp
typedef void (* XPLMMapCreatedCallback_f)(
                         const char *         mapIdentifier,
                         void *               refcon);

```

A callback to notify your plugin that a new map has been created in X-Plane.
This is the best time to add a custom map layer
using[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)().

No OpenGL drawing is permitted within this callback.

### [XPLMRegisterMapCreationHook](/sdk/XPLMRegisterMapCreationHook/)

```cpp
XPLM_API void       XPLMRegisterMapCreationHook(
                         XPLMMapCreatedCallback_f callback,
                         void *               refcon);

```

Registers your callback to receive a notification each time a new map is
constructed in X-Plane. This callback is the best time to add your custom map
layer using[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)().

Note that you will not be notified about any maps that already exist—you can
use[XPLMMapExists](/sdk/XPLMMapExists/)() to check for maps that were created
previously.

### [XPLMMapExists](/sdk/XPLMMapExists/)

```cpp
XPLM_API int        XPLMMapExists(
                         const char *         mapIdentifier);

```

Returns 1 if the map with the specified identifier already exists in X-Plane. In
that case, you can safely call[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)()
specifying that your layer should be added to that map.

## MAP DRAWING

These APIs are only valid from within a map drawing callback (one of
XPLMIconDrawingCallback_t
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/)). Your
drawing callbacks are registered when you create a new map layer as part of
your[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/). The functions here hook
into X-Plane’s built-in map drawing functionality for icons and labels, so that
you get a consistent style with the rest of the X-Plane map.

Note that the X-Plane 11 map introduces a strict ordering: layers of
type[xplm_MapLayer_Fill](/sdk/xplm_MapLayer_Fill/)get drawn beneath
all[xplm_MapLayer_Markings](/sdk/xplm_MapLayer_Markings/)layers. Likewise, all
OpenGL drawing (performed in your
layer’s[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/)) will appear
beneath any icons and labels you draw.

### [XPLMMapOrientation](/sdk/XPLMMapOrientation/)

Indicates whether a map element should be match its rotation to the map itself,
or to the user interface. For instance, the map itself may be rotated such that
“up” matches the user’s aircraft, but you may want to draw a text label such
that it is always rotated zero degrees relative to the user’s perspective. In
that case, you would have it draw with UI orientation.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_MapOrientation_Map](/sdk/xplm_MapOrientation_Map/) | "0" | Orient such
that a 0 degree rotation matches the map's north |
| [xplm_MapOrientation_UI](/sdk/xplm_MapOrientation_UI/) | "1" | Orient such
that a 0 degree rotation is "up" relative to the user interface |

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

## MAP PROJECTIONS

As of X-Plane 11, the map draws using true cartographic projections, and
different maps may use different projections. Thus, to draw at a particular
latitude and longitude, you must first transform your real-world coordinates
into map coordinates.

The map projection is also responsible for giving you the current scale of the
map. That is, the projection can tell you how many map units correspond to 1
meter at a given point.

Finally, the map projection can give you the current rotation of the map. Since
X-Plane 11 maps can rotate to match the heading of the aircraft, the map’s
rotation can potentially change every frame.

### [XPLMMapProject](/sdk/XPLMMapProject/)

```cpp
XPLM_API void       XPLMMapProject(
                         XPLMMapProjectionID  projection,
                         double               latitude,
                         double               longitude,
                         float *              outX,
                         float *              outY);

```

Projects a latitude/longitude into map coordinates. This is the inverse
of[XPLMMapUnproject](/sdk/XPLMMapUnproject/)().

Only valid from within a map layer callback (one
of[XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/),[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/),[XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/),
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/).)

### [XPLMMapUnproject](/sdk/XPLMMapUnproject/)

```cpp
XPLM_API void       XPLMMapUnproject(
                         XPLMMapProjectionID  projection,
                         float                mapX,
                         float                mapY,
                         double *             outLatitude,
                         double *             outLongitude);

```

Transforms map coordinates back into a latitude and longitude. This is the
inverse of[XPLMMapProject](/sdk/XPLMMapProject/)().

Only valid from within a map layer callback (one
of[XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/),[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/),[XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/),
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/).)

### [XPLMMapScaleMeter](/sdk/XPLMMapScaleMeter/)

```cpp
XPLM_API float      XPLMMapScaleMeter(
                         XPLMMapProjectionID  projection,
                         float                mapX,
                         float                mapY);

```

Returns the number of map units that correspond to a distance of one meter at a
given set of map coordinates.

Only valid from within a map layer callback (one
of[XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/),[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/),[XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/),
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/).)

### [XPLMMapGetNorthHeading](/sdk/XPLMMapGetNorthHeading/)

```cpp
XPLM_API float      XPLMMapGetNorthHeading(
                         XPLMMapProjectionID  projection,
                         float                mapX,
                         float                mapY);

```

Returns the heading (in degrees clockwise) from the positive Y axis in the
cartesian mapping coordinate system to true north at the point passed in. You
can use it as a clockwise rotational offset to align icons and other 2-d drawing
with true north on the map, compensating for rotations in the map due to
projection.

Only valid from within a map layer callback (one
of[XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/),[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/),[XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/),
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/).)

### [XPLMMapCreatedCallback_f](/sdk/XPLMMapCreatedCallback_f/)

```cpp
typedef void (* XPLMMapCreatedCallback_f)(
                         const char *         mapIdentifier,
                         void *               refcon);

```

A callback to notify your plugin that a new map has been created in X-Plane.
This is the best time to add a custom map layer
using[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)().

No OpenGL drawing is permitted within this callback.

### [XPLMMapExists](/sdk/XPLMMapExists/)

```cpp
XPLM_API int        XPLMMapExists(
                         const char *         mapIdentifier);

```

Returns 1 if the map with the specified identifier already exists in X-Plane. In
that case, you can safely call[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)()
specifying that your layer should be added to that map.

### [XPLMMapGetNorthHeading](/sdk/XPLMMapGetNorthHeading/)

```cpp
XPLM_API float      XPLMMapGetNorthHeading(
                         XPLMMapProjectionID  projection,
                         float                mapX,
                         float                mapY);

```

Returns the heading (in degrees clockwise) from the positive Y axis in the
cartesian mapping coordinate system to true north at the point passed in. You
can use it as a clockwise rotational offset to align icons and other 2-d drawing
with true north on the map, compensating for rotations in the map due to
projection.

Only valid from within a map layer callback (one
of[XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/),[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/),[XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/),
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/).)

### [XPLMMapLayerID](/sdk/XPLMMapLayerID/)

```cpp
typedef void * XPLMMapLayerID;
```

This is an opaque handle for a plugin-created map layer. Pass it to the map
drawing APIs from an appropriate callback to draw in the layer you created.

### [XPLMMapLayerType](/sdk/XPLMMapLayerType/)

Indicates the type of map layer you are creating. Fill layers will always be
drawn beneath markings layers.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_MapLayer_Fill](/sdk/xplm_MapLayer_Fill/) | "0" | A layer that draws
"fill" graphics, like weather patterns, terrain, etc. Fill layers frequently
cover a large portion of the visible map area. |
| [xplm_MapLayer_Markings](/sdk/xplm_MapLayer_Markings/) | "1" | A layer that
provides markings for particular map features, like NAVAIDs, airports, etc. Even
dense markings layers cover a small portion of the total map area. |

### [XPLMMapOrientation](/sdk/XPLMMapOrientation/)

Indicates whether a map element should be match its rotation to the map itself,
or to the user interface. For instance, the map itself may be rotated such that
“up” matches the user’s aircraft, but you may want to draw a text label such
that it is always rotated zero degrees relative to the user’s perspective. In
that case, you would have it draw with UI orientation.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_MapOrientation_Map](/sdk/xplm_MapOrientation_Map/) | "0" | Orient such
that a 0 degree rotation matches the map's north |
| [xplm_MapOrientation_UI](/sdk/xplm_MapOrientation_UI/) | "1" | Orient such
that a 0 degree rotation is "up" relative to the user interface |

### [XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/)

```cpp
typedef void (* XPLMMapPrepareCacheCallback_f)(
                         XPLMMapLayerID       inLayer,
                         const float *        inTotalMapBoundsLeftTopRightBottom,
                         XPLMMapProjectionID  projection,
                         void *               inRefcon);

```

A callback used to allow you to cache whatever information your layer needs to
draw in the current map area.

This is called each time the map’s total bounds change. This is typically
triggered by new DSFs being loaded, such that X-Plane discards old, now-distant
DSFs and pulls in new ones. At that point, the available bounds of the map also
change to match the new DSF area.

By caching just the information you need to draw in this area, your future draw
calls can be made faster, since you’ll be able to simply “splat” your
precomputed information each frame.

We guarantee that the map projection will not change between successive prepare
cache calls, nor will any draw call give you bounds outside these total map
bounds. So, if you cache the projected map coordinates of all the items you
might want to draw in the total map area, you can be guaranteed that no draw
call will be asked to do any new work.

### [XPLMMapProject](/sdk/XPLMMapProject/)

```cpp
XPLM_API void       XPLMMapProject(
                         XPLMMapProjectionID  projection,
                         double               latitude,
                         double               longitude,
                         float *              outX,
                         float *              outY);

```

Projects a latitude/longitude into map coordinates. This is the inverse
of[XPLMMapUnproject](/sdk/XPLMMapUnproject/)().

Only valid from within a map layer callback (one
of[XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/),[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/),[XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/),
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/).)

### [XPLMMapProjectionID](/sdk/XPLMMapProjectionID/)

```cpp
typedef void * XPLMMapProjectionID;
```

This is an opaque handle for a map projection. Pass it to the projection APIs to
translate between map coordinates and latitude/longitudes.

### [XPLMMapScaleMeter](/sdk/XPLMMapScaleMeter/)

```cpp
XPLM_API float      XPLMMapScaleMeter(
                         XPLMMapProjectionID  projection,
                         float                mapX,
                         float                mapY);

```

Returns the number of map units that correspond to a distance of one meter at a
given set of map coordinates.

Only valid from within a map layer callback (one
of[XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/),[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/),[XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/),
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/).)

### [XPLMMapStyle](/sdk/XPLMMapStyle/)

Indicates the visual style being drawn by the map. In X-Plane, the user can
choose between a number of map types, and different map types may have use a
different visual representation for the same elements (for instance, the visual
style of the terrain layer changes drastically between the VFR and IFR layers),
or certain layers may be disabled entirely in some map types (e.g., localizers
are only visible in the IFR low-enroute style).

| Name | Value | Description |
| --- | --- | --- |
| [xplm_MapStyle_VFR_Sectional](/sdk/xplm_MapStyle_VFR_Sectional/) | "0" |
| [xplm_MapStyle_IFR_LowEnroute](/sdk/xplm_MapStyle_IFR_LowEnroute/) | "1" |
| [xplm_MapStyle_IFR_HighEnroute](/sdk/xplm_MapStyle_IFR_HighEnroute/) | "2" |

### [XPLMMapUnproject](/sdk/XPLMMapUnproject/)

```cpp
XPLM_API void       XPLMMapUnproject(
                         XPLMMapProjectionID  projection,
                         float                mapX,
                         float                mapY,
                         double *             outLatitude,
                         double *             outLongitude);

```

Transforms map coordinates back into a latitude and longitude. This is the
inverse of[XPLMMapProject](/sdk/XPLMMapProject/)().

Only valid from within a map layer callback (one
of[XPLMMapPrepareCacheCallback_f](/sdk/XPLMMapPrepareCacheCallback_f/),[XPLMMapDrawingCallback_f](/sdk/XPLMMapDrawingCallback_f/),[XPLMMapIconDrawingCallback_f](/sdk/XPLMMapIconDrawingCallback_f/),
or[XPLMMapLabelDrawingCallback_f](/sdk/XPLMMapLabelDrawingCallback_f/).)

### [XPLMMapWillBeDeletedCallback_f](/sdk/XPLMMapWillBeDeletedCallback_f/)

```cpp
typedef void (* XPLMMapWillBeDeletedCallback_f)(
                         XPLMMapLayerID       inLayer,
                         void *               inRefcon);

```

Called just before your map layer gets deleted. Because SDK-created map layers
have the same lifetime as the X-Plane map that contains them, if the map gets
unloaded from memory, your layer will too.

### [XPLMRegisterMapCreationHook](/sdk/XPLMRegisterMapCreationHook/)

```cpp
XPLM_API void       XPLMRegisterMapCreationHook(
                         XPLMMapCreatedCallback_f callback,
                         void *               refcon);

```

Registers your callback to receive a notification each time a new map is
constructed in X-Plane. This callback is the best time to add your custom map
layer using[XPLMCreateMapLayer](/sdk/XPLMCreateMapLayer/)().

Note that you will not be notified about any maps that already exist—you can
use[XPLMMapExists](/sdk/XPLMMapExists/)() to check for maps that were created
previously.

### [XPLM_MAP_IOS](/sdk/XPLM_MAP_IOS/)

```cpp
#define XPLM_MAP_IOS         "XPLM_MAP_IOS"
```

Globally unique identifier for X-Plane’s Instructor Operator Station window,
used as the mapToCreateLayerIn parameter
in[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)

### [XPLM_MAP_USER_INTERFACE](/sdk/XPLM_MAP_USER_INTERFACE/)

```cpp
#define XPLM_MAP_USER_INTERFACE "XPLM_MAP_USER_INTERFACE"
```

Globally unique identifier for X-Plane’s Map window, used as the
mapToCreateLayerIn parameter
in[XPLMCreateMapLayer_t](/sdk/XPLMCreateMapLayer_t/)

| |
| --- | --- |
| [xplm_Host_PFD_Map](/sdk/xplm_Host_PFD_Map/) | "10" |

| |  |
| --- | --- | --- |
| [xplm_MapLayer_Fill](/sdk/xplm_MapLayer_Fill/) | "0" | A layer that draws "fill" graphics, like weather patterns, terrain, etc. Fill layers frequently cover a large portion of the visible map area. |

| |  |
| --- | --- | --- |
| [xplm_MapLayer_Markings](/sdk/xplm_MapLayer_Markings/) | "1" | A layer that provides markings for particular map features, like NAVAIDs, airports, etc. Even dense markings layers cover a small portion of the total map area. |

| |  |
| --- | --- | --- |
| [xplm_MapOrientation_Map](/sdk/xplm_MapOrientation_Map/) | "0" | Orient such that a 0 degree rotation matches the map's north |

| |  |
| --- | --- | --- |
| [xplm_MapOrientation_UI](/sdk/xplm_MapOrientation_UI/) | "1" | Orient such that a 0 degree rotation is "up" relative to the user interface |

| |
| --- | --- |
| [xplm_MapStyle_IFR_HighEnroute](/sdk/xplm_MapStyle_IFR_HighEnroute/) | "2" |

| |
| --- | --- |
| [xplm_MapStyle_IFR_LowEnroute](/sdk/xplm_MapStyle_IFR_LowEnroute/) | "1" |

| |
| --- | --- |
| [xplm_MapStyle_VFR_Sectional](/sdk/xplm_MapStyle_VFR_Sectional/) | "0" |

| |  |
| --- | --- | --- |
| [xplm_Phase_LocalMap2D](/sdk/xplm_Phase_LocalMap2D/) | "101" | Removed as of XPLM300; Use the full-blown[XPLMMap](/sdk/XPLMMap/)API instead. |

| |  |
| --- | --- | --- |
| [xplm_Phase_LocalMap3D](/sdk/xplm_Phase_LocalMap3D/) | "100" | Removed as of XPLM300; Use the full-blown[XPLMMap](/sdk/XPLMMap/)API instead. |

| |  |
| --- | --- | --- |
| [xplm_Phase_LocalMapProfile](/sdk/xplm_Phase_LocalMapProfile/) | "102" | Removed as of XPLM300; Use the full-blown[XPLMMap](/sdk/XPLMMap/)API instead. |

| |  |
| --- | --- | --- |
| [xplm_Tex_AircraftLiteMap](/sdk/xplm_Tex_AircraftLiteMap/) | "2" | The exterior light map for the user's aircraft. |

