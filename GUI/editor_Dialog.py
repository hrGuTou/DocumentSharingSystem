# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import threading
from pathlib import Path
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from GUI import shareOption
from Editor.ShareEngine import ngrok as Tunnel

import Document
from Editor import BE

class Ui_Dialog(object):
    def setupUi(self, Dialog, email, filename):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1090, 780)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Share = QtWidgets.QPushButton(Dialog)
        self.Share.setObjectName("Share")
        self.gridLayout.addWidget(self.Share, 3, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.History = QtWidgets.QPushButton(Dialog)
        self.History.setObjectName("History")
        self.gridLayout.addWidget(self.History, 4, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.webView = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.webView.setUrl(QtCore.QUrl("http://127.0.0.1:8000/"))
        self.webView.setObjectName("webView")
        self.webView.page().profile().clearHttpCache()
        self.gridLayout.addWidget(self.webView, 1, 0, 4, 2)

        self.lockFile = QtWidgets.QPushButton(Dialog)
        self.lockFile.setObjectName("lockFile")
        self.gridLayout.addWidget(self.lockFile, 2, 2, 1, 1)

        self.ngrok = None
        self.email = email
        self.filename = filename
        self.lineEdit.setText(self.filename)
        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.Share.clicked.connect(self.clickShare)
        self.lockFile.clicked.connect(self.lockfile)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Share.setText(_translate("Dialog", "Share"))
        self.History.setText(_translate("Dialog", "History"))
        self.label.setText(_translate("Dialog", "File Name"))
        locked = Document.isFileLocked(self.email, self.filename)
        if locked is not None:
            if locked:
                self.lockFile.setText(_translate("Dialog","Unlock"))
            else:
                self.lockFile.setText(_translate("Dialog","Lock"))
        else:
            self.lockFile.setText(_translate("Dialog","Lock"))


    def lockfile(self):
        currStatus = self.lockFile.text()
        Document.changeLock(self.email,self.filename,currStatus)
        if currStatus == "Lock":
            self.lockFile.setText("Unlock")

        else:
            self.lockFile.setText("Lock")




    def clickShare(self):

        self.shareOption = QtWidgets.QDialog()
        self.ui = shareOption.Ui_shareOption()
        filename = self.lineEdit.text()
        self.ui.setupUi(self.shareOption, self.email, filename)
        self.shareOption.exec_()

        if self.ui.getNgrokTunnel() is not None:
            self.ngrok = self.ui.getNgrokTunnel()


    def uploadDoc(self, newFile):
        #### RUN AT EXIT ####
        """

        :param email:
        :param newFile: True for new file, False for exist file
        :return:
        """
        if self.ngrok is not None:
            self.ngrok.stop()


        fileName = self.lineEdit.text()
        fileName = fileName.replace(" ","_")

        if newFile:
            checkfileExist = Document.listallfiles(self.email)
            print(checkfileExist)
            if not checkfileExist == 0:
                if fileName in checkfileExist:
                    print("display warning")

        modified = Path("../cacheModified")
        original = Path("../cache")
        permission = Document.checkFilePermission(self.email, fileName)
        if permission is None:
            permission = 'private'

        if modified.is_file():
            print("saving doc")
            Document.saveDoc(self.email, '../cacheModified', fileName, permission)
            os.remove('../cacheModified')
        else:
            if modified.is_file():
                os.remove('../cacheModified')
            if original.is_file():
                os.remove('../cache')


    def setFileName(self, name):
        self.name = name
        name = name.replace("_", " ")
        self.lineEdit.setText(name)

from PyQt5 import QtWebEngineWidgets


def loadBE():
    js = threading.Thread(target=BE.backend,args=())
    js.daemon=True
    js.start()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

