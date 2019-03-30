import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        x, y = 0, 0
        self.text = "x: {0},  y: {1}".format(x, y)
        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)
        self.setMouseTracking(True)
        self.setLayout(grid)

        self.x, self.y, self.width, self.height = 400, 400, 400, 400
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowTitle('PyQt5 GUI')  
        self.show()

    def mouseMoveEvent(self, e):
        x, y = e.x(), e.y()
        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())