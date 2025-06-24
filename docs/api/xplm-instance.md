---
title: "Instance APIs"
description: "X-Plane SDK Instance APIs documentation"
category: "XPLM_Instance"
date: "2025-06-24T17:34:11.202013"
---

# Instance APIs

### [XPLMCreateInstance](/sdk/XPLMCreateInstance/)

```cpp
XPLM_API XPLMInstanceRef XPLMCreateInstance(
                         XPLMObjectRef        obj,
                         const char **        datarefs);

```

[XPLMCreateInstance](/sdk/XPLMCreateInstance/)creates a new instance, managed by
your plug-in, and returns a handle to the instance. A few important
requirements:

- The object passed in must be fully loaded and returned from the XPLM before you
  can create your instance; you cannot pass a null obj ref, nor can you change the
  ref later.
- If you use any custom datarefs in your object, they must be registered before
  the object is loaded. This is true even if their data will be provided via the
  instance dataref list.
- The instance dataref array must be a valid pointer to a null-terminated array.
  That is, if you do not want any datarefs, you must pass a pointer to a
  one-element array containing a null item. You cannot pass null for the array
  itself.

### [XPLMDestroyInstance](/sdk/XPLMDestroyInstance/)

```cpp
XPLM_API void       XPLMDestroyInstance(
                         XPLMInstanceRef      instance);

```

[XPLMDestroyInstance](/sdk/XPLMDestroyInstance/)destroys and deallocates your
instance; once called, you are still responsible for releasing the OBJ ref.

Tip: you can release your OBJ ref after you
call[XPLMCreateInstance](/sdk/XPLMCreateInstance/)as long as you never use it
again; the instance will maintain its own reference to the OBJ and the object
OBJ be deallocated when the instance is destroyed.

### [XPLMGetNthAircraftModel](/sdk/XPLMGetNthAircraftModel/)

```cpp
XPLM_API void       XPLMGetNthAircraftModel(
                         int                  inIndex,
                         char *               outFileName,
                         char *               outPath);

```

This function returns the aircraft model for the Nth aircraft. Indices are zero
based, with zero being the user’s aircraft. The file name should be at least 256
chars in length; the path should be at least 512 chars in length.

# [XPLMInstance](/sdk/XPLMInstance/)API

This API provides instanced drawing of X-Plane objects (.obj files). In contrast
to old drawing APIs, which required you to draw your own objects per-frame, the
instancing API allows you to simply register an OBJ for drawing, then move or
manipulate it later (as needed).

This provides one tremendous benefit: it keeps all dataref operations for your
object in one place. Because datarefs access may be done from the main thread
only, allowing dataref access anywhere is a serious performance bottleneck for
the simulator - the whole simulator has to pause and wait for each dataref
access. This performance penalty will only grow worse as X-Plane moves toward an
ever more heavily multithreaded engine.

The instancing API allows X-Plane to isolate all dataref manipulations for all
plugin object drawing to one place, potentially providing huge performance
gains.

Here’s how it works:

When an instance is created, it provides a list of all datarefs you want to
manipulate for the OBJ in the future. This list of datarefs replaces the ad-hoc
collections of dataref objects previously used by art assets. Then, per-frame,
you can manipulate the instance by passing in a “block” of packed floats
representing the current values of the datarefs for your instance. (Note that
the ordering of this set of packed floats must exactly match the ordering of the
datarefs when you created your instance.)

## Instance Creation and Destruction

Registers and unregisters instances.

### [XPLMInstanceRef](/sdk/XPLMInstanceRef/)

```cpp
typedef void * XPLMInstanceRef;
```

An opaque handle to an instance.

### [XPLMCreateInstance](/sdk/XPLMCreateInstance/)

```cpp
XPLM_API XPLMInstanceRef XPLMCreateInstance(
                         XPLMObjectRef        obj,
                         const char **        datarefs);

```

[XPLMCreateInstance](/sdk/XPLMCreateInstance/)creates a new instance, managed by
your plug-in, and returns a handle to the instance. A few important
requirements:

- The object passed in must be fully loaded and returned from the XPLM before you
  can create your instance; you cannot pass a null obj ref, nor can you change the
  ref later.
