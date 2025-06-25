---
title: "Widget System"
description: "X-Plane SDK Widget System documentation"
category: "Widget_System"
date: "2025-06-25T15:45:56.655424"
---

# Widget System

### [Button Behavior Values](/sdk/Button Behavior Values/)

These define how the button responds to mouse clicks.

| Name | Value | Description |
| --- | --- | --- |
| [xpButtonBehaviorPushButton](/sdk/xpButtonBehaviorPushButton/) | "0" |
Standard push button behavior. The button highlights while the mouse is
clickedover it and unhighlights when the mouse is moved outside of it or
released.If the mouse is released over the button,
the[xpMsg_PushButtonPressed](/sdk/xpMsg_PushButtonPressed/)messageis sent. |
| [xpButtonBehaviorCheckBox](/sdk/xpButtonBehaviorCheckBox/) | "1" | Check box
behavior. The button immediately toggles its value when the mouse is clicked and
sends out a[xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/)message. |
| [xpButtonBehaviorRadioButton](/sdk/xpButtonBehaviorRadioButton/) | "2" | Radio
button behavior. The button immediately sets its state to oneand sends out
a[xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/)message if it was not
already setto one. You must turn off other radio buttons in a group in your
code. |

### [Button Properties](/sdk/Button Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_ButtonType](/sdk/xpProperty_ButtonType/) | "1300" | This property
sets the visual type of button. Use one of the button types above. |
| [xpProperty_ButtonBehavior](/sdk/xpProperty_ButtonBehavior/) | "1301" | This
property sets the button's behavior. Use one of the button behaviors above. |
| [xpProperty_ButtonState](/sdk/xpProperty_ButtonState/) | "1302" | This
property tells whether a check box or radio button is "checked" or not. Not used
for push buttons. |

### [Button Types](/sdk/Button Types/)

These define the visual appearance of buttons but not how they respond to the
mouse.

| Name | Value | Description |
| --- | --- | --- |
| [xpPushButton](/sdk/xpPushButton/) | "0" | This is a standard push button,
like an 'OK' or 'Cancel' button in a dialog box. |
| [xpRadioButton](/sdk/xpRadioButton/) | "1" | A check box or radio button. Use
this and the button behaviors below to get the desired behavior. |
| [xpWindowCloseBox](/sdk/xpWindowCloseBox/) | "3" | A window close box. |
| [xpLittleDownArrow](/sdk/xpLittleDownArrow/) | "5" | A small down arrow. |
| [xpLittleUpArrow](/sdk/xpLittleUpArrow/) | "6" | A small up arrow. |

### [Caption Properties](/sdk/Caption Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_CaptionLit](/sdk/xpProperty_CaptionLit/) | "1600" | This property
specifies whether the caption is lit; use lit captions against screens. |

### [Progress Indicator Properties](/sdk/Progress Indicator Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_ProgressPosition](/sdk/xpProperty_ProgressPosition/) | "1800" |
This is the current value of the progress indicator. |
| [xpProperty_ProgressMin](/sdk/xpProperty_ProgressMin/) | "1801" | This is the
minimum value, equivalent to 0% filled. |
| [xpProperty_ProgressMax](/sdk/xpProperty_ProgressMax/) | "1802" | This is the
maximum value, equivalent to 100% filled. |

### [Scroll Bar Properties](/sdk/Scroll Bar Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_ScrollBarSliderPosition](/sdk/xpProperty_ScrollBarSliderPosition/)
| "1500" | The current position of the thumb (in between the min and max,
inclusive) |
| [xpProperty_ScrollBarMin](/sdk/xpProperty_ScrollBarMin/) | "1501" | The value
the scroll bar has when the thumb is in the lowest position. |
| [xpProperty_ScrollBarMax](/sdk/xpProperty_ScrollBarMax/) | "1502" | The value
the scroll bar has when the thumb is in the highest position. |
| [xpProperty_ScrollBarPageAmount](/sdk/xpProperty_ScrollBarPageAmount/) |
"1503" | How many units to move the scroll bar when clicking next to the thumb.
The scroll bar always moves one unit when the arrows are clicked. |
| [xpProperty_ScrollBarType](/sdk/xpProperty_ScrollBarType/) | "1504" | The type
of scrollbar from the enums above. |
| [xpProperty_ScrollBarSlop](/sdk/xpProperty_ScrollBarSlop/) | "1505" | Used
internally. |

### [Scroll Bar Type Values](/sdk/Scroll Bar Type Values/)

This defines how the scroll bar looks.

| Name | Value | Description |
| --- | --- | --- |
| [xpScrollBarTypeScrollBar](/sdk/xpScrollBarTypeScrollBar/) | "0" | A standard
X-Plane scroll bar (with arrows on the ends). |
| [xpScrollBarTypeSlider](/sdk/xpScrollBarTypeSlider/) | "1" | A slider, no
arrows. |

### [Text Field Properties](/sdk/Text Field Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_EditFieldSelStart](/sdk/xpProperty_EditFieldSelStart/) | "1400" |
This is the character position the selection starts at, zero based.If it is the
same as the end insertion point, the insertion pointis not a selection. |
| [xpProperty_EditFieldSelEnd](/sdk/xpProperty_EditFieldSelEnd/) | "1401" | This
is the character position of the end of the selection. |
| [xpProperty_EditFieldSelDragStart](/sdk/xpProperty_EditFieldSelDragStart/) |
"1402" | This is the character position a drag was started at if the user is
dragging to select text, or -1 if a drag is not in progress. |
| [xpProperty_TextFieldType](/sdk/xpProperty_TextFieldType/) | "1403" | This is
the type of text field to display, from the above list. |
| [xpProperty_PasswordMode](/sdk/xpProperty_PasswordMode/) | "1404" | Set this
property to 1 to password protect the field. Characters will be drawn as *s even
though the descriptor will contain plain-text. |
| [xpProperty_MaxCharacters](/sdk/xpProperty_MaxCharacters/) | "1405" | The max
number of characters you can enter, if limited. Zero means unlimited. |
| [xpProperty_ScrollPosition](/sdk/xpProperty_ScrollPosition/) | "1406" | The
first visible character on the left. This effectively scrolls the text field. |
| [xpProperty_Font](/sdk/xpProperty_Font/) | "1407" | The font to draw the
field's text with. (An[XPLMFontID](/sdk/XPLMFontID/).) |
| [xpProperty_ActiveEditSide](/sdk/xpProperty_ActiveEditSide/) | "1408" | This
is the active side of the insert selection. (Internal) |

### [Text Field Type Values](/sdk/Text Field Type Values/)

These control the look of the text field.

| Name | Value | Description |
| --- | --- | --- |
| [xpTextEntryField](/sdk/xpTextEntryField/) | "0" | A field for text entry. |
| [xpTextTransparent](/sdk/xpTextTransparent/) | "3" | A transparent text field.
The user can type and the text is drawn, but no background is drawn.You can draw
your own background by adding a widget handler and prehandling the draw message.
|
| [xpTextTranslucent](/sdk/xpTextTranslucent/) | "4" | A translucent edit field,
dark gray. |

### [XPBringRootWidgetToFront](/sdk/XPBringRootWidgetToFront/)

```cpp
WIDGET_API void       XPBringRootWidgetToFront(
                         XPWidgetID           inWidget);

```

This routine makes the specified widget be in the frontmost widget hierarchy. If
this widget is a root widget, its widget hierarchy comes to front, otherwise the
widget’s root is brought to the front. If this widget is not in an active widget
hiearchy (e.g. there is no root widget at the top of the tree), this routine
does nothing.

### [XPCountChildWidgets](/sdk/XPCountChildWidgets/)

```cpp
WIDGET_API int        XPCountChildWidgets(
                         XPWidgetID           inWidget);

```

This routine returns the number of widgets another widget contains.

### [XPCreateCustomWidget](/sdk/XPCreateCustomWidget/)

```cpp
WIDGET_API XPWidgetID XPCreateCustomWidget(
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom,
                         int                  inVisible,
                         const char *         inDescriptor,
                         int                  inIsRoot,
                         XPWidgetID           inContainer,
                         XPWidgetFunc_t       inCallback);

```

This function is the same as[XPCreateWidget](/sdk/XPCreateWidget/)except that
instead of passing a class ID, you pass your widget callback function pointer
defining the widget. Use this function to define a custom widget. All parameters
are the same as[XPCreateWidget](/sdk/XPCreateWidget/), except that the widget
class has been replaced with the widget function.

### [XPCreateWidget](/sdk/XPCreateWidget/)

```cpp
WIDGET_API XPWidgetID XPCreateWidget(
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom,
                         int                  inVisible,
                         const char *         inDescriptor,
                         int                  inIsRoot,
                         XPWidgetID           inContainer,
                         XPWidgetClass        inClass);

```

This function creates a new widget and returns the new widget’s ID to you. If
the widget creation fails for some reason, it returns NULL. Widget creation will
fail either if you pass a bad class ID or if there is not adequate memory.

Input Parameters:

- Top, left, bottom, and right in global screen coordinates defining the widget’s location on the screen.
- inVisible is 1 if the widget should be drawn, 0 to start the widget as hidden.
- inDescriptor is a null terminated string that will become the widget’s descriptor.
- inIsRoot is 1 if this is going to be a root widget, 0 if it will not be.
- inContainer is the ID of this widget’s container. It must be 0 for a root widget. For a non-root widget, pass the widget ID of the widget to place this widget within. If this widget is not going to start inside another widget, pass 0; this new widget will be created but will not be drawn until it is placed inside another widget.
- inClass is the class of the widget to draw. Use one of the predefined class-IDs to create a standard widget.

A note on widget embedding: a widget is only called (and will be drawn, etc.) if
it is placed within a widget that will be called. Root widgets are always
called. So it is possible to have whole chains of widgets that are simply not
called. You can preconstruct widget trees and then place them into root widgets
later to activate them if you wish.

### [XPDestroyWidget](/sdk/XPDestroyWidget/)

```cpp
WIDGET_API void       XPDestroyWidget(
                         XPWidgetID           inWidget,
                         int                  inDestroyChildren);

```

This class destroys a widget. Pass in the ID of the widget to kill. If you pass
1 for inDestroyChilren, the widget’s children will be destroyed first, then this
widget will be destroyed. (Furthermore, the widget’s children will be destroyed
with the inDestroyChildren flag set to 1, so the destruction will recurse down
the widget tree.) If you pass 0 for this flag, direct child widgets will simply
end up with their parent set to 0.

### [XPFindRootWidget](/sdk/XPFindRootWidget/)

```cpp
WIDGET_API XPWidgetID XPFindRootWidget(
                         XPWidgetID           inWidget);

```

Returns the Widget ID of the root widget that contains the passed in widget or
NULL if the passed in widget is not in a rooted hierarchy.

