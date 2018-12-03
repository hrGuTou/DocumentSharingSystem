# -*- coding: utf-8 -*-

import sys
# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import threading
import time
from pathlib import Path

from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtWebEngineWidgets
from Editor.ShareEngine import ngrok
from Editor import BE
import sys
import Document
import os



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1090, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.history = QtWidgets.QPushButton(self.centralwidget)
        self.history.setObjectName("history")
        self.gridLayout.addWidget(self.history, 5, 2, 1, 1)

        self.fileName = QtWidgets.QLineEdit(self.centralwidget)
        self.fileName.setObjectName("fileName")
        self.gridLayout.addWidget(self.fileName, 0, 1, 1, 1)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.share = QtWidgets.QPushButton(self.centralwidget)
        self.share.setObjectName("share")
        self.gridLayout.addWidget(self.share, 4, 2, 1, 1)

        self.webView = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.webView.setUrl(QtCore.QUrl("http://127.0.0.1:8000/"))
        self.webView.setObjectName("webView")
        self.webView.page().profile().clearHttpCache()
        self.gridLayout.addWidget(self.webView, 1, 0, 5, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    #========= UI 按钮链接=======
        self.history.clicked.connect(self.clickHistory)
        self.share.clicked.connect(self.clickShare)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.history.setText(_translate("MainWindow", "History"))
        self.share.setText(_translate("MainWindow", "Share"))
        self.label.setText(_translate("MainWindow", "File Name:"))

    def clickHistory(self):
        pass

    def clickShare(self):
        """
            When share button is clicked, the current state of document will be saved
            The document property will be updated to SHARED
            Display the list of all OU, select one to share

            Then call Ngrok to get a share link
            Store that share link to the other OU's database

        :return:
        """
        print("share button")
        link = ngrok.NgrokTunnel()
        url = link.start()


def uploadDoc():
    my_file = Path("../cacheModified")
    if my_file.is_file():
        Document.saveDoc('hrgutou@gmail.com','../cacheModified','newtest')
        os.remove(my_file)
    else:
        pass

def loadBE():
    js = threading.Thread(target=BE.backend,args=())
    js.daemon=True
    js.start()


def loadGUI():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    rec = app.exec_()
    uploadDoc()
    sys.exit(rec)

def load(email):
    loadBE()
    loadGUI()



if __name__ == "__main__":
    load("")







