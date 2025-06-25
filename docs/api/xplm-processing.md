---
title: "Processing APIs"
description: "X-Plane SDK Processing APIs documentation"
category: "XPLM_Processing"
date: "2025-06-25T15:45:56.661425"
---

# Processing APIs

### [XPAddWidgetCallback](/sdk/XPAddWidgetCallback/)

```cpp
WIDGET_API void       XPAddWidgetCallback(
                         XPWidgetID           inWidget,
                         XPWidgetFunc_t       inNewCallback);

```

This function adds a new widget callback to a widget. This widget callback
supercedes any existing ones and will receive messages first; if it does not
handle messages they will go on to be handled by pre-existing widgets.

The widget function will remain on the widget for the life of the widget. The
creation message will be sent to the new callback immediately with the widget
ID, and the destruction message will be sent before the other widget function
receives a destruction message.

This provides a way to ‘subclass’ an existing widget. By providing a second hook
that only handles certain widget messages, you can customize or extend widget
behavior.

### [XPLMAvionicsBezelCallback_f](/sdk/XPLMAvionicsBezelCallback_f/)

```cpp
typedef void (* XPLMAvionicsBezelCallback_f)(
                         float                inAmbiantR,
                         float                inAmbiantG,
                         float                inAmbiantB,
                         void *               inRefcon);

```

This is the prototype for drawing callbacks for custom devices' bezel. You are
passed in the red, green, and blue values you can optinally use for tinting your
bezel accoring to ambiant light.

Refcon is a unique value that you specify when creating the device, allowing you
to slip a pointer to your own data to the callback.

Upon entry the OpenGL context will be correctly set up for you and OpenGL will
be in panel coordinates for 2d drawing. The OpenGL state (texturing, etc.) will
be unknown.

### [XPLMAvionicsCallback_f](/sdk/XPLMAvionicsCallback_f/)

```cpp
typedef int (* XPLMAvionicsCallback_f)(
                         XPLMDeviceID         inDeviceID,
                         int                  inIsBefore,
                         void *               inRefcon);

```

This is the prototype for drawing callbacks for customized built-in device. You
are passed in the device you are enhancing/replacing, and (if this is used for a
built-in device that you are customizing) whether it is before or after X-Plane
drawing. If you are before X-Plane, return 1 to let X-Plane draw or 0 to
suppress X-Plane drawing. If you are called after X-Plane, the return value is
ignored.

Refcon is a unique value that you specify when registering the callback,
allowing you to slip a pointer to your own data to the callback.

Upon entry the OpenGL context will be correctly set up for you and OpenGL will
be in panel coordinates for 2d drawing. The OpenGL state (texturing, etc.) will
be unknown.

### [XPLMCommandCallback_f](/sdk/XPLMCommandCallback_f/)

```cpp
typedef int (* XPLMCommandCallback_f)(
                         XPLMCommandRef       inCommand,
                         XPLMCommandPhase     inPhase,
                         void *               inRefcon);

```

A command callback is a function in your plugin that is called when a command is
pressed. Your callback receives the command reference for the particular
command, the phase of the command that is executing, and a reference pointer
that you specify when registering the callback.

Your command handler should return 1 to let processing of the command continue
to other plugins and X-Plane, or 0 to halt processing, potentially bypassing
X-Plane code.

### [XPLMCreateFlightLoop](/sdk/XPLMCreateFlightLoop/)

```cpp
XPLM_API XPLMFlightLoopID XPLMCreateFlightLoop(
                         XPLMCreateFlightLoop_t * inParams);

```

This routine creates a flight loop callback and returns its ID. The flight loop
callback is created using the input param struct, and is inited to be
unscheduled.

### [XPLMCreateFlightLoop_t](/sdk/XPLMCreateFlightLoop_t/)

[XPLMCreateFlightLoop_t](/sdk/XPLMCreateFlightLoop_t/)contains the parameters to
create a new flight loop callback. The structure may be expanded in future SDKs
- always set structSize to the size of your structure in bytes.

```cpp
typedef struct {
     int                       structSize;
     XPLMFlightLoopPhaseType   phase;
     XPLMFlightLoop_f          callbackFunc;
     void *                    refcon;
} XPLMCreateFlightLoop_t;
```

