# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import User

import Control
import DB
from GUI.Signup import Signup_Dialog
from GUI.OUSUmainwindow import OUSU_mainwindow_Dialog


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        QtWidgets.QWidget.__init__(self)
        Dialog.setObjectName("Dialog")
        Dialog.resize(605, 458)
        Dialog.setMinimumSize(QtCore.QSize(605, 458))
        Dialog.setMaximumSize(QtCore.QSize(605, 458))
        Dialog.setBaseSize(QtCore.QSize(605, 358))
        Dialog.setStyleSheet("QDialog{\n"
"    background-image: url(images/login_image.jpeg)\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(255, 255, 255)\n"
"    border: none;\n"
"}")
        Dialog.setSizeGripEnabled(False)
        Dialog.setWindowTitle('Login Page')
        oImage = QImage("images/login_image.jpeg")
        sImage = oImage.scaled(QSize(605, 458))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        Dialog.setPalette(palette)
        Dialog.resize(605, 458)
        Dialog.setMinimumSize(QtCore.QSize(605, 458))
        Dialog.setMaximumSize(QtCore.QSize(605, 458))
        Dialog.setBaseSize(QtCore.QSize(605, 358))

        self.login_button = QtWidgets.QPushButton(Dialog)
        self.login_button.setGeometry(QtCore.QRect(300, 390, 93, 28))
        #########################3 Login button event ########################
        self.login_button.clicked.connect(self.login_event)
        #######################################################################
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(200, 390, 93, 31))
        #########################3 Signup button event ########################
        self.signup_button.clicked.connect(self.signup_event)
        #######################################################################
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(140, 300, 291, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet("font: 13pt \".SF NS Text\";")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.password_field = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_field.setObjectName("password_field")
        self.password_field.setPlaceholderText("Enter your password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password_field)
        self.email_field = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.email_field.setText("")
        self.email_field.setObjectName("email_field")
        self.email_field.setPlaceholderText("Enter your email")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.email_field)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    page_status = 0

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("Login Page")
        self.login_button.setText(_translate("Dialog", "Login"))
        self.signup_button.setText(_translate("Dialog", "Sign Up"))
        self.label_2.setText(_translate("Dialog", "Email:"))
        self.label.setText(_translate("Dialog", "Password:"))

    # event handler for login button
    def login_event(self):
        print("login is pressed")

        #===============  CHANGES ===================

        email = self.email_field.text()
        password = self.password_field.text()
        status = Control.signIn(email,password)

        #============================================

        print("this is status: ", status)
        if (not email):
            em = QtWidgets.QMessageBox()
            em.setIcon(QtWidgets.QMessageBox.Warning)
            em.setText("Please enter email！")
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec_()
            self.email_field.setText("")
            self.password_field.setText("")

        elif status == -1:
            em = QtWidgets.QMessageBox()
            em.setIcon(QtWidgets.QMessageBox.Warning)
            em.setText("Account not found, Please create an account")
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec_()
            self.signup_event()


        # correct users
        elif status == 1:
            print('login login')
            self.mainwinodw = QtWidgets.QDialog()
            self.ui = OUSU_mainwindow_Dialog()
            self.ui.setupUi(self.mainwinodw, self.email_field.text())
            em = QtWidgets.QMessageBox()
            em.setText("Welcome, "+ self.email_field.text())
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec_()
            Dialog.close()
            self.mainwinodw.exec_()


            Control.signOut(self.email_field.text())
            #===== USER object



        # already login
        elif status == 2:
            em = QtWidgets.QMessageBox()
            em.setIcon(QtWidgets.QMessageBox.Warning)
            em.setText("Already login!")
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec_()

        else: # THIS RETURN 3, LAUNCH GUEST UI
            print("HERE ADD GUEST UI")


    def signup_event(self):
        print("sign up button is clicked")
        Dialog.close()
        self.signUpWindow = QtWidgets.QDialog()
        self.ui = Signup_Dialog()
        self.ui.setupUi(self.signUpWindow)
        self.signUpWindow.exec_()
        self.email_field.setText("")
        self.password_field.setText("")
        Dialog.show()



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
