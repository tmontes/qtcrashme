import sys

from PyQt5 import QtWidgets
import qcrash.api as qcrash


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super().__init__()

        self.setWindowTitle("Qt Crash Friendly Test")
        self.resize(320, 70)

        self.button = QtWidgets.QPushButton("Click to crash", self)
        self.button.move(20, 20)
        self.button.resize(280, 30)

        self.button.clicked.connect(self.raise_exception)

    def raise_exception(self):

        raise BaseException("root of the exception hierarchy")


def setup_qcrash():

    github = qcrash.backends.GithubBackend("tmontes", "qtcrashme")
    qcrash.install_backend(github)

    email = qcrash.backends.EmailBackend("user@example.com", "qtcrashme")
    qcrash.install_backend(email)

    qcrash.get_application_log = lambda: "line1\nline2\n"
    qcrash.get_system_information = lambda: "system information here"

    qcrash.install_except_hook()


def main():

    app = QtWidgets.QApplication(sys.argv)
    setup_qcrash()
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    main()