### [XPLMDestroyFlightLoop](/sdk/XPLMDestroyFlightLoop/)

```cpp
XPLM_API void       XPLMDestroyFlightLoop(
                         XPLMFlightLoopID     inFlightLoopID);

```

This routine destroys a flight loop callback by ID. Only call it on flight loops
created with the newer[XPLMCreateFlightLoop](/sdk/XPLMCreateFlightLoop/)API.

### [XPLMFlightLoopID](/sdk/XPLMFlightLoopID/)

```cpp
typedef void * XPLMFlightLoopID;
```

This is an opaque identifier for a flight loop callback. You can use this
identifier to easily track and remove your callbacks, or to use the new flight
loop APIs.

### [XPLMFlightLoopPhaseType](/sdk/XPLMFlightLoopPhaseType/)

You can register a flight loop callback to run either before or after the flight
model is integrated by X-Plane.

| Name | Value | Description |
| --- | --- | --- |
|
[xplm_FlightLoop_Phase_BeforeFlightModel](/sdk/xplm_FlightLoop_Phase_BeforeFlightModel/)
| "0" | Your callback runs before X-Plane integrates the flight model. |
|
[xplm_FlightLoop_Phase_AfterFlightModel](/sdk/xplm_FlightLoop_Phase_AfterFlightModel/)
| "1" | Your callback runs after X-Plane integrates the flight model. |

### [XPLMFlightLoop_f](/sdk/XPLMFlightLoop_f/)

```cpp
typedef float (* XPLMFlightLoop_f)(
                         float                inElapsedSinceLastCall,
                         float                inElapsedTimeSinceLastFlightLoop,
                         int                  inCounter,
                         void *               inRefcon);

```

This is your flight loop callback. Each time the flight loop is iterated
through, you receive this call at the end.

Flight loop callbacks receive a number of input timing parameters. These input
timing parameters are not particularly useful; you may need to track your own
timing data (e.g. by reading datarefs). The input parameters are:

- inElapsedSinceLastCall: the wall time since your last callback.
- inElapsedTimeSinceLastFlightLoop: the wall time since any flight loop was dispatched.
- inCounter: a monotonically increasing counter, bumped once per flight loop dispatch from the sim.
- inRefcon: your own pointer constant provided when you registered yor callback.

Your return value controls when you will next be called.

- Return 0 to stop receiving callbacks.
- Return a positive number to specify how many seconds until the next callback. (You will be called at or after this time, not before.)
- Return a negative number to specify how many loops must go by until you are called. For example, -1.0 means call me the very next loop.

Try to run your flight loop as infrequently as is practical, and suspend it
(using return value 0) when you do not need it; lots of flight loop callbacks
that do nothing lowers X-Plane’s frame rate.

Your callback will NOT be unregistered if you return 0; it will merely be
inactive.

# [XPLMProcessing](/sdk/XPLMProcessing/)API

This API allows you to get regular callbacks during the flight loop, the part of
X-Plane where the plane’s position calculates the physics of flight, etc. Use
these APIs to accomplish periodic tasks like logging data and performing I/O.

You can receive a callback either just before or just after the per-frame
physics calculations happen - you can use post-flightmodel callbacks to “patch”
the flight model after it has run.

If the user has set the number of flight model iterations per frame greater than
one your plugin will*not*see this; these integrations run on the sub-section of
the flight model where iterations improve responsiveness (e.g. physical
integration, not simple systems tracking) and are thus opaque to plugins.

Flight loop scheduling, when scheduled by time, is scheduled by a “first
callback after the deadline” schedule, e.g. your callbacks will always be
slightly late to ensure that we don’t run faster than your deadline.

WARNING: Do NOT use these callbacks to draw! You cannot draw during flight loop
callbacks. Use the drawing callbacks (see[XPLMDisplay](/sdk/XPLMDisplay/)for
more info) for graphics or the[XPLMInstance](/sdk/XPLMInstance/)functions for
aircraft or models. (One exception: you can use a post-flight loop callback to
update your own off-screen FBOs.)

## FLIGHT LOOP CALLBACKS

### [XPLMFlightLoopPhaseType](/sdk/XPLMFlightLoopPhaseType/)

