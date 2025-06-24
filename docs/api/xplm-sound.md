---
title: "Sound APIs"
description: "X-Plane SDK Sound APIs documentation"
category: "XPLM_Sound"
date: "2025-06-24T17:34:11.206518"
---

# Sound APIs

### [XPLMAudioBus](/sdk/XPLMAudioBus/)

This enumeration states the type of audio you wish to play - that is, the part
of the simulated environment that the audio belongs in. If you use FMOD
directly, note that COM1, COM2, Pilot and GND exist in a different FMOD bank so
you may see these channels being unloaded/reloaded independently of the others.
They may also be using a different FMOD::System if the user has selected a
dedicated headset output device.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_AudioRadioCom1](/sdk/xplm_AudioRadioCom1/) | "0" | Incoming speech on
COM1 |
| [xplm_AudioRadioCom2](/sdk/xplm_AudioRadioCom2/) | "1" | Incoming speech on
COM2 |
| [xplm_AudioRadioPilot](/sdk/xplm_AudioRadioPilot/) | "2" | Pilot's own speech
|
| [xplm_AudioRadioCopilot](/sdk/xplm_AudioRadioCopilot/) | "3" | Copilot's own
speech |
| [xplm_AudioExteriorAircraft](/sdk/xplm_AudioExteriorAircraft/) | "4" |
| [xplm_AudioExteriorEnvironment](/sdk/xplm_AudioExteriorEnvironment/) | "5" |
| [xplm_AudioExteriorUnprocessed](/sdk/xplm_AudioExteriorUnprocessed/) | "6" |
| [xplm_AudioInterior](/sdk/xplm_AudioInterior/) | "7" |
| [xplm_AudioUI](/sdk/xplm_AudioUI/) | "8" |
| [xplm_AudioGround](/sdk/xplm_AudioGround/) | "9" | Dedicated ground vehicle
cable |
| [xplm_Master](/sdk/xplm_Master/) | "10" | Master bus. Not normally to be used
directly. |

### [XPLMGetFMODChannelGroup](/sdk/XPLMGetFMODChannelGroup/)

```cpp
XPLM_API FMOD_CHANNELGROUP* XPLMGetFMODChannelGroup(
                         XPLMAudioBus         audioType);

```

Get a reference to a particular channel group - that is, an output channel. See
the table above for values.

### [XPLMGetFMODStudio](/sdk/XPLMGetFMODStudio/)

```cpp
XPLM_API FMOD_STUDIO_SYSTEM* XPLMGetFMODStudio(void);

```

Get a handle to the FMOD Studio, allowing you to load/process whatever else you
need. This also gives access to the underlying system via
FMOD::Studio::System::getCoreSystem() / FMOD_Studio_System_GetCoreSystem() .
When a separate output device is being used for the radio, this will always
return the FMOD::Studio that is running the environment output, as before. If
you want to specifically target the headset output device, you can obtain that
FMOD::Studio by getting one of the radio-specific output channelgroups and using
the getSystem() call on that.

### [XPLMSetAudioCone](/sdk/XPLMSetAudioCone/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioCone(
                         FMOD_CHANNEL*        fmod_channel,
                         float                inside_angle,
                         float                outside_angle,
                         float                outside_volume,
                         FMOD_VECTOR*         orientation);

```

Set a directional cone for an active FMOD channel. The orientation vector is in
local coordinates. This will set the sound to 3D if it is not already.

### [XPLMSetAudioFadeDistance](/sdk/XPLMSetAudioFadeDistance/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioFadeDistance(
                         FMOD_CHANNEL*        fmod_channel,
                         float                min_fade_distance,
                         float                max_fade_distance);

```

Set the minimum and maximum fade distances for a given sound. This is highly
unlikely to be 0 - please see
https://documentation.help/FMOD-Studio-API/FMOD_Sound_Set3DMinMaxDistance.html
for full details. This will set the sound to 3D if it is not already. You can
set a 3D sound back to 2D by passing negative values for both min amd max.

### [XPLMSetAudioPitch](/sdk/XPLMSetAudioPitch/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioPitch(
                         FMOD_CHANNEL*        fmod_channel,
                         float                audio_pitch_hz);

