# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from signup import Ui_Signup

class Ui_Dialog(object):

    # event handler for signup button
    def signup_check(self):
        print("signup button is clicked")

        self.signupWindow = QtWidgets.QDialog()
        self.ui = Ui_Signup()
        self.ui.setupUi(self.signupWindow)
        self.signupWindow.show()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(637, 477)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0     rgba(255, 170, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(255, 255, 255)\n"
"    border: none;\n"
"}")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 170, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(160, 220, 91, 21))
        self.label_3.setObjectName("label_3")
        self.email_field = QtWidgets.QLineEdit(Dialog)
        self.email_field.setGeometry(QtCore.QRect(240, 170, 201, 22))
        self.email_field.setText("")
        self.email_field.setObjectName("email_field")
        self.password_field = QtWidgets.QLineEdit(Dialog)
        self.password_field.setGeometry(QtCore.QRect(240, 220, 201, 22))
        self.password_field.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_field.setObjectName("password_field")
        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(290, 280, 93, 28))
        self.login_button.setObjectName("login_button")
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(290, 320, 93, 28))
        self.signup_button.setObjectName("signup_button")
        #########################3 Signup button event ########################
        self.signup_button.clicked.connect(self.signup_check)
        #######################################################################
        self.login_page_label = QtWidgets.QLabel(Dialog)
        self.login_page_label.setGeometry(QtCore.QRect(220, 70, 211, 91))
        self.login_page_label.setMinimumSize(QtCore.QSize(5, 0))
        self.login_page_label.setBaseSize(QtCore.QSize(40, 16))
        font = QtGui.QFont()
        font.setPointSize(41)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.login_page_label.setFont(font)
        self.login_page_label.setFocusPolicy(QtCore.Qt.NoFocus)
        self.login_page_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.login_page_label.setTextFormat(QtCore.Qt.AutoText)
        self.login_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_page_label.setObjectName("login_page_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Email:"))
        self.label_3.setText(_translate("Dialog", "Password: "))
        self.login_button.setText(_translate("Dialog", "Login"))
        self.signup_button.setText(_translate("Dialog", "Sign Up"))
        self.login_page_label.setText(_translate("Dialog", "Login Page"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
