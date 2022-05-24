from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

Diodes = ['D07','D08','D23','D24']
Rows = [-4,-3,-2,-1,0,1,2,3,4]
Cols = [-4,-3,-2,-1,0,1,2,3,4]

#Class function of the launcher
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(500,500,560,300)
        self.setWindowTitle("Team A2 Launcher")
        self.initUI()

    #Widgets & configurations
    def initUI(self):
        #Wafer section
        self.label = QtWidgets.QLabel(self)
        self.label.setText("[ Wafer ]")
        self.label.move(10 , 5)

        self.b07 = QtWidgets.QCheckBox(self)
        self.b07.setText('D07')
        self.b07.clicked.connect(self.Diodecheck)
        self.b07.move(10,25)

        self.b08 = QtWidgets.QCheckBox(self)
        self.b08.setText('D08')
        self.b08.clicked.connect(self.Diodecheck)
        self.b08.move(10,45)

        self.b23 = QtWidgets.QCheckBox(self)
        self.b23.setText('D23')
        self.b23.clicked.connect(self.Diodecheck)
        self.b23.move(10,65)

        self.b24 = QtWidgets.QCheckBox(self)
        self.b24.setText('D24')
        self.b24.clicked.connect(self.Diodecheck)
        self.b24.move(10,85)

        #Row selection

        self.label = QtWidgets.QLabel(self)
        self.label.setText("[ Rows ]")
        self.label.move(125 , 5)

        self.r04 = QtWidgets.QCheckBox(self)
        self.r04.setText('-4')
        self.r04.clicked.connect(self.rowcheck)
        self.r04.move(125,25)

        self.r03 = QtWidgets.QCheckBox(self)
        self.r03.setText('-3')
        self.r03.clicked.connect(self.rowcheck)
        self.r03.move(125,45)

        self.r02 = QtWidgets.QCheckBox(self)
        self.r02.setText('-2')
        self.r02.clicked.connect(self.rowcheck)
        self.r02.move(125,65)

        self.r01 = QtWidgets.QCheckBox(self)
        self.r01.setText('-1')
        self.r01.clicked.connect(self.rowcheck)
        self.r01.move(125,85)

        self.r0 = QtWidgets.QCheckBox(self)
        self.r0.setText('0')
        self.r0.clicked.connect(self.rowcheck)
        self.r0.move(125,105)

        self.r1 = QtWidgets.QCheckBox(self)
        self.r1.setText('1')
        self.r1.clicked.connect(self.rowcheck)
        self.r1.move(200,25)

        self.r2 = QtWidgets.QCheckBox(self)
        self.r2.setText('2')
        self.r2.clicked.connect(self.rowcheck)
        self.r2.move(200,45)

        self.r3 = QtWidgets.QCheckBox(self)
        self.r3.setText('3')
        self.r3.clicked.connect(self.rowcheck)
        self.r3.move(200,65)

        self.r4 = QtWidgets.QCheckBox(self)
        self.r4.setText('4')
        self.r4.clicked.connect(self.rowcheck)
        self.r4.move(200,85)


        #Column selection

        self.label = QtWidgets.QLabel(self)
        self.label.setText("[ Columns ]")
        self.label.move(300 , 5)

        self.c04 = QtWidgets.QCheckBox(self)
        self.c04.setText('-4')
        self.c04.clicked.connect(self.colcheck)
        self.c04.move(300,25)

        self.c03 = QtWidgets.QCheckBox(self)
        self.c03.setText('-3')
        self.c03.clicked.connect(self.colcheck)
        self.c03.move(300,45)

        self.c02 = QtWidgets.QCheckBox(self)
        self.c02.setText('-2')
        self.c02.clicked.connect(self.colcheck)
        self.c02.move(300,65)

        self.c01 = QtWidgets.QCheckBox(self)
        self.c01.setText('-1')
        self.c01.clicked.connect(self.colcheck)
        self.c01.move(300,85)

        self.c0 = QtWidgets.QCheckBox(self)
        self.c0.setText('0')
        self.c0.clicked.connect(self.colcheck)
        self.c0.move(300,105)

        self.c1 = QtWidgets.QCheckBox(self)
        self.c1.setText('1')
        self.c1.clicked.connect(self.colcheck)
        self.c1.move(375,25)

        self.c2 = QtWidgets.QCheckBox(self)
        self.c2.setText('2')
        self.c2.clicked.connect(self.colcheck)
        self.c2.move(375,45)

        self.c3 = QtWidgets.QCheckBox(self)
        self.c3.setText('3')
        self.c3.clicked.connect(self.colcheck)
        self.c3.move(375,65)

        self.c4 = QtWidgets.QCheckBox(self)
        self.c4.setText('4')
        self.c4.clicked.connect(self.colcheck)
        self.c4.move(375, 85)

        #Restrictions
        self.Option = QtWidgets.QLabel(self)
        self.Option.setText('[ Option ]')
        self.Option.move(10, 130)

        self.showplot = QtWidgets.QCheckBox(self)
        self.showplot.setText('Show plot')
        self.showplot.move(10,160)

        self.saveplot = QtWidgets.QCheckBox(self)
        self.saveplot.setText('Save plot')
        self.saveplot.move(130,160)

        self.savexlsx = QtWidgets.QCheckBox(self)
        self.savexlsx.setText('Save Excel File')
        self.savexlsx.resize(200, 30)
        self.savexlsx.move(250,160)

        #Executions
        self.check = QtWidgets.QPushButton(self)
        self.check.setText('Run')
        self.check.clicked.connect(self.start_progress)
        self.check.move(10,265)

        self.exit = QtWidgets.QPushButton(self)
        self.exit.setText('Exit')
        self.exit.clicked.connect(QCoreApplication.instance().quit)
        self.exit.move(450,265)

        # progress bar
        self.pbarlabel = QtWidgets.QLabel(self)
        self.pbarlabel.setText('[ Progress ]')
        self.pbarlabel.move(230, 200)

        self.pbar = QProgressBar(self)
        self.pbar.value()
        self.pbar.setGeometry(30, 230, 500, 20)
        self.pbar.setAlignment(Qt.AlignCenter)

        # Timer
        self.timer = QTimer()


    #Functions
    def timer_progress(self, e):
        self.count = self.pbar.value()
        self.count += 1
        self.pbar.setValue(self.count)

        if self.count >= self.pbar.maximum():
            self.timer.stop()
            self.check.setText('Finished')
            self.check.setEnabled(True)


    def start_progress(self):
        if self.count == self.pbar.minimum():
            self.timer.setInterval(1000)
            self.timer.timeout.connect(self.timer_progress)
            self.timer.start()
            self.check.setText('Loading')
            self.check.setEnabled(False)

        elif self.count == self.pbar.maximum():
            self.pbar.reset()
            self.check.setText('Run')


    def Diodecheck(self):
        if self.b07.isChecked() is True:
            Diodes[0] = "D07"
        else:
            Diodes[0] = ""
        if self.b08.isChecked() is True:
            Diodes[1] = "D08"
        else:
            Diodes[1] = ""
            self.d08 = ''
        if self.b23.isChecked() is True:
            Diodes[2] = "D23"
            self.d23 = 'D23'
        else:
            Diodes[2] = ""
            self.d23 = ''
        if self.b24.isChecked() is True:
            Diodes[3] = "D24"
        else:
            Diodes[3] = ""
        return Diodes

    def rowcheck(self):
        if self.r04.isChecked() is True:
            Rows[0] = -4
        else:
            Rows[0] = ""
        if self.r03.isChecked() is True:
            Rows[1] = -3
        else:
            Rows[1] = ""
        if self.r02.isChecked() is True:
            Rows[2] = -2
        else:
            Rows[2] = ""
        if self.r01.isChecked() is True:
            Rows[3] = -1
        else:
            Rows[3] = ""
        if self.r0.isChecked() is True:
            Rows[4] = 0
        else:
            Rows[4] = ""
        if self.r1.isChecked() is True:
            Rows[5] = 1
        else:
            Rows[5] = ""
        if self.r2.isChecked() is True:
            Rows[6] = 2
        else:
            Rows[6] = ""
        if self.r3.isChecked() is True:
            Rows[7] = 3
        else:
            Rows[7] = ""
        if self.r4.isChecked() is True:
            Rows[8] = 4
        else:
            Rows[8] = ""
        return Rows


    def colcheck(self):
        if self.c04.isChecked() is True:
            Rows[0] = -4
        else:
            Rows[0] = ""
        if self.c03.isChecked() is True:
            Rows[1] = -3
        else:
            Rows[1] = ""
        if self.c02.isChecked() is True:
            Rows[2] = -2
        else:
            Rows[2] = ""
        if self.c01.isChecked() is True:
            Rows[3] = -1
        else:
            Rows[3] = ""
        if self.c0.isChecked() is True:
            Rows[4] = 0
        else:
            Rows[4] = ""
        if self.c1.isChecked() is True:
            Rows[5] = 1
        else:
            Rows[5] = ""
        if self.c2.isChecked() is True:
            Rows[6] = 2
        else:
            Rows[6] = ""
        if self.c3.isChecked() is True:
            Rows[7] = 3
        else:
            Rows[7] = ""
        return Cols


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

