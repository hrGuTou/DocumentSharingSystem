# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import Control, DB

class OUSU_mainwindow_Dialog(QDialog):
    def setupUi(self, Dialog,email):
        QtWidgets.QWidget.__init__(self)
        Dialog.setObjectName("Dialog")
        Dialog.resize(792, 563)
        Dialog.setStyleSheet("QDialog {background-image: url(images/ou_su_image.JPG)\n"
"}")
        self.welcome_label = QtWidgets.QLabel(Dialog)
        self.welcome_label.setGeometry(QtCore.QRect(30, 20, 91, 16))
        self.welcome_label.setStyleSheet("#welcome_label{\n"
"    color: purple\n"
"}")
        self.welcome_label.setObjectName("welcome_label")
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setGeometry(QtCore.QRect(20, 50, 201, 16))
        self.email_label.setStyleSheet("#email_label{\n"
"    color: purple;\n"
"}")
        self.email_label.setText("")
        self.email_label.setObjectName("email_label")
        self.email_label.setText(email)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(-5, 141, 811, 421))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(430, 40, 341, 83))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.search_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.manage_button = QtWidgets.QPushButton(Dialog)
        self.manage_button.setGeometry(QtCore.QRect(650, 0, 114, 32))
        self.manage_button.setObjectName("manage_button")
        self.manage_button.setText("Manage")
        self.manage_button.setVisible(False)

        # check if SU exist
        if not DB.SUexists():
            print("not exist ")
            self.manage_button.setVisible(True)
        else:
            if DB.currentUserGroup(email) == 0:
                self.manage_button.setVisible(True)
        #########################3 Signup button event ########################
        self.manage_button.clicked.connect(self.manage_event)
        #######################################################################


        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.textEdit, self.search_button)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.welcome_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Welcome, </span></p></body></html>"))
        self.search_button.setText(_translate("Dialog", "Search"))

    def manage_event(self):
        print("manage button is clicked")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Mainwindow_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

