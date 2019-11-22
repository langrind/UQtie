====================
Stylesheet Variables
====================


There are advantages and disadvantages to Qt stylesheets. Qt stylesheets
partially overlap other Qt features, such as Qt Style. They aren't mutually
exclusive, and they don't all play together either.

UqtStylesheet attempts to make it possible to use a stylesheet while still
using the QFontDialog to select fonts, and zoom-in/zoom-out shortcuts such
as CTRL-+.

The idea is that we have variables (which come from somewhere, right now a
pickled dictionary, but later could be elsewhere, or multiple elsewheres).
These variables can be used in the stylesheet, such that the dynamic changes in
appearance can be made at runtime without requiring stylesheet changes, and the
changes can be persisted also without changing the stylesheet.

Widget sizes (e.g ``QScrollBar:vertical { width }``), Font, and font size seem like
good candidates to be determined dynamically instead of via hardcoded values
in a stylesheet. That way, when you have high-DPI monitor and less-than-perfect
vision, you can adjust easily.

Part of my motivation for doing this is because PyQt running on Windows, Linux,
MacOS and Cygwin doesn't behave identically, not even close to identical in
some ways. If they would all have identical QScreens given identical monitors
and graphics cards, then you could just make reasonable choices for your stylesheet,
and rely on the OS GUI settings.

Variables you can use in a QSS file are::

 $main_font_family
 $main_font_weight (not supported yet)
 $main_font_size
 $scroll_bar_width
