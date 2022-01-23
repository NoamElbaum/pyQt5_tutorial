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
        my_label = qtw.QLabel("Type somthing in the box below: ")
        # change font size
        my_label.setFont(qtg.QFont('Ariel', 24))
        #place label
        self.layout().addWidget(my_label)

        # create text box
        my_text = qtw.QTextEdit(self,
            # plainText="text",
            # html="<h1>wefww</h1>",
            acceptRichText=True,
            lineWrapMode=qtw.QTextEdit.FixedColumnWidth,
            lineWrapColumnOrWidth=40,
            placeholderText="Write Here",
            readOnly=False,
            )
        # change font size
        # my_spin.setFont(qtg.QFont('Ariel', 18))
        # put combo box on screen
        self.layout().addWidget(my_text)

        # create a button
        my_button = qtw.QPushButton("Press Me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            my_label.setText(f'You Typed: {my_text.toPlainText()}')
            my_text.setPlainText("You Pressed The Button!")
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()