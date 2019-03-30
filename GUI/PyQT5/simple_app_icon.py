## example3 - An application Icon

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.left, self.top, self.width, self.height = 400, 400, 400, 400
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle('PyQt5 GUI')
        self.setWindowIcon(QIcon('akashjeez_logo.ico'))        
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())