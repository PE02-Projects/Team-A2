from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

#Class function of the launcher
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Launcher test")
        self.initUI()
    #Widgets configurations
    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Wafer")
        self.label.move(10,5)

        self.b07 = QtWidgets.QCheckBox(self)
        self.b07.setText("D07")
        self.b07.clicked.connect(self.fb07)
        self.b07.move(10,25)

        self.b08 = QtWidgets.QCheckBox(self)
        self.b08.setText("D08")
        self.b08.clicked.connect(self.clicked)
        self.b08.move(10,45)

        self.b23 = QtWidgets.QCheckBox(self)
        self.b23.setText("D23")
        self.b23.clicked.connect(self.clicked)
        self.b23.move(10,65)

        self.b24 = QtWidgets.QCheckBox(self)
        self.b24.setText("D24")
        self.b24.clicked.connect(self.clicked)
        self.b24.move(10,85)

    #Functions

    def fb07(self):
        if QCheckBox:checkState(self.b07) = True:
            self.label.setText("You selected Diode D07")
            self.update()
        elif QCheckBox:checkState(self.b07) = False:
            self.label.setText("You unselected Diode D07")
            self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()