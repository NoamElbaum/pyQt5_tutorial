from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.num = ""
        self.sum = 0
        self.sign = '+'
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(361, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.output = QtWidgets.QLCDNumber(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(10, 10, 341, 91))
        self.output.setFrameShape(QtWidgets.QFrame.Box)
        self.output.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output.setSmallDecimalPoint(False)
        self.output.setDigitCount(8)
        self.output.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.output.setProperty("value", 0.0)
        self.output.setObjectName("output")
        self.precentButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("%"))
        self.precentButton.setGeometry(QtCore.QRect(10, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.precentButton.setFont(font)
        self.precentButton.setObjectName("precentButton")
        self.clearButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("c"))
        self.clearButton.setGeometry(QtCore.QRect(100, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("<<"))
        self.arrowButton.setGeometry(QtCore.QRect(190, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        self.divideButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("/"))
        self.divideButton.setGeometry(QtCore.QRect(280, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.divideButton.setFont(font)
        self.divideButton.setObjectName("divideButton")
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(280, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(190, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(280, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(190, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 375, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+"))
        self.addButton.setGeometry(QtCore.QRect(280, 375, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 375, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(190, 375, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        self.plusMinusButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("+/-"))
        self.plusMinusButton.setGeometry(QtCore.QRect(10, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plusMinusButton.setFont(font)
        self.plusMinusButton.setObjectName("plusMinusButton")
        self.equelButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("="))
        self.equelButton.setGeometry(QtCore.QRect(280, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equelButton.setFont(font)
        self.equelButton.setObjectName("equelButton")
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        self.decimalButton = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it("."))
        self.decimalButton.setGeometry(QtCore.QRect(190, 460, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.decimalButton.setFont(font)
        self.decimalButton.setObjectName("decimalButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 361, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self, pressed):
        # print(pressed)
        if pressed.isdigit():
            self.num += pressed
        elif pressed == "+":
            self.sum += int(self.num)
            print(self.sum)
            self.num = ''
        elif pressed == '-':
            self.sum += int(self.num)
            print(self.sum)
            self.num = ''
            self.sign = '-'
        if pressed == '=':
            if self.sign == '+':
                self.sum += int(self.num)
            elif self.sign == '-':
                self.sum -= int(self.num)
            self.num = ''
            self.output.display(int(self.sum))
        else:
            self.output.display(self.num)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.precentButton.setText(_translate("MainWindow", "%"))
        self.clearButton.setText(_translate("MainWindow", "C"))
        self.arrowButton.setText(_translate("MainWindow", "<<"))
        self.divideButton.setText(_translate("MainWindow", "/"))
        self.sevenButton.setText(_translate("MainWindow", "7"))
        self.multiplyButton.setText(_translate("MainWindow", "x"))
        self.eightButton.setText(_translate("MainWindow", "8"))
        self.nineButton.setText(_translate("MainWindow", "9"))
        self.fourButton.setText(_translate("MainWindow", "4"))
        self.minusButton.setText(_translate("MainWindow", "-"))
        self.fiveButton.setText(_translate("MainWindow", "5"))
        self.sixButton.setText(_translate("MainWindow", "6"))
        self.oneButton.setText(_translate("MainWindow", "1"))
        self.addButton.setText(_translate("MainWindow", "+"))
        self.twoButton.setText(_translate("MainWindow", "2"))
        self.threeButton.setText(_translate("MainWindow", "3"))
        self.plusMinusButton.setText(_translate("MainWindow", "+/-"))
        self.equelButton.setText(_translate("MainWindow", "="))
        self.zeroButton.setText(_translate("MainWindow", "0"))
        self.decimalButton.setText(_translate("MainWindow", "."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())