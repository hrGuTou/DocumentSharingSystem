import sys
from PyQt5 import QtCore, QtWidgets
from GUI.login import Login
from GUI.Signup import Signup


class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        if self.login.signup_event():
            self.login.switch_window.connect(self.show_signup)

        else:
            print("not a new account")
        self.login.show()

    def show_signup(self):
        self.login.email_field.setText("")
        self.login.password_field.setText("")
        self.window = Signup()
        self.window.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()