```

Change the current pitch of an active FMOD channel.

### [XPLMSetAudioPosition](/sdk/XPLMSetAudioPosition/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioPosition(
                         FMOD_CHANNEL*        fmod_channel,
                         FMOD_VECTOR*         position,
                         FMOD_VECTOR*         velocity);

```

Move the given audio channel (i.e. a single sound) to a specific location in
local co-ordinates. This will set the sound to 3D if it is not already.

### [XPLMSetAudioVolume](/sdk/XPLMSetAudioVolume/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioVolume(
                         FMOD_CHANNEL*        fmod_channel,
                         float                source_volume);

```

Set the current volume of an active FMOD channel. This should be used to handle
changes in the audio source volume, not for fading with distance. Values from 0
to 1 are normal, above 1 can be used to artificially amplify a sound.

# [XPLMSound](/sdk/XPLMSound/)API

This provides a minimal interface into the FMOD audio system. On the simplest
level, you can request that X-Plane plays an in-memory audio buffer. This will
work without linking to FMOD yourself. If you want to do anything more, such as
modifying the sound, or loading banks and triggering your own events, you can
get a pointer to the FMOD Studio instance.

## FMOD ACCESS

### [XPLMAudioBus](/sdk/XPLMAudioBus/)

This enumeration states the type of audio you wish to play - that is, the part
of the simulated environment that the audio belongs in. If you use FMOD
directly, note that COM1, COM2, Pilot and GND exist in a different FMOD bank so
you may see these channels being unloaded/reloaded independently of the others.
They may also be using a different FMOD::System if the user has selected a
dedicated headset output device.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_AudioRadioCom1](/sdk/xplm_AudioRadioCom1/) | "0" | Incoming speech on
COM1 |
| [xplm_AudioRadioCom2](/sdk/xplm_AudioRadioCom2/) | "1" | Incoming speech on
COM2 |
| [xplm_AudioRadioPilot](/sdk/xplm_AudioRadioPilot/) | "2" | Pilot's own speech
|
| [xplm_AudioRadioCopilot](/sdk/xplm_AudioRadioCopilot/) | "3" | Copilot's own
speech |
| [xplm_AudioExteriorAircraft](/sdk/xplm_AudioExteriorAircraft/) | "4" |
| [xplm_AudioExteriorEnvironment](/sdk/xplm_AudioExteriorEnvironment/) | "5" |
| [xplm_AudioExteriorUnprocessed](/sdk/xplm_AudioExteriorUnprocessed/) | "6" |
| [xplm_AudioInterior](/sdk/xplm_AudioInterior/) | "7" |
| [xplm_AudioUI](/sdk/xplm_AudioUI/) | "8" |
| [xplm_AudioGround](/sdk/xplm_AudioGround/) | "9" | Dedicated ground vehicle
cable |
| [xplm_Master](/sdk/xplm_Master/) | "10" | Master bus. Not normally to be used
directly. |

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

### [XPLMGetFMODStudio](/sdk/XPLMGetFMODStudio/)

```cpp
XPLM_API FMOD_STUDIO_SYSTEM* XPLMGetFMODStudio(void);

```

Get a handle to the FMOD Studio, allowing you to load/process whatever else you
need. This also gives access to the underlying system via
FMOD::Studio::System::getCoreSystem() / FMOD_Studio_System_GetCoreSystem() .
When a separate output device is being used for the radio, this will always
return the FMOD::Studio that is running the environment output, as before. If
you want to specifically target the headset output device, you can obtain that
FMOD::Studio by getting one of the radio-specific output channelgroups and using
the getSystem() call on that.

### [XPLMGetFMODChannelGroup](/sdk/XPLMGetFMODChannelGroup/)

```cpp
XPLM_API FMOD_CHANNELGROUP* XPLMGetFMODChannelGroup(
                         XPLMAudioBus         audioType);

```

Get a reference to a particular channel group - that is, an output channel. See
the table above for values.

### [XPLMPCMComplete_f](/sdk/XPLMPCMComplete_f/)

```cpp
typedef void (* XPLMPCMComplete_f)(
                         void *               inRefcon,
                         FMOD_RESULT          status);

```

If you use[XPLMPlayPCMOnBus](/sdk/XPLMPlayPCMOnBus/)() you may use this optional
callback to find out when the FMOD::Channel is complete, if you need to
deallocate memory for example.

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

### [XPLMStopAudio](/sdk/XPLMStopAudio/)

```cpp
XPLM_API FMOD_RESULT XPLMStopAudio(
                         FMOD_CHANNEL*        fmod_channel);