- If you use any custom datarefs in your object, they must be registered before
  the object is loaded. This is true even if their data will be provided via the
  instance dataref list.
- The instance dataref array must be a valid pointer to a null-terminated array.
  That is, if you do not want any datarefs, you must pass a pointer to a
  one-element array containing a null item. You cannot pass null for the array
  itself.

### [XPLMDestroyInstance](/sdk/XPLMDestroyInstance/)

```cpp
XPLM_API void       XPLMDestroyInstance(
                         XPLMInstanceRef      instance);

```

[XPLMDestroyInstance](/sdk/XPLMDestroyInstance/)destroys and deallocates your
instance; once called, you are still responsible for releasing the OBJ ref.

Tip: you can release your OBJ ref after you
call[XPLMCreateInstance](/sdk/XPLMCreateInstance/)as long as you never use it
again; the instance will maintain its own reference to the OBJ and the object
OBJ be deallocated when the instance is destroyed.

## Instance Manipulation

### [XPLMInstanceSetPosition](/sdk/XPLMInstanceSetPosition/)

```cpp
XPLM_API void       XPLMInstanceSetPosition(
                         XPLMInstanceRef      instance,
                         const XPLMDrawInfo_t * new_position,
                         const float *        data);

```

Updates both the position of the instance and all datarefs you registered for
it. Call this from a flight loop callback or UI callback.

**DO_NOT**call[XPLMInstanceSetPosition](/sdk/XPLMInstanceSetPosition/)from a
drawing callback; the whole point of instancing is that you do not need any
drawing callbacks. Setting instance data from a drawing callback may have
undefined consequences, and the drawing callback hurts FPS unnecessarily.

The memory pointed to by the data pointer must be large enough to hold one float
for every dataref you have registered, and must contain valid floating point
data.

BUG: before X-Plane 11.50, if you have no dataref registered, you must still
pass a valid pointer for data and not null.

### [XPLMInstanceRef](/sdk/XPLMInstanceRef/)

```cpp
typedef void * XPLMInstanceRef;
```

An opaque handle to an instance.

### [XPLMInstanceSetPosition](/sdk/XPLMInstanceSetPosition/)

```cpp
XPLM_API void       XPLMInstanceSetPosition(
                         XPLMInstanceRef      instance,
                         const XPLMDrawInfo_t * new_position,
                         const float *        data);

```

Updates both the position of the instance and all datarefs you registered for
it. Call this from a flight loop callback or UI callback.

**DO_NOT**call[XPLMInstanceSetPosition](/sdk/XPLMInstanceSetPosition/)from a
drawing callback; the whole point of instancing is that you do not need any
drawing callbacks. Setting instance data from a drawing callback may have
undefined consequences, and the drawing callback hurts FPS unnecessarily.

The memory pointed to by the data pointer must be large enough to hold one float
for every dataref you have registered, and must contain valid floating point
data.

BUG: before X-Plane 11.50, if you have no dataref registered, you must still
pass a valid pointer for data and not null.

### [XPLMLoadObject](/sdk/XPLMLoadObject/)

```cpp
XPLM_API XPLMObjectRef XPLMLoadObject(
                         const char *         inPath);

```

This routine loads an OBJ file and returns a handle to it. If X-Plane has
already loaded the object, the handle to the existing object is returned. Do not
assume you will get the same handle back twice, but do make sure to call unload
once for every load to avoid “leaking” objects. The object will be purged from
memory when no plugins and no scenery are using it.

The path for the object must be relative to the X-System base folder. If the
path is in the root of the X-System folder you may need to prepend ./ to it;
loading objects in the root of the X-System folder is STRONGLY discouraged -
your plugin should not dump art resources in the root folder!

[XPLMLoadObject](/sdk/XPLMLoadObject/)will return NULL if the object cannot be
loaded (either because it is not found or the file is misformatted). This
routine will load any object that can be used in the X-Plane scenery system.

It is important that the datarefs an object uses for animation already be
registered before you load the object. For this reason it may be necessary to
defer object loading until the sim has fully started.

### [XPLMLoadObjectAsync](/sdk/XPLMLoadObjectAsync/)

```cpp
XPLM_API void       XPLMLoadObjectAsync(
                         const char *         inPath,
                         XPLMObjectLoaded_f   inCallback,
                         void *               inRefcon);

```

