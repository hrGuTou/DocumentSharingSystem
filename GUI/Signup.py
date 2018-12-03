# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'signup.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Control
import sys

class Signup_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog):
        QtWidgets.QWidget.__init__(self)
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(590, 458)
        Dialog.setMinimumSize(QtCore.QSize(590, 458))
        Dialog.setMaximumSize(QtCore.QSize(594, 458))
        Dialog.setBaseSize(QtCore.QSize(590, 458))
        Dialog.setStyleSheet("QDialog{\n"
"    background-image: url(images/signup_image.jpeg);\n"
"}\n"
"QPushButton{\n"
"    background-color:rgb(255, 255, 255)\n"
"    border: none;\n"
"}")
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setGeometry(QtCore.QRect(230, 410, 93, 28))
        self.signup_button.setObjectName("signup_button")
        ################################# signup button event ###########
        self.signup_button.clicked.connect(self.signup_event)
        #################################################################
        self.formLayoutWidget_2 = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 240, 411, 173))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.name_field = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.name_field.setObjectName("name_field")
        self.name_field.setPlaceholderText("Enter your name")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name_field)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.interest_field = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.interest_field.setObjectName("interest_field")
        self.interest_field.setPlaceholderText("Enter your interest")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.interest_field)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.password_field = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.password_field.setObjectName("password_field")
        self.password_field.setPlaceholderText("Enter your password")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.password_field)
        self.label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.confirm_password_field = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.confirm_password_field.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.confirm_password_field.setDragEnabled(False)
        self.confirm_password_field.setPlaceholderText("")
        self.confirm_password_field.setObjectName("confirm_password_field")
        self.confirm_password_field.setPlaceholderText("Confirm your password")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.confirm_password_field)
        self.email_field = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.email_field.setText("")
        self.email_field.setPlaceholderText("")
        self.email_field.setObjectName("email_field")
        self.email_field.setPlaceholderText("Enter your email")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.email_field)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.signup_button.setText(_translate("Dialog", "Sign Up"))
        self.label_2.setText(_translate("Dialog", "Email:"))
        self.label_4.setText(_translate("Dialog", "Name:"))
        self.label_5.setText(_translate("Dialog", "Technical Interests:"))
        self.label_3.setText(_translate("Dialog", "Password:"))
        self.label.setText(_translate("Dialog", "Confirm Your Password:"))
        self.email_field.setWhatsThis(_translate("Dialog", "<html><head/><body><p>sadsad</p></body></html>"))

    def signup_event(self):

        #       GET DATA FROM INPUT         #
        email = self.email_field.text()
        password = self.password_field.text()
        name = self.name_field.text()
        confirm = self.confirm_password_field.text()
        techInterest = self.interest_field.text()
        print(email)
        print(password)
        print(name)
        print(techInterest)
        #=============================================
        print("this is the value from control: ", Control.signUp(email, password, name, techInterest))
        if (password == confirm):
            print("this is the value from control inside of if: ", Control.signUp(email, password, name, techInterest))
            # sign up successful
            if Control.signUp(email, password, name, techInterest) == 1:
                em = QtWidgets.QMessageBox()
                em.setText("Sign Up Successfully")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec_()


            # guest user registered
            elif Control.signUp(email, password, name, techInterest) == 0:
                em = QtWidgets.QMessageBox()
                em.setText("Guest User Registered")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec_()


            # account existed, go back to login page
            else:
                em = QtWidgets.QMessageBox()
                em.setIcon(QtWidgets.QMessageBox.Warning)
                em.setText("User already existed, please login")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec_()


        else:
            em = QtWidgets.QMessageBox()
            em.setIcon(QtWidgets.QMessageBox.Warning)
            em.setText("Password doesn't match, please try again")
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec_()
            self.password_field.setText("")
            self.confirm_password_field.setText("")



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Signup_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
