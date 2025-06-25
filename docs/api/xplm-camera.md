---
title: "Camera APIs"
description: "X-Plane SDK Camera APIs documentation"
category: "XPLM_Camera"
date: "2025-06-25T15:45:56.655424"
---

# Camera APIs

### [XPLMCameraControlDuration](/sdk/XPLMCameraControlDuration/)

This enumeration states how long you want to retain control of the camera. You
can retain it indefinitely or until the user selects a new view.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_ControlCameraUntilViewChanges](/sdk/xplm_ControlCameraUntilViewChanges/)
| "1" | Control the camera until the user picks a new view. |
| [xplm_ControlCameraForever](/sdk/xplm_ControlCameraForever/) | "2" | Control
the camera until your plugin is disabled or another plugin forcibly takes
control. |

### [XPLMCameraControl_f](/sdk/XPLMCameraControl_f/)

```cpp
typedef int (* XPLMCameraControl_f)(
                         XPLMCameraPosition_t * outCameraPosition,    /* Can be NULL */
                         int                  inIsLosingControl,
                         void *               inRefcon);

```

You use an XPLMCameraControl function to provide continuous control over the
camera. You are passed a structure in which to put the new camera position;
modify it and return 1 to reposition the camera. Return 0 to surrender control
of the camera; camera control will be handled by X-Plane on this draw loop. The
contents of the structure as you are called are undefined.

If X-Plane is taking camera control away from you, this function will be called
with inIsLosingControl set to 1 and ioCameraPosition NULL.

### [XPLMCameraPosition_t](/sdk/XPLMCameraPosition_t/)

This structure contains a full specification of the camera. X, Y, and Z are the
camera’s position in OpenGL coordinates; pitch, roll, and yaw are rotations from
a camera facing flat north in degrees. Positive pitch means nose up, positive
roll means roll right, and positive yaw means yaw right, all in degrees. Zoom is
a zoom factor, with 1.0 meaning normal zoom and 2.0 magnifying by 2x (objects
appear larger).

```cpp
typedef struct {
     float                     x;
     float                     y;
     float                     z;
     float                     pitch;
     float                     heading;
     float                     roll;
     float                     zoom;
} XPLMCameraPosition_t;
```

### [XPLMControlCamera](/sdk/XPLMControlCamera/)

```cpp
XPLM_API void       XPLMControlCamera(
                         XPLMCameraControlDuration inHowLong,
                         XPLMCameraControl_f  inControlFunc,
                         void *               inRefcon);

```

This function repositions the camera on the next drawing cycle. You must pass a
non-null control function. Specify in inHowLong how long you’d like control
(indefinitely or until a new view mode is set by the user).

### [XPLMDontControlCamera](/sdk/XPLMDontControlCamera/)

```cpp
XPLM_API void       XPLMDontControlCamera(void);

```

This function stops you from controlling the camera. If you have a camera
control function, it will not be called with an inIsLosingControl flag. X-Plane
will control the camera on the next cycle.

For maximum compatibility you should not use this routine unless you are in
posession of the camera.

### [XPLMIsCameraBeingControlled](/sdk/XPLMIsCameraBeingControlled/)

```cpp
XPLM_API int        XPLMIsCameraBeingControlled(
                         XPLMCameraControlDuration * outCameraControlDuration);    /* Can be NULL */

```

This routine returns 1 if the camera is being controlled, zero if it is not. If
it is and you pass in a pointer to a camera control duration, the current
control duration will be returned.

### [XPLMReadCameraPosition](/sdk/XPLMReadCameraPosition/)

```cpp
XPLM_API void       XPLMReadCameraPosition(
                         XPLMCameraPosition_t * outCameraPosition);

```

This function reads the current camera position.

| |  |
| --- | --- | --- |
| [xpSubWindowStyle_ListView](/sdk/xpSubWindowStyle_ListView/) | "3" | A list view for scrolling lists. |

| |  |
| --- | --- | --- |
| [xpWindow_ListView](/sdk/xpWindow_ListView/) | "5" | A list view within a panel for scrolling file names, etc. |

| |  |
| --- | --- | --- |
| [xplm_ControlCameraForever](/sdk/xplm_ControlCameraForever/) | "2" | Control the camera until your plugin is disabled or another plugin forcibly takes control. |

| |  |
| --- | --- | --- |
| [xplm_ControlCameraUntilViewChanges](/sdk/xplm_ControlCameraUntilViewChanges/) | "1" | Control the camera until the user picks a new view. |

