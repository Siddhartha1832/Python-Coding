import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu, QTextEdit, QApplication
from PyQt5.QtGui import QFont, QIcon

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        exitAct = QAction(QIcon('exit_icon.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAct)
        
        self.x, self.y, self.width, self.height = 400, 400, 400, 400
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle('PyQt5 GUI')  
        self.setWindowIcon(QIcon('akashjeez_logo.ico'))   
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())