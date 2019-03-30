import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QApplication
from PyQt5.QtGui import QFont, QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar() # create menubar
        fileMenu = menubar.addMenu('&File') # create first menu bar name - File
        new_submenu = QAction('New', self) # New submenu under File menu
        fileMenu.addAction(new_submenu) # add new submenu action under file menu
        import_submenu = QMenu('Import', self) # Import submenu under File menu
        import_action = QAction('Import mail', self) # Import mail submenu under Import submenu
        import_submenu.addAction(import_action) 
        fileMenu.addMenu(import_submenu) # add Import submenu under File menu
        exitAct = QAction(QIcon('exit.png'), '&Exit', self) # exit submenu icon
        exitAct.setShortcut('Ctrl+Q') # exit submenu shorcut
        exitAct.setStatusTip('Exit application') # exit submenu status tooltip
        exitAct.triggered.connect(qApp.quit) # terminate app if click exit submenu
        fileMenu.addAction(exitAct) # add exit submenu under File menu

        viewMenu = menubar.addMenu('View')
        viewStatAct = QAction('View statusbar', self, checkable=True)
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True)
        viewStatAct.triggered.connect(self.toggleMenu)
        viewMenu.addAction(viewStatAct)

        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        self.x, self.y, self.width, self.height = 400, 400, 400, 400
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle('PyQt5 GUI')  
        self.setWindowIcon(QIcon('akashjeez_logo.ico'))   
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())