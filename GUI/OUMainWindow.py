# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ou_su_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import time

from PyQt5 import QtCore, QtGui, QtWidgets
import User, DB
#from GUI.editor import Ui_MainWindow as EDITOR
from GUI import editor_Dialog
from GUI.editor_Dialog import Ui_Dialog as UI_Dialog_editor
from GUI.invitation import Ui_seeInvitation

class Ui_Dialog(object):
    def setupUi(self, Dialog, email):

        self.email = email
        userType = DB.currentUserGroup(email)

        if userType == 1:
            self.userObject = User.OU(email)  ######## object
        else:
            self.userObject = User.SU(email)  ######## object

        Dialog.setObjectName("Dialog")
        Dialog.resize(966, 746)
        Dialog.setStyleSheet("QDialog {background-image: url(///Users/kappa/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/1feec28dbcbbd41c908e5319f9080e3b/Message/MessageTemp/047868fcf45822c2e58d288b5fe5d070/File/editabletreemodel/img/IMG_2432.JPG)\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.mostView = QtWidgets.QListWidget(Dialog)
        self.mostView.setObjectName("mostView")
        self.gridLayout.addWidget(self.mostView, 4, 0, 1, 3)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 3)
        self.newDoc = QtWidgets.QPushButton(Dialog)
        self.newDoc.setObjectName("newDoc")
        self.gridLayout.addWidget(self.newDoc, 9, 2, 1, 1)
        self.manage_button = QtWidgets.QPushButton(Dialog)
        self.manage_button.setObjectName("manage_button")
        self.gridLayout.addWidget(self.manage_button, 0, 2, 1, 1)
        self.welcome_label = QtWidgets.QLabel(Dialog)
        self.welcome_label.setStyleSheet("#welcome_label{\n"
"    color: purple\n"
"}")
        self.welcome_label.setObjectName("welcome_label")
        self.gridLayout.addWidget(self.welcome_label, 0, 0, 2, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 3)
        self.selfDocs = QtWidgets.QListWidget(Dialog)
        self.selfDocs.setObjectName("selfDocs")
        self.gridLayout.addWidget(self.selfDocs, 8, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 20))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.search_button = QtWidgets.QPushButton(Dialog)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 2, 2, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.email_label = QtWidgets.QLabel(Dialog)
        self.email_label.setStyleSheet("#email_label{\n"
"    color: purple;\n"
"}")
        self.email_label.setObjectName("email_label")
        self.email_label.setText(email)
        self.gridLayout.addWidget(self.email_label, 2, 0, 1, 2)
        self.publicDoc = QtWidgets.QListWidget(Dialog)
        self.publicDoc.setObjectName("publicDoc")
        self.gridLayout.addWidget(self.publicDoc, 6, 0, 1, 3)
        self.invitation = QtWidgets.QPushButton(Dialog)
        self.invitation.setObjectName("invitation")
        self.gridLayout.addWidget(self.invitation, 9, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.textEdit, self.search_button)

        self.addItem()


        #########################3  button event ########################
        self.manage_button.clicked.connect(self.refresh)
        self.selfDocs.itemActivated.connect(self.selfDocsClickListener)
        self.newDoc.clicked.connect(self.createNewDoc)
        self.invitation.clicked.connect(self.invite)
        #######################################################################

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LLHC"))
        self.label_3.setText(_translate("Dialog", "Your Documents"))
        self.newDoc.setText(_translate("Dialog", "New Document"))
        self.manage_button.setText(_translate("Dialog", "Refresh"))
        self.welcome_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Welcome, </span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Public Documents"))
        self.search_button.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Most Viewed"))
        self.invitation.setText(_translate("Dialog", "Invitation"))


    def addItem(self):
        listofFile = self.userObject.listallfiles()
        publicFile = self.userObject.getPermissionFile('public')
        mostviewFile = self.userObject.mostPopular()

        if mostviewFile is not None:
            for tup in mostviewFile:
                self.mostView.addItem('"'+tup[1]+'"'+" Views: "+str(tup[2]))

        if publicFile is not None:
            for user in publicFile:
                for file in publicFile[user]:
                    self.publicDoc.addItem(file.replace("_"," "))


        if listofFile == 0:
            listofFile = self.userObject.mostPopular()
            # got the list of tuples

        else:
            for file in listofFile:
                self.selfDocs.addItem(file.replace("_", " "))



    def selfDocsClickListener(self,item):
        clickedTarget = item.text()

        clickedTarget = clickedTarget.replace(" ","_")
        self.userObject.openDoc(self.email, clickedTarget, "")
            #this will store a cache file in disk for BE to read
        editor_Dialog.loadBE()
        time.sleep(1)
        self.editorWindow = QtWidgets.QDialog()
        self.editor = UI_Dialog_editor()
        self.editor.setupUi(self.editorWindow, self.email)
        self.editor.setFileName(clickedTarget)
        self.editorWindow.exec_()
        self.editor.uploadDoc(False)

    def refresh(self):
        self.mostView.clear()
        self.publicDoc.clear()
        self.selfDocs.clear()
        self.addItem()

    def createNewDoc(self):
        ### This will create a new document ###
        editor_Dialog.loadBE()
        time.sleep(1)
        self.editorWindow = QtWidgets.QDialog()
        self.editor = UI_Dialog_editor()
        self.editor.setupUi(self.editorWindow, self.email)
        self.editorWindow.exec_()
        self.editor.uploadDoc(True)  # true because it is new file

    def invite(self):

        self.inviteWindow = QtWidgets.QDialog()
        self.inviteW = Ui_seeInvitation()
        self.inviteW.setupUi(self.inviteWindow, self.email)
        self.inviteWindow.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

