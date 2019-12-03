import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QVBoxLayout
)


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle('Qt Crash Friendly Test')
        self.resize(320, 240)

        self.python = QLineEdit(self)
        self.python.move(20, 20)
        self.python.resize(280, 20)

        self.label = QLabel('(submit a Python expression)', self)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.label.setWordWrap(True)
        self.label.move(20, 50)
        self.label.resize(280, 170)

        self.python.editingFinished.connect(self.evaluate_python)


    def evaluate_python(self):

        globals = {}
        locals = {}
        python = self.python.text().strip()
        if python:
            result = eval(python, globals, locals)
            output = str(result)
        else:
            output = 'empty Python expression'
        self.update_label(output)

    def update_label(self, text):
        self.label.setText(text)
        self.label.repaint()


def main():

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':

    main()