### [XPGetNthChildWidget](/sdk/XPGetNthChildWidget/)

```cpp
WIDGET_API XPWidgetID XPGetNthChildWidget(
                         XPWidgetID           inWidget,
                         int                  inIndex);

```

This routine returns the widget ID of a child widget by index. Indexes are 0
based, from 0 to the number of widgets in the parentone minus one, inclusive. If
the index is invalid, 0 is returned.

### [XPGetParentWidget](/sdk/XPGetParentWidget/)

```cpp
WIDGET_API XPWidgetID XPGetParentWidget(
                         XPWidgetID           inWidget);

```

Returns the parent of a widget, or 0 if the widget has no parent. Root widgets
never have parents and therefore always return 0.

### [XPGetWidgetClassFunc](/sdk/XPGetWidgetClassFunc/)

```cpp
WIDGET_API XPWidgetFunc_t XPGetWidgetClassFunc(
                         XPWidgetClass        inWidgetClass);

```

Given a widget class, this function returns the callbacks that power that widget
class.

### [XPGetWidgetDescriptor](/sdk/XPGetWidgetDescriptor/)

```cpp
WIDGET_API int        XPGetWidgetDescriptor(
                         XPWidgetID           inWidget,
                         char *               outDescriptor,
                         int                  inMaxDescLength);

```

This routine returns the widget’s descriptor. Pass in the length of the buffer
you are going to receive the descriptor in. The descriptor will be null
terminated for you. This routine returns the length of the actual descriptor; if
you pass NULL for outDescriptor, you can get the descriptor’s length without
getting its text. If the length of the descriptor exceeds your buffer length,
the buffer will not be null terminated (this routine has ‘strncpy’ semantics).

### [XPGetWidgetExposedGeometry](/sdk/XPGetWidgetExposedGeometry/)

```cpp
WIDGET_API void       XPGetWidgetExposedGeometry(
                         XPWidgetID           inWidgetID,
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

This routine returns the bounds of the area of a widget that is completely
within its parent widgets. Since a widget’s bounding box can be outside its
parent, part of its area will not be eligible for mouse clicks and should not
draw. Use[XPGetWidgetGeometry](/sdk/XPGetWidgetGeometry/)to find out what area
defines your widget’s shape, but use this routine to find out what area to
actually draw into. Note that the widget library does not use OpenGL clipping to
keep frame rates up, although you could use it internally.

### [XPGetWidgetForLocation](/sdk/XPGetWidgetForLocation/)

```cpp
WIDGET_API XPWidgetID XPGetWidgetForLocation(
                         XPWidgetID           inContainer,
                         int                  inXOffset,
                         int                  inYOffset,
                         int                  inRecursive,
                         int                  inVisibleOnly);

