---
title: "Planes APIs"
description: "X-Plane SDK Planes APIs documentation"
category: "XPLM_Planes"
date: "2025-06-24T17:34:11.204012"
---

# Planes APIs

### [XPLMAcquirePlanes](/sdk/XPLMAcquirePlanes/)

```cpp
XPLM_API int        XPLMAcquirePlanes(
                         char **              inAircraft,    /* Can be NULL */
                         XPLMPlanesAvailable_f inCallback,
                         void *               inRefcon);

```

[XPLMAcquirePlanes](/sdk/XPLMAcquirePlanes/)grants your plugin exclusive access
to the aircraft. It returns 1 if you gain access, 0 if you do not.

inAircraft - pass in an array of pointers to strings specifying the planes you
want loaded. For any plane index you do not want loaded, pass a 0-length string.
Other strings should be full paths with the .acf extension. NULL terminates this
array, or pass NULL if there are no planes you want loaded.

If you pass in a callback and do not receive access to the planes your callback
will be called when the airplanes are available. If you do receive airplane
access, your callback will not be called.

### [XPLMCountAircraft](/sdk/XPLMCountAircraft/)

```cpp
XPLM_API void       XPLMCountAircraft(
                         int *                outTotalAircraft,
                         int *                outActiveAircraft,
                         XPLMPluginID *       outController);

```

This function returns the number of aircraft X-Plane is capable of having, as
well as the number of aircraft that are currently active. These numbers count
the user’s aircraft. It can also return the plugin that is currently controlling
aircraft. In X-Plane 7, this routine reflects the number of aircraft the user
has enabled in the rendering options window.

### [XPLMDisableAIForPlane](/sdk/XPLMDisableAIForPlane/)

```cpp
XPLM_API void       XPLMDisableAIForPlane(
                         int                  inPlaneIndex);

```

This routine turns off X-Plane’s AI for a given plane. The plane will continue
to draw and be a real plane in X-Plane, but will not move itself.

# [XPLMPlanes](/sdk/XPLMPlanes/)API

The[XPLMPlanes](/sdk/XPLMPlanes/)APIs allow you to control the various aircraft
in X-Plane, both the user’s and the sim’s.

*Note*: unlike almost all other APIs in the SDK, aircraft paths are*full*file
system paths for historical reasons. You’ll need to prefix all relative paths
with the X-Plane path as accessed
via[XPLMGetSystemPath](/sdk/XPLMGetSystemPath/).

## USER AIRCRAFT ACCESS

### [XPLMSetUsersAircraft](/sdk/XPLMSetUsersAircraft/)

```cpp
XPLM_API void       XPLMSetUsersAircraft(
                         const char *         inAircraftPath);

```

This routine changes the user’s aircraft. Note that this will reinitialize the
user to be on the nearest airport’s first runway. Pass in a full path (hard
drive and everything including the .acf extension) to the .acf file.

### [XPLMPlaceUserAtAirport](/sdk/XPLMPlaceUserAtAirport/)

```cpp
XPLM_API void       XPLMPlaceUserAtAirport(
                         const char *         inAirportCode);

```

This routine places the user at a given airport. Specify the airport by its
X-Plane airport ID (e.g. ‘KBOS’).

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

## GLOBAL AIRCRAFT ACCESS

### [XPLM_USER_AIRCRAFT](/sdk/XPLM_USER_AIRCRAFT/)

```cpp
#define XPLM_USER_AIRCRAFT   0
```

The user’s aircraft is always index 0.

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

### [XPLMCountAircraft](/sdk/XPLMCountAircraft/)

```cpp
XPLM_API void       XPLMCountAircraft(
                         int *                outTotalAircraft,
                         int *                outActiveAircraft,
                         XPLMPluginID *       outController);

```

This function returns the number of aircraft X-Plane is capable of having, as
well as the number of aircraft that are currently active. These numbers count
the user’s aircraft. It can also return the plugin that is currently controlling
aircraft. In X-Plane 7, this routine reflects the number of aircraft the user
has enabled in the rendering options window.

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

