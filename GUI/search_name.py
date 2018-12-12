# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search_name.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, Dialog, parent=None,search_name = '',display_list =[]):
        super(Ui_Dialog, self).__init__(parent=parent)
        self.setObjectName("Dialog")
        self.setWindowTitle("Result Window")
        self.resize(424, 324)

        # the list is being pass in
        self.display_list = display_list

        # the name to be display at the top
        self.search_name = search_name
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 70, 331, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.name_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.name_label.setObjectName("name_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.name_label)
        self.nameResult_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.nameResult_label.setText(str(self.display_list[2]))
        self.nameResult_label.setObjectName("nameResult_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameResult_label)
        self.email_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.email_label.setObjectName("email_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.email_label)
        self.emailResult_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.emailResult_label.setText(str(self.display_list[0]))
        self.emailResult_label.setObjectName("emailResult_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.emailResult_label)
        self.interest_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.interest_label.setObjectName("interest_label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.interest_label)
        self.interestResult_label = QtWidgets.QLabel(self.formLayoutWidget)
        self.interestResult_label.setObjectName("interestResult_label")
        self.interestResult_label.setText(str(self.display_list[1]))
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.interestResult_label)
        self.result_label = QtWidgets.QLabel(self)
        self.result_label.setGeometry(QtCore.QRect(100, 20, 141, 20))
        self.result_label.setObjectName("result_label")
        self.targetName_label = QtWidgets.QLabel(self)
        self.targetName_label.setGeometry(QtCore.QRect(260, 20, 59, 16))
        self.targetName_label.setText(self.search_name)
        self.targetName_label.setObjectName("targetName_label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.name_label.setText(_translate("Dialog", "Name:"))
        self.email_label.setText(_translate("Dialog", "Email:"))
        self.interest_label.setText(_translate("Dialog", "Technical Interests:"))
        self.result_label.setText(_translate("Dialog", "Result for the name: "))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.show()
    sys.exit(app.exec_())