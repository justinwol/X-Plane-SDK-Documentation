---
title: "Data Access APIs"
description: "X-Plane SDK Data Access APIs documentation"
category: "XPLM_DataAccess"
date: "2025-06-24T17:34:11.199009"
---

# Data Access APIs

### [XPLMCanWriteDataRef](/sdk/XPLMCanWriteDataRef/)

```cpp
XPLM_API int        XPLMCanWriteDataRef(
                         XPLMDataRef          inDataRef);

```

Given a dataref, this routine returns true if you can successfully set the data,
false otherwise. Some datarefs are read-only.

NOTE: even if a dataref is marked writable, it may not act writable. This can
happen for datarefs that X-Plane writes to on every frame of simulation. In some
cases, the dataref is writable but you have to set a separate “override” dataref
to 1 to stop X-Plane from writing it.

### [XPLMCountDataRefs](/sdk/XPLMCountDataRefs/)

```cpp
XPLM_API int        XPLMCountDataRefs(void);

```

Returns the total number of datarefs that have been registered in X-Plane.

### [XPLMDataChanged_f](/sdk/XPLMDataChanged_f/)

```cpp
typedef void (* XPLMDataChanged_f)(
                         void *               inRefcon);

```

An[XPLMDataChanged_f](/sdk/XPLMDataChanged_f/)is a callback that the XPLM calls
whenever any other plug-in modifies shared data. A refcon you provide is passed
back to help identify which data is being changed. In response, you may want to
call one of the XPLMGetDataxxx routines to find the new value of the data.

### [XPLMDataFileType](/sdk/XPLMDataFileType/)

These enums define types of data files you can load or unload using the SDK.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_DataFile_Situation](/sdk/xplm_DataFile_Situation/) | "1" | A situation
(.sit) file, which starts off a flight in a given configuration. |
| [xplm_DataFile_ReplayMovie](/sdk/xplm_DataFile_ReplayMovie/) | "2" | A
situation movie (.smo) file, which replays a past flight. |

### [XPLMDataRef](/sdk/XPLMDataRef/)

```cpp
typedef void * XPLMDataRef;
```

A dataref is an opaque handle to data provided by the simulator or another
plugin. It uniquely identifies one variable (or array of variables) over the
lifetime of your plugin. You never hard code these values; you always get them
from[XPLMFindDataRef](/sdk/XPLMFindDataRef/).

### [XPLMDataRefInfo_t](/sdk/XPLMDataRefInfo_t/)

The[XPLMDataRefInfo_t](/sdk/XPLMDataRefInfo_t/)structure contains all of the
information about a single data ref. The structure can be expanded in future SDK
APIs to include more features. Always set the structSize member to the size of
your struct in bytes!

```cpp
typedef struct {
     // Used to inform XPLMGetDatarefInfo() of the SDK version you compiled against; should always be set to sizeof(XPLMDataRefInfo_t)
     int                       structSize;
     // The full name/path of the data ref
     const char *              name;
     XPLMDataTypeID            type;
     // TRUE if the data ref permits writing to it. FALSE if it's read-only.
     int                       writable;
     // The handle to the plugin that registered this dataref.
     XPLMPluginID              owner;
} XPLMDataRefInfo_t;
```

### [XPLMDataTypeID](/sdk/XPLMDataTypeID/)

This is an enumeration that defines the type of the data behind a data
reference. This allows you to sanity check that the data type matches what you
expect. But for the most part, you will know the type of data you are expecting
from the online documentation.

Data types each take a bit field; it is legal to have a single dataref be more
than one type of data. Whe this happens, you can pick any matching get/set API.

| Name | Value | Description |
| --- | --- | --- |
| [xplmType_Unknown](/sdk/xplmType_Unknown/) | "0" | Data of a type the current
XPLM doesn't do. |
| [xplmType_Int](/sdk/xplmType_Int/) | "1" | A single 4-byte integer, native
endian. |
| [xplmType_Float](/sdk/xplmType_Float/) | "2" | A single 4-byte float, native
endian. |
| [xplmType_Double](/sdk/xplmType_Double/) | "4" | A single 8-byte double,
native endian. |
| [xplmType_FloatArray](/sdk/xplmType_FloatArray/) | "8" | An array of 4-byte
floats, native endian. |
| [xplmType_IntArray](/sdk/xplmType_IntArray/) | "16" | An array of 4-byte
integers, native endian. |
| [xplmType_Data](/sdk/xplmType_Data/) | "32" | A variable block of data. |