## EXCLUSIVE AIRCRAFT ACCESS

The following routines require exclusive access to the airplane APIs. Only one
plugin may have this access at a time.

### [XPLMPlanesAvailable_f](/sdk/XPLMPlanesAvailable_f/)

```cpp
typedef void (* XPLMPlanesAvailable_f)(
                         void *               inRefcon);

```

Your airplanes available callback is called when another plugin gives up access
to the multiplayer planes. Use this to wait for access to multiplayer.

### [XPLMAcquirePlanes](/sdk/XPLMAcquirePlanes/)

```cpp
XPLM_API int        XPLMAcquirePlanes(
                         char **              inAircraft,    /* Can be NULL */
                         XPLMPlanesAvailable_f inCallback,
                         void *               inRefcon);

```

[XPLMAcquirePlanes](/sdk/XPLMAcquirePlanes/)grants your plugin exclusive access
to the aircraft. It returns 1 if you gain access, 0 if you do not.

inAircraft - pass in an array of pointers to strings specifying the planes you
want loaded. For any plane index you do not want loaded, pass a 0-length string.
Other strings should be full paths with the .acf extension. NULL terminates this
array, or pass NULL if there are no planes you want loaded.

If you pass in a callback and do not receive access to the planes your callback
will be called when the airplanes are available. If you do receive airplane
access, your callback will not be called.

### [XPLMReleasePlanes](/sdk/XPLMReleasePlanes/)

```cpp
XPLM_API void       XPLMReleasePlanes(void);

```

Call this function to release access to the planes. Note that if you are
disabled, access to planes is released for you and you must reacquire it.

### [XPLMSetActiveAircraftCount](/sdk/XPLMSetActiveAircraftCount/)

```cpp
XPLM_API void       XPLMSetActiveAircraftCount(
                         int                  inCount);

```

This routine sets the number of active planes. If you pass in a number higher
than the total number of planes availables, only the total number of planes
available is actually used.

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

### [XPLMDisableAIForPlane](/sdk/XPLMDisableAIForPlane/)

```cpp
XPLM_API void       XPLMDisableAIForPlane(
                         int                  inPlaneIndex);

```

This routine turns off X-Plane’s AI for a given plane. The plane will continue
to draw and be a real plane in X-Plane, but will not move itself.

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

### [XPLMReinitUsersPlane](/sdk/XPLMReinitUsersPlane/)

```cpp
XPLM_API void       XPLMReinitUsersPlane(void);

```

WARNING: DO NOT USE.
Use[XPLMPlaceUserAtAirport](/sdk/XPLMPlaceUserAtAirport/)or[XPLMPlaceUserAtLocation](/sdk/XPLMPlaceUserAtLocation/).

This function recomputes the derived flight model data from the aircraft
structure in memory. If you have used the data access layer to modify the
aircraft structure, use this routine to resynchronize X-Plane; since X-Plane
works at least partly from derived values, the sim will not behave properly
until this is called.

WARNING: this routine does not necessarily place the airplane at the airport;
use[XPLMSetUsersAircraft](/sdk/XPLMSetUsersAircraft/)to be compatible. This
routine is provided to do special experimentation with flight models without
resetting flight.

### [XPLMPlanesAvailable_f](/sdk/XPLMPlanesAvailable_f/)

```cpp
typedef void (* XPLMPlanesAvailable_f)(
                         void *               inRefcon);

```

Your airplanes available callback is called when another plugin gives up access
to the multiplayer planes. Use this to wait for access to multiplayer.

### [XPLMReinitUsersPlane](/sdk/XPLMReinitUsersPlane/)

```cpp
XPLM_API void       XPLMReinitUsersPlane(void);

```

WARNING: DO NOT USE.
Use[XPLMPlaceUserAtAirport](/sdk/XPLMPlaceUserAtAirport/)or[XPLMPlaceUserAtLocation](/sdk/XPLMPlaceUserAtLocation/).