```

Given a widget and a location, this routine returns the widget ID of the child
of that widget that owns that location. If inRecursive is true then this will
return a child of a child of a widget as it tries to find the deepest widget at
that location. If inVisibleOnly is true, then only visible widgets are
considered, otherwise all widgets are considered. The widget ID passed for
inContainer will be returned if the location is in that widget but not in a
child widget. 0 is returned if the location is not in the container.

NOTE: if a widget’s geometry extends outside its parents geometry, it will not
be returned by this call for mouse locations outside the parent geometry. The
parent geometry limits the child’s eligibility for mouse location.

### [XPGetWidgetGeometry](/sdk/XPGetWidgetGeometry/)

```cpp
WIDGET_API void       XPGetWidgetGeometry(
                         XPWidgetID           inWidget,
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

This routine returns the bounding box of a widget in global coordinates. Pass
NULL for any parameter you are not interested in.

### [XPGetWidgetProperty](/sdk/XPGetWidgetProperty/)

```cpp
WIDGET_API intptr_t   XPGetWidgetProperty(
                         XPWidgetID           inWidget,
                         XPWidgetPropertyID   inProperty,
                         int *                inExists);    /* Can be NULL */

```

This routine returns the value of a widget’s property, or 0 if the property is
not defined. If you need to know whether the property is defined, pass a pointer
to an int for inExists; the existence of that property will be returned in the
int. Pass NULL for inExists if you do not need this information.

### [XPGetWidgetWithFocus](/sdk/XPGetWidgetWithFocus/)

```cpp
WIDGET_API XPWidgetID XPGetWidgetWithFocus(void);

```

This routine returns the widget that has keyboard focus, or 0 if X-Plane has
keyboard focus or some other plugin window that does not have widgets has focus.

### [XPHideWidget](/sdk/XPHideWidget/)

```cpp
WIDGET_API void       XPHideWidget(
                         XPWidgetID           inWidget);

```

Makes a widget invisible. See[XPShowWidget](/sdk/XPShowWidget/)for
considerations of when a widget might not be visible despite its own visibility
state.

### [XPIsWidgetInFront](/sdk/XPIsWidgetInFront/)

```cpp
WIDGET_API int        XPIsWidgetInFront(
                         XPWidgetID           inWidget);

```

This routine returns true if this widget’s hierarchy is the frontmost hierarchy.
It returns false if the widget’s hierarchy is not in front, or if the widget is
not in a rooted hierarchy.

### [XPIsWidgetVisible](/sdk/XPIsWidgetVisible/)

```cpp
WIDGET_API int        XPIsWidgetVisible(
                         XPWidgetID           inWidget);

```

This returns 1 if a widget is visible, 0 if it is not. Note that this routine
takes into consideration whether a parent is invisible. Use this routine to tell
if the user can see the widget.

### [XPLMCommandButtonID](/sdk/XPLMCommandButtonID/)

These are enumerations for all of the things you can do with a joystick button
in X-Plane. They currently match the buttons menu in the equipment setup dialog,
but these enums will be stable even if they change in X-Plane.

```cpp
enum {
          xplm_joy_nothing=0,
          xplm_joy_start_all,
          xplm_joy_start_0,
          xplm_joy_start_1,
          xplm_joy_start_2,
          xplm_joy_start_3,
          xplm_joy_start_4,
          xplm_joy_start_5,
          xplm_joy_start_6,
          xplm_joy_start_7,
          xplm_joy_throt_up,
          xplm_joy_throt_dn,
          xplm_joy_prop_up,
          xplm_joy_prop_dn,
          xplm_joy_mixt_up,
          xplm_joy_mixt_dn,
          xplm_joy_carb_tog,
          xplm_joy_carb_on,
          xplm_joy_carb_off,
          xplm_joy_trev,
          xplm_joy_trm_up,
          xplm_joy_trm_dn,
          xplm_joy_rot_trm_up,
          xplm_joy_rot_trm_dn,
          xplm_joy_rud_lft,
          xplm_joy_rud_cntr,
          xplm_joy_rud_rgt,
          xplm_joy_ail_lft,
          xplm_joy_ail_cntr,
          xplm_joy_ail_rgt,
          xplm_joy_B_rud_lft,
          xplm_joy_B_rud_rgt,
          xplm_joy_look_up,
          xplm_joy_look_dn,
          xplm_joy_look_lft,
          xplm_joy_look_rgt,
          xplm_joy_glance_l,
          xplm_joy_glance_r,
          xplm_joy_v_fnh,
          xplm_joy_v_fwh,
          xplm_joy_v_tra,
          xplm_joy_v_twr,
          xplm_joy_v_run,
          xplm_joy_v_cha,
          xplm_joy_v_fr1,
          xplm_joy_v_fr2,
          xplm_joy_v_spo,
          xplm_joy_flapsup,
          xplm_joy_flapsdn,
          xplm_joy_vctswpfwd,
          xplm_joy_vctswpaft,
          xplm_joy_gear_tog,
          xplm_joy_gear_up,
          xplm_joy_gear_down,
          xplm_joy_lft_brake,
          xplm_joy_rgt_brake,
          xplm_joy_brakesREG,
          xplm_joy_brakesMAX,
          xplm_joy_speedbrake,
          xplm_joy_ott_dis,
          xplm_joy_ott_atr,
          xplm_joy_ott_asi,
          xplm_joy_ott_hdg,
          xplm_joy_ott_alt,
          xplm_joy_ott_vvi,
          xplm_joy_tim_start,
          xplm_joy_tim_reset,
          xplm_joy_ecam_up,
          xplm_joy_ecam_dn,
          xplm_joy_fadec,
          xplm_joy_yaw_damp,
          xplm_joy_art_stab,
          xplm_joy_chute,
          xplm_joy_JATO,
          xplm_joy_arrest,
          xplm_joy_jettison,
          xplm_joy_fuel_dump,
          xplm_joy_puffsmoke,
          xplm_joy_prerotate,
          xplm_joy_UL_prerot,
          xplm_joy_UL_collec,
          xplm_joy_TOGA,
          xplm_joy_shutdown,
          xplm_joy_con_atc,
          xplm_joy_fail_now,
          xplm_joy_pause,
          xplm_joy_rock_up,
          xplm_joy_rock_dn,
          xplm_joy_rock_lft,
          xplm_joy_rock_rgt,
          xplm_joy_rock_for,
          xplm_joy_rock_aft,
          xplm_joy_idle_hilo,
          xplm_joy_lanlights,
          xplm_joy_max
};
typedef int XPLMCommandButtonID;
```

### [XPLMCommandButtonPress](/sdk/XPLMCommandButtonPress/)

```cpp
XPLM_API void       XPLMCommandButtonPress(
                         XPLMCommandButtonID  inButton);

```

This function simulates any of the actions that might be taken by pressing a
joystick button. However, this lets you call the command directly rather than
having to know which button is mapped where. Important: you must release each
button you press. The APIs are separate so that you can ‘hold down’ a button for
a fixed amount of time.

Deprecated: use[XPLMCommandBegin](/sdk/XPLMCommandBegin/).

### [XPLMCommandButtonRelease](/sdk/XPLMCommandButtonRelease/)

```cpp
XPLM_API void       XPLMCommandButtonRelease(
                         XPLMCommandButtonID  inButton);

```

This function simulates any of the actions that might be taken by pressing a
joystick button. See[XPLMCommandButtonPress](/sdk/XPLMCommandButtonPress/).

Deprecated: use[XPLMCommandEnd](/sdk/XPLMCommandEnd/).

### [XPPlaceWidgetWithin](/sdk/XPPlaceWidgetWithin/)

```cpp
WIDGET_API void       XPPlaceWidgetWithin(
                         XPWidgetID           inSubWidget,
                         XPWidgetID           inContainer);

```

This function changes which container a widget resides in. You may NOT use this
function on a root widget! inSubWidget is the widget that will be moved. Pass a
widget ID in inContainer to make inSubWidget be a child of inContainer. It will
become the last/closest widget in the container. Pass 0 to remove the widget
from any container. Any call to this other than passing the widget ID of the old
parent of the affected widget will cause the widget to be removed from its old
parent. Placing a widget within its own parent simply makes it the last widget.

NOTE: this routine does not reposition the sub widget in global coordinates. If
the container has layout management code, it will reposition the subwidget for
you, otherwise you must do it with SetWidgetGeometry.

### [XPSetWidgetDescriptor](/sdk/XPSetWidgetDescriptor/)

```cpp
WIDGET_API void       XPSetWidgetDescriptor(
                         XPWidgetID           inWidget,
                         const char *         inDescriptor);

```

Every widget has a descriptor, which is a text string. What the text string is
used for varies from widget to widget; for example, a push button’s text is its
descriptor, a caption shows its descriptor, and a text field’s descriptor is the
text being edited. In other words, the usage for the text varies from widget to
widget, but this API provides a universal and convenient way to get at it. While
not all UI widgets need their descriptor, many do.

### [XPSetWidgetGeometry](/sdk/XPSetWidgetGeometry/)

```cpp
WIDGET_API void       XPSetWidgetGeometry(
                         XPWidgetID           inWidget,
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

This function changes the bounding box of a widget.

### [XPSetWidgetProperty](/sdk/XPSetWidgetProperty/)

```cpp
WIDGET_API void       XPSetWidgetProperty(
                         XPWidgetID           inWidget,
                         XPWidgetPropertyID   inProperty,
                         intptr_t             inValue);

```

This function sets a widget’s property. Properties are arbitrary values
associated by a widget by ID.

### [XPShowWidget](/sdk/XPShowWidget/)

```cpp
WIDGET_API void       XPShowWidget(
                         XPWidgetID           inWidget);

```

This routine makes a widget visible if it is not already. Note that if a widget
is not in a rooted widget hierarchy or one of its parents is not visible, it
will still not be visible to the user.

# [XPStandardWidgets](/sdk/XPStandardWidgets/)API

## THEORY OF OPERATION

The standard widgets are widgets built into the widgets library. While you can
gain access to the widget function that drives them, you generally use them by
calling[XPCreateWidget](/sdk/XPCreateWidget/)and then listening for special
messages, etc.

The standard widgets often send messages to themselves when the user performs an
event; these messages are sent up the widget hierarchy until they are handled.
So you can add a widget proc directly to a push button (for example) to
intercept the message when it is clicked, or you can put one widget proc on a
window for all of the push buttons in the window. Most of these messages contain
the original widget ID as a parameter so you can know which widget is messaging
no matter who it is sent to.

## MAIN WINDOW

The main window widget class provides a “window” as the user knows it. These
windows are draggable and can be selected. Use them to create floating windows
and non-modal dialogs.

### [xpWidgetClass_MainWindow](/sdk/xpWidgetClass_MainWindow/)

```cpp
#define xpWidgetClass_MainWindow 1
```

### [Main Window Type Values](/sdk/Main Window Type Values/)

These type values are used to control the appearance of a main window.

| Name | Value | Description |
| --- | --- | --- |
| [xpMainWindowStyle_MainWindow](/sdk/xpMainWindowStyle_MainWindow/) | "0" | The
standard main window; pin stripes on XP7, metal frame on XP 6. |
| [xpMainWindowStyle_Translucent](/sdk/xpMainWindowStyle_Translucent/) | "1" | A
translucent dark gray window. |

### [Main Window Properties](/sdk/Main Window Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_MainWindowType](/sdk/xpProperty_MainWindowType/) | "1100" | This
property specifies the type of window. Set to one of the main window types
above. |
| [xpProperty_MainWindowHasCloseBoxes](/sdk/xpProperty_MainWindowHasCloseBoxes/)
| "1200" | This property specifies whether the main window has close boxes in
its corners. |

### [MainWindow Messages](/sdk/MainWindow Messages/)

| Name | Value | Description |
| --- | --- | --- |
| [xpMessage_CloseButtonPushed](/sdk/xpMessage_CloseButtonPushed/) | "1200" |
This message is sent when the close buttons for your window are pressed. |

## SUB WINDOW

X-Plane dialogs are divided into separate areas; the sub window widgets allow
you to make these areas. Create one main window and place several subwindows
inside it. Then place your controls inside the subwindows.

### [xpWidgetClass_SubWindow](/sdk/xpWidgetClass_SubWindow/)

```cpp
#define xpWidgetClass_SubWindow 2
```

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

### [SubWindow Properties](/sdk/SubWindow Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_SubWindowType](/sdk/xpProperty_SubWindowType/) | "1200" | This
property specifies the type of window. Set to one of the subwindow types above.
|

## BUTTON

The button class provides a number of different button styles and behaviors,
including push buttons, radio buttons, check boxes, etc. The button label
appears on or next to the button depending on the button’s appearance or type.

The button’s behavior is a separate property that dictates who it highlights and
what kinds of messages it sends. Since behavior and type are different, you can
do strange things like make check boxes that act as push buttons or push buttons
with radio button behavior.

In X-Plane 6 there were no check box graphics. The result is the following
behavior: in X-Plane 6 all check box and radio buttons are round (radio-button
style) buttons; in X-Plane 7 they are all square (check-box style) buttons. In a
future version of X-Plane, the xpButtonBehavior enums will provide the correct
graphic (check box or radio button) giving the expected result.

### [xpWidgetClass_Button](/sdk/xpWidgetClass_Button/)

```cpp
#define xpWidgetClass_Button 3
```

### [Button Types](/sdk/Button Types/)

These define the visual appearance of buttons but not how they respond to the
mouse.

| Name | Value | Description |
| --- | --- | --- |
| [xpPushButton](/sdk/xpPushButton/) | "0" | This is a standard push button,
like an 'OK' or 'Cancel' button in a dialog box. |
| [xpRadioButton](/sdk/xpRadioButton/) | "1" | A check box or radio button. Use
this and the button behaviors below to get the desired behavior. |
| [xpWindowCloseBox](/sdk/xpWindowCloseBox/) | "3" | A window close box. |
| [xpLittleDownArrow](/sdk/xpLittleDownArrow/) | "5" | A small down arrow. |
| [xpLittleUpArrow](/sdk/xpLittleUpArrow/) | "6" | A small up arrow. |

### [Button Behavior Values](/sdk/Button Behavior Values/)

These define how the button responds to mouse clicks.

| Name | Value | Description |
| --- | --- | --- |
| [xpButtonBehaviorPushButton](/sdk/xpButtonBehaviorPushButton/) | "0" |
Standard push button behavior. The button highlights while the mouse is
clickedover it and unhighlights when the mouse is moved outside of it or
released.If the mouse is released over the button,
the[xpMsg_PushButtonPressed](/sdk/xpMsg_PushButtonPressed/)messageis sent. |
| [xpButtonBehaviorCheckBox](/sdk/xpButtonBehaviorCheckBox/) | "1" | Check box
behavior. The button immediately toggles its value when the mouse is clicked and
sends out a[xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/)message. |
| [xpButtonBehaviorRadioButton](/sdk/xpButtonBehaviorRadioButton/) | "2" | Radio
button behavior. The button immediately sets its state to oneand sends out
a[xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/)message if it was not
already setto one. You must turn off other radio buttons in a group in your
code. |

### [Button Properties](/sdk/Button Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_ButtonType](/sdk/xpProperty_ButtonType/) | "1300" | This property
sets the visual type of button. Use one of the button types above. |
| [xpProperty_ButtonBehavior](/sdk/xpProperty_ButtonBehavior/) | "1301" | This
property sets the button's behavior. Use one of the button behaviors above. |
| [xpProperty_ButtonState](/sdk/xpProperty_ButtonState/) | "1302" | This
property tells whether a check box or radio button is "checked" or not. Not used
for push buttons. |

### [Button Messages](/sdk/Button Messages/)

These messages are sent by the button to itself and then up the widget chain
when the button is clicked. (You may intercept them by providing a widget
handler for the button itself or by providing a handler in a parent widget.)

| Name | Value | Description |
| --- | --- | --- |
| [xpMsg_PushButtonPressed](/sdk/xpMsg_PushButtonPressed/) | "1300" | This
message is sent when the user completes a click and release in a button withpush
button behavior. Parameterone of the message is the widget ID of the button.
This message is dispatched up thewidget hierarchy. |
| [xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/) | "1301" | This
message is sent when a button is clicked that has radio button or check box
behaviorand its value changes. (Note that if the value changes by setting a
property you do not receivethis message!) Parameter one is the widget ID of the
button, parameter 2 is the new state value,either zero or one. This message is
dispatched up the widget hierarchy. |

## TEXT FIELD

The text field widget provides an editable text field including mouse selection
and keyboard navigation. The contents of the text field are its descriptor. (The
descriptor changes as the user types.)

The text field can have a number of types, that affect the visual layout of the
text field. The text field sends messages to itself so you may control its
behavior.

If you need to filter keystrokes, add a new handler and intercept the key press
message. Since key presses are passed by pointer, you can modify the keystroke
and pass it through to the text field widget.

WARNING: in X-Plane before 7.10 (including 6.70) null characters could crash
X-Plane. To prevent this, wrap this object with a filter function (more
instructions can be found on the SDK website).

### [xpWidgetClass_TextField](/sdk/xpWidgetClass_TextField/)

```cpp
#define xpWidgetClass_TextField 4
```

### [Text Field Type Values](/sdk/Text Field Type Values/)

These control the look of the text field.

| Name | Value | Description |
| --- | --- | --- |
| [xpTextEntryField](/sdk/xpTextEntryField/) | "0" | A field for text entry. |
| [xpTextTransparent](/sdk/xpTextTransparent/) | "3" | A transparent text field.
The user can type and the text is drawn, but no background is drawn.You can draw
your own background by adding a widget handler and prehandling the draw message.
|
| [xpTextTranslucent](/sdk/xpTextTranslucent/) | "4" | A translucent edit field,
dark gray. |

### [Text Field Properties](/sdk/Text Field Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_EditFieldSelStart](/sdk/xpProperty_EditFieldSelStart/) | "1400" |
This is the character position the selection starts at, zero based.If it is the
same as the end insertion point, the insertion pointis not a selection. |
| [xpProperty_EditFieldSelEnd](/sdk/xpProperty_EditFieldSelEnd/) | "1401" | This
is the character position of the end of the selection. |
| [xpProperty_EditFieldSelDragStart](/sdk/xpProperty_EditFieldSelDragStart/) |
"1402" | This is the character position a drag was started at if the user is
dragging to select text, or -1 if a drag is not in progress. |
| [xpProperty_TextFieldType](/sdk/xpProperty_TextFieldType/) | "1403" | This is
the type of text field to display, from the above list. |
| [xpProperty_PasswordMode](/sdk/xpProperty_PasswordMode/) | "1404" | Set this
property to 1 to password protect the field. Characters will be drawn as *s even
though the descriptor will contain plain-text. |
| [xpProperty_MaxCharacters](/sdk/xpProperty_MaxCharacters/) | "1405" | The max
number of characters you can enter, if limited. Zero means unlimited. |
| [xpProperty_ScrollPosition](/sdk/xpProperty_ScrollPosition/) | "1406" | The
first visible character on the left. This effectively scrolls the text field. |
| [xpProperty_Font](/sdk/xpProperty_Font/) | "1407" | The font to draw the
field's text with. (An[XPLMFontID](/sdk/XPLMFontID/).) |
| [xpProperty_ActiveEditSide](/sdk/xpProperty_ActiveEditSide/) | "1408" | This
is the active side of the insert selection. (Internal) |

### [Text Field Messages](/sdk/Text Field Messages/)

| Name | Value | Description |
| --- | --- | --- |
| [xpMsg_TextFieldChanged](/sdk/xpMsg_TextFieldChanged/) | "1400" | The text
field sends this message to itself when its text changes. It sends the message
up the call chain; param1 is the text field's widget ID. |

## SCROLL BAR

A standard scroll bar or slider control. The scroll bar has a minimum, maximum
and current value that is updated when the user drags it. The scroll bar sends
continuous messages as it is dragged.

### [xpWidgetClass_ScrollBar](/sdk/xpWidgetClass_ScrollBar/)

```cpp
#define xpWidgetClass_ScrollBar 5
```

### [Scroll Bar Type Values](/sdk/Scroll Bar Type Values/)

This defines how the scroll bar looks.

| Name | Value | Description |
| --- | --- | --- |
| [xpScrollBarTypeScrollBar](/sdk/xpScrollBarTypeScrollBar/) | "0" | A standard
X-Plane scroll bar (with arrows on the ends). |
| [xpScrollBarTypeSlider](/sdk/xpScrollBarTypeSlider/) | "1" | A slider, no
arrows. |

### [Scroll Bar Properties](/sdk/Scroll Bar Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_ScrollBarSliderPosition](/sdk/xpProperty_ScrollBarSliderPosition/)
| "1500" | The current position of the thumb (in between the min and max,
inclusive) |
| [xpProperty_ScrollBarMin](/sdk/xpProperty_ScrollBarMin/) | "1501" | The value
the scroll bar has when the thumb is in the lowest position. |
| [xpProperty_ScrollBarMax](/sdk/xpProperty_ScrollBarMax/) | "1502" | The value
the scroll bar has when the thumb is in the highest position. |
| [xpProperty_ScrollBarPageAmount](/sdk/xpProperty_ScrollBarPageAmount/) |
"1503" | How many units to move the scroll bar when clicking next to the thumb.
The scroll bar always moves one unit when the arrows are clicked. |
| [xpProperty_ScrollBarType](/sdk/xpProperty_ScrollBarType/) | "1504" | The type
of scrollbar from the enums above. |
| [xpProperty_ScrollBarSlop](/sdk/xpProperty_ScrollBarSlop/) | "1505" | Used
internally. |

### [Scroll Bar Messages](/sdk/Scroll Bar Messages/)

| Name | Value | Description |
| --- | --- | --- |
|
[xpMsg_ScrollBarSliderPositionChanged](/sdk/xpMsg_ScrollBarSliderPositionChanged/)
| "1500" | The scroll bar sends this message when the slider position changes.
It sends the message up the call chain; param1 is the scroll bar widget ID. |

## CAPTION

A caption is a simple widget that shows its descriptor as a string, useful for
labeling parts of a window. It always shows its descriptor as its string and is
otherwise transparent.

### [xpWidgetClass_Caption](/sdk/xpWidgetClass_Caption/)

```cpp
#define xpWidgetClass_Caption 6
```

### [Caption Properties](/sdk/Caption Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_CaptionLit](/sdk/xpProperty_CaptionLit/) | "1600" | This property
specifies whether the caption is lit; use lit captions against screens. |

## GENERAL GRAPHICS

The general graphics widget can show one of many icons available from X-Plane.

### [xpWidgetClass_GeneralGraphics](/sdk/xpWidgetClass_GeneralGraphics/)

```cpp
#define xpWidgetClass_GeneralGraphics 7
```

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

### [General Graphics Properties](/sdk/General Graphics Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_GeneralGraphicsType](/sdk/xpProperty_GeneralGraphicsType/) |
"1700" | This property controls the type of icon that is drawn. |

## PROGRESS INDICATOR

This widget implements a progress indicator as seen when X-Plane starts up.

### [xpWidgetClass_Progress](/sdk/xpWidgetClass_Progress/)

```cpp
#define xpWidgetClass_Progress 8
```

### [Progress Indicator Properties](/sdk/Progress Indicator Properties/)

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_ProgressPosition](/sdk/xpProperty_ProgressPosition/) | "1800" |
This is the current value of the progress indicator. |
| [xpProperty_ProgressMin](/sdk/xpProperty_ProgressMin/) | "1801" | This is the
minimum value, equivalent to 0% filled. |
| [xpProperty_ProgressMax](/sdk/xpProperty_ProgressMax/) | "1802" | This is the
maximum value, equivalent to 100% filled. |

### [XPUCreateWidgets](/sdk/XPUCreateWidgets/)

```cpp
WIDGET_API void       XPUCreateWidgets(
                         const XPWidgetCreate_t * inWidgetDefs,
                         int                  inCount,
                         XPWidgetID           inParamParent,
                         XPWidgetID *         ioWidgets);

```

This function creates a series of widgets from a table (see XPCreateWidget_t
above). Pass in an array of widget creation structures and an array of widget
IDs that will receive each widget.

Widget parents are specified by index into the created widget table, allowing
you to create nested widget structures. You can create multiple widget trees in
one table. Generally you should create widget trees from the top down.

You can also pass in a widget ID that will be used when the widget’s parent is
listed as[PARAM_PARENT](/sdk/PARAM_PARENT/); this allows you to embed widgets
created with[XPUCreateWidgets](/sdk/XPUCreateWidgets/)in a widget created
previously.

### [XPUDragWidget](/sdk/XPUDragWidget/)

```cpp
WIDGET_API int        XPUDragWidget(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2,
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

[XPUDragWidget](/sdk/XPUDragWidget/)drags the widget in response to mouse
clicks. Pass in not only the event, but the global coordinates of the drag
region, which might be a sub-region of your widget (for example, a title bar).

### [XPUMoveWidgetBy](/sdk/XPUMoveWidgetBy/)

```cpp
WIDGET_API void       XPUMoveWidgetBy(
                         XPWidgetID           inWidget,
                         int                  inDeltaX,
                         int                  inDeltaY);

```

Simply moves a widget by an amount, +x = right, +y = up, without resizing the
widget.

### [XPWidgetClass](/sdk/XPWidgetClass/)

```cpp
typedef int XPWidgetClass;
```

Widget classes define predefined widget types. A widget class basically
specifies from a library the widget function to be used for the widget. Most
widgets can be made right from classes.

### [XPWidgetCreate_t](/sdk/XPWidgetCreate_t/)

This structure contains all of the parameters needed to create a widget. It is
used with[XPUCreateWidgets](/sdk/XPUCreateWidgets/)to create widgets in bulk
from an array. All parameters correspond to those
of[XPCreateWidget](/sdk/XPCreateWidget/)except for the container index.

If the container index is equal to the index of a widget in the array, the
widget in the array passed to[XPUCreateWidgets](/sdk/XPUCreateWidgets/)is used
as the parent of this widget. Note that if you pass an index greater than your
own position in the array, the parent you are requesting will not exist yet.

If the container index is[NO_PARENT](/sdk/NO_PARENT/), the parent widget is
specified as NULL. If the container index is[PARAM_PARENT](/sdk/PARAM_PARENT/),
the widget passed into[XPUCreateWidgets](/sdk/XPUCreateWidgets/)is used.

```cpp
typedef struct {
     int                       left;
     int                       top;
     int                       right;
     int                       bottom;
     int                       visible;
     const char *              descriptor;
     // Whether this widget is a root widget
     int                       isRoot;
     // The index of the widget to be contained within, or a constant
     int                       containerIndex;
     XPWidgetClass             widgetClass;
} XPWidgetCreate_t;
```

# [XPWidgetDefs](/sdk/XPWidgetDefs/)API

## WIDGET DEFINITIONS

A widget is a call-back driven screen entity like a push-button, window, text
entry field, etc.

Use the widget API to create widgets of various classes. You can nest them into
trees of widgets to create complex user interfaces.

### [XPWidgetID](/sdk/XPWidgetID/)

```cpp
typedef void * XPWidgetID;
```

A Widget ID is an opaque unique non-zero handle identifying your widget. Use 0
to specify “no widget”. This type is defined as wide enough to hold a pointer.
You receive a widget ID when you create a new widget and then use that widget ID
to further refer to the widget.

### [XPWidgetPropertyID](/sdk/XPWidgetPropertyID/)

Properties are values attached to instances of your widgets. A property is
identified by a 32-bit ID and its value is the width of a pointer.

Each widget instance may have a property or not have it. When you set a property
on a widget for the first time, the property is added to the widget; it then
stays there for the life of the widget.

Some property IDs are predefined by the widget package; you can make up your own
property IDs as well.

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_Refcon](/sdk/xpProperty_Refcon/) | "0" | A window's refcon is an
opaque value used by client code to find other data based on it. |
| [xpProperty_Dragging](/sdk/xpProperty_Dragging/) | "1" | These properties are
used by the utilities to implement dragging. |
| [xpProperty_DragXOff](/sdk/xpProperty_DragXOff/) | "2" |
| [xpProperty_DragYOff](/sdk/xpProperty_DragYOff/) | "3" |
| [xpProperty_Hilited](/sdk/xpProperty_Hilited/) | "4" | Is the widget
highlighted? (For widgets that support this kind of thing.) |
| [xpProperty_Object](/sdk/xpProperty_Object/) | "5" | Is there a C++ object
attached to this widget? |
| [xpProperty_Clip](/sdk/xpProperty_Clip/) | "6" | If this property is 1, the
widget package will use OpenGL to restrict drawing to the Widget's exposed
rectangle. |
| [xpProperty_Enabled](/sdk/xpProperty_Enabled/) | "7" | Is this widget enabled
(for those that have a disabled state too)? |
| [xpProperty_UserStart](/sdk/xpProperty_UserStart/) | "10000" | NOTE: Property
IDs 1 - 999 are reserved for the widgets library.NOTE: Property IDs 1000 - 9999
are allocated to the standard widget classes provided with the
library.Properties 1000 - 1099 are for widget class 0, 1100 - 1199 for widget
class 1, etc. |

### [XPMouseState_t](/sdk/XPMouseState_t/)

When the mouse is clicked or dragged, a pointer to this structure is passed to
your widget function.

```cpp
typedef struct {
     int                       x;
     int                       y;
     // Mouse button number, left = 0 (right button not yet supported.
     int                       button;
     // Scroll wheel delta (button in this case would be the wheel axis number).
     int                       delta;
} XPMouseState_t;
```

### [XPKeyState_t](/sdk/XPKeyState_t/)

When a key is pressed, a pointer to this struct is passed to your widget
function.

```cpp
typedef struct {
     // The ASCII key that was pressed.  WARNING: this may be 0 for some non-ASCII key sequences.
     char                      key;
     // The flags.  Make sure to check this if you only want key-downs!
     XPLMKeyFlags              flags;
     // The virtual key code for the key
     char                      vkey;
} XPKeyState_t;
```

### [XPWidgetGeometryChange_t](/sdk/XPWidgetGeometryChange_t/)

This structure contains the deltas for your widget’s geometry when it changes.

```cpp
typedef struct {
     int                       dx;
     // +Y = the widget moved up
     int                       dy;
     int                       dwidth;
     int                       dheight;
} XPWidgetGeometryChange_t;
```

### [XPDispatchMode](/sdk/XPDispatchMode/)

The dispatching modes describe how the widgets library sends out messages.
Currently there are three modes:

| Name | Value | Description |
| --- | --- | --- |
| [xpMode_Direct](/sdk/xpMode_Direct/) | "0" | The message will only be sent to
the target widget. |
| [xpMode_UpChain](/sdk/xpMode_UpChain/) | "1" | The message is sent to the
target widget, then up the chain of parents until the message ishandled or a
parentless widget is reached. |
| [xpMode_Recursive](/sdk/xpMode_Recursive/) | "2" | The message is sent to the
target widget and then all of its children recursively depth-first. |
| [xpMode_DirectAllCallbacks](/sdk/xpMode_DirectAllCallbacks/) | "3" | The
message is sent just to the target, but goes to every callback, even if it is
handled. |
| [xpMode_Once](/sdk/xpMode_Once/) | "4" | The message is only sent to the very
first handler even if it is not accepted. (This is really only useful for some
internal widget library functions.) |

### [XPWidgetClass](/sdk/XPWidgetClass/)

```cpp
typedef int XPWidgetClass;
```

Widget classes define predefined widget types. A widget class basically
specifies from a library the widget function to be used for the widget. Most
widgets can be made right from classes.

### [xpWidgetClass_None](/sdk/xpWidgetClass_None/)

```cpp
#define xpWidgetClass_None   0
```

An unspecified widget class. Other widget classes are
in[XPStandardWidgets](/sdk/XPStandardWidgets/).h

## WIDGET MESSAGES

### [XPWidgetMessage](/sdk/XPWidgetMessage/)

Widgets receive 32-bit messages indicating what action is to be taken or
notifications of events. The list of messages may be expanded.

| Name | Value | Description |
| --- | --- | --- |
| [xpMsg_None](/sdk/xpMsg_None/) | "0" | No message, should not be sent. |
| [xpMsg_Create](/sdk/xpMsg_Create/) | "1" | The create message is sent once per
widget that is created with your widget function and oncefor any widget that has
your widget function attached.Dispatching: DirectParam 1: 1 if you are being
added as a subclass, 0 if the widget is first being created. |
| [xpMsg_Destroy](/sdk/xpMsg_Destroy/) | "2" | The destroy message is sent once
for each message that is destroyed that has your widget function.Dispatching:
Direct for allParam 1: 1 if being deleted by a recursive delete to the parent, 0
for explicit deletion. |
| [xpMsg_Paint](/sdk/xpMsg_Paint/) | "3" | The paint message is sent to your
widget to draw itself. The paint message is the bare-bonesmessage; in response
you must draw yourself, draw your children, set up clipping and culling,check
for visibility, etc. If you don't want to do all of this, ignore the paint
message anda draw message (see below) will be sent to you.Dispatching: Direct |
| [xpMsg_Draw](/sdk/xpMsg_Draw/) | "4" | The draw message is sent to your widget
when it is time to draw yourself. OpenGL will be set upto draw in 2-d global
screen coordinates, but you should use the XPLM to set up OpenGL
state.Dispatching: Direct |
| [xpMsg_KeyPress](/sdk/xpMsg_KeyPress/) | "5" | The key press message is sent
once per key that is pressed. The first parameter is the type of keycode
(integer or char) and the second is the code itself. By handling this event, you
consume thekey stroke.Handling this message 'consumes' the keystroke; not
handling it passes it to your parent widget.Dispatching: Up ChainParam 1: A
pointer to an[XPKeyState_t](/sdk/XPKeyState_t/)structure with the keystroke. |
| [xpMsg_KeyTakeFocus](/sdk/xpMsg_KeyTakeFocus/) | "6" | Keyboard focus is being
given to you. By handling this message you accept keyboard focus. Thefirst
parameter will be one if a child of yours gave up focus to you, 0 if someone set
focus onyou explicitly.Handling this message accepts focus; not handling refuses
focus.Dispatching: directParam 1: 1 if you are gaining focus because your child
is giving it up, 0 if someone is explicitlygiving you focus. |
| [xpMsg_KeyLoseFocus](/sdk/xpMsg_KeyLoseFocus/) | "7" | Keyboard focus is being
taken away from you. The first parameter will be 1 if you are losingfocus
because another widget is taking it, or 0 if someone called the API to make you
lose focusexplicitly.Dispatching: DirectParam 1: 1 if focus is being taken by
another widget, 0 if code requested to remove focus. |
| [xpMsg_MouseDown](/sdk/xpMsg_MouseDown/) | "8" | You receive one mousedown
event per click with a mouse-state structure pointed to by parameter 1.By
accepting this you eat the click, otherwise your parent gets it. You will not
receive drag andmouse up messages if you do not accept the down message.Handling
this message consumes the mouse click, not handling it passes it to the next
widget.You can act 'transparent' as a window by never handling moues clicks to
certain areas.Dispatching: Up chain NOTE: Technically this is direct dispatched,
but the widgets library will shipit to each widget until one consumes the click,
making it effectively "up chain".Param 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |
| [xpMsg_MouseDrag](/sdk/xpMsg_MouseDrag/) | "9" | You receive a series of mouse
drag messages (typically one per frame in the sim) as the mouse ismoved once you
have accepted a mouse down message. Parameter one points to a mouse-state
structuredescribing the mouse location. You will continue to receive these until
the mouse button isreleased.You may receive multiple mouse state messages with
the same mouse position. You will receive mousedrag events even if the mouse is
dragged out of your current or original bounds at the time of themouse
down.Dispatching: DirectParam 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |
| [xpMsg_MouseUp](/sdk/xpMsg_MouseUp/) | "10" | The mouseup event is sent once
when the mouse button is released after a drag or click. You onlyreceive this
message if you accept the mouseDown message. Parameter one points to a mouse
statestructure.Dispatching: DirectParam 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |
| [xpMsg_Reshape](/sdk/xpMsg_Reshape/) | "11" | Your geometry or a child's
geometry is being changed.Dispatching: Up chainParam 1: The widget ID of the
original reshaped target.Param 2: A pointer to
a[XPWidgetGeometryChange_t](/sdk/XPWidgetGeometryChange_t/)struct describing the
change. |
| [xpMsg_ExposedChanged](/sdk/xpMsg_ExposedChanged/) | "12" | Your exposed area
has changed.Dispatching: Direct |
| [xpMsg_AcceptChild](/sdk/xpMsg_AcceptChild/) | "13" | A child has been added
to you. The child's ID is passed in parameter one.Dispatching: DirectParam 1:
The Widget ID of the child being added. |
| [xpMsg_LoseChild](/sdk/xpMsg_LoseChild/) | "14" | A child has been removed
from you. The child's ID is passed in parameter one.Dispatching: DirectParam 1:
The Widget ID of the child being removed. |
| [xpMsg_AcceptParent](/sdk/xpMsg_AcceptParent/) | "15" | You now have a new
parent, or have no parent. The parent's ID is passed in, or 0 for no
parent.Dispatching: DirectParam 1: The Widget ID of your parent |
| [xpMsg_Shown](/sdk/xpMsg_Shown/) | "16" | You or a child has been shown. Note
that this does not include you being shown because your parentwas shown, you
were put in a new parent, your root was shown, etc.Dispatching: Up chainParam 1:
The widget ID of the shown widget. |
| [xpMsg_Hidden](/sdk/xpMsg_Hidden/) | "17" | You have been hidden. See
limitations above.Dispatching: Up chainParam 1: The widget ID of the hidden
widget. |
| [xpMsg_DescriptorChanged](/sdk/xpMsg_DescriptorChanged/) | "18" | Your
descriptor has changed.Dispatching: Direct |
| [xpMsg_PropertyChanged](/sdk/xpMsg_PropertyChanged/) | "19" | A property has
changed. Param 1 contains the property ID.Dispatching: DirectParam 1: The
Property ID being changed.Param 2: The new property value |
| [xpMsg_MouseWheel](/sdk/xpMsg_MouseWheel/) | "20" | The mouse wheel has
moved.Return 1 to consume the mouse wheel move, or 0 to pass the message to a
parent.Dispatching: Up chainParam 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)containing the mouse status. |
| [xpMsg_CursorAdjust](/sdk/xpMsg_CursorAdjust/) | "21" | The cursor is over
your widget. If you consume this message, change
the[XPLMCursorStatus](/sdk/XPLMCursorStatus/)value to indicate the desired
result, with the same rules as in[XPLMDisplay](/sdk/XPLMDisplay/).h.Return 1 to
consume this message, 0 to pass it on.Dispatching: Up chainParam 1: A pointer to
an[XPMouseState_t](/sdk/XPMouseState_t/)struct containing the mouse status.Param
2: A pointer to a[XPLMCursorStatus](/sdk/XPLMCursorStatus/)- set this to the
cursor result you desire. |
| [xpMsg_UserStart](/sdk/xpMsg_UserStart/) | "10000" | NOTE: Message IDs 1000 -
9999 are allocated to the standard widget classes provided with the librarywith
1000 - 1099 for widget class 0, 1100 - 1199 for widget class 1, etc. Message IDs
10,000 andbeyond are for plugin use. |

