import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # title
        self.setWindowTitle('Hello world!!!')
        # set vertical layout
        self.setLayout(qtw.QVBoxLayout())
        # create label
        my_label = qtw.QLabel("Hello World! Whats your name? ")
        # change font size
        my_label.setFont(qtg.QFont('Ariel', 20))
        #place label
        self.layout().addWidget(my_label)

        # create entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("sf")
        self.layout().addWidget(my_entry)

        # create a button
        my_button = qtw.QPushButton("Press Me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            # add name to label
            my_label.setText('Hello '+ str(my_entry.text()))
            # Clear entry box
            my_entry.setText("")
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()