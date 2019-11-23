==============
Intro to UQtie
==============

The basic point of **UQtie** is to make it easy to create a simple GUI app
that supports some useful features that I typically want. So far, these
are:

* Window geometry persistence - you resize and reposition the window,
  then quit the app. Next time you start the app, it starts with the
  size and position you chose.
* Font selection through a Font Dialog
* Zoom in and Zoom out - you use CTRL-+ and CTRL-- to make text, widgets
  and borders larger or smaller
* Qt Stylesheet (QSS) support that doesn't preclude runtime changes to
  look-and-feel attributes (e.g. font)

These are obviously not all the features you might want your app to
have. I intend to add more features as time goes on.

Most of the features are obtained simply by making your main window
a subclass of :code:`UqtWin.MainWindow` instead of
:code:`PyQt5.QtWidgets.QMainWindow`. See :doc:`main_window`.

These are the modules in the **UQtie** package:

+---------------+-----------------------------------------------------------------+
| Module Name   | Purpose                                                         |
+===============+=================================================================+
| UqtMav        | UqtMavConn allows easy use of pymavlink connections in Qt app   |
+---------------+-----------------------------------------------------------------+
| UqtWin        | MainWindow class provides an app main window with features      |
+---------------+-----------------------------------------------------------------+
| UqtStylesheet | Maintains a QSS file with variable properties -                 |
|               | a "poor man's SASS"                                             |
+---------------+-----------------------------------------------------------------+

**UqtMav** is not particularly generic, but I have written a handful of little
MAVLink tools, so MAVLink is generic for *me*