## WIDGET CALLBACK FUNCTION

### [XPWidgetFunc_t](/sdk/XPWidgetFunc_t/)

```cpp
typedef int (* XPWidgetFunc_t)(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2);

```

This function defines your custom widget’s behavior. It will be called by the
widgets library to send messages to your widget. The message and widget ID are
passed in, as well as two pointer-width signed parameters whose meaning varies
with the message. Return 1 to indicate that you have processed the message, 0 to
indicate that you have not. For any message that is not understood, return 0.

### [XPWidgetFunc_t](/sdk/XPWidgetFunc_t/)

```cpp
typedef int (* XPWidgetFunc_t)(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2);

```

This function defines your custom widget’s behavior. It will be called by the
widgets library to send messages to your widget. The message and widget ID are
passed in, as well as two pointer-width signed parameters whose meaning varies
with the message. Return 1 to indicate that you have processed the message, 0 to
indicate that you have not. For any message that is not understood, return 0.

### [XPWidgetGeometryChange_t](/sdk/XPWidgetGeometryChange_t/)

This structure contains the deltas for your widget’s geometry when it changes.

```cpp
typedef struct {
     int                       dx;
     // +Y = the widget moved up
     int                       dy;
     int                       dwidth;
     int                       dheight;
} XPWidgetGeometryChange_t;
```

