import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button1 = QPushButton("Button 1", self)
        button1.move(30, 50)
        button2 = QPushButton("Button 2", self)
        button2.move(150, 50)
        button1.clicked.connect(self.buttonClicked)            
        button2.clicked.connect(self.buttonClicked)
        
        self.statusBar()

        self.x, self.y, self.width, self.height = 400, 400, 400, 400
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle('PyQt5 GUI')  
        self.show()

    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed!')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
