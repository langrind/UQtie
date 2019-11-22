=======================
Main Application Window
=======================


Most of the features are obtained simply by making your main window
a subclass of :code:`UqtWin.MainWindow` instead of
:code:`PyQt5.QtWidgets.QMainWindow`.


For example, note these three steps in the source of :code:`simple_uqtie.py`
in the :code:`example/` subdirectory of the repo":

1. Import the ``UqtWin`` module::
	
    from   uqtie import UqtWin
    

#. Use :code:`UqtWin.MainWindow` as the base class of the main window::
    
    class TestAppMainWindow(UqtWin.MainWindow):
        def __init__(self, parsedArgs, **kwargs ):
            super(TestAppMainWindow, self).__init__(parsedArgs, **kwargs)
	
#. Instantiate the subclass::

    # can add optional title='<OptionalTitle>' if it is different from your app name
    mainw = TestAppMainWindow(parsedArgs, app=app, organizationName='Craton', appName='UqtTest')

