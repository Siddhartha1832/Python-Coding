import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QMessageBox, QPushButton, QDesktopWidget, QApplication
from PyQt5.QtGui import QFont, QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')
        
        simple_button = QPushButton('Simple Button', self)
        simple_button.setToolTip('This is a <b>QPushButton</b> widget')
        #simple_button.clicked.connect(closeEvent)
        simple_button.resize(simple_button.sizeHint())
        simple_button.move(0, 0) 
        
        quit_button = QPushButton('Quit', self)
        quit_button.setToolTip('This is a <b>Close</b> button')
        quit_button.clicked.connect(QApplication.instance().quit)
        quit_button.resize(quit_button.sizeHint())
        quit_button.move(0, 30)

        self.x, self.y, self.width, self.height = 400, 400, 400, 400
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.center()
        self.setWindowTitle('PyQt5 GUI')  
        self.setWindowIcon(QIcon('akashjeez_logo.ico'))   
        self.show()

    # Function used to centers a window on the screen. 
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())