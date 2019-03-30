import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtGui import QFont, QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.x, self.y, self.width, self.height = 400, 400, 400, 400
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle('PyQt5 GUI')  
        self.setWindowIcon(QIcon('akashjeez_logo.ico'))   
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())