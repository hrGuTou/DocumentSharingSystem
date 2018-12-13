# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SUMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import re
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import User
import Document
from GUI import viewOnlyEditor, editor_Dialog
from GUI.editor_Dialog import Ui_Dialog as UI_Dialog_editor
from GUI.invitation import Ui_seeInvitation
import Taboo,DB



class Ui_Dialog(object):
    def setupUi(self, Dialog, userEmail):
        self.email = userEmail
        self.userObject = User.SU(self.email)

        Dialog.setObjectName("Super User")
        Dialog.resize(1143, 924)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Refresh = QtWidgets.QPushButton(Dialog)
        self.Refresh.setObjectName("Refresh")
        self.gridLayout.addWidget(self.Refresh, 0, 4, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabooWord_list = QtWidgets.QTableWidget(self.tab)
        self.tabooWord_list.setObjectName("tabooWord_list")
        self.tabooWord_list.setColumnCount(2)
        self.tabooWord_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tabooWord_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabooWord_list.setHorizontalHeaderItem(1, item)
        self.tabooWord_list.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tabooWord_list, 0, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.tableWidget, 0, 1, 1, 1)
        self.clear_suggest = QtWidgets.QPushButton(self.tab)
        self.clear_suggest.setObjectName("clear_suggest")
        self.gridLayout_2.addWidget(self.clear_suggest, 1, 1, 1, 1)
        self.clear_effective = QtWidgets.QPushButton(self.tab)
        self.clear_effective.setObjectName("clear_effective")
        self.gridLayout_2.addWidget(self.clear_effective, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.requestList = QtWidgets.QTableWidget(self.tab_2)
        self.requestList.setObjectName("requestList")
        self.requestList.setColumnCount(3)
        self.requestList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.requestList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.requestList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.requestList.setHorizontalHeaderItem(2, item)
        self.requestList.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_3.addWidget(self.requestList, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.complaint_list = QtWidgets.QTableWidget(self.tab_3)
        self.complaint_list.setObjectName("complaint_list")
        self.complaint_list.setColumnCount(4)
        self.complaint_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.complaint_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.complaint_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.complaint_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.complaint_list.setHorizontalHeaderItem(3, item)
        self.complaint_list.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_4.addWidget(self.complaint_list, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lockDoc_list = QtWidgets.QTableWidget(self.tab_4)
        self.lockDoc_list.setObjectName("lockDoc_list")
        self.lockDoc_list.setColumnCount(3)
        self.lockDoc_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.lockDoc_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.lockDoc_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.lockDoc_list.setHorizontalHeaderItem(2, item)
        self.lockDoc_list.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.lockDoc_list, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.tab_5)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 3, 0, 1, 3)
        self.invitation = QtWidgets.QPushButton(self.tab_5)
        self.invitation.setObjectName("invitation")
        self.gridLayout_6.addWidget(self.invitation, 7, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_5)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_6.addWidget(self.label_3, 5, 0, 1, 3)
        self.label = QtWidgets.QLabel(self.tab_5)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 1, 0, 1, 3)
        self.selfDocs = QtWidgets.QListWidget(self.tab_5)
        self.selfDocs.setObjectName("selfDocs")
        self.gridLayout_6.addWidget(self.selfDocs, 6, 0, 1, 5)
        self.publicDoc = QtWidgets.QListWidget(self.tab_5)
        self.publicDoc.setObjectName("publicDoc")
        self.gridLayout_6.addWidget(self.publicDoc, 4, 0, 1, 5)
        self.newDoc = QtWidgets.QPushButton(self.tab_5)
        self.newDoc.setObjectName("newDoc")
        self.gridLayout_6.addWidget(self.newDoc, 7, 4, 1, 1)
        self.mostView = QtWidgets.QListWidget(self.tab_5)
        self.mostView.setObjectName("mostView")
        self.gridLayout_6.addWidget(self.mostView, 2, 0, 1, 5)
        self.comboBox = QtWidgets.QComboBox(self.tab_5)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_6.addWidget(self.comboBox, 0, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(self.tab_5)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_6.addWidget(self.pushButton, 0, 4, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_6.addWidget(self.lineEdit, 0, 3, 1, 1)
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 5)
        self.welcome_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.welcome_label.setFont(font)
        self.welcome_label.setObjectName("welcome_label")
        self.gridLayout.addWidget(self.welcome_label, 0, 0, 1, 1)
        self.email_label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.email_label.setFont(font)
        self.email_label.setText("")
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 0, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.additems()
        self.addTaboo()
        self.getGUapp()
        self.addComplain()
        self.addlockFile()

        ######################## button events ########################
        self.selfDocs.itemActivated.connect(self.selfDocsClickListener)
        self.mostView.itemActivated.connect(self.mostviewClickListener)
        self.publicDoc.itemActivated.connect(self.publicdocClickListener)
        self.newDoc.clicked.connect(self.createNewDoc)
        self.invitation.clicked.connect(self.invite)
        self.Refresh.clicked.connect(self.refresh)
        self.clear_effective.clicked.connect(self.deleteAlleffective)
        self.clear_suggest.clicked.connect(self.deleteAllsuggest)
        ###############################################################

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Refresh.setText(_translate("Dialog", "Refresh"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Action"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Suggested Taboo Word"))
        item = self.tabooWord_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Action"))
        item = self.tabooWord_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Effective Taboo Word"))
        self.clear_suggest.setText(_translate("Dialog", "Clear All"))
        self.clear_effective.setText(_translate("Dialog", "Clear All"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Taboo Word List"))
        item = self.requestList.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Accept"))
        item = self.requestList.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "User Information"))
        item = self.requestList.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Reject"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "GU Application"))
        item = self.complaint_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Action"))
        item = self.complaint_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Target"))
        item = self.complaint_list.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "File Name"))
        item = self.complaint_list.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Complain"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Complaints"))
        item = self.lockDoc_list.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Action"))
        item = self.lockDoc_list.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "File Owner"))
        item = self.lockDoc_list.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "File Name"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "Locked Document"))
        self.label_2.setText(_translate("Dialog", "Public Documents"))
        self.invitation.setText(_translate("Dialog", "Invitation"))
        self.label_3.setText(_translate("Dialog", "Your Documents"))
        self.label.setText(_translate("Dialog", "Most Viewed"))
        self.newDoc.setText(_translate("Dialog", "New Document"))
        self.comboBox.setItemText(0, _translate("Dialog", "Search in own documents"))
        self.comboBox.setItemText(1, _translate("Dialog", "Search others by name"))
        self.pushButton.setText(_translate("Dialog", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Dialog", "Main"))
        self.welcome_label.setText(_translate("Dialog", "Welcome,"))


    def additems(self):
        listofFile = self.userObject.listallfiles()
        self.publicFile = self.userObject.getPermissionFile('public')
        self.restrictedFile = self.userObject.getPermissionFile('restricted')
        mostviewFile = self.userObject.mostPopular()

        if mostviewFile is not None:
            for tup in mostviewFile:
                self.mostView.addItem('"' + tup[1] + '"' + " Views: " + str(tup[2]))

        if self.publicFile is not None:
            for user in self.publicFile:
                for file in self.publicFile[user]:
                    self.publicDoc.addItem(file.replace("_", " "))

        if listofFile is not 0:
            for file in listofFile:
                self.selfDocs.addItem(file.replace("_", " "))

    def mostviewClickListener(self, item):
        clickTarget = item.text()
        clickTarget = re.findall(r'"([^"]*)"', clickTarget)

        origin = ""
        self.notPrivate = Document.notPrivateFile()
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

    def refresh(self):
        self.mostView.clear()
        self.publicDoc.clear()
        self.selfDocs.clear()
        self.tabooWord_list.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.requestList.setRowCount(0)
        self.lockDoc_list.setRowCount(0)
        self.addlockFile()
        self.getGUapp()
        self.addTaboo()
        self.additems()

    def addTaboo(self):
        self.effectiveTaboo = Taboo.getTaboo()
        if self.effectiveTaboo:
            for word in self.effectiveTaboo:
                delete = QtWidgets.QPushButton()
                delete.setText("Delete")
                rowPosition = self.tabooWord_list.rowCount()
                self.tabooWord_list.insertRow(rowPosition)
                self.tabooWord_list.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(word))
                self.tabooWord_list.setCellWidget(rowPosition, 0, delete)
                delete.clicked.connect(lambda  *args, target = word: self.deleteEffectiveTaboo(target))

        self.suggestedTaboo = Taboo.getSuggestedTaboo()
        if self.suggestedTaboo:
            for word in self.suggestedTaboo:
                approve = QtWidgets.QPushButton()
                approve.setText("Approve")
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(word))
                self.tableWidget.setCellWidget(rowPosition, 0, approve)
                approve.clicked.connect(lambda  *args, target = word: self.approveSuggestTaboo(target))

    def deleteEffectiveTaboo(self, word):
        Taboo.deleteTaboo(word)
        self.tabooWord_list.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.addTaboo()

    def approveSuggestTaboo(self, word):
        Taboo.deleteSuggestTaboo(word)
        Taboo.addTaboo(word)
        self.tabooWord_list.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.addTaboo()

    def deleteAlleffective(self):
        Taboo.deleteAllTaboo()
        self.tabooWord_list.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.addTaboo()

    def deleteAllsuggest(self):
        Taboo.deleteAllSuggest()
        self.tabooWord_list.setRowCount(0)
        self.tableWidget.setRowCount(0)
        self.addTaboo()

    def getGUapp(self):
        allApp = DB.getPendingApp()
        application = ""
        if allApp is not None:
            for user in allApp:
                application = "Email: {}, " \
                              "Name: {}, " \
                              "Technical Interest: {}".format(allApp[user]['Email'],allApp[user]['Name'],allApp[user]['Tech_interest'])
                approve = QtWidgets.QPushButton()
                approve.setText("Approve")
                deny = QtWidgets.QPushButton()
                deny.setText("Deny")
                rowPosition = self.requestList.rowCount()
                self.requestList.insertRow(rowPosition)
                self.requestList.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(application))
                self.requestList.setCellWidget(rowPosition, 0, approve)
                self.requestList.setCellWidget(rowPosition, 1, deny)
                approve.clicked.connect(lambda *args, app = user: self.GUpromote(app))
                deny.clicked.connect(lambda *args, app= user: self.GUreject(app))

    def GUpromote(self, email):
        DB.GUpromote(email)
        self.requestList.setRowCount(0)
        self.getGUapp()

    def GUreject(self, email):
        DB.GUdeleteAPP(email)
        self.requestList.setRowCount(0)
        self.getGUapp()

    def addComplain(self):
        complains = DB.getComplains()
        if complains is not None:
            for complain in complains:

                for filename in complains[complain]:
                    resolve = QtWidgets.QPushButton()
                    resolve.setText("Resolve")
                    rowPosition = self.complaint_list.rowCount()
                    self.complaint_list.insertRow(rowPosition)
                    self.complaint_list.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(complain))
                    self.complaint_list.setItem(rowPosition,2, QtWidgets.QTableWidgetItem(filename))
                    self.complaint_list.setItem(rowPosition,3, QtWidgets.QTableWidgetItem(complains[complain][filename]))
                    self.complaint_list.setCellWidget(rowPosition, 0, resolve)
                    resolve.clicked.connect(lambda *args, user = complain, file = filename: self.resolveComplain(user,file))

    def resolveComplain(self, user, filename):
        DB.resolveComplains(user,filename)
        self.complaint_list.setRowCount(0)
        self.addComplain()

    def addlockFile(self):
        dict = Document.getAllLockFile()
        if dict is not None:
            for user in dict:
                for file in dict[user]:
                    unlock = QtWidgets.QPushButton()
                    unlock.setText("Unlock")
                    rowPosition = self.lockDoc_list.rowCount()
                    self.lockDoc_list.insertRow(rowPosition)
                    self.lockDoc_list.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(user))
                    self.lockDoc_list.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem(file))
                    self.lockDoc_list.setCellWidget(rowPosition, 0, unlock)
                    unlock.clicked.connect(lambda *args, person=user, doc=file: self.unlockDoc(person, doc))

    def unlockDoc(self, user, filename):
        Document.changeLock(user,filename,False)
        self.lockDoc_list.setRowCount(0)
        self.addlockFile()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

