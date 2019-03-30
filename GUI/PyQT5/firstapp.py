# example 2 - first app 

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(500, 500) # resizes the widget of 500px wide and 500px high
    window.move(300, 300) # moves the widget to a position on screen at x=300, y=300 coordinates.
    window.setWindowTitle('PyQt5 GUI') # set the title of the window.
    window.show() # displays the widget on the screen
    sys.exit(app.exec_())