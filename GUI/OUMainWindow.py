# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ou_su_mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import re
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import User, DB
#from GUI.editor import Ui_MainWindow as EDITOR
from GUI.complaint import Ui_Dialog as Complaint_window

from GUI import editor_Dialog, viewOnlyEditor
from GUI.editor_Dialog import Ui_Dialog as UI_Dialog_editor
from GUI.invitation import Ui_seeInvitation
from Document import *
from GUI.matchFiled import Ui_Dialog as MatchedFiled_Dialog
from GUI.search_name import Ui_Dialog as SearchName_Dialog

class Ui_Dialog(object):
    def setupUi(self, Dialog, email):
        self.email = email
        #userType = DB.currentUserGroup(email)

        self.userObject = User.OU(email)  ######## object

        Dialog.setObjectName("Dialog")
        Dialog.resize(966, 746)
        Dialog.setStyleSheet(
            "QDialog {background-image: url(///Users/kappa/Library/Containers/com.tencent.xinWeChat/Data/Library/Application Support/com.tencent.xinWeChat/2.0b4.0.9/1feec28dbcbbd41c908e5319f9080e3b/Message/MessageTemp/047868fcf45822c2e58d288b5fe5d070/File/editabletreemodel/img/IMG_2432.JPG)\n"
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
        self.refresh_button = QtWidgets.QPushButton(Dialog)
        self.refresh_button.setObjectName("refresh_button")
        self.gridLayout.addWidget(self.refresh_button, 0, 2, 1, 1)
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

        self.search_options = QtWidgets.QComboBox(Dialog)
        self.search_options.setObjectName("search_options")
        self.search_options.addItem("")
        self.search_options.addItem("")
        self.horizontalLayout.addWidget(self.search_options)

        self.search_options.currentIndexChanged.connect(self.selectionchange)

        self.search_field = QtWidgets.QTextEdit(Dialog)
        self.search_field.setMaximumSize(QtCore.QSize(16777215, 25))
        self.search_field.setObjectName("search_field")
        self.search_field.setPlaceholderText("Please enter the keyword")

        self.horizontalLayout.addWidget(self.search_field)
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

        self.complaint_button = QtWidgets.QPushButton(Dialog)
        self.complaint_button.setObjectName("complaint_button")
        self.gridLayout.addWidget(self.complaint_button, 9, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.search_field, self.search_button)

        self.addItem()

        #########################3  button event ########################
        self.refresh_button.clicked.connect(self.refresh)
        self.selfDocs.itemActivated.connect(self.selfDocsClickListener)
        self.mostView.itemActivated.connect(self.mostviewClickListener)
        self.publicDoc.itemActivated.connect(self.publicdocClickListener)
        self.newDoc.clicked.connect(self.createNewDoc)
        self.invitation.clicked.connect(self.invite)
        self.complaint_button.clicked.connect(self.complaint)
        self.search_button.clicked.connect(self.search_event)
        #######################################################################

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "LLHC"))
        self.label_3.setText(_translate("Dialog", "Your Documents"))
        self.newDoc.setText(_translate("Dialog", "New Document"))
        self.refresh_button.setText(_translate("Dialog", "Refresh"))
        self.welcome_label.setText(_translate("Dialog",
                                              "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Welcome, </span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Public Documents"))
        self.search_options.setItemText(0, _translate("Dialog", "Search in own documents"))
        self.search_options.setItemText(1, _translate("Dialog", "search others by name"))
        self.search_button.setText(_translate("Dialog", "Search"))
        self.label.setText(_translate("Dialog", "Most Viewed"))
        self.invitation.setText(_translate("Dialog", "Invitation"))
        self.complaint_button.setText(_translate("Dialog", "Complaint"))


    def selectionchange(self):

        if self.search_options.currentIndex() == 0:
            self.search_field.setPlaceholderText("Please enter the keyword")
        else:
            self.search_field.setPlaceholderText("Please enter the name")

    def search_event(self):
        print("search event is pressed")

        # serach within user's own docs by keywords
        if self.search_options.currentIndex() == 0:
            print("now it is searching by keywords")

            ownDoc_list = listallfiles(self.email_label.text())

            if ownDoc_list != 0:

                keyword = self.search_field.toPlainText()
                print("this is the keword: ", keyword)
                matching_files = [file for file in ownDoc_list if keyword in file]

                # there is at least one matched file in the created documents
                if matching_files:
                    self.matchedFileWidnow = QtWidgets.QDialog()
                    self.ui = MatchedFiled_Dialog(self.matchedFileWidnow, display_keyword=keyword,
                                                  doc_list=matching_files)
                    self.ui.exec()
                else:
                    em = QtWidgets.QMessageBox()
                    em.setIcon(QtWidgets.QMessageBox.Warning)
                    em.setText("There's no document matched the keyword, please try another keyword")
                    em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                    em.exec()

            else:
                em = QtWidgets.QMessageBox()
                em.setIcon(QtWidgets.QMessageBox.Warning)
                em.setText("You haven't created any document yet!")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec()


        else:
            # search by name
            target_name = self.search_field.toPlainText()
            print("this is the name to be searched: ", target_name)
            matched_info = DB.getUserINFO(target_name.lower())

            if matched_info:
                print("there's a match in the database")


                for item in matched_info:
                    print(item)


                self.searchNameWidnow = QtWidgets.QDialog()
                self.ui = SearchName_Dialog(self.searchNameWidnow, search_name=target_name,display_list=matched_info)
                self.ui.exec()

            else:
                em = QtWidgets.QMessageBox()
                em.setIcon(QtWidgets.QMessageBox.Warning)
                em.setText("There's no match for the name: " + target_name +" in the system, make sure your spelling is correct!")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec()

    def complaint(self):
        self.complaintWindow = QtWidgets.QDialog()
        self.ui = Complaint_window(self.complaintWindow)
        #self.ui.setTargetEmail(self.email)
        self.ui.exec()

    def publicdocClickListener(self, item):
        clickTarget = item.text()
        origin =""
        for key in self.publicFile:
            if self.publicFile[key] is not None:
                if clickTarget in self.publicFile[key]:
                    origin = key
                    break
        self.userObject.openDoc(origin, clickTarget, '')
        self.viewonlyWindow = QtWidgets.QDialog()
        self.viewonly = viewOnlyEditor.Ui_viewOnly()
        self.viewonly.setupUi(self.viewonlyWindow, origin, clickTarget)
        self.viewonlyWindow.exec_()
        os.remove('../cache')


    def mostviewClickListener(self, item):
        clickTarget = item.text()
        clickTarget = re.findall(r'"([^"]*)"', clickTarget)

        origin = ""
        self.notPrivate = notPrivateFile()
        for key in self.notPrivate:
            if self.notPrivate[key] is not None:
                if clickTarget[0] in self.notPrivate[key]:
                    origin = key
                    break

        self.userObject.openDoc(origin, clickTarget[0], '')
        self.viewonlyWindow = QtWidgets.QDialog()
        self.viewonly = viewOnlyEditor.Ui_viewOnly()
        self.viewonly.setupUi(self.viewonlyWindow, origin, clickTarget[0])
        self.viewonlyWindow.exec_()
        os.remove('../cache')


    def addItem(self):
        listofFile = self.userObject.listallfiles()
        self.publicFile = self.userObject.getPermissionFile('public')
        self.restrictedFile = self.userObject.getPermissionFile('restricted')
        mostviewFile = self.userObject.mostPopular()

        if mostviewFile is not None:
            for tup in mostviewFile:
                self.mostView.addItem('"'+tup[1]+'"'+" Views: "+str(tup[2]))

        if self.publicFile is not None:
            for user in self.publicFile:
                for file in self.publicFile[user]:
                    self.publicDoc.addItem(file.replace("_"," "))



        if listofFile is not 0:
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
        self.editor.setupUi(self.editorWindow, self.email, clickedTarget)
        #self.editor.setFileName(clickedTarget)
        self.editorWindow.exec_()
        self.editor.uploadDoc(False)

    def refresh(self):
        print("refresh clicked")
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
        self.editor.setupUi(self.editorWindow, self.email, '')
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
    ui.setupUi(Dialog,'tring2')
    Dialog.show()
    sys.exit(app.exec_())