```

Stop playing an active FMOD channel. If you defined a completion callback, this
will be called. After this, the FMOD::Channel* will no longer be valid and must
not be used in any future calls.

### [XPLMSetAudioPosition](/sdk/XPLMSetAudioPosition/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioPosition(
                         FMOD_CHANNEL*        fmod_channel,
                         FMOD_VECTOR*         position,
                         FMOD_VECTOR*         velocity);

```

Move the given audio channel (i.e. a single sound) to a specific location in
local co-ordinates. This will set the sound to 3D if it is not already.

### [XPLMSetAudioFadeDistance](/sdk/XPLMSetAudioFadeDistance/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioFadeDistance(
                         FMOD_CHANNEL*        fmod_channel,
                         float                min_fade_distance,
                         float                max_fade_distance);

```

Set the minimum and maximum fade distances for a given sound. This is highly
unlikely to be 0 - please see
https://documentation.help/FMOD-Studio-API/FMOD_Sound_Set3DMinMaxDistance.html
for full details. This will set the sound to 3D if it is not already. You can
set a 3D sound back to 2D by passing negative values for both min amd max.

### [XPLMSetAudioVolume](/sdk/XPLMSetAudioVolume/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioVolume(
                         FMOD_CHANNEL*        fmod_channel,
                         float                source_volume);

```

Set the current volume of an active FMOD channel. This should be used to handle
changes in the audio source volume, not for fading with distance. Values from 0
to 1 are normal, above 1 can be used to artificially amplify a sound.

### [XPLMSetAudioPitch](/sdk/XPLMSetAudioPitch/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioPitch(
                         FMOD_CHANNEL*        fmod_channel,
                         float                audio_pitch_hz);

```

Change the current pitch of an active FMOD channel.

### [XPLMSetAudioCone](/sdk/XPLMSetAudioCone/)

```cpp
XPLM_API FMOD_RESULT XPLMSetAudioCone(
                         FMOD_CHANNEL*        fmod_channel,
                         float                inside_angle,
                         float                outside_angle,
                         float                outside_volume,
                         FMOD_VECTOR*         orientation);

```

Set a directional cone for an active FMOD channel. The orientation vector is in
local coordinates. This will set the sound to 3D if it is not already.

### [XPLMStopAudio](/sdk/XPLMStopAudio/)

```cpp
XPLM_API FMOD_RESULT XPLMStopAudio(
                         FMOD_CHANNEL*        fmod_channel);

```

Stop playing an active FMOD channel. If you defined a completion callback, this
will be called. After this, the FMOD::Channel* will no longer be valid and must
not be used in any future calls.

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

| |
| --- | --- |
| [xplm_AudioExteriorAircraft](/sdk/xplm_AudioExteriorAircraft/) | "4" |

| |
| --- | --- |
| [xplm_AudioExteriorEnvironment](/sdk/xplm_AudioExteriorEnvironment/) | "5" |

| |
| --- | --- |
| [xplm_AudioExteriorUnprocessed](/sdk/xplm_AudioExteriorUnprocessed/) | "6" |

| |  |
| --- | --- | --- |
| [xplm_AudioGround](/sdk/xplm_AudioGround/) | "9" | Dedicated ground vehicle cable |

| |
| --- | --- |
| [xplm_AudioInterior](/sdk/xplm_AudioInterior/) | "7" |

| |  |
| --- | --- | --- |
| [xplm_AudioRadioCom1](/sdk/xplm_AudioRadioCom1/) | "0" | Incoming speech on COM1 |

| |  |
| --- | --- | --- |
| [xplm_AudioRadioCom2](/sdk/xplm_AudioRadioCom2/) | "1" | Incoming speech on COM2 |

| |  |
| --- | --- | --- |
| [xplm_AudioRadioCopilot](/sdk/xplm_AudioRadioCopilot/) | "3" | Copilot's own speech |

| |  |
| --- | --- | --- |
| [xplm_AudioRadioPilot](/sdk/xplm_AudioRadioPilot/) | "2" | Pilot's own speech |

| |
| --- | --- |
| [xplm_AudioUI](/sdk/xplm_AudioUI/) | "8" |

