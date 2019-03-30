import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        name_label = QLabel('Akashjeez', self).move(15, 10)
        program_label = QLabel('Python', self).move(35, 40)
        Vehicle = QLabel('Car & Bikes', self).move(55, 70)

        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(ok_button)
        hbox.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)  
        
        self.x, self.y, self.width, self.height = 400, 400, 400, 400
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle('PyQt5 GUI')  
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())