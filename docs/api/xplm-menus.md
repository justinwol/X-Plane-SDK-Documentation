---
title: "Menus APIs"
description: "X-Plane SDK Menus APIs documentation"
category: "XPLM_Menus"
date: "2025-06-25T15:45:56.659424"
---

# Menus APIs

### [XPLMCheckMenuItem](/sdk/XPLMCheckMenuItem/)

```cpp
XPLM_API void       XPLMCheckMenuItem(
                         XPLMMenuID           inMenu,
                         int                  index,
                         XPLMMenuCheck        inCheck);

```

Set whether a menu item is checked. Pass in the menu ID and item index.

### [XPLMCheckMenuItemState](/sdk/XPLMCheckMenuItemState/)

```cpp
XPLM_API void       XPLMCheckMenuItemState(
                         XPLMMenuID           inMenu,
                         int                  index,
                         XPLMMenuCheck *      outCheck);

```

This routine returns whether a menu item is checked or not. A menu item’s check
mark may be on or off, or a menu may not have an icon at all.

### [XPLMClearAllMenuItems](/sdk/XPLMClearAllMenuItems/)

```cpp
XPLM_API void       XPLMClearAllMenuItems(
                         XPLMMenuID           inMenuID);

```

This function removes all menu items from a menu, allowing you to rebuild it.
Use this function if you need to change the number of items on a menu.

### [XPLMCreateMenu](/sdk/XPLMCreateMenu/)

```cpp
XPLM_API XPLMMenuID XPLMCreateMenu(
                         const char *         inName,
                         XPLMMenuID           inParentMenu,
                         int                  inParentItem,
                         XPLMMenuHandler_f    inHandler,
                         void *               inMenuRef);

```

This function creates a new menu and returns its ID. It returns NULL if the menu
cannot be created. Pass in a parent menu ID and an item index to create a
submenu, or NULL for the parent menu to put the menu in the menu bar. The menu’s
name is only used if the menu is in the menubar. You also pass a handler
function and a menu reference value. Pass NULL for the handler if you do not
need callbacks from the menu (for example, if it only contains submenus).

Important: you must pass a valid, non-empty menu title even if the menu is a
submenu where the title is not visible.

### [XPLMDestroyMenu](/sdk/XPLMDestroyMenu/)

```cpp
XPLM_API void       XPLMDestroyMenu(
                         XPLMMenuID           inMenuID);

```

This function destroys a menu that you have created. Use this to remove a
submenu if necessary. (Normally this function will not be necessary.)

### [XPLMEnableMenuItem](/sdk/XPLMEnableMenuItem/)

```cpp
XPLM_API void       XPLMEnableMenuItem(
                         XPLMMenuID           inMenu,
                         int                  index,
                         int                  enabled);

```

Sets whether this menu item is enabled. Items start out enabled.

### [XPLMEnumerateFeatures](/sdk/XPLMEnumerateFeatures/)

```cpp
XPLM_API void       XPLMEnumerateFeatures(
                         XPLMFeatureEnumerator_f inEnumerator,
                         void *               inRef);

```

This routine calls your enumerator callback once for each feature that this
running version of X-Plane supports. Use this routine to determine all of the
features that X-Plane can support.

### [XPLMFindAircraftMenu](/sdk/XPLMFindAircraftMenu/)

```cpp
XPLM_API XPLMMenuID XPLMFindAircraftMenu(void);

```

This function returns the ID of the menu for the currently-loaded aircraft, used
for showing aircraft-specific commands.

The aircraft menu is created by X-Plane at startup, but it remains hidden until
it is populated via[XPLMAppendMenuItem](/sdk/XPLMAppendMenuItem/)()
or[XPLMAppendMenuItemWithCommand](/sdk/XPLMAppendMenuItemWithCommand/)().

Only plugins loaded with the user’s current aircraft are allowed to access the
aircraft menu. For all other plugins, this will return NULL, and any attempts to
add menu items to it will fail.

### [XPLMFindPluginsMenu](/sdk/XPLMFindPluginsMenu/)

```cpp
XPLM_API XPLMMenuID XPLMFindPluginsMenu(void);

```

This function returns the ID of the plug-ins menu, which is created for you at
startup.

### [XPLMMenuCheck](/sdk/XPLMMenuCheck/)

These enumerations define the various ‘check’ states for an X-Plane menu.
‘Checking’ in X-Plane actually appears as a light which may or may not be lit.
So there are three possible states.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_Menu_NoCheck](/sdk/xplm_Menu_NoCheck/) | "0" | There is no symbol to the
left of the menu item. |
| [xplm_Menu_Unchecked](/sdk/xplm_Menu_Unchecked/) | "1" | The menu has a mark
next to it that is unmarked (not lit). |
| [xplm_Menu_Checked](/sdk/xplm_Menu_Checked/) | "2" | The menu has a mark next
to it that is checked (lit). |

