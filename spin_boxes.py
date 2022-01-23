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
        my_label = qtw.QLabel("Pick Someting from the box below:")
        # change font size
        my_label.setFont(qtg.QFont('Ariel', 24))
        #place label
        self.layout().addWidget(my_label)

        # create spin box
        my_spin = qtw.QDoubleSpinBox(self,
            value=10.5,
            maximum=100,
            minimum=0,
            singleStep=0.5,
            prefix='#',
            suffix=' Order')
        # change font size
        my_spin.setFont(qtg.QFont('Ariel', 18))
        # put combo box on screen
        self.layout().addWidget(my_spin)

        # create a button
        my_button = qtw.QPushButton("Press Me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            # show spin val
            my_label.setText(f'You picked: {my_spin.value()}')
            # show combo data
            # my_label.setText(f'You picked {my_combo.currentData()}')
            # show index
            # my_label.setText(f'You picked {my_combo.currentIndex()}')
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()