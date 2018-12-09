# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'invitation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import DB

class Ui_seeInvitation(object):
    def setupUi(self, seeInvitation, email):
        self.email = email
        seeInvitation.setObjectName("seeInvitation")
        seeInvitation.resize(822, 569)
        self.gridLayout = QtWidgets.QGridLayout(seeInvitation)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(seeInvitation)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)

        self.addItem()

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.retranslateUi(seeInvitation)
        QtCore.QMetaObject.connectSlotsByName(seeInvitation)

    def retranslateUi(self, seeInvitation):
        _translate = QtCore.QCoreApplication.translate
        seeInvitation.setWindowTitle(_translate("seeInvitation", "Invitation"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("seeInvitation", "From"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("seeInvitation", "File Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("seeInvitation", "Accept"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("seeInvitation", "Reject"))

    def addItem(self):
        #items = DB.getInvitation(self.email)
        items = {
            'user1':{
                'File name': 'file1',
                'Link':'abc'
            },
            'user2':{
                'File name': 'file2',
                'Link': 'efd'
            }

        }
        if items is not None:
            connect = QtWidgets.QPushButton()
            connect.setText("Connect")
            delete = QtWidgets.QPushButton()
            delete.setText("Delete")
            rows = self.tableWidget.rowCount()
            print(rows)

            for key in items:

                self.tableWidget.insertRow(rows)
                self.tableWidget.setItem(rows,0, QtWidgets.QTableWidgetItem(key))
                self.tableWidget.setItem(rows,1, QtWidgets.QTableWidgetItem(items[key]['File name']))
                self.tableWidget.setCellWidget(rows,2, connect)
                self.tableWidget.setCellWidget(rows,3, delete)
                print(rows)

            connect.clicked.connect(lambda *args, row=rows: self.conn(row))
            delete.clicked.connect(self.rej)


    def conn(self,row):
        print(row)


    def rej(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    seeInvitation = QtWidgets.QDialog()
    ui = Ui_seeInvitation()
    ui.setupUi(seeInvitation,'hrgutou@gmail.com')
    seeInvitation.show()
    sys.exit(app.exec_())