### [XPLMMenuHandler_f](/sdk/XPLMMenuHandler_f/)

```cpp
typedef void (* XPLMMenuHandler_f)(
                         void *               inMenuRef,
                         void *               inItemRef);

```

A menu handler function takes two reference pointers, one for the menu
(specified when the menu was created) and one for the item (specified when the
item was created).

### [XPLMMenuID](/sdk/XPLMMenuID/)

```cpp
typedef void * XPLMMenuID;
```

This is a unique ID for each menu you create.

# [XPLMMenus](/sdk/XPLMMenus/)API

Plug-ins can create menus in the menu bar of X-Plane. This is done by creating a
menu and then creating items. Menus are referred to by an opaque ID. Items are
referred to by (zero-based) index number.

Menus are “sandboxed” between plugins - no plugin can access the menus of any
other plugin. Furthermore, all menu indices are relative to your plugin’s menus
only; if your plugin creates two sub-menus in the Plugins menu at different
times, it doesn’t matter how many other plugins also create sub-menus of Plugins
in the intervening time: your sub-menus will be given menu indices 0 and 1. (The
SDK does some work in the back-end to filter out menus that are irrelevant to
your plugin in order to deliver this consistency for each plugin.)

When you create a menu item, you specify how we should handle clicks on that
menu item. You can either have the XPLM trigger a callback
(the[XPLMMenuHandler_f](/sdk/XPLMMenuHandler_f/)associated with the menu that
contains the item), or you can simply have a command be triggered (with no
associated call to your menu handler). The advantage of the latter method is
that X-Plane will display any keyboard shortcuts associated with the command.
(In contrast, there are no keyboard shortcuts associated with menu handler
callbacks with specific parameters.)

Menu text in X-Plane is UTF8; X-Plane’s character set covers latin, greek and
cyrillic characters, Katakana, as well as some Japanese symbols. Some APIs have
a inDeprecatedAndIgnored parameter that used to select a character set; since
X-Plane 9 all localization is done via UTF-8 only.

## XPLM MENUS

### [XPLMMenuCheck](/sdk/XPLMMenuCheck/)

These enumerations define the various ‘check’ states for an X-Plane menu.
‘Checking’ in X-Plane actually appears as a light which may or may not be lit.
So there are three possible states.

| Name | Value | Description |
| --- | --- | --- |
| [xplm_Menu_NoCheck](/sdk/xplm_Menu_NoCheck/) | "0" | There is no symbol to the
left of the menu item. |
| [xplm_Menu_Unchecked](/sdk/xplm_Menu_Unchecked/) | "1" | The menu has a mark
next to it that is unmarked (not lit). |
| [xplm_Menu_Checked](/sdk/xplm_Menu_Checked/) | "2" | The menu has a mark next
to it that is checked (lit). |

### [XPLMMenuID](/sdk/XPLMMenuID/)

```cpp
typedef void * XPLMMenuID;
```

This is a unique ID for each menu you create.

### [XPLMMenuHandler_f](/sdk/XPLMMenuHandler_f/)

```cpp
typedef void (* XPLMMenuHandler_f)(
                         void *               inMenuRef,
                         void *               inItemRef);

```

A menu handler function takes two reference pointers, one for the menu
(specified when the menu was created) and one for the item (specified when the
item was created).

### [XPLMFindPluginsMenu](/sdk/XPLMFindPluginsMenu/)

```cpp
XPLM_API XPLMMenuID XPLMFindPluginsMenu(void);

```

This function returns the ID of the plug-ins menu, which is created for you at
startup.

### [XPLMFindAircraftMenu](/sdk/XPLMFindAircraftMenu/)

```cpp
XPLM_API XPLMMenuID XPLMFindAircraftMenu(void);

```

This function returns the ID of the menu for the currently-loaded aircraft, used
for showing aircraft-specific commands.

The aircraft menu is created by X-Plane at startup, but it remains hidden until
it is populated via[XPLMAppendMenuItem](/sdk/XPLMAppendMenuItem/)()
or[XPLMAppendMenuItemWithCommand](/sdk/XPLMAppendMenuItemWithCommand/)().

Only plugins loaded with the user’s current aircraft are allowed to access the
aircraft menu. For all other plugins, this will return NULL, and any attempts to
add menu items to it will fail.

### [XPLMCreateMenu](/sdk/XPLMCreateMenu/)

```cpp
XPLM_API XPLMMenuID XPLMCreateMenu(
                         const char *         inName,
                         XPLMMenuID           inParentMenu,
                         int                  inParentItem,
                         XPLMMenuHandler_f    inHandler,
                         void *               inMenuRef);

```

This function creates a new menu and returns its ID. It returns NULL if the menu
cannot be created. Pass in a parent menu ID and an item index to create a
submenu, or NULL for the parent menu to put the menu in the menu bar. The menu’s
name is only used if the menu is in the menubar. You also pass a handler
function and a menu reference value. Pass NULL for the handler if you do not
need callbacks from the menu (for example, if it only contains submenus).

Important: you must pass a valid, non-empty menu title even if the menu is a
submenu where the title is not visible.

### [XPLMDestroyMenu](/sdk/XPLMDestroyMenu/)

```cpp
XPLM_API void       XPLMDestroyMenu(
                         XPLMMenuID           inMenuID);

```

This function destroys a menu that you have created. Use this to remove a
submenu if necessary. (Normally this function will not be necessary.)

### [XPLMClearAllMenuItems](/sdk/XPLMClearAllMenuItems/)

```cpp
XPLM_API void       XPLMClearAllMenuItems(
                         XPLMMenuID           inMenuID);

```

This function removes all menu items from a menu, allowing you to rebuild it.
Use this function if you need to change the number of items on a menu.

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

### [XPLMSetMenuItemName](/sdk/XPLMSetMenuItemName/)

```cpp
XPLM_API void       XPLMSetMenuItemName(
                         XPLMMenuID           inMenu,
                         int                  inIndex,
                         const char *         inItemName,
                         int                  inDeprecatedAndIgnored);

```

This routine changes the name of an existing menu item. Pass in the menu ID and
the index of the menu item.

### [XPLMCheckMenuItem](/sdk/XPLMCheckMenuItem/)

```cpp
XPLM_API void       XPLMCheckMenuItem(
                         XPLMMenuID           inMenu,
                         int                  index,
                         XPLMMenuCheck        inCheck);

```

Set whether a menu item is checked. Pass in the menu ID and item index.

### [XPLMCheckMenuItemState](/sdk/XPLMCheckMenuItemState/)

```cpp
XPLM_API void       XPLMCheckMenuItemState(
                         XPLMMenuID           inMenu,
                         int                  index,
                         XPLMMenuCheck *      outCheck);

```

This routine returns whether a menu item is checked or not. A menu item’s check
mark may be on or off, or a menu may not have an icon at all.

### [XPLMEnableMenuItem](/sdk/XPLMEnableMenuItem/)

```cpp
XPLM_API void       XPLMEnableMenuItem(
                         XPLMMenuID           inMenu,
                         int                  index,
                         int                  enabled);

```

Sets whether this menu item is enabled. Items start out enabled.

### [XPLMRemoveMenuItem](/sdk/XPLMRemoveMenuItem/)

```cpp
XPLM_API void       XPLMRemoveMenuItem(
                         XPLMMenuID           inMenu,
                         int                  inIndex);

```

Removes one item from a menu. Note that all menu items below are moved up one;
your plugin must track the change in index numbers.

### [XPLMRemoveMenuItem](/sdk/XPLMRemoveMenuItem/)

```cpp
XPLM_API void       XPLMRemoveMenuItem(
                         XPLMMenuID           inMenu,
                         int                  inIndex);

```

Removes one item from a menu. Note that all menu items below are moved up one;
your plugin must track the change in index numbers.

### [XPLMSetMenuItemName](/sdk/XPLMSetMenuItemName/)

```cpp
XPLM_API void       XPLMSetMenuItemName(
                         XPLMMenuID           inMenu,
                         int                  inIndex,
                         const char *         inItemName,
                         int                  inDeprecatedAndIgnored);

```

This routine changes the name of an existing menu item. Pass in the menu ID and
the index of the menu item.

| |  |
| --- | --- | --- |
| [xpButtonBehaviorCheckBox](/sdk/xpButtonBehaviorCheckBox/) | "1" | Check box behavior. The button immediately toggles its value when the mouse is clicked and sends out a[xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/)message. |

| |  |
| --- | --- | --- |
| [xpElement_CheckBox](/sdk/xpElement_CheckBox/) | "9" | none metal |

| |  |
| --- | --- | --- |
| [xpElement_CheckBoxLit](/sdk/xpElement_CheckBoxLit/) | "10" | none metal |

| |  |
| --- | --- | --- |
| [xplmFont_Menus](/sdk/xplmFont_Menus/) | "1" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplmFont_Menus_Localized](/sdk/xplmFont_Menus_Localized /) | "17" | Deprecated, do not use. |

| |  |
| --- | --- | --- |
| [xplm_Menu_Checked](/sdk/xplm_Menu_Checked/) | "2" | The menu has a mark next to it that is checked (lit). |

| |  |
| --- | --- | --- |
| [xplm_Menu_NoCheck](/sdk/xplm_Menu_NoCheck/) | "0" | There is no symbol to the left of the menu item. |

| |  |
| --- | --- | --- |
| [xplm_Menu_Unchecked](/sdk/xplm_Menu_Unchecked/) | "1" | The menu has a mark next to it that is unmarked (not lit). |