This function recomputes the derived flight model data from the aircraft
structure in memory. If you have used the data access layer to modify the
aircraft structure, use this routine to resynchronize X-Plane; since X-Plane
works at least partly from derived values, the sim will not behave properly
until this is called.

WARNING: this routine does not necessarily place the airplane at the airport;
use[XPLMSetUsersAircraft](/sdk/XPLMSetUsersAircraft/)to be compatible. This
routine is provided to do special experimentation with flight models without
resetting flight.

### [XPLMReleasePlanes](/sdk/XPLMReleasePlanes/)

```cpp
XPLM_API void       XPLMReleasePlanes(void);

```

Call this function to release access to the planes. Note that if you are
disabled, access to planes is released for you and you must reacquire it.

### [XPLMSetActiveAircraftCount](/sdk/XPLMSetActiveAircraftCount/)

```cpp
XPLM_API void       XPLMSetActiveAircraftCount(
                         int                  inCount);

```

This routine sets the number of active planes. If you pass in a number higher
than the total number of planes availables, only the total number of planes
available is actually used.

### [XPLMSetUsersAircraft](/sdk/XPLMSetUsersAircraft/)

```cpp
XPLM_API void       XPLMSetUsersAircraft(
                         const char *         inAircraftPath);

```

This routine changes the user’s aircraft. Note that this will reinitialize the
user to be on the nearest airport’s first runway. Pass in a full path (hard
drive and everything including the .acf extension) to the .acf file.

### [XPLM_MSG_AIRPLANE_COUNT_CHANGED](/sdk/XPLM_MSG_AIRPLANE_COUNT_CHANGED/)

```cpp
#define XPLM_MSG_AIRPLANE_COUNT_CHANGED 105
```

This message is sent whenever the user adjusts the number of X-Plane aircraft
models. You must use XPLMCountPlanes to find out how many planes are now
available. This message will only be sent in XP7 and higher because in XP6 the
number of aircraft is not user-adjustable. The parameter is ignored.

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

### [XPLM_MSG_PLANE_UNLOADED](/sdk/XPLM_MSG_PLANE_UNLOADED/)

```cpp
#define XPLM_MSG_PLANE_UNLOADED 106
```

This message is sent to your plugin whenever a plane is unloaded. The parameter
contains the index number of the plane being unloaded; 0 indicates the user’s
plane. The parameter is of type int, passed as the value of the pointer. (That
is: the parameter is an int, not a pointer to an int.)

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

### [XPLM_PLUGIN_XPLANE](/sdk/XPLM_PLUGIN_XPLANE/)

```cpp
#define XPLM_PLUGIN_XPLANE   (0)
```

X-Plane itself

### [XPLM_USER_AIRCRAFT](/sdk/XPLM_USER_AIRCRAFT/)

```cpp
#define XPLM_USER_AIRCRAFT   0
```

The user’s aircraft is always index 0.

| |
| --- | --- |
| [xpAircraftCarrier](/sdk/xpAircraftCarrier/) | "11" |

| |  |
| --- | --- | --- |
| [xpElement_AircraftCarrier](/sdk/xpElement_AircraftCarrier/) | "34" | none any |

| |
| --- | --- |
| [xplm_Host_PlaneMaker](/sdk/xplm_Host_PlaneMaker/) | "2" |

| |
| --- | --- |
| [xplm_Host_XPlane](/sdk/xplm_Host_XPlane/) | "1" |

| |  |
| --- | --- | --- |
| [xplm_Phase_Airplanes](/sdk/xplm_Phase_Airplanes/) | "25" | Deprecated as of XPLM302. External views of airplanes, both yours and the AI aircraft. |

| |  |
| --- | --- | --- |
| [xplm_Tex_AircraftPaint](/sdk/xplm_Tex_AircraftPaint/) | "1" | The exterior paint for the user's aircraft (daytime). |

