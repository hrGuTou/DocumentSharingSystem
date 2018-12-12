# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shareWith.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DB
from Editor.ShareEngine import ngrok as Tunnel
import Document


class Ui_ShareWith(object):
    def setupUi(self, ShareWith, src, filename):
        self.src = src
        self.filename= filename
        self.target = None

        ShareWith.setObjectName("ShareWith")
        ShareWith.resize(651, 198)
        self.gridLayout = QtWidgets.QGridLayout(ShareWith)
        self.gridLayout.setObjectName("gridLayout")
        self.shareTarget = QtWidgets.QLineEdit(ShareWith)
        self.shareTarget.setObjectName("shareTarget")
        self.gridLayout.addWidget(self.shareTarget, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(ShareWith)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(ShareWith)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 1, 0, 1, 1)

        self.retranslateUi(ShareWith)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(ShareWith.reject)



        QtCore.QMetaObject.connectSlotsByName(ShareWith)


    def retranslateUi(self, ShareWith):
        _translate = QtCore.QCoreApplication.translate
        ShareWith.setWindowTitle(_translate("ShareWith", "Share With .."))
        self.checkBox.setText(_translate("ShareWith", "Restricted: Can be viewed by GU"))



    def accept(self):
        self.target = self.shareTarget.text()
        if not self.target == "":
            if DB.checkUserExists(self.target):
                DB.shareTarget(self.src, self.filename, self.target,'')
                em = QtWidgets.QMessageBox()
                em.setIcon(QtWidgets.QMessageBox.Information)
                em.setText("Sharing document with " + self.target)
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec_()

            else:
                em = QtWidgets.QMessageBox()
                em.setIcon(QtWidgets.QMessageBox.Warning)
                em.setText("No such user, please check your input!")
                em.setStandardButtons(QtWidgets.QMessageBox.Ok)
                em.exec_()
                self.shareTarget.setText("")
        else:
            em = QtWidgets.QMessageBox()
            em.setIcon(QtWidgets.QMessageBox.Warning)
            em.setText("Please enter a valid username")
            em.setStandardButtons(QtWidgets.QMessageBox.Ok)
            em.exec_()

    def returnShare(self):
        if self.target is not None:
            return self.target

    def checkStatus(self):
        return self.checkBox.isChecked()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShareWith = QtWidgets.QDialog()
    ui = Ui_ShareWith()
    ui.setupUi(ShareWith,'','')
    ShareWith.show()
    sys.exit(app.exec_())