This routine loads an object asynchronously; control is returned to you
immediately while X-Plane loads the object. The sim will not stop flying while
the object loads. For large objects, it may be several seconds before the load
finishes.

You provide a callback function that is called once the load has completed. Note
that if the object cannot be loaded, you will not find out until the callback
function is called with a NULL object handle.

There is no way to cancel an asynchronous object load; you must wait for the
load to complete and then release the object if it is no longer desired.

### [XPLMLookupObjects](/sdk/XPLMLookupObjects/)

```cpp
XPLM_API int        XPLMLookupObjects(
                         const char *         inPath,
                         float                inLatitude,
                         float                inLongitude,
                         XPLMLibraryEnumerator_f enumerator,
                         void *               ref);

```

This routine looks up a virtual path in the library system and returns all
matching elements. You provide a callback - one virtual path may match many
objects in the library.[XPLMLookupObjects](/sdk/XPLMLookupObjects/)returns the
number of objects found.

The latitude and longitude parameters specify the location the object will be
used. The library system allows for scenery packages to only provide objects to
certain local locations. Only objects that are allowed at the latitude/longitude
you provide will be returned.

### [XPLMObjectLoaded_f](/sdk/XPLMObjectLoaded_f/)

```cpp
typedef void (* XPLMObjectLoaded_f)(
                         XPLMObjectRef        inObject,
                         void *               inRefcon);

```

You provide this callback when loading an object asynchronously; it will be
called once the object is loaded. Your refcon is passed back. The object ref
passed in is the newly loaded object (ready for use) or NULL if an error
occured.

If your plugin is disabled, this callback will be delivered as soon as the
plugin is re-enabled. If your plugin is unloaded before this callback is ever
called, the SDK will release the object handle for you.

### [XPLMObjectRef](/sdk/XPLMObjectRef/)

```cpp
typedef void * XPLMObjectRef;
```

An[XPLMObjectRef](/sdk/XPLMObjectRef/)is a opaque handle to an .obj file that
has been loaded into memory.

### [XPLMSetAircraftModel](/sdk/XPLMSetAircraftModel/)

```cpp
XPLM_API void       XPLMSetAircraftModel(
                         int                  inIndex,
                         const char *         inAircraftPath);

```

This routine loads an aircraft model. It may only be called if you have
exclusive access to the airplane APIs. Pass in the path of the model with the
.acf extension. The index is zero based, but you may not pass in 0
(use[XPLMSetUsersAircraft](/sdk/XPLMSetUsersAircraft/)to load the user’s
aircracft).

### [XPLMUnloadObject](/sdk/XPLMUnloadObject/)

```cpp
XPLM_API void       XPLMUnloadObject(
                         XPLMObjectRef        inObject);

```

This routine marks an object as no longer being used by your plugin. Objects are
reference counted: once no plugins are using an object, it is purged from
memory. Make sure to call[XPLMUnloadObject](/sdk/XPLMUnloadObject/)once for each
successful call to[XPLMLoadObject](/sdk/XPLMLoadObject/).

| |
| --- | --- |
| [xpCustomObject](/sdk/xpCustomObject/) | "14" |

| |  |
| --- | --- | --- |
| [xpElement_CustomObject](/sdk/xpElement_CustomObject/) | "37" | none any |

| |  |
| --- | --- | --- |
| [xpProperty_Object](/sdk/xpProperty_Object/) | "5" | Is there a C++ object attached to this widget? |

| |  |
| --- | --- | --- |
| [xplm_FlightLoop_Phase_AfterFlightModel](/sdk/xplm_FlightLoop_Phase_AfterFlightModel/) | "1" | Your callback runs after X-Plane integrates the flight model. |

| |  |
| --- | --- | --- |
| [xplm_FlightLoop_Phase_BeforeFlightModel](/sdk/xplm_FlightLoop_Phase_BeforeFlightModel/) | "0" | Your callback runs before X-Plane integrates the flight model. |

| |  |
| --- | --- | --- |
| [xplm_Phase_Objects](/sdk/xplm_Phase_Objects/) | "20" | Deprecated as of XPLM302. 3-d objects (houses, smokestacks, etc. |

