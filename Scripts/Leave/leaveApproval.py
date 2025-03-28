import os
import sys
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils
from PyQt5 import QtCore, QtGui, QtWidgets

class Leave(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(946, 600)
        self.centralwidget = utils.widgetDrawer(None,0,0,0,0)
        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        self.widget = utils.widgetDrawer(self.centralwidget, 60, 130, 821, 101)
        # self.widget = QtWidgets.QWidget(self.centralwidget)
        # self.widget.setGeometry(QtCore.QRect(60, 130, 821, 101))
        # self.widget.setObjectName("widget")
        self.gridLayout = utils.gridLayoutDrawer(self.widget)
        # self.gridLayout = QtWidgets.QGridLayout(self.widget)
        # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = utils.tableWidgetDrawer(self.widget, 0, 0, 3, 1,8,3,["Employee","Leave Type","Start Date","End Date","Shift","Current Year","Previous Year","Status"])
        # self.tableWidget = QtWidgets.QTableWidget(self.widget)
        # self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(8)
        # self.tableWidget.setRowCount(3)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setHorizontalHeaderItem(7, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(0, 7, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(1, 7, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 2, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 3, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 4, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 5, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setItem(2, 7, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 3, 1)
        self.horizontalLayout = utils.horizontalLayoutDrawer(self.widget)
        # self.horizontalLayout = QtWidgets.QHBoxLayout()
        # self.horizontalLayout.setObjectName("horizontalLayout")
        

        self.approveButton = utils.pushButtonDrawers(self.widget, 0, 0, 80, 30, "Approve" , "")
        self.deleteButton = utils.pushButtonDrawers(self.widget, 0, 0, 80, 30, "Delete" , "")
        # self.pushButton = QtWidgets.QPushButton(self.widget)
        # self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.approveButton)


        # self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 2, 1)
        
        
        
        # self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        # self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_3.setObjectName("pushButton_3")
        # self.horizontalLayout_2.addWidget(self.pushButton_3)
        # self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_4.setObjectName("pushButton_4")
        # self.horizontalLayout_2.addWidget(self.pushButton_4)
        # self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        # self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        # self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_5.setObjectName("pushButton_5")
        # self.horizontalLayout_3.addWidget(self.pushButton_5)
        # self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        # self.pushButton_6.setObjectName("pushButton_6")
        # self.horizontalLayout_3.addWidget(self.pushButton_6)
        # self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = utils.menuBarDrawer(MainWindow, 0, 0, 946, 20)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 946, 20))
        # self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = utils.statusBarDrawer(MainWindow)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # return self.centralwidget

    # def retranslateUi(self, MainWindow):
    #     _translate = QtCore.QCoreApplication.translate
    #     MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    #     item = self.tableWidget.horizontalHeaderItem(0)
    #     item.setText(_translate("MainWindow", "Employee"))
    #     item = self.tableWidget.horizontalHeaderItem(1)
    #     item.setText(_translate("MainWindow", "Leave Type"))
    #     item = self.tableWidget.horizontalHeaderItem(2)
    #     item.setText(_translate("MainWindow", "Start Date"))
    #     item = self.tableWidget.horizontalHeaderItem(3)
    #     item.setText(_translate("MainWindow", "End Date"))
    #     item = self.tableWidget.horizontalHeaderItem(4)
    #     item.setText(_translate("MainWindow", "Shift"))
    #     item = self.tableWidget.horizontalHeaderItem(5)
    #     item.setText(_translate("MainWindow", "Current Year"))
    #     item = self.tableWidget.horizontalHeaderItem(6)
    #     item.setText(_translate("MainWindow", "Previous Year"))
    #     item = self.tableWidget.horizontalHeaderItem(7)
    #     item.setText(_translate("MainWindow", "Status"))
    #     __sortingEnabled = self.tableWidget.isSortingEnabled()
    #     self.tableWidget.setSortingEnabled(False)
    #     item = self.tableWidget.item(0, 0)
    #     item.setText(_translate("MainWindow", "Dereje Tadesse"))
    #     item = self.tableWidget.item(0, 1)
    #     item.setText(_translate("MainWindow", "Sick"))
    #     item = self.tableWidget.item(0, 2)
    #     item.setText(_translate("MainWindow", "August 5"))
    #     item = self.tableWidget.item(0, 3)
    #     item.setText(_translate("MainWindow", "September 18"))
    #     item = self.tableWidget.item(0, 4)
    #     item.setText(_translate("MainWindow", "Morning"))
    #     item = self.tableWidget.item(0, 5)
    #     item.setText(_translate("MainWindow", "2"))
    #     item = self.tableWidget.item(0, 6)
    #     item.setText(_translate("MainWindow", "1"))
    #     item = self.tableWidget.item(0, 7)
    #     item.setText(_translate("MainWindow", "Approved"))
    #     item = self.tableWidget.item(1, 0)
    #     item.setText(_translate("MainWindow", "Israel"))
    #     item = self.tableWidget.item(1, 1)
    #     item.setText(_translate("MainWindow", "Sick"))
    #     item = self.tableWidget.item(1, 2)
    #     item.setText(_translate("MainWindow", "August 16"))
    #     item = self.tableWidget.item(1, 3)
    #     item.setText(_translate("MainWindow", "January 1"))
    #     item = self.tableWidget.item(1, 4)
    #     item.setText(_translate("MainWindow", "Morning"))
    #     item = self.tableWidget.item(1, 5)
    #     item.setText(_translate("MainWindow", "1"))
    #     item = self.tableWidget.item(1, 6)
    #     item.setText(_translate("MainWindow", "1"))
    #     item = self.tableWidget.item(1, 7)
    #     item.setText(_translate("MainWindow", "Pending"))
    #     item = self.tableWidget.item(2, 0)
    #     item.setText(_translate("MainWindow", "Natnael"))
    #     item = self.tableWidget.item(2, 1)
    #     item.setText(_translate("MainWindow", "Annual"))
    #     item = self.tableWidget.item(2, 2)
    #     item.setText(_translate("MainWindow", "June 14"))
    #     item = self.tableWidget.item(2, 3)
    #     item.setText(_translate("MainWindow", "July 16"))
    #     item = self.tableWidget.item(2, 4)
    #     item.setText(_translate("MainWindow", "Afternoon"))
    #     item = self.tableWidget.item(2, 5)
    #     item.setText(_translate("MainWindow", "1"))
    #     item = self.tableWidget.item(2, 6)
    #     item.setText(_translate("MainWindow", "0"))
    #     item = self.tableWidget.item(2, 7)
    #     item.setText(_translate("MainWindow", "Approved"))
    #     self.tableWidget.setSortingEnabled(__sortingEnabled)
    #     self.pushButton.setText(_translate("MainWindow", "Approve"))
    #     self.pushButton_2.setText(_translate("MainWindow", "Delete"))
    #     self.pushButton_3.setText(_translate("MainWindow", "Approve"))
    #     self.pushButton_4.setText(_translate("MainWindow", "Delete"))
    #     self.pushButton_5.setText(_translate("MainWindow", "Approve"))
    #     self.pushButton_6.setText(_translate("MainWindow", "Delete"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Leave()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

