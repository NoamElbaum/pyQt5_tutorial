# command to convert .ui to .py:
# pyuic5 -x hello_world.ui -o hello_world.py
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.click_me = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.press_it())
        self.click_me.setGeometry(QtCore.QRect(210, 380, 181, 111))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(28)
        font.setItalic(True)
        self.click_me.setFont(font)
        self.click_me.setObjectName("click_me")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 20, 341, 141))
        font = QtGui.QFont()
        font.setPointSize(46)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self):
        if self.label.text() == "Hello World":
            self.label.setText("Boom!")
        else:
            self.label.setText("Hello World")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.click_me.setText(_translate("MainWindow", "Click Me!"))
        self.label.setText(_translate("MainWindow", "Hello World"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