You can register a flight loop callback to run either before or after the flight
model is integrated by X-Plane.

| Name | Value | Description |
| --- | --- | --- |
|
[xplm_FlightLoop_Phase_BeforeFlightModel](/sdk/xplm_FlightLoop_Phase_BeforeFlightModel/)
| "0" | Your callback runs before X-Plane integrates the flight model. |
|
[xplm_FlightLoop_Phase_AfterFlightModel](/sdk/xplm_FlightLoop_Phase_AfterFlightModel/)
| "1" | Your callback runs after X-Plane integrates the flight model. |

### [XPLMFlightLoopID](/sdk/XPLMFlightLoopID/)

```cpp
typedef void * XPLMFlightLoopID;
```

This is an opaque identifier for a flight loop callback. You can use this
identifier to easily track and remove your callbacks, or to use the new flight
loop APIs.

### [XPLMFlightLoop_f](/sdk/XPLMFlightLoop_f/)

```cpp
typedef float (* XPLMFlightLoop_f)(
                         float                inElapsedSinceLastCall,
                         float                inElapsedTimeSinceLastFlightLoop,
                         int                  inCounter,
                         void *               inRefcon);

```

This is your flight loop callback. Each time the flight loop is iterated
through, you receive this call at the end.

Flight loop callbacks receive a number of input timing parameters. These input
timing parameters are not particularly useful; you may need to track your own
timing data (e.g. by reading datarefs). The input parameters are:

- inElapsedSinceLastCall: the wall time since your last callback.
- inElapsedTimeSinceLastFlightLoop: the wall time since any flight loop was dispatched.
- inCounter: a monotonically increasing counter, bumped once per flight loop dispatch from the sim.
- inRefcon: your own pointer constant provided when you registered yor callback.

Your return value controls when you will next be called.

- Return 0 to stop receiving callbacks.
- Return a positive number to specify how many seconds until the next callback. (You will be called at or after this time, not before.)
- Return a negative number to specify how many loops must go by until you are called. For example, -1.0 means call me the very next loop.

Try to run your flight loop as infrequently as is practical, and suspend it
(using return value 0) when you do not need it; lots of flight loop callbacks
that do nothing lowers X-Plane’s frame rate.

Your callback will NOT be unregistered if you return 0; it will merely be
inactive.

### [XPLMCreateFlightLoop_t](/sdk/XPLMCreateFlightLoop_t/)

[XPLMCreateFlightLoop_t](/sdk/XPLMCreateFlightLoop_t/)contains the parameters to
create a new flight loop callback. The structure may be expanded in future SDKs
- always set structSize to the size of your structure in bytes.

```cpp
typedef struct {
     int                       structSize;
     XPLMFlightLoopPhaseType   phase;
     XPLMFlightLoop_f          callbackFunc;
     void *                    refcon;
} XPLMCreateFlightLoop_t;
```

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

### [XPLMGetCycleNumber](/sdk/XPLMGetCycleNumber/)

```cpp
XPLM_API int        XPLMGetCycleNumber(void);

```

This routine returns a counter starting at zero for each sim cycle
computed/video frame rendered.

### [XPLMRegisterFlightLoopCallback](/sdk/XPLMRegisterFlightLoopCallback/)

```cpp
XPLM_API void       XPLMRegisterFlightLoopCallback(
                         XPLMFlightLoop_f     inFlightLoop,
                         float                inInterval,
                         void *               inRefcon);

```

This routine registers your flight loop callback. Pass in a pointer to a flight
loop function and a refcon (an optional reference value determined by you).
inInterval defines when you will be called. Pass in a positive number to specify
seconds from registration time to the next callback. Pass in a negative number
to indicate when you will be called (e.g. pass -1 to be called at the next
cylcle). Pass 0 to not be called; your callback will be inactive.

(This legacy function only installs pre-flight-loop callbacks;
use[XPLMCreateFlightLoop](/sdk/XPLMCreateFlightLoop/)for more control.)

### [XPLMUnregisterFlightLoopCallback](/sdk/XPLMUnregisterFlightLoopCallback/)

```cpp
XPLM_API void       XPLMUnregisterFlightLoopCallback(
                         XPLMFlightLoop_f     inFlightLoop,
                         void *               inRefcon);

```

