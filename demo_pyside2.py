
from PySide2 import QtCore, QtGui, QtWidgets
from widgets import Toggle


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()

        toggle_1 = Toggle()

        container = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        button = QtWidgets.QPushButton()
        button.clicked.connect(lambda: print(toggle_1.isChecked()))
        layout.addWidget(toggle_1)
        layout.addWidget(button)
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QtWidgets.QApplication([])
w = Window()
w.show()
app.exec_()
