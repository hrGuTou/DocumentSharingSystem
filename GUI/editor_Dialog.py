# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor_Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import os
import threading
from pathlib import Path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import Document
from Editor import BE

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1090, 780)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.Share = QtWidgets.QPushButton(Dialog)
        self.Share.setObjectName("Share")
        self.gridLayout.addWidget(self.Share, 2, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.History = QtWidgets.QPushButton(Dialog)
        self.History.setObjectName("History")
        self.gridLayout.addWidget(self.History, 3, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.webView = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.webView.setUrl(QtCore.QUrl("http://127.0.0.1:8000/"))
        self.webView.setObjectName("webView")
        self.webView.page().profile().clearHttpCache()
        self.gridLayout.addWidget(self.webView, 1, 0, 3, 2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Share.setText(_translate("Dialog", "Share"))
        self.History.setText(_translate("Dialog", "History"))
        self.label.setText(_translate("Dialog", "File Name"))

    def uploadDoc(self, email, newFile):
        #### RUN AT EXIT ####
        """

        :param email:
        :param newFile: True for new file, False for exist file
        :return:
        """
        fileName = self.lineEdit.text()
        fileName = fileName.replace(" ","_")

        if newFile:
            checkfileExist = Document.listallfiles(email)
            while fileName in checkfileExist:
                print("display warning")

        modified = Path("../cacheModified")
        original = Path("../cache")
        if modified.is_file():
            print("saving doc")
            Document.saveDoc(email, '../cacheModified', fileName)
            os.remove('../cacheModified')
        else:
            if modified.is_file():
                os.remove('../cacheModified')
            if original.is_file():
                os.remove('../cache')


    def setFileName(self, name):
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

