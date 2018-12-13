# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suggestion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from DB import *

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, Dialog, parent=None):
        super(Ui_Dialog, self).__init__(parent=parent)
        self.setObjectName("Dialog")
        self.resize(532, 413)
        self.setWindowTitle("Complaint Page")

        ################### sumbit button #########################
        self.sumbit_button = QtWidgets.QPushButton(self)
        self.sumbit_button.setGeometry(QtCore.QRect(210, 380, 114, 32))
        self.sumbit_button.setObjectName("sumbit_button")
        ################### sumbit buttont event ###################
        self.sumbit_button.clicked.connect(self.submit_event)
        ############################################################


        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(110, 200, 331, 71))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.owner_email_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.owner_email_label.setObjectName("owner_email_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.owner_email_label)
        self.owner_email_field = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.owner_email_field.setObjectName("owner_email_field")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.owner_email_field)
        self.doc_name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.doc_name_label.setObjectName("doc_name_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.doc_name_label)
        self.doc_name_field = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.doc_name_field.setObjectName("doc_name_field")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doc_name_field)
        self.reason_text_field = QtWidgets.QPlainTextEdit(self)
        self.reason_text_field.setGeometry(QtCore.QRect(110, 280, 291, 71))
        self.reason_text_field.setObjectName("reason_text_field")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sumbit_button.setText(_translate("Dialog", "Sumbit"))
        self.owner_email_label.setText(_translate("Dialog", "Complaint target's email"))
        self.owner_email_field.setPlaceholderText(_translate("Dialog", "Please enter the target email"))
        self.doc_name_label.setText(_translate("Dialog", "Document name:"))
        self.doc_name_field.setPlaceholderText(_translate("Dialog", "Please enter the name of the document"))
        self.reason_text_field.setPlaceholderText(_translate("Dialog", "Please enter your complaints for this documents"))

    # submit button is clicked
    def submit_event(self):
        print('submit is clicked')

        email = self.owner_email_field.text()
        filename = self.doc_name_field.text()
        reason = self.reason_text_field.toPlainText()

        if email == '' or filename == '' or reason =='':
            em = QtWidgets.QMessageBox()
            em.setIcon(QtWidgets.QMessageBox.Warning)
            em.setText("Please complete all of the information above")
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec()

        else:
            fileComplain(email, filename, reason)
            em = QtWidgets.QMessageBox()
            em.setIcon(QtWidgets.QMessageBox.Information)
            em.setText("Complaint is sent to Super User!")
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec()

    def setFileName(self, filename):
        self.doc_name_field.setText(filename)

    def setTargetEmail(self, email):
        self.owner_email_field.setText(email)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.show()
    sys.exit(app.exec_())