This routine unregisters your flight loop callback. Do NOT call it from your
flight loop callback. Once your flight loop callback is unregistered, it will
not be called again.

Only use this on flight loops registered
via[XPLMRegisterFlightLoopCallback](/sdk/XPLMRegisterFlightLoopCallback/).

### [XPLMSetFlightLoopCallbackInterval](/sdk/XPLMSetFlightLoopCallbackInterval/)

```cpp
XPLM_API void       XPLMSetFlightLoopCallbackInterval(
                         XPLMFlightLoop_f     inFlightLoop,
                         float                inInterval,
                         int                  inRelativeToNow,
                         void *               inRefcon);

```

This routine sets when a callback will be called. Do NOT call it from your
callback; use the return value of the callback to change your callback interval
from inside your callback.

inInterval is formatted the same way as
in[XPLMRegisterFlightLoopCallback](/sdk/XPLMRegisterFlightLoopCallback/);
positive for seconds, negative for cycles, and 0 for deactivating the callback.
If inRelativeToNow is 1, times are from the time of this call; otherwise they
are from the time the callback was last called (or the time it was registered if
it has never been called.

### [XPLMCreateFlightLoop](/sdk/XPLMCreateFlightLoop/)

```cpp
XPLM_API XPLMFlightLoopID XPLMCreateFlightLoop(
                         XPLMCreateFlightLoop_t * inParams);

```

This routine creates a flight loop callback and returns its ID. The flight loop
callback is created using the input param struct, and is inited to be
unscheduled.

### [XPLMDestroyFlightLoop](/sdk/XPLMDestroyFlightLoop/)

```cpp
XPLM_API void       XPLMDestroyFlightLoop(
                         XPLMFlightLoopID     inFlightLoopID);

```

This routine destroys a flight loop callback by ID. Only call it on flight loops
created with the newer[XPLMCreateFlightLoop](/sdk/XPLMCreateFlightLoop/)API.

### [XPLMScheduleFlightLoop](/sdk/XPLMScheduleFlightLoop/)

```cpp
XPLM_API void       XPLMScheduleFlightLoop(
                         XPLMFlightLoopID     inFlightLoopID,
                         float                inInterval,
                         int                  inRelativeToNow);

```

This routine schedules a flight loop callback for future execution. If
inInterval is negative, it is run in a certain number of frames based on the
absolute value of the input. If the interval is positive, it is a duration in
seconds.

If inRelativeToNow is true, times are interpreted relative to the time this
routine is called; otherwise they are relative to the last call time or the time
the flight loop was registered (if never called).

### [XPLMRegisterAvionicsCallbacksEx](/sdk/XPLMRegisterAvionicsCallbacksEx/)

```cpp
XPLM_API XPLMAvionicsID XPLMRegisterAvionicsCallbacksEx(
                         XPLMCustomizeAvionics_t * inParams);

```

This routine registers your callbacks for a built-in device. This returns a
handle. If the returned handle is NULL, there was a problem interpreting your
input, most likely the struct size was wrong for your SDK version. If the
returned handle is not NULL, your callbacks will be called according to schedule
as long as your plugin is not deactivated, or unloaded, or you
call[XPLMUnregisterAvionicsCallbacks](/sdk/XPLMUnregisterAvionicsCallbacks/)().

Note that you cannot register new callbacks for a device that is not a built-in
one (for example a device that you have created, or a device another plugin has
created).

### [XPLMRegisterFlightLoopCallback](/sdk/XPLMRegisterFlightLoopCallback/)

```cpp
XPLM_API void       XPLMRegisterFlightLoopCallback(
                         XPLMFlightLoop_f     inFlightLoop,
                         float                inInterval,
                         void *               inRefcon);

```

This routine registers your flight loop callback. Pass in a pointer to a flight
loop function and a refcon (an optional reference value determined by you).
inInterval defines when you will be called. Pass in a positive number to specify
seconds from registration time to the next callback. Pass in a negative number
to indicate when you will be called (e.g. pass -1 to be called at the next
cylcle). Pass 0 to not be called; your callback will be inactive.

(This legacy function only installs pre-flight-loop callbacks;
use[XPLMCreateFlightLoop](/sdk/XPLMCreateFlightLoop/)for more control.)

### [XPLMScheduleFlightLoop](/sdk/XPLMScheduleFlightLoop/)

```cpp
XPLM_API void       XPLMScheduleFlightLoop(
                         XPLMFlightLoopID     inFlightLoopID,
                         float                inInterval,
                         int                  inRelativeToNow);

```

This routine schedules a flight loop callback for future execution. If
inInterval is negative, it is run in a certain number of frames based on the
absolute value of the input. If the interval is positive, it is a duration in
seconds.

If inRelativeToNow is true, times are interpreted relative to the time this
routine is called; otherwise they are relative to the last call time or the time
the flight loop was registered (if never called).

### [XPLMSetErrorCallback](/sdk/XPLMSetErrorCallback/)

```cpp
XPLM_API void       XPLMSetErrorCallback(
                         XPLMError_f          inCallback);

```

[XPLMSetErrorCallback](/sdk/XPLMSetErrorCallback/)installs an error-reporting
callback for your plugin. Normally the plugin system performs minimum
diagnostics to maximize performance. When you install an error callback, you
will receive calls due to certain plugin errors, such as passing bad parameters
or incorrect data.

Important: the error callback determines*programming*errors, e.g. bad API
parameters. Every error that is returned by the error callback represents a
mistake in your plugin that you should fix. Error callbacks are not used to
report expected run-time problems (e.g. disk I/O errors).

The intention is for you to install the error callback during debug sections and
put a break-point inside your callback. This will cause you to break into the
debugger from within the SDK at the point in your plugin where you made an
illegal call.

Installing an error callback may activate error checking code that would not
normally run, and this may adversely affect performance, so do not leave error
callbacks installed in shipping plugins. Since the only useful response to an
error is to change code, error callbacks are not useful “in the field”.

### [XPLMSetFlightLoopCallbackInterval](/sdk/XPLMSetFlightLoopCallbackInterval/)

```cpp
XPLM_API void       XPLMSetFlightLoopCallbackInterval(
                         XPLMFlightLoop_f     inFlightLoop,
                         float                inInterval,
                         int                  inRelativeToNow,
                         void *               inRefcon);

```

This routine sets when a callback will be called. Do NOT call it from your
callback; use the return value of the callback to change your callback interval
from inside your callback.

inInterval is formatted the same way as
in[XPLMRegisterFlightLoopCallback](/sdk/XPLMRegisterFlightLoopCallback/);
positive for seconds, negative for cycles, and 0 for deactivating the callback.
If inRelativeToNow is 1, times are from the time of this call; otherwise they
are from the time the callback was last called (or the time it was registered if
it has never been called.

### [XPLMUnregisterAvionicsCallbacks](/sdk/XPLMUnregisterAvionicsCallbacks/)

```cpp
XPLM_API void       XPLMUnregisterAvionicsCallbacks(
                         XPLMAvionicsID       inAvionicsId);

```

This routine unregisters your callbacks for a built-in device. You should only
call this for handles you acquired
from[XPLMRegisterAvionicsCallbacksEx](/sdk/XPLMRegisterAvionicsCallbacksEx/)().
They will no longer be called.

### [XPLMUnregisterFlightLoopCallback](/sdk/XPLMUnregisterFlightLoopCallback/)

```cpp
XPLM_API void       XPLMUnregisterFlightLoopCallback(
                         XPLMFlightLoop_f     inFlightLoop,
                         void *               inRefcon);

```

This routine unregisters your flight loop callback. Do NOT call it from your
flight loop callback. Once your flight loop callback is unregistered, it will
not be called again.

Only use this on flight loops registered
via[XPLMRegisterFlightLoopCallback](/sdk/XPLMRegisterFlightLoopCallback/).

| |  |
| --- | --- | --- |
| [xpMode_DirectAllCallbacks](/sdk/xpMode_DirectAllCallbacks/) | "3" | The message is sent just to the target, but goes to every callback, even if it is handled. |

| |  |
| --- | --- | --- |
| [xplmFont_Timer](/sdk/xplmFont_Timer /) | "14" | Deprecated, do not use. |

