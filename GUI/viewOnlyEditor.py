# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewOnlyEditor.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Document
from GUI import fileHistory
from GUI.suggestTaboo import Ui_Dialog as Suggestion_window
from GUI.complaint import Ui_Dialog as Complaint_window



class Ui_viewOnly(object):
    def setupUi(self, viewOnly, email, filename):
        self.email = email
        self.filename = filename

        viewOnly.setObjectName("viewOnly")
        viewOnly.resize(973, 713)
        self.gridLayout = QtWidgets.QGridLayout(viewOnly)
        self.gridLayout.setObjectName("gridLayout")
        self.viewOnly_2 = QtWidgets.QTextEdit(viewOnly)
        self.viewOnly_2.setEnabled(False)
        self.viewOnly_2.setObjectName("viewOnly_2")
        self.gridLayout.addWidget(self.viewOnly_2, 0, 0, 3, 1)
        self.suggestTaboo = QtWidgets.QPushButton(viewOnly)
        self.suggestTaboo.setObjectName("suggestTaboo")
        self.gridLayout.addWidget(self.suggestTaboo, 3, 1, 1, 1)
        self.history = QtWidgets.QPushButton(viewOnly)
        self.history.setObjectName("history")
        self.gridLayout.addWidget(self.history, 2, 1, 1, 1)
        self.complain = QtWidgets.QPushButton(viewOnly)
        self.complain.setObjectName("history")
        self.gridLayout.addWidget(self.complain, 1, 1, 1, 1)
        self.readFile()
        self.retranslateUi(viewOnly)
        QtCore.QMetaObject.connectSlotsByName(viewOnly)

        self.history.clicked.connect(self.showHistory)
        self.suggestTaboo.clicked.connect(self.taboo)
        self.complain.clicked.connect(self.complaint)

    def retranslateUi(self, viewOnly):
        _translate = QtCore.QCoreApplication.translate
        viewOnly.setWindowTitle(_translate("viewOnly", "View Only"))
        self.suggestTaboo.setText(_translate("viewOnly", "Suggest Taboo"))
        self.history.setText(_translate("viewOnly", "History"))
        self.complain.setText(_translate("viewOnly", "Complain"))

    def readFile(self):
        f = open('../cache','r')
        file = f.read()
        self.viewOnly_2.setText(file)
        font = QtGui.QFont()
        font.setPointSize(16)

        self.viewOnly_2.setFont(font)
        f.close()

    def showHistory(self):
        allHistory = Document.listallhistory(self.email,self.filename)
        self.historyWindow = QtWidgets.QDialog()
        self.history = fileHistory.Ui_fileHistory()
        self.history.setupUi(self.historyWindow, allHistory, self.email, self.filename)
        self.historyWindow.exec_()
        self.readFile()

    def taboo(self):
        self.suggestionWindow = QtWidgets.QDialog()
        self.ui = Suggestion_window(self.suggestionWindow)
        self.ui.exec()

    def complaint(self):
        self.complaintWindow = QtWidgets.QDialog()
        self.ui = Complaint_window(self.complaintWindow)
        self.ui.setFileName(self.filename)
        self.ui.setTargetEmail(self.email)
        self.ui.exec()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    viewOnly = QtWidgets.QDialog()
    ui = Ui_viewOnly()
    ui.setupUi(viewOnly, 'hrgutou@gmail.com','publiceveryone')
    viewOnly.show()
    sys.exit(app.exec_())

