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

        # create combo box
        my_combo = qtw.QComboBox(self,
            editable=True,
            insertPolicy=qtw.QComboBox.InsertAtBottom)
        # add Item
        my_combo.addItem('chips', "Someting")
        my_combo.addItem('cheese', 2)
        my_combo.addItem('pepper', qtw.QWidget)
        my_combo.addItem('cola')
        my_combo.addItems(["one",'two','three'])
        my_combo.insertItem(2,"third Thing")
        # put combo box on screen
        self.layout().addWidget(my_combo)

        # create a button
        my_button = qtw.QPushButton("Press Me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button)

        self.show()

        def press_it():
            # show combo text
            my_label.setText(f'You picked {my_combo.currentText()}')
            # show combo data
            # my_label.setText(f'You picked {my_combo.currentData()}')
            # show index
            # my_label.setText(f'You picked {my_combo.currentIndex()}')
app = qtw.QApplication([])
mw = MainWindow()

app.exec_()