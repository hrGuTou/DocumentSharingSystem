# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shareEditor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from flask import Flask
import threading
import Document
import DB
class Ui_shareDoc(object):
    def setupUi(self, shareDoc, url, original, filename):
        self.url = url
        self.original = original
        self.filename = filename

        shareDoc.setObjectName("shareDoc")
        shareDoc.resize(983, 740)
        self.gridLayout = QtWidgets.QGridLayout(shareDoc)
        self.gridLayout.setObjectName("gridLayout")
        self.webView = QtWebEngineWidgets.QWebEngineView(shareDoc)
        self.webView.setUrl(QtCore.QUrl(self.url))
        self.webView.setObjectName("webView")
        self.webView.page().profile().clearHttpCache()
        self.gridLayout.addWidget(self.webView, 1, 0, 3, 2)
        self.suggestTaboo = QtWidgets.QPushButton(shareDoc)
        self.suggestTaboo.setObjectName("suggestTaboo")
        self.gridLayout.addWidget(self.suggestTaboo, 3, 0, 1, 1)


        self.retranslateUi(shareDoc)
        QtCore.QMetaObject.connectSlotsByName(shareDoc)
        self.be()


    def be(self):
        self.docID = Document.getLastestVersion(self.original, self.filename)
        DB.user.child(DB.removeIllegalChar(self.original)).child("Document_history").child(self.docID).listen(self.handler)

    def handler(self,data):
        ref = DB.user.child(DB.removeIllegalChar(self.original)).child("Document_history").child(self.docID).get()
        print(ref)
        if ref['Locked'] == 'Lock':
            time.sleep(1)
            self.webView.page().runJavaScript("$('#Editor').prop('disabled', true);")
        else:
            time.sleep(1)
            self.webView.page().runJavaScript("$('#Editor').prop('disabled', false);")

    def retranslateUi(self, shareDoc):
        _translate = QtCore.QCoreApplication.translate
        shareDoc.setWindowTitle(_translate("shareDoc", "Share Docs"))
        self.suggestTaboo.setText(_translate("shareDoc", "Suggest Taboo"))

    def disableTextEdit(self, disable):
        print('check')
        if disable:
            self.webView.page().runJavaScript("$('#Editor').prop('disabled', true);")
        else:
            self.webView.page().runJavaScript("$('#Editor').prop('disabled', false);")


from PyQt5 import QtWebEngineWidgets





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shareDoc = QtWidgets.QDialog()
    ui = Ui_shareDoc()
    ui.setupUi(shareDoc, 'https://f8b835db.ngrok.io/','hrgutou@gmail.com','shared')
    shareDoc.show()

    sys.exit(app.exec_())