### [XPWidgetID](/sdk/XPWidgetID/)

```cpp
typedef void * XPWidgetID;
```

A Widget ID is an opaque unique non-zero handle identifying your widget. Use 0
to specify “no widget”. This type is defined as wide enough to hold a pointer.
You receive a widget ID when you create a new widget and then use that widget ID
to further refer to the widget.

### [XPWidgetPropertyID](/sdk/XPWidgetPropertyID/)

Properties are values attached to instances of your widgets. A property is
identified by a 32-bit ID and its value is the width of a pointer.

Each widget instance may have a property or not have it. When you set a property
on a widget for the first time, the property is added to the widget; it then
stays there for the life of the widget.

Some property IDs are predefined by the widget package; you can make up your own
property IDs as well.

| Name | Value | Description |
| --- | --- | --- |
| [xpProperty_Refcon](/sdk/xpProperty_Refcon/) | "0" | A window's refcon is an
opaque value used by client code to find other data based on it. |
| [xpProperty_Dragging](/sdk/xpProperty_Dragging/) | "1" | These properties are
used by the utilities to implement dragging. |
| [xpProperty_DragXOff](/sdk/xpProperty_DragXOff/) | "2" |
| [xpProperty_DragYOff](/sdk/xpProperty_DragYOff/) | "3" |
| [xpProperty_Hilited](/sdk/xpProperty_Hilited/) | "4" | Is the widget
highlighted? (For widgets that support this kind of thing.) |
| [xpProperty_Object](/sdk/xpProperty_Object/) | "5" | Is there a C++ object
attached to this widget? |
| [xpProperty_Clip](/sdk/xpProperty_Clip/) | "6" | If this property is 1, the
widget package will use OpenGL to restrict drawing to the Widget's exposed
rectangle. |
| [xpProperty_Enabled](/sdk/xpProperty_Enabled/) | "7" | Is this widget enabled
(for those that have a disabled state too)? |
| [xpProperty_UserStart](/sdk/xpProperty_UserStart/) | "10000" | NOTE: Property
IDs 1 - 999 are reserved for the widgets library.NOTE: Property IDs 1000 - 9999
are allocated to the standard widget classes provided with the
library.Properties 1000 - 1099 are for widget class 0, 1100 - 1199 for widget
class 1, etc. |

