#!/usr/bin/env python

import argparse, sys

from   uqtie           import UqtWin
from   PyQt5.QtWidgets import QApplication

class TestAppMainWindow(UqtWin.MainWindow):

    def __init__(self, parsedArgs, **kwargs ):
        super(TestAppMainWindow, self).__init__(parsedArgs, **kwargs)
        self.show()

parser = argparse.ArgumentParser()
parser.add_argument('-x', '--test', help='Test Argument placeholder', default='Test')
parsedArgs,unparsedArgs = parser.parse_known_args()

# Pass unparsed args to Qt, might have some X Windows args, like --display
qtArgs = sys.argv[:1] + unparsedArgs
app = QApplication(qtArgs)

#mainw = TestAppMainWindow(parsedArgs, app=app, organizationName='Craton', appName='UqtTest', title='OptionalTitle')
mainw = TestAppMainWindow(parsedArgs, app=app, organizationName='Craton', appName='UqtTest')

sys.exit(app.exec_())
