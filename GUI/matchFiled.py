# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'matchedfile.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, Dialog, parent=None, display_keyword ='', doc_list=[]):
        super(Ui_Dialog, self).__init__(parent=parent)
        self.setObjectName("Dialog")
        self.setWindowTitle("Mathced Document List")
        self.display_keyword = display_keyword
        self.doc_list = doc_list
        self.resize(340, 483)
        self.matched_list = QtWidgets.QListWidget(self)
        self.matched_list.setGeometry(QtCore.QRect(0, 80, 341, 411))
        self.matched_list.setObjectName("matched_list")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 20, 171, 16))
        self.label.setObjectName("label")
        self.keyword_label = QtWidgets.QLabel(self)
        self.keyword_label.setGeometry(QtCore.QRect(190, 20, 141, 16))
        self.keyword_label.setText(self.display_keyword)
        self.keyword_label.setObjectName("keyword_label")

        self.addItem()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Documents that contains: "))

    def addItem(self):
        for doc in self.doc_list:
            self.matched_list.addItem(doc.replace("_"," "))

if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.show()
    sys.exit(app.exec_())