# [XPWidgetUtils](/sdk/XPWidgetUtils/)API

## USAGE NOTES

The[XPWidgetUtils](/sdk/XPWidgetUtils/)library contains useful functions that
make writing and using widgets less of a pain.

One set of functions are the widget behavior functions. These functions each add
specific useful behaviors to widgets. They can be used in two manners:

1. You can add a widget behavior function to a widget as a callback proc using
   the[XPAddWidgetCallback](/sdk/XPAddWidgetCallback/)function. The widget will
   gain that behavior. Remember that the last function you add has highest
   priority. You can use this to change or augment the behavior of an existing
   finished widget.
2. You can call a widget function from inside your own widget function. This allows
   you to include useful behaviors in custom-built widgets. A number of the
   standard widgets get their behavior from this library. To do this, call the
   behavior function from your function first. If it returns 1, that means it
   handled the event and you don’t need to; simply return 1.

## GENERAL UTILITIES

### [XPWidgetCreate_t](/sdk/XPWidgetCreate_t/)

This structure contains all of the parameters needed to create a widget. It is
used with[XPUCreateWidgets](/sdk/XPUCreateWidgets/)to create widgets in bulk
from an array. All parameters correspond to those
of[XPCreateWidget](/sdk/XPCreateWidget/)except for the container index.

If the container index is equal to the index of a widget in the array, the
widget in the array passed to[XPUCreateWidgets](/sdk/XPUCreateWidgets/)is used
as the parent of this widget. Note that if you pass an index greater than your
own position in the array, the parent you are requesting will not exist yet.

If the container index is[NO_PARENT](/sdk/NO_PARENT/), the parent widget is
specified as NULL. If the container index is[PARAM_PARENT](/sdk/PARAM_PARENT/),
the widget passed into[XPUCreateWidgets](/sdk/XPUCreateWidgets/)is used.

```cpp
typedef struct {
     int                       left;
     int                       top;
     int                       right;
     int                       bottom;
     int                       visible;
     const char *              descriptor;
     // Whether this widget is a root widget
     int                       isRoot;
     // The index of the widget to be contained within, or a constant
     int                       containerIndex;
     XPWidgetClass             widgetClass;
} XPWidgetCreate_t;
```

### [NO_PARENT](/sdk/NO_PARENT/)

```cpp
#define NO_PARENT            -1
```

### [PARAM_PARENT](/sdk/PARAM_PARENT/)

```cpp
#define PARAM_PARENT         -2
```

### [XPUCreateWidgets](/sdk/XPUCreateWidgets/)

```cpp
WIDGET_API void       XPUCreateWidgets(
                         const XPWidgetCreate_t * inWidgetDefs,
                         int                  inCount,
                         XPWidgetID           inParamParent,
                         XPWidgetID *         ioWidgets);

```

This function creates a series of widgets from a table (see XPCreateWidget_t
above). Pass in an array of widget creation structures and an array of widget
IDs that will receive each widget.

Widget parents are specified by index into the created widget table, allowing
you to create nested widget structures. You can create multiple widget trees in
one table. Generally you should create widget trees from the top down.

You can also pass in a widget ID that will be used when the widget’s parent is
listed as[PARAM_PARENT](/sdk/PARAM_PARENT/); this allows you to embed widgets
created with[XPUCreateWidgets](/sdk/XPUCreateWidgets/)in a widget created
previously.

### [XPUMoveWidgetBy](/sdk/XPUMoveWidgetBy/)

```cpp
WIDGET_API void       XPUMoveWidgetBy(
                         XPWidgetID           inWidget,
                         int                  inDeltaX,
                         int                  inDeltaY);

```

Simply moves a widget by an amount, +x = right, +y = up, without resizing the
widget.

## LAYOUT MANAGERS

The layout managers are widget behavior functions for handling where widgets
move. Layout managers can be called from a widget function or attached to a
widget later.

### [XPUFixedLayout](/sdk/XPUFixedLayout/)

```cpp
WIDGET_API int        XPUFixedLayout(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2);

```

This function causes the widget to maintain its children in fixed position
relative to itself as it is resized. Use this on the top level ‘window’ widget
for your window.

## WIDGET PROC BEHAVIORS

These widget behavior functions add other useful behaviors to widgets. These
functions cannot be attached to a widget; they must be called from your widget
function.

### [XPUSelectIfNeeded](/sdk/XPUSelectIfNeeded/)

```cpp
WIDGET_API int        XPUSelectIfNeeded(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2,
                         int                  inEatClick);

```

This causes the widget to bring its window to the foreground if it is not
already. inEatClick specifies whether clicks in the background should be
consumed by bringing the window to the foreground.

### [XPUDefocusKeyboard](/sdk/XPUDefocusKeyboard/)

```cpp
WIDGET_API int        XPUDefocusKeyboard(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2,
                         int                  inEatClick);

```

This causes the widget to send keyboard focus back to X-Plane. This stops
editing of any text fields, etc.

### [XPUDragWidget](/sdk/XPUDragWidget/)

```cpp
WIDGET_API int        XPUDragWidget(
                         XPWidgetMessage      inMessage,
                         XPWidgetID           inWidget,
                         intptr_t             inParam1,
                         intptr_t             inParam2,
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

[XPUDragWidget](/sdk/XPUDragWidget/)drags the widget in response to mouse
clicks. Pass in not only the event, but the global coordinates of the drag
region, which might be a sub-region of your widget (for example, a title bar).

# [XPWidgets](/sdk/XPWidgets/)API

## THEORY OF OPERATION AND NOTES

Widgets are persistent view ‘objects’ for X-Plane. A widget is an object
referenced by its opaque handle (widget ID) and the APIs in this file. You
cannot access the widget’s guts directly. Every Widget has the following
intrinsic data:

- A bounding box defined in global screen coordinates with 0,0 in the bottom left and +y = up, +x = right.
- A visible box, which is the intersection of the bounding box with the widget’s parents visible box.
- Zero or one parent widgets. (Always zero if the widget is a root widget.
- Zero or more child widgets.
- Whether the widget is a root. Root widgets are the top level plugin windows.
- Whether the widget is visible.
- A text string descriptor, whose meaning varies from widget to widget.
- An arbitrary set of 32 bit integral properties defined by 32-bit integral keys. This is how specific widgets store specific data.
- A list of widget callback procedures that implements the widgets behaviors.

The Widgets library sends messages to widgets to request specific behaviors or
notify the widget of things.

Widgets may have more than one callback function, in which case messages are
sent to the most recently added callback function until the message is handled.
Messages may also be sent to parents or children; see
the[XPWidgetDefs](/sdk/XPWidgetDefs/).h header file for the different widget
message dispatching functions. By adding a callback function to a window you can
‘subclass’ its behavior.

A set of standard widgets are provided that serve common UI purposes. You can
also customize or implement entirely custom widgets.

Widgets are different than other view hierarchies (most notably Win32, which
they bear a striking resemblance to) in the following ways:

- Not all behavior can be patched. State that is managed by the[XPWidgets](/sdk/XPWidgets/)DLL and not by individual widgets cannot be customized.
- All coordinates are in global screen coordinates. Coordinates are not relative to an enclosing widget, nor are they relative to a display window.
- Widget messages are always dispatched synchronously, and there is no concept of scheduling an update or a dirty region. Messages originate from X-Plane as the sim cycle goes by. Since X-Plane is constantly redrawing, so are widgets; there is no need to mark a part of a widget as ‘needing redrawing’ because redrawing happens frequently whether the widget needs it or not.
- Any widget may be a ‘root’ widget, causing it to be drawn; there is no relationship between widget class and rootness. Root widgets are implemented as[XPLMDisplay](/sdk/XPLMDisplay/)windows.

## WIDGET CREATION AND MANAGEMENT

### [XPCreateWidget](/sdk/XPCreateWidget/)

```cpp
WIDGET_API XPWidgetID XPCreateWidget(
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom,
                         int                  inVisible,
                         const char *         inDescriptor,
                         int                  inIsRoot,
                         XPWidgetID           inContainer,
                         XPWidgetClass        inClass);

```

This function creates a new widget and returns the new widget’s ID to you. If
the widget creation fails for some reason, it returns NULL. Widget creation will
fail either if you pass a bad class ID or if there is not adequate memory.

Input Parameters:

- Top, left, bottom, and right in global screen coordinates defining the widget’s location on the screen.
- inVisible is 1 if the widget should be drawn, 0 to start the widget as hidden.
- inDescriptor is a null terminated string that will become the widget’s descriptor.
- inIsRoot is 1 if this is going to be a root widget, 0 if it will not be.
- inContainer is the ID of this widget’s container. It must be 0 for a root widget. For a non-root widget, pass the widget ID of the widget to place this widget within. If this widget is not going to start inside another widget, pass 0; this new widget will be created but will not be drawn until it is placed inside another widget.
- inClass is the class of the widget to draw. Use one of the predefined class-IDs to create a standard widget.

A note on widget embedding: a widget is only called (and will be drawn, etc.) if
it is placed within a widget that will be called. Root widgets are always
called. So it is possible to have whole chains of widgets that are simply not
called. You can preconstruct widget trees and then place them into root widgets
later to activate them if you wish.

### [XPCreateCustomWidget](/sdk/XPCreateCustomWidget/)

```cpp
WIDGET_API XPWidgetID XPCreateCustomWidget(
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom,
                         int                  inVisible,
                         const char *         inDescriptor,
                         int                  inIsRoot,
                         XPWidgetID           inContainer,
                         XPWidgetFunc_t       inCallback);

```

This function is the same as[XPCreateWidget](/sdk/XPCreateWidget/)except that
instead of passing a class ID, you pass your widget callback function pointer
defining the widget. Use this function to define a custom widget. All parameters
are the same as[XPCreateWidget](/sdk/XPCreateWidget/), except that the widget
class has been replaced with the widget function.

### [XPDestroyWidget](/sdk/XPDestroyWidget/)

```cpp
WIDGET_API void       XPDestroyWidget(
                         XPWidgetID           inWidget,
                         int                  inDestroyChildren);

```

This class destroys a widget. Pass in the ID of the widget to kill. If you pass
1 for inDestroyChilren, the widget’s children will be destroyed first, then this
widget will be destroyed. (Furthermore, the widget’s children will be destroyed
with the inDestroyChildren flag set to 1, so the destruction will recurse down
the widget tree.) If you pass 0 for this flag, direct child widgets will simply
end up with their parent set to 0.

### [XPSendMessageToWidget](/sdk/XPSendMessageToWidget/)

```cpp
WIDGET_API int        XPSendMessageToWidget(
                         XPWidgetID           inWidget,
                         XPWidgetMessage      inMessage,
                         XPDispatchMode       inMode,
                         intptr_t             inParam1,
                         intptr_t             inParam2);

```

This sends any message to a widget. You should probably not go around simulating
the predefined messages that the widgets library defines for you. You may
however define custom messages for your widgets and send them with this method.

This method supports several dispatching patterns;
see[XPDispatchMode](/sdk/XPDispatchMode/)for more info. The function returns 1
if the message was handled, 0 if it was not.

For each widget that receives the message (see the dispatching modes), each
widget function from the most recently installed to the oldest one receives the
message in order until it is handled.

## WIDGET POSITIONING AND VISIBILITY

### [XPPlaceWidgetWithin](/sdk/XPPlaceWidgetWithin/)

```cpp
WIDGET_API void       XPPlaceWidgetWithin(
                         XPWidgetID           inSubWidget,
                         XPWidgetID           inContainer);

```

This function changes which container a widget resides in. You may NOT use this
function on a root widget! inSubWidget is the widget that will be moved. Pass a
widget ID in inContainer to make inSubWidget be a child of inContainer. It will
become the last/closest widget in the container. Pass 0 to remove the widget
from any container. Any call to this other than passing the widget ID of the old
parent of the affected widget will cause the widget to be removed from its old
parent. Placing a widget within its own parent simply makes it the last widget.

NOTE: this routine does not reposition the sub widget in global coordinates. If
the container has layout management code, it will reposition the subwidget for
you, otherwise you must do it with SetWidgetGeometry.

### [XPCountChildWidgets](/sdk/XPCountChildWidgets/)

```cpp
WIDGET_API int        XPCountChildWidgets(
                         XPWidgetID           inWidget);

```

This routine returns the number of widgets another widget contains.

### [XPGetNthChildWidget](/sdk/XPGetNthChildWidget/)

```cpp
WIDGET_API XPWidgetID XPGetNthChildWidget(
                         XPWidgetID           inWidget,
                         int                  inIndex);

```

This routine returns the widget ID of a child widget by index. Indexes are 0
based, from 0 to the number of widgets in the parentone minus one, inclusive. If
the index is invalid, 0 is returned.

### [XPGetParentWidget](/sdk/XPGetParentWidget/)

```cpp
WIDGET_API XPWidgetID XPGetParentWidget(
                         XPWidgetID           inWidget);

```

Returns the parent of a widget, or 0 if the widget has no parent. Root widgets
never have parents and therefore always return 0.

### [XPShowWidget](/sdk/XPShowWidget/)

```cpp
WIDGET_API void       XPShowWidget(
                         XPWidgetID           inWidget);

```

This routine makes a widget visible if it is not already. Note that if a widget
is not in a rooted widget hierarchy or one of its parents is not visible, it
will still not be visible to the user.

### [XPHideWidget](/sdk/XPHideWidget/)

```cpp
WIDGET_API void       XPHideWidget(
                         XPWidgetID           inWidget);

```

Makes a widget invisible. See[XPShowWidget](/sdk/XPShowWidget/)for
considerations of when a widget might not be visible despite its own visibility
state.

### [XPIsWidgetVisible](/sdk/XPIsWidgetVisible/)

```cpp
WIDGET_API int        XPIsWidgetVisible(
                         XPWidgetID           inWidget);

```

This returns 1 if a widget is visible, 0 if it is not. Note that this routine
takes into consideration whether a parent is invisible. Use this routine to tell
if the user can see the widget.

### [XPFindRootWidget](/sdk/XPFindRootWidget/)

```cpp
WIDGET_API XPWidgetID XPFindRootWidget(
                         XPWidgetID           inWidget);

```

Returns the Widget ID of the root widget that contains the passed in widget or
NULL if the passed in widget is not in a rooted hierarchy.

### [XPBringRootWidgetToFront](/sdk/XPBringRootWidgetToFront/)

```cpp
WIDGET_API void       XPBringRootWidgetToFront(
                         XPWidgetID           inWidget);

```

This routine makes the specified widget be in the frontmost widget hierarchy. If
this widget is a root widget, its widget hierarchy comes to front, otherwise the
widget’s root is brought to the front. If this widget is not in an active widget
hiearchy (e.g. there is no root widget at the top of the tree), this routine
does nothing.

### [XPIsWidgetInFront](/sdk/XPIsWidgetInFront/)

```cpp
WIDGET_API int        XPIsWidgetInFront(
                         XPWidgetID           inWidget);