### [XPLMFindDataRef](/sdk/XPLMFindDataRef/)

```cpp
XPLM_API XPLMDataRef XPLMFindDataRef(
                         const char *         inDataRefName);

```

Given a C-style string that names the dataref, this routine looks up the actual
opaque[XPLMDataRef](/sdk/XPLMDataRef/)that you use to read and write the data.
The string names for datarefs are published on the X-Plane SDK web site.

This function returns NULL if the dataref cannot be found.

NOTE: this function is relatively expensive; save
the[XPLMDataRef](/sdk/XPLMDataRef/)this function returns for future use. Do not
look up your dataref by string every time you need to read or write it.

### [XPLMGetDataRefInfo](/sdk/XPLMGetDataRefInfo/)

```cpp
XPLM_API void       XPLMGetDataRefInfo(
                         XPLMDataRef          inDataRef,
                         XPLMDataRefInfo_t *  outInfo);

```

Give a data ref, this routine returns a populated struct containing the
available information about the dataref.

### [XPLMGetDataRefTypes](/sdk/XPLMGetDataRefTypes/)

```cpp
XPLM_API XPLMDataTypeID XPLMGetDataRefTypes(
                         XPLMDataRef          inDataRef);

```

This routine returns the types of the dataref for accessor use. If a dataref is
available in multiple data types, the bit-wise OR of these types will be
returned.

### [XPLMGetDataRefsByIndex](/sdk/XPLMGetDataRefsByIndex/)

```cpp
XPLM_API void       XPLMGetDataRefsByIndex(
                         int                  offset,
                         int                  count,
                         XPLMDataRef *        outDataRefs);

```

Given an offset and count, this function will return an array of XPLMDataRefs in
that range. The offset/count idiom is useful for things like pagination.

### [XPLMGetDatab](/sdk/XPLMGetDatab/)

```cpp
XPLM_API int        XPLMGetDatab(
                         XPLMDataRef          inDataRef,
                         void *               outValue,    /* Can be NULL */
                         int                  inOffset,
                         int                  inMaxBytes);

```

Read a part of a byte array dataref. If you pass NULL for outValues, the routine
will return the size of the array, ignoring inOffset and inMax.

If outValues is not NULL, then up to inMax values are copied from the dataref
into outValues, starting at inOffset in the dataref. If inMax + inOffset is
larger than the size of the dataref, less than inMax values will be copied. The
number of values copied is returned.

Note: the semantics of array datarefs are entirely implemented by the plugin (or
X-Plane) that provides the dataref, not the SDK itself; the above description is
how these datarefs are intended to work, but a rogue plugin may have different
behavior.

### [XPLMGetDatab_f](/sdk/XPLMGetDatab_f/)

```cpp
typedef int (* XPLMGetDatab_f)(
                         void *               inRefcon,
                         void *               outValue,    /* Can be NULL */
                         int                  inOffset,
                         int                  inMaxLength);

```

### [XPLMGetDatad](/sdk/XPLMGetDatad/)

```cpp
XPLM_API double     XPLMGetDatad(
                         XPLMDataRef          inDataRef);

```

Read a double precision floating point dataref and return its value. The return
value is the dataref value or 0.0 if the dataref is NULL or the plugin is
disabled.

### [XPLMGetDatad_f](/sdk/XPLMGetDatad_f/)

```cpp
typedef double (* XPLMGetDatad_f)(
                         void *               inRefcon);

```

### [XPLMGetDataf](/sdk/XPLMGetDataf/)

```cpp
XPLM_API float      XPLMGetDataf(
                         XPLMDataRef          inDataRef);

```

Read a single precision floating point dataref and return its value. The return
value is the dataref value or 0.0 if the dataref is NULL or the plugin is
disabled.

### [XPLMGetDataf_f](/sdk/XPLMGetDataf_f/)

```cpp
typedef float (* XPLMGetDataf_f)(
                         void *               inRefcon);

```

### [XPLMGetDatai](/sdk/XPLMGetDatai/)

```cpp
XPLM_API int        XPLMGetDatai(
                         XPLMDataRef          inDataRef);

```

Read an integer dataref and return its value. The return value is the dataref
value or 0 if the dataref is NULL or the plugin is disabled.

### [XPLMGetDatai_f](/sdk/XPLMGetDatai_f/)

