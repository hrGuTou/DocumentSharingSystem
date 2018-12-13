# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gu_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import re
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from GUI.Signup import Signup_Dialog
from GUI.complaint import Ui_Dialog as Complaint_window
from GUI.suggestTaboo import Ui_Dialog as Suggestion_window
from Document import *
import os
from GUI import viewOnlyEditor


class Guest_Dialog(QDialog):
    def __init__(self, Dialog, parent=None):
        super(Guest_Dialog, self).__init__(parent=parent)
        self.setObjectName("Guest")
        self.resize(966, 746)
        self.setStyleSheet("QDialog {background-image: url(/Users/kappa/Desktop/python/DocumentSharingSystem/GUI/images/guest_ui.JPG)\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.welcome_label = QtWidgets.QLabel(Dialog)
        self.welcome_label.setStyleSheet("#welcome_label{\n"
                                         "    color: purple\n"
                                         "}")
        self.welcome_label.setObjectName("welcome_label")
        self.gridLayout.addWidget(self.welcome_label, 0, 0, 2, 1)
        self.public_label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.public_label.setFont(font)
        self.public_label.setAlignment(QtCore.Qt.AlignCenter)
        self.public_label.setObjectName("public_label")
        self.gridLayout.addWidget(self.public_label, 5, 0, 1, 3)

        ############### sign up button    #####################
        self.signup_button = QtWidgets.QPushButton(Dialog)
        self.signup_button.setObjectName("signup_button")
        self.gridLayout.addWidget(self.signup_button, 9, 0, 1, 1)

        ########################## sign up button event ################
        self.signup_button.clicked.connect(self.signup_event)
        ################################################################

        self.publicDoc = QtWidgets.QListWidget(Dialog)
        self.publicDoc.setObjectName("publicDoc")
        self.gridLayout.addWidget(self.publicDoc, 6, 0, 1, 3)

        self.mostView = QtWidgets.QListWidget(Dialog)
        self.mostView.setObjectName("mostView")
        self.gridLayout.addWidget(self.mostView, 4, 0, 1, 3)
        self.restricted_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.restricted_label.setFont(font)
        self.restricted_label.setAlignment(QtCore.Qt.AlignCenter)
        self.restricted_label.setObjectName("restricted_label")
        self.gridLayout.addWidget(self.restricted_label, 7, 0, 1, 3)

        self.mostView_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.mostView_label.setFont(font)
        self.mostView_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mostView_label.setObjectName("mostView_label")
        self.gridLayout.addWidget(self.mostView_label, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)


        self.restrictDoc = QtWidgets.QListWidget(Dialog)
        self.restrictDoc.setObjectName("restrictDoc")
        self.gridLayout.addWidget(self.restrictDoc, 8, 0, 1, 3)

        self.mostView.raise_()
        self.welcome_label.raise_()
        self.public_label.raise_()
        self.restrictDoc.raise_()
        self.mostView_label.raise_()
        self.publicDoc.raise_()
        self.signup_button.raise_()
        self.restricted_label.raise_()

        self.addItem()

        ##################### click event to oepn docs ##########
        self.restrictDoc.itemActivated.connect(self.restrictDocListener)
        self.publicDoc.itemActivated.connect(self.publicDocListener)
        self.mostView.itemActivated.connect(self.mostViewDocListener)
        #########################################################
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))
        self.signup_button.setText(_translate("Dialog", "Sign Up"))
        self.welcome_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-style:italic; color:#ffffff;\">Welcome To LLHC</span></p><p><span style=\" font-size:18pt; font-style:italic; color:#ffffff;\">Document Sharing System</span></p></body></html>"))
        self.public_label.setText(_translate("Dialog", "Public Documents"))
        self.restricted_label.setText(_translate("Dialog", "Restricted Documents"))
        self.mostView_label.setText(_translate("Dialog", "Most Viewed"))

    # event hanlder for sign up button
    def signup_event(self):
        print("sign up is pressed")
        self.signUpWindow = QtWidgets.QDialog()
        self.ui = Signup_Dialog(self.signUpWindow, type ='gu')
        self.ui.exec_()

    def addItem(self):
        self.mostViewFile = getMostview()
        self.publicFile = getPermissionFiles('public')
        self.restrictedFile = getPermissionFiles("restricted")

        if self.mostViewFile is not None:
            for tup in self.mostViewFile:
                self.mostView.addItem('"'+tup[1]+'"'+" Views: "+str(tup[2]))

        if self.publicFile is not None:
            for user in self.publicFile:
                for file in self.publicFile[user]:
                    self.publicDoc.addItem(file.replace("_"," "))

        if self.restrictedFile is not None:
            for user in self.restrictedFile:
                for file in self.restrictedFile[user]:
                    self.restrictDoc.addItem(file.replace("_"," "))


    def restrictDocListener(self, item):
        clickTarget = item.text()
        origin = ""
        for key in self.restrictedFile:
            if self.restrictedFile[key] is not None:
                if clickTarget in self.restrictedFile[key]:
                    origin = key
                    break
        openfile('', origin, clickTarget, '')
        self.viewonlyWindow = QtWidgets.QDialog()
        self.viewonly = viewOnlyEditor.Ui_viewOnly()
        self.viewonly.setupUi(self.viewonlyWindow, origin, clickTarget)
        self.viewonlyWindow.exec_()
        os.remove('../cache')

    def publicDocListener(self, item):
        clickTarget = item.text()
        origin = ""
        for key in self.publicFile:
            if self.publicFile[key] is not None:
                if clickTarget in self.publicFile[key]:
                    origin = key
                    break
        openfile('',origin, clickTarget, '')
        self.viewonlyWindow = QtWidgets.QDialog()
        self.viewonly = viewOnlyEditor.Ui_viewOnly()
        self.viewonly.setupUi(self.viewonlyWindow, origin, clickTarget)
        self.viewonlyWindow.exec_()
        os.remove('../cache')

    def mostViewDocListener(self, item):
        clickTarget = item.text()
        clickTarget = re.findall(r'"([^"]*)"', clickTarget)

        origin = ""
        self.notPrivate = notPrivateFile()
        for key in self.notPrivate:
            if self.notPrivate[key] is not None:
                if clickTarget[0] in self.notPrivate[key]:
                    origin = key
                    break
        print(self.publicFile)
        print("key:"+origin)
        openfile('',origin, clickTarget[0], '')
        self.viewonlyWindow = QtWidgets.QDialog()
        self.viewonly = viewOnlyEditor.Ui_viewOnly()
        self.viewonly.setupUi(self.viewonlyWindow, origin, clickTarget[0])
        self.viewonlyWindow.exec_()
        os.remove('../cache')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Guest_Dialog(Dialog)
    ui.show()
    sys.exit(app.exec_())