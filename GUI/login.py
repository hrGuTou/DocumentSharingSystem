from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush
import Control


class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal()


    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Login Page')
        oImage = QImage("images/login_image.jpeg")
        sImage = oImage.scaled(QSize(605, 458))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.resize(605, 458)
        self.setMinimumSize(QtCore.QSize(605, 458))
        self.setMaximumSize(QtCore.QSize(605, 458))
        self.setBaseSize(QtCore.QSize(605, 358))

        self.login_button = QtWidgets.QPushButton(self)
        self.login_button.setGeometry(QtCore.QRect(300, 390, 93, 28))
        #########################3 Login button event ########################
        self.login_button.clicked.connect(self.login_event)
        #######################################################################
        self.signup_button = QtWidgets.QPushButton(self)
        self.signup_button.setDefault(True)
        self.signup_button.setGeometry(QtCore.QRect(200, 390, 93, 31))
        #########################3 Signup button event ########################
        self.signup_button.clicked.connect(self.signup_event)
        #######################################################################
        self.formLayoutWidget = QtWidgets.QWidget(self)
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

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle("Login Page")
        self.login_button.setText(_translate("Dialog", "Login"))
        self.signup_button.setText(_translate("Dialog", "Sign Up"))
        self.label_2.setText(_translate("Dialog", "Email:"))
        self.label.setText(_translate("Dialog", "Password:"))

    def login_event(self):
        print("login is pressed")

        #===============  CHANGES ===================

        email = self.email_field.text()
        password = self.password_field.text()


        #============================================

        # if user didn't enter password or email
        if email=='':
             em = QtWidgets.QMessageBox()
             em.setIcon(QtWidgets.QMessageBox.Warning)
             em.setText("Please enter username and/or password!")
             em.setStandardButtons(QtWidgets.QMessageBox.Ok)
             em.exec_()
             self.email_field.setText("")
             self.password_field.setText("")

        else:
            status = Control.signIn(email, password)
        # user is not exist
            if status == -1:
                em = QtWidgets.QMessageBox()
                em.setIcon(QtWidgets.QMessageBox.Warning)
                em.setText("Account not found, Please create an account")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec_()
                self.switch_window.emit()


            # correct users
            elif status == 1:
                print('here')
                self.switch_window.emit()
                em = QtWidgets.QMessageBox()
                em.setText("Welcome")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec_()
                self.switch_window.emit()
            #++++++++++++++++++++++++++++++++++++++++
            #           welcome弹窗按了OK后就可以关闭login窗口了
            #+++++++++++++++++++++++++++++++++++++++++


            # already login
            elif status == 2:
                em = QtWidgets.QMessageBox()
                em.setIcon(QtWidgets.QMessageBox.Warning)
                em.setText("Already login!")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec_()
                self.switch_window.emit()


            else: # THIS RETURN 3, LAUNCH GUEST UI
                print("HERE ADD GUEST UI")
                page_status = 3


    def signup_event(self):
        self.switch_window.emit()
        print("sign up is pressed")