```cpp
typedef int (* XPLMGetDatai_f)(
                         void *               inRefcon);

```

Data provider function pointers.

These define the function pointers you provide to get or set data. Note that you
are passed a generic pointer for each one. This is the same pointer you pass in
your register routine; you can use it to locate plugin variables, etc.

The semantics of your callbacks are the same as the dataref accessors above -
basically routines like[XPLMGetDatai](/sdk/XPLMGetDatai/)are just pass-throughs
from a caller to your plugin. Be particularly mindful in implementing array
dataref read-write accessors; you are responsible for avoiding overruns,
supporting offset read/writes, and handling a read with a NULL buffer.

### [XPLMGetDatavf](/sdk/XPLMGetDatavf/)

```cpp
XPLM_API int        XPLMGetDatavf(
                         XPLMDataRef          inDataRef,
                         float *              outValues,    /* Can be NULL */
                         int                  inOffset,
                         int                  inMax);

```

Read a part of a single precision floating point array dataref. If you pass NULL
for outValues, the routine will return the size of the array, ignoring inOffset
and inMax.

If outValues is not NULL, then up to inMax values are copied from the dataref
into outValues, starting at inOffset in the dataref. If inMax + inOffset is
larger than the size of the dataref, less than inMax values will be copied. The
number of values copied is returned.

Note: the semantics of array datarefs are entirely implemented by the plugin (or
X-Plane) that provides the dataref, not the SDK itself; the above description is
how these datarefs are intended to work, but a rogue plugin may have different
behavior.

### [XPLMGetDatavf_f](/sdk/XPLMGetDatavf_f/)

```cpp
typedef int (* XPLMGetDatavf_f)(
                         void *               inRefcon,
                         float *              outValues,    /* Can be NULL */
                         int                  inOffset,
                         int                  inMax);

```

### [XPLMGetDatavi](/sdk/XPLMGetDatavi/)

```cpp
XPLM_API int        XPLMGetDatavi(
                         XPLMDataRef          inDataRef,
                         int *                outValues,    /* Can be NULL */
                         int                  inOffset,
                         int                  inMax);

```

Read a part of an integer array dataref. If you pass NULL for outValues, the
routine will return the size of the array, ignoring inOffset and inMax.

If outValues is not NULL, then up to inMax values are copied from the dataref
into outValues, starting at inOffset in the dataref. If inMax + inOffset is
larger than the size of the dataref, less than inMax values will be copied. The
number of values copied is returned.

Note: the semantics of array datarefs are entirely implemented by the plugin (or
X-Plane) that provides the dataref, not the SDK itself; the above description is
how these datarefs are intended to work, but a rogue plugin may have different
behavior.

### [XPLMGetDatavi_f](/sdk/XPLMGetDatavi_f/)

```cpp
typedef int (* XPLMGetDatavi_f)(
                         void *               inRefcon,
                         int *                outValues,    /* Can be NULL */
                         int                  inOffset,
                         int                  inMax);

```

### [XPLMIsDataRefGood](/sdk/XPLMIsDataRefGood/)

```cpp
XPLM_API int        XPLMIsDataRefGood(
                         XPLMDataRef          inDataRef);

```

This function returns true if the passed in handle is a valid dataref that is
not orphaned.

Note: there is normally no need to call this function; datarefs returned
by[XPLMFindDataRef](/sdk/XPLMFindDataRef/)remain valid (but possibly orphaned)
unless there is a complete plugin reload (in which case your plugin is reloaded
anyway). Orphaned datarefs can be safely read and return 0. Therefore you never
need to call[XPLMIsDataRefGood](/sdk/XPLMIsDataRefGood/)to ‘check’ the safety of
a dataref. ([XPLMIsDataRefGood](/sdk/XPLMIsDataRefGood/)performs some slow
checking of the handle validity, so it has a perormance cost.)

### [XPLMSetDatab](/sdk/XPLMSetDatab/)

```cpp
XPLM_API void       XPLMSetDatab(
                         XPLMDataRef          inDataRef,
                         void *               inValue,
                         int                  inOffset,
                         int                  inLength);

```

Write part or all of a byte array dataref. The values passed by inValues are
written into the dataref starting at inOffset. Up to inCount values are written;
however if the values would write “off the end” of the dataref array, then fewer
values are written.

Note: the semantics of array datarefs are entirely implemented by the plugin (or
X-Plane) that provides the dataref, not the SDK itself; the above description is
how these datarefs are intended to work, but a rogue plugin may have different
behavior.

