# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'suggestion.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Taboo

class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self, Dialog, parent=None):
        super(Ui_Dialog, self).__init__(parent=parent)
        self.setObjectName("Dialog")
        self.setWindowTitle('Taboo Word Suggestion')
        self.resize(485, 270)
        self.sumbit_button = QtWidgets.QPushButton(self)
        self.sumbit_button.setGeometry(QtCore.QRect(170, 200, 114, 32))
        self.sumbit_button.setObjectName("sumbit_button")

        ##################### submit buttont event handler ######
        self.sumbit_button.clicked.connect(self.submit_event)
        #########################################################

        self.taboo_word_field = QtWidgets.QPlainTextEdit(self)
        self.taboo_word_field.setGeometry(QtCore.QRect(50, 30, 371, 151))
        self.taboo_word_field.setObjectName("taboo_word_field")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.sumbit_button.setText(_translate("Dialog", "Sumbit"))
        self.taboo_word_field.setPlaceholderText(_translate("Dialog", "Please enter your suggestion taboo words here"))

    def submit_event(self):
        taboo_words = self.taboo_word_field.toPlainText()




        print("submit button in suggestion taboo word is clicked")
        if taboo_words =='':
            em = QtWidgets.QMessageBox()
            em.setIcon(QtWidgets.QMessageBox.Warning)
            em.setText("Please enter at least one taboo word, separate with comma.")
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec()

        else:
            result = taboo_words.split(',')
            for i in range(len(result)):
                result[i] = result[i].strip(" ")

            Taboo.suggestTaboo(result)
        em = QtWidgets.QMessageBox()
        em.setIcon(QtWidgets.QMessageBox.Warning)
        em.setText("Suggestion is sent to Super User")
        em.setStandardButtons(QtWidgets.QMessageBox.Ok)
        em.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.show()
    sys.exit(app.exec_())