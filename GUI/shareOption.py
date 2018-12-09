# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shareOption.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from pathlib import Path
from shutil import copyfile

from PyQt5 import QtCore, QtGui, QtWidgets
from Editor.ShareEngine import ngrok as Tunnel
import Document,DB
from GUI import shareWith

class Ui_shareOption(object):
    def setupUi(self, shareOption, email, filename):
        self.ngrok = None
        self.email = email
        self.filename = filename
        self.modified = Path('../cacheModified')


        shareOption.setObjectName("shareOption")
        shareOption.resize(394, 217)
        self.gridLayout = QtWidgets.QGridLayout(shareOption)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(shareOption)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        self.pushButton_2 = QtWidgets.QPushButton(shareOption)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(shareOption)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(shareOption)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 3)
        self.pushButton = QtWidgets.QPushButton(shareOption)
        self.pushButton.setObjectName("pushButton")

        if not Document.checkFilePermission(self.email, self.filename) == 'private' or None:
            self.pushButton.setText("Private")
        else:
            self.pushButton.setText("Public")


        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(shareOption)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 3)

        self.retranslateUi(shareOption)
        QtCore.QMetaObject.connectSlotsByName(shareOption)



        self.pushButton.clicked.connect(self.public)
        self.pushButton_2.clicked.connect(self.share)
        self.pushButton_3.clicked.connect(self.restricted)


    def retranslateUi(self, shareOption):
        _translate = QtCore.QCoreApplication.translate
        shareOption.setWindowTitle(_translate("shareOption", "Dialog"))
        self.label.setText(_translate("shareOption", "Public: Can be seen by everyone. (Read-only)   "))
        self.pushButton_2.setText(_translate("shareOption", "Shared"))
        self.pushButton_3.setText(_translate("shareOption", "Restricted"))
        self.label_2.setText(_translate("shareOption", "Shared: View and edit with other OUs"))



        self.label_3.setText(_translate("shareOption", "Restricted: Shared and with GU read-only"))

    def public(self):
        if self.pushButton.text() == 'Public':
            if not self.modified.is_file():
                Document.saveDoc(self.email, '../cache', self.filename,'public')
            else:
                Document.saveDoc(self.email, self.modified, self.filename,'public')

            Document.setPermission(self.email, self.filename, 'public')
        else:
            if not self.modified.is_file():
                Document.saveDoc(self.email, '../cache', self.filename, 'private')
            else:
                Document.saveDoc(self.email, self.modified, self.filename, 'private')

            Document.setPermission(self.email, self.filename, 'private')

    def share(self):
        """
            save the current docs

        """

        if self.modified.is_file():
            Document.saveDoc(self.email, self.modified, self.filename,'share')
            copyfile('../cacheModified', '../cacheShare')
        else:
            Document.saveDoc(self.email, '../cache', self.filename,'share')
        Document.setPermission(self.email, self.filename, 'share')

        self.shareWith = QtWidgets.QDialog()
        self.ui = shareWith.Ui_ShareWith()
        self.ui.setupUi(self.shareWith, self.email, self.filename)
        self.shareWith.exec_()
        """
            start ngrok for real time editing
                    
        """
        self.ngrok = Tunnel.NgrokTunnel()
        self.link = self.ngrok.start()
        DB.shareTarget(self.email,self.filename, self.ui.returnShare(), self.link)

        print(self.ngrok.start())

    def restricted(self):
        Document.saveDoc(self.email, self.modified, self.filename,'restricted')

        Document.setPermission(self.email, self.filename, 'restricted')

    def getNgrokTunnel(self):
        if self.ngrok is not None:
            return self.ngrok
        else:
            return None

    def stopNgrok(self):
        self.ngrok.stop()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    shareOption = QtWidgets.QDialog()
    ui = Ui_shareOption()
    ui.setupUi(shareOption)
    shareOption.show()
    sys.exit(app.exec_())