### [XPLMSetDatab_f](/sdk/XPLMSetDatab_f/)

```cpp
typedef void (* XPLMSetDatab_f)(
                         void *               inRefcon,
                         void *               inValue,
                         int                  inOffset,
                         int                  inLength);

```

### [XPLMSetDatad](/sdk/XPLMSetDatad/)

```cpp
XPLM_API void       XPLMSetDatad(
                         XPLMDataRef          inDataRef,
                         double               inValue);

```

Write a new value to a double precision floating point dataref. This routine is
a no-op if the plugin publishing the dataref is disabled, the dataref is NULL,
or the dataref is not writable.

### [XPLMSetDatad_f](/sdk/XPLMSetDatad_f/)

```cpp
typedef void (* XPLMSetDatad_f)(
                         void *               inRefcon,
                         double               inValue);

```

### [XPLMSetDataf](/sdk/XPLMSetDataf/)

```cpp
XPLM_API void       XPLMSetDataf(
                         XPLMDataRef          inDataRef,
                         float                inValue);

```

Write a new value to a single precision floating point dataref. This routine is
a no-op if the plugin publishing the dataref is disabled, the dataref is NULL,
or the dataref is not writable.

### [XPLMSetDataf_f](/sdk/XPLMSetDataf_f/)

```cpp
typedef void (* XPLMSetDataf_f)(
                         void *               inRefcon,
                         float                inValue);

```

### [XPLMSetDatai](/sdk/XPLMSetDatai/)

```cpp
XPLM_API void       XPLMSetDatai(
                         XPLMDataRef          inDataRef,
                         int                  inValue);

```

Write a new value to an integer dataref. This routine is a no-op if the plugin
publishing the dataref is disabled, the dataref is NULL, or the dataref is not
writable.

### [XPLMSetDatai_f](/sdk/XPLMSetDatai_f/)

```cpp
typedef void (* XPLMSetDatai_f)(
                         void *               inRefcon,
                         int                  inValue);

```

### [XPLMSetDatavf](/sdk/XPLMSetDatavf/)

```cpp
XPLM_API void       XPLMSetDatavf(
                         XPLMDataRef          inDataRef,
                         float *              inValues,
                         int                  inoffset,
                         int                  inCount);

```

Write part or all of a single precision floating point array dataref. The values
passed by inValues are written into the dataref starting at inOffset. Up to
inCount values are written; however if the values would write past the end of
the dataref array, then fewer values are written.

Note: the semantics of array datarefs are entirely implemented by the plugin (or
X-Plane) that provides the dataref, not the SDK itself; the above description is
how these datarefs are intended to work, but a rogue plugin may have different
behavior.

### [XPLMSetDatavf_f](/sdk/XPLMSetDatavf_f/)

```cpp
typedef void (* XPLMSetDatavf_f)(
                         void *               inRefcon,
                         float *              inValues,
                         int                  inOffset,
                         int                  inCount);

```

### [XPLMSetDatavi](/sdk/XPLMSetDatavi/)

```cpp
XPLM_API void       XPLMSetDatavi(
                         XPLMDataRef          inDataRef,
                         int *                inValues,
                         int                  inoffset,
                         int                  inCount);

```

Write part or all of an integer array dataref. The values passed by inValues are
written into the dataref starting at inOffset. Up to inCount values are written;
however if the values would write past the end of the dataref array, then fewer
values are written.

Note: the semantics of array datarefs are entirely implemented by the plugin (or
X-Plane) that provides the dataref, not the SDK itself; the above description is
how these datarefs are intended to work, but a rogue plugin may have different
behavior.

### [XPLMSetDatavi_f](/sdk/XPLMSetDatavi_f/)

```cpp
typedef void (* XPLMSetDatavi_f)(
                         void *               inRefcon,
                         int *                inValues,
                         int                  inOffset,
                         int                  inCount);

```

### [XPLM_MSG_DATAREFS_ADDED](/sdk/XPLM_MSG_DATAREFS_ADDED/)

```cpp
#define XPLM_MSG_DATAREFS_ADDED 114
```

Sent to your plugin per-frame (at-most) when/if datarefs are added. It will
include the new data ref total count so that your plugin can keep a local cache
of the total, see what’s changed and know which ones to inquire about if it
cares.

This message is only sent to plugins that enable the
XPLM_WANTS_DATAREF_NOTIFICATIONS feature.

