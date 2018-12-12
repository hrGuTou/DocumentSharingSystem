# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileHistory.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import Document


class Ui_fileHistory(object):
    def setupUi(self, fileHistory, history, email, filename):
        self.history = history
        self.email = email
        self.filename = filename

        fileHistory.setObjectName("fileHistory")
        fileHistory.resize(403, 625)
        self.gridLayout = QtWidgets.QGridLayout(fileHistory)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(fileHistory)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.listWidget.addItem(item)
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.additems()

        self.retranslateUi(fileHistory)
        QtCore.QMetaObject.connectSlotsByName(fileHistory)

        self.listWidget.itemActivated.connect(self.openfile)

    def retranslateUi(self, fileHistory):
        _translate = QtCore.QCoreApplication.translate
        fileHistory.setWindowTitle(_translate("fileHistory", "History"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("fileHistory", "Time Edited"))
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def additems(self):
        for item in self.history:
            self.listWidget.addItem(item)

    def openfile(self, item):
        selectedTarget = item.text()
        Document.openfile(self.email, self.email, self.filename, selectedTarget)
        em = QtWidgets.QMessageBox()
        em.setIcon(QtWidgets.QMessageBox.Information)
        em.setText("Load history file finished")
        em.setStandardButtons(QtWidgets.QMessageBox.Ok)
        em.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fileHistory = QtWidgets.QDialog()
    ui = Ui_fileHistory()
    ui.setupUi(fileHistory, ['1','2','3'])
    fileHistory.show()
    sys.exit(app.exec_())