```

This routine returns true if this widget’s hierarchy is the frontmost hierarchy.
It returns false if the widget’s hierarchy is not in front, or if the widget is
not in a rooted hierarchy.

### [XPGetWidgetGeometry](/sdk/XPGetWidgetGeometry/)

```cpp
WIDGET_API void       XPGetWidgetGeometry(
                         XPWidgetID           inWidget,
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

This routine returns the bounding box of a widget in global coordinates. Pass
NULL for any parameter you are not interested in.

### [XPSetWidgetGeometry](/sdk/XPSetWidgetGeometry/)

```cpp
WIDGET_API void       XPSetWidgetGeometry(
                         XPWidgetID           inWidget,
                         int                  inLeft,
                         int                  inTop,
                         int                  inRight,
                         int                  inBottom);

```

This function changes the bounding box of a widget.

### [XPGetWidgetForLocation](/sdk/XPGetWidgetForLocation/)

```cpp
WIDGET_API XPWidgetID XPGetWidgetForLocation(
                         XPWidgetID           inContainer,
                         int                  inXOffset,
                         int                  inYOffset,
                         int                  inRecursive,
                         int                  inVisibleOnly);

```

Given a widget and a location, this routine returns the widget ID of the child
of that widget that owns that location. If inRecursive is true then this will
return a child of a child of a widget as it tries to find the deepest widget at
that location. If inVisibleOnly is true, then only visible widgets are
considered, otherwise all widgets are considered. The widget ID passed for
inContainer will be returned if the location is in that widget but not in a
child widget. 0 is returned if the location is not in the container.

NOTE: if a widget’s geometry extends outside its parents geometry, it will not
be returned by this call for mouse locations outside the parent geometry. The
parent geometry limits the child’s eligibility for mouse location.

### [XPGetWidgetExposedGeometry](/sdk/XPGetWidgetExposedGeometry/)

```cpp
WIDGET_API void       XPGetWidgetExposedGeometry(
                         XPWidgetID           inWidgetID,
                         int *                outLeft,    /* Can be NULL */
                         int *                outTop,    /* Can be NULL */
                         int *                outRight,    /* Can be NULL */
                         int *                outBottom);    /* Can be NULL */

```

This routine returns the bounds of the area of a widget that is completely
within its parent widgets. Since a widget’s bounding box can be outside its
parent, part of its area will not be eligible for mouse clicks and should not
draw. Use[XPGetWidgetGeometry](/sdk/XPGetWidgetGeometry/)to find out what area
defines your widget’s shape, but use this routine to find out what area to
actually draw into. Note that the widget library does not use OpenGL clipping to
keep frame rates up, although you could use it internally.

## ACCESSING WIDGET DATA

### [XPSetWidgetDescriptor](/sdk/XPSetWidgetDescriptor/)

```cpp
WIDGET_API void       XPSetWidgetDescriptor(
                         XPWidgetID           inWidget,
                         const char *         inDescriptor);

```

Every widget has a descriptor, which is a text string. What the text string is
used for varies from widget to widget; for example, a push button’s text is its
descriptor, a caption shows its descriptor, and a text field’s descriptor is the
text being edited. In other words, the usage for the text varies from widget to
widget, but this API provides a universal and convenient way to get at it. While
not all UI widgets need their descriptor, many do.

### [XPGetWidgetDescriptor](/sdk/XPGetWidgetDescriptor/)

```cpp
WIDGET_API int        XPGetWidgetDescriptor(
                         XPWidgetID           inWidget,
                         char *               outDescriptor,
                         int                  inMaxDescLength);

```

This routine returns the widget’s descriptor. Pass in the length of the buffer
you are going to receive the descriptor in. The descriptor will be null
terminated for you. This routine returns the length of the actual descriptor; if
you pass NULL for outDescriptor, you can get the descriptor’s length without
getting its text. If the length of the descriptor exceeds your buffer length,
the buffer will not be null terminated (this routine has ‘strncpy’ semantics).

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

### [XPSetWidgetProperty](/sdk/XPSetWidgetProperty/)

```cpp
WIDGET_API void       XPSetWidgetProperty(
                         XPWidgetID           inWidget,
                         XPWidgetPropertyID   inProperty,
                         intptr_t             inValue);

```

This function sets a widget’s property. Properties are arbitrary values
associated by a widget by ID.

### [XPGetWidgetProperty](/sdk/XPGetWidgetProperty/)

```cpp
WIDGET_API intptr_t   XPGetWidgetProperty(
                         XPWidgetID           inWidget,
                         XPWidgetPropertyID   inProperty,
                         int *                inExists);    /* Can be NULL */

```

This routine returns the value of a widget’s property, or 0 if the property is
not defined. If you need to know whether the property is defined, pass a pointer
to an int for inExists; the existence of that property will be returned in the
int. Pass NULL for inExists if you do not need this information.

## KEYBOARD MANAGEMENT

### [XPSetKeyboardFocus](/sdk/XPSetKeyboardFocus/)

```cpp
WIDGET_API XPWidgetID XPSetKeyboardFocus(
                         XPWidgetID           inWidget);

```

Controls which widget will receive keystrokes. Pass the widget ID of the widget
to get the keys. Note that if the widget does not care about keystrokes, they
will go to the parent widget, and if no widget cares about them, they go to
X-Plane.

If you set the keyboard focus to widget ID 0, X-Plane gets keyboard focus.

This routine returns the widget ID that ended up with keyboard focus, or 0 for
X-Plane.

Keyboard focus is not changed if the new widget will not accept it. For setting
to X-Plane, keyboard focus is always accepted.

### [XPLoseKeyboardFocus](/sdk/XPLoseKeyboardFocus/)

```cpp
WIDGET_API void       XPLoseKeyboardFocus(
                         XPWidgetID           inWidget);

```

This causes the specified widget to lose focus; focus is passed to its parent,
or the next parent that will accept it. This routine does nothing if this widget
does not have focus.

### [XPGetWidgetWithFocus](/sdk/XPGetWidgetWithFocus/)

```cpp
WIDGET_API XPWidgetID XPGetWidgetWithFocus(void);

```

This routine returns the widget that has keyboard focus, or 0 if X-Plane has
keyboard focus or some other plugin window that does not have widgets has focus.

## CREATING CUSTOM WIDGETS

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

### [XPGetWidgetClassFunc](/sdk/XPGetWidgetClassFunc/)

```cpp
WIDGET_API XPWidgetFunc_t XPGetWidgetClassFunc(
                         XPWidgetClass        inWidgetClass);

```

Given a widget class, this function returns the callbacks that power that widget
class.

| |  |
| --- | --- | --- |
| [xpButtonBehaviorPushButton](/sdk/xpButtonBehaviorPushButton/) | "0" | Standard push button behavior. The button highlights while the mouse is clickedover it and unhighlights when the mouse is moved outside of it or released.If the mouse is released over the button, the[xpMsg_PushButtonPressed](/sdk/xpMsg_PushButtonPressed/)messageis sent. |

| |  |
| --- | --- | --- |
| [xpButtonBehaviorRadioButton](/sdk/xpButtonBehaviorRadioButton/) | "2" | Radio button behavior. The button immediately sets its state to oneand sends out a[xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/)message if it was not already setto one. You must turn off other radio buttons in a group in your code. |

| |  |
| --- | --- | --- |
| [xpElement_CopyButtons](/sdk/xpElement_CopyButtons/) | "45" | none metal |

| |  |
| --- | --- | --- |
| [xpElement_CopyButtonsWithEditingGrid](/sdk/xpElement_CopyButtonsWithEditingGrid/) | "46" | none metal |

| |  |
| --- | --- | --- |
| [xpElement_PushButton](/sdk/xpElement_PushButton/) | "16" | x metal |

| |  |
| --- | --- | --- |
| [xpElement_PushButtonLit](/sdk/xpElement_PushButtonLit/) | "17" | x metal |

| |  |
| --- | --- | --- |
| [xpElement_ScrollBar](/sdk/xpElement_ScrollBar/) | "48" | THIS CAN PROBABLY BE REMOVED |

| |  |
| --- | --- | --- |
| [xpElement_TextField](/sdk/xpElement_TextField/) | "6" | x metal |

| |  |
| --- | --- | --- |
| [xpElement_TextFieldMiddle](/sdk/xpElement_TextFieldMiddle/) | "52" | x, y metal |

| |  |
| --- | --- | --- |
| [xpMsg_ButtonStateChanged](/sdk/xpMsg_ButtonStateChanged/) | "1301" | This message is sent when a button is clicked that has radio button or check box behaviorand its value changes. (Note that if the value changes by setting a property you do not receivethis message!) Parameter one is the widget ID of the button, parameter 2 is the new state value,either zero or one. This message is dispatched up the widget hierarchy. |

| |  |
| --- | --- | --- |
| [xpMsg_PushButtonPressed](/sdk/xpMsg_PushButtonPressed/) | "1300" | This message is sent when the user completes a click and release in a button withpush button behavior. Parameterone of the message is the widget ID of the button. This message is dispatched up thewidget hierarchy. |

| |  |
| --- | --- | --- |
| [xpMsg_ScrollBarSliderPositionChanged](/sdk/xpMsg_ScrollBarSliderPositionChanged/) | "1500" | The scroll bar sends this message when the slider position changes. It sends the message up the call chain; param1 is the scroll bar widget ID. |

| |  |
| --- | --- | --- |
| [xpMsg_TextFieldChanged](/sdk/xpMsg_TextFieldChanged/) | "1400" | The text field sends this message to itself when its text changes. It sends the message up the call chain; param1 is the text field's widget ID. |

| |  |
| --- | --- | --- |
| [xpProperty_ButtonBehavior](/sdk/xpProperty_ButtonBehavior/) | "1301" | This property sets the button's behavior. Use one of the button behaviors above. |

| |  |
| --- | --- | --- |
| [xpProperty_ButtonState](/sdk/xpProperty_ButtonState/) | "1302" | This property tells whether a check box or radio button is "checked" or not. Not used for push buttons. |

| |  |
| --- | --- | --- |
| [xpProperty_ButtonType](/sdk/xpProperty_ButtonType/) | "1300" | This property sets the visual type of button. Use one of the button types above. |

| |  |
| --- | --- | --- |
| [xpProperty_CaptionLit](/sdk/xpProperty_CaptionLit/) | "1600" | This property specifies whether the caption is lit; use lit captions against screens. |

| |  |
| --- | --- | --- |
| [xpProperty_ProgressMax](/sdk/xpProperty_ProgressMax/) | "1802" | This is the maximum value, equivalent to 100% filled. |

| |  |
| --- | --- | --- |
| [xpProperty_ProgressMin](/sdk/xpProperty_ProgressMin/) | "1801" | This is the minimum value, equivalent to 0% filled. |

| |  |
| --- | --- | --- |
| [xpProperty_ProgressPosition](/sdk/xpProperty_ProgressPosition/) | "1800" | This is the current value of the progress indicator. |

| |  |
| --- | --- | --- |
| [xpProperty_ScrollBarMax](/sdk/xpProperty_ScrollBarMax/) | "1502" | The value the scroll bar has when the thumb is in the highest position. |

| |  |
| --- | --- | --- |
| [xpProperty_ScrollBarMin](/sdk/xpProperty_ScrollBarMin/) | "1501" | The value the scroll bar has when the thumb is in the lowest position. |

| |  |
| --- | --- | --- |
| [xpProperty_ScrollBarPageAmount](/sdk/xpProperty_ScrollBarPageAmount/) | "1503" | How many units to move the scroll bar when clicking next to the thumb. The scroll bar always moves one unit when the arrows are clicked. |

| |  |
| --- | --- | --- |
| [xpProperty_ScrollBarSliderPosition](/sdk/xpProperty_ScrollBarSliderPosition/) | "1500" | The current position of the thumb (in between the min and max, inclusive) |

| |  |
| --- | --- | --- |
| [xpProperty_ScrollBarSlop](/sdk/xpProperty_ScrollBarSlop/) | "1505" | Used internally. |

| |  |
| --- | --- | --- |
| [xpProperty_ScrollBarType](/sdk/xpProperty_ScrollBarType/) | "1504" | The type of scrollbar from the enums above. |

| |  |
| --- | --- | --- |
| [xpProperty_TextFieldType](/sdk/xpProperty_TextFieldType/) | "1403" | This is the type of text field to display, from the above list. |

| |  |
| --- | --- | --- |
| [xpPushButton](/sdk/xpPushButton/) | "0" | This is a standard push button, like an 'OK' or 'Cancel' button in a dialog box. |

| |  |
| --- | --- | --- |
| [xpRadioButton](/sdk/xpRadioButton/) | "1" | A check box or radio button. Use this and the button behaviors below to get the desired behavior. |

| |  |
| --- | --- | --- |
| [xpScrollBarTypeScrollBar](/sdk/xpScrollBarTypeScrollBar/) | "0" | A standard X-Plane scroll bar (with arrows on the ends). |

| |  |
| --- | --- | --- |
| [xpScrollBarTypeSlider](/sdk/xpScrollBarTypeSlider/) | "1" | A slider, no arrows. |

| |  |
| --- | --- | --- |
| [xpTextEntryField](/sdk/xpTextEntryField/) | "0" | A field for text entry. |

| |  |
| --- | --- | --- |
| [xpTrack_Progress](/sdk/xpTrack_Progress/) | "2" | over metal cannot be lit cannot be rotated |

| |  |
| --- | --- | --- |
| [xpTrack_ScrollBar](/sdk/xpTrack_ScrollBar/) | "0" | not over metal can be lit can be rotated |

### [xpWidgetClass_Button](/sdk/xpWidgetClass_Button/)

```cpp
#define xpWidgetClass_Button 3
```

### [xpWidgetClass_Caption](/sdk/xpWidgetClass_Caption/)

```cpp
#define xpWidgetClass_Caption 6
```

### [xpWidgetClass_None](/sdk/xpWidgetClass_None/)

```cpp
#define xpWidgetClass_None   0
```

An unspecified widget class. Other widget classes are
in[XPStandardWidgets](/sdk/XPStandardWidgets/).h

### [xpWidgetClass_Progress](/sdk/xpWidgetClass_Progress/)

```cpp
#define xpWidgetClass_Progress 8
```

### [xpWidgetClass_ScrollBar](/sdk/xpWidgetClass_ScrollBar/)

```cpp
#define xpWidgetClass_ScrollBar 5
```

### [xpWidgetClass_TextField](/sdk/xpWidgetClass_TextField/)

```cpp
#define xpWidgetClass_TextField 4
```

