# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pc\Desktop\resourse\Attendance.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 501)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 721, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_9)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 721, 471))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.label = QtWidgets.QLabel(self.tab_12)
        self.label.setGeometry(QtCore.QRect(0, 10, 81, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.tab_12)
        self.lineEdit.setGeometry(QtCore.QRect(0, 30, 211, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.tab_12)
        self.label_2.setGeometry(QtCore.QRect(290, 10, 31, 16))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.tab_12)
        self.dateEdit.setGeometry(QtCore.QRect(290, 30, 110, 21))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(self.tab_12)
        self.pushButton.setGeometry(QtCore.QRect(220, 30, 41, 21))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_12)
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 401, 301))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_12)
        self.pushButton_2.setGeometry(QtCore.QRect(451, 30, 121, 23))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.tab_13)
        self.tabWidget_3.setGeometry(QtCore.QRect(0, 0, 711, 451))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_18 = QtWidgets.QWidget()
        self.tab_18.setObjectName("tab_18")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab_18)
        self.treeWidget.setGeometry(QtCore.QRect(0, 50, 231, 311))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.tab_18)
        self.dateEdit_2.setGeometry(QtCore.QRect(120, 20, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.comboBox = QtWidgets.QComboBox(self.tab_18)
        self.comboBox.setGeometry(QtCore.QRect(0, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.tab_18)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 71, 21))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(self.tab_18)
        self.label_6.setGeometry(QtCore.QRect(120, 0, 61, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_18)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 0, 61, 21))
        self.pushButton_3.setObjectName("pushButton_3")
        self.tabWidget_3.addTab(self.tab_18, "")
        self.tab_19 = QtWidgets.QWidget()
        self.tab_19.setObjectName("tab_19")
        self.treeWidget_2 = QtWidgets.QTreeWidget(self.tab_19)
        self.treeWidget_2.setGeometry(QtCore.QRect(0, 50, 191, 381))
        self.treeWidget_2.setObjectName("treeWidget_2")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_19)
        self.comboBox_2.setGeometry(QtCore.QRect(0, 20, 69, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_5 = QtWidgets.QLabel(self.tab_19)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_7 = QtWidgets.QLabel(self.tab_19)
        self.label_7.setGeometry(QtCore.QRect(120, 0, 61, 16))
        self.label_7.setObjectName("label_7")
        self.comboBox_5 = QtWidgets.QComboBox(self.tab_19)
        self.comboBox_5.setGeometry(QtCore.QRect(120, 20, 69, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_19)
        self.pushButton_6.setGeometry(QtCore.QRect(210, 0, 91, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget_3.addTab(self.tab_19, "")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.treeWidget_3 = QtWidgets.QTreeWidget(self.tab_20)
        self.treeWidget_3.setGeometry(QtCore.QRect(0, 60, 191, 351))
        self.treeWidget_3.setObjectName("treeWidget_3")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_3)
        self.label_8 = QtWidgets.QLabel(self.tab_20)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 71, 16))
        self.label_8.setObjectName("label_8")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_20)
        self.comboBox_3.setGeometry(QtCore.QRect(0, 20, 69, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_9 = QtWidgets.QLabel(self.tab_20)
        self.label_9.setGeometry(QtCore.QRect(120, 0, 71, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox_4 = QtWidgets.QComboBox(self.tab_20)
        self.comboBox_4.setGeometry(QtCore.QRect(120, 20, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_20)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 0, 91, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget_3.addTab(self.tab_20, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.label_22 = QtWidgets.QLabel(self.tab_21)
        self.label_22.setGeometry(QtCore.QRect(0, 0, 71, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.tab_21)
        self.label_23.setGeometry(QtCore.QRect(220, 0, 71, 16))
        self.label_23.setObjectName("label_23")
        self.treeWidget_10 = QtWidgets.QTreeWidget(self.tab_21)
        self.treeWidget_10.setGeometry(QtCore.QRect(0, 50, 231, 381))
        self.treeWidget_10.setObjectName("treeWidget_10")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_10)
        self.comboBox_17 = QtWidgets.QComboBox(self.tab_21)
        self.comboBox_17.setGeometry(QtCore.QRect(0, 20, 69, 22))
        self.comboBox_17.setObjectName("comboBox_17")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.comboBox_17.addItem("")
        self.dateEdit_5 = QtWidgets.QDateEdit(self.tab_21)
        self.dateEdit_5.setGeometry(QtCore.QRect(120, 20, 110, 22))
        self.dateEdit_5.setObjectName("dateEdit_5")
        self.dateEdit_6 = QtWidgets.QDateEdit(self.tab_21)
        self.dateEdit_6.setGeometry(QtCore.QRect(260, 20, 110, 22))
        self.dateEdit_6.setObjectName("dateEdit_6")
        self.label_3 = QtWidgets.QLabel(self.tab_21)
        self.label_3.setGeometry(QtCore.QRect(240, 20, 21, 21))
        self.label_3.setObjectName("label_3")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_21)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 20, 111, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget_3.addTab(self.tab_21, "")
        self.tabWidget_2.addTab(self.tab_13, "")
        self.tabWidget.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.tabWidget.addTab(self.tab_10, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tabWidget.addTab(self.tab_11, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_3.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("MainWindow", "Personel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "Department"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "Device"))
        self.label.setText(_translate("MainWindow", "Search Member"))
        self.label_2.setText(_translate("MainWindow", "Date"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Clock In"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Clock Out"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Time Worked"))
        self.pushButton_2.setText(_translate("MainWindow", "See Today\'s Report"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "Clock In/Out"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Employees"))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "Toltal Hours"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Abebe"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Kebede"))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "Hirut"))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "Faba"))
        self.treeWidget.topLevelItem(4).setText(0, _translate("MainWindow", "Nebil"))
        self.treeWidget.topLevelItem(5).setText(0, _translate("MainWindow", "Mekonen"))
        self.treeWidget.topLevelItem(6).setText(0, _translate("MainWindow", "Sara"))
        self.treeWidget.topLevelItem(7).setText(0, _translate("MainWindow", "Abreham"))
        self.treeWidget.topLevelItem(8).setText(0, _translate("MainWindow", "Dawit"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.comboBox.setItemText(0, _translate("MainWindow", "Finance"))
        self.comboBox.setItemText(1, _translate("MainWindow", "HR"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Managment"))
        self.label_4.setText(_translate("MainWindow", "Department"))
        self.label_6.setText(_translate("MainWindow", "Select Date"))
        self.pushButton_3.setText(_translate("MainWindow", "Generate"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_18), _translate("MainWindow", "Daily"))
        self.treeWidget_2.headerItem().setText(0, _translate("MainWindow", "Employees"))
        self.treeWidget_2.headerItem().setText(1, _translate("MainWindow", "Toltal Hours"))
        __sortingEnabled = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        self.treeWidget_2.topLevelItem(0).setText(0, _translate("MainWindow", "Abebe"))
        self.treeWidget_2.topLevelItem(1).setText(0, _translate("MainWindow", "Kebede"))
        self.treeWidget_2.topLevelItem(2).setText(0, _translate("MainWindow", "Hirut"))
        self.treeWidget_2.topLevelItem(3).setText(0, _translate("MainWindow", "Faba"))
        self.treeWidget_2.topLevelItem(4).setText(0, _translate("MainWindow", "Nebil"))
        self.treeWidget_2.topLevelItem(5).setText(0, _translate("MainWindow", "Mekonen"))
        self.treeWidget_2.topLevelItem(6).setText(0, _translate("MainWindow", "Sara"))
        self.treeWidget_2.topLevelItem(7).setText(0, _translate("MainWindow", "Abreham"))
        self.treeWidget_2.topLevelItem(8).setText(0, _translate("MainWindow", "Dawit"))
        self.treeWidget_2.setSortingEnabled(__sortingEnabled)
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Finance"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "HR"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Managment"))
        self.label_5.setText(_translate("MainWindow", "Department"))
        self.label_7.setText(_translate("MainWindow", "Select Week"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Mon"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "Tue"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Wen"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "New Item"))
        self.pushButton_6.setText(_translate("MainWindow", "Generate Report"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_19), _translate("MainWindow", "Weekly"))
        self.treeWidget_3.headerItem().setText(0, _translate("MainWindow", "Employees"))
        self.treeWidget_3.headerItem().setText(1, _translate("MainWindow", "Toltal Hours"))
        __sortingEnabled = self.treeWidget_3.isSortingEnabled()
        self.treeWidget_3.setSortingEnabled(False)
        self.treeWidget_3.topLevelItem(0).setText(0, _translate("MainWindow", "Abebe"))
        self.treeWidget_3.topLevelItem(1).setText(0, _translate("MainWindow", "Kebede"))
        self.treeWidget_3.topLevelItem(2).setText(0, _translate("MainWindow", "Hirut"))
        self.treeWidget_3.topLevelItem(3).setText(0, _translate("MainWindow", "Faba"))
        self.treeWidget_3.topLevelItem(4).setText(0, _translate("MainWindow", "Nebil"))
        self.treeWidget_3.topLevelItem(5).setText(0, _translate("MainWindow", "Mekonen"))
        self.treeWidget_3.topLevelItem(6).setText(0, _translate("MainWindow", "Sara"))
        self.treeWidget_3.topLevelItem(7).setText(0, _translate("MainWindow", "Abreham"))
        self.treeWidget_3.topLevelItem(8).setText(0, _translate("MainWindow", "Dawit"))
        self.treeWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "Department"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Finance"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "HR"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Managment"))
        self.label_9.setText(_translate("MainWindow", "Select Month"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "January"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "February"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "March"))
        self.pushButton_4.setText(_translate("MainWindow", "Generate Report"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_20), _translate("MainWindow", "Monthly"))
        self.label_22.setText(_translate("MainWindow", "Department"))
        self.label_23.setText(_translate("MainWindow", "Date Range"))
        self.treeWidget_10.headerItem().setText(0, _translate("MainWindow", "Employees"))
        self.treeWidget_10.headerItem().setText(1, _translate("MainWindow", "Total hours"))
        __sortingEnabled = self.treeWidget_10.isSortingEnabled()
        self.treeWidget_10.setSortingEnabled(False)
        self.treeWidget_10.topLevelItem(0).setText(0, _translate("MainWindow", "Abebe"))
        self.treeWidget_10.topLevelItem(1).setText(0, _translate("MainWindow", "Kebede"))
        self.treeWidget_10.topLevelItem(2).setText(0, _translate("MainWindow", "Hirut"))
        self.treeWidget_10.topLevelItem(3).setText(0, _translate("MainWindow", "Faba"))
        self.treeWidget_10.topLevelItem(4).setText(0, _translate("MainWindow", "Nebil"))
        self.treeWidget_10.topLevelItem(5).setText(0, _translate("MainWindow", "Mekonen"))
        self.treeWidget_10.topLevelItem(6).setText(0, _translate("MainWindow", "Sara"))
        self.treeWidget_10.topLevelItem(7).setText(0, _translate("MainWindow", "Abreham"))
        self.treeWidget_10.topLevelItem(8).setText(0, _translate("MainWindow", "Dawit"))
        self.treeWidget_10.setSortingEnabled(__sortingEnabled)
        self.comboBox_17.setItemText(0, _translate("MainWindow", "Finance"))
        self.comboBox_17.setItemText(1, _translate("MainWindow", "HR"))
        self.comboBox_17.setItemText(2, _translate("MainWindow", "Managment"))
        self.label_3.setText(_translate("MainWindow", "To"))
        self.pushButton_5.setText(_translate("MainWindow", "Generate Report"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_21), _translate("MainWindow", "Custom"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), _translate("MainWindow", " Report"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_9), _translate("MainWindow", "Attendance"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_10), _translate("MainWindow", "Payroll"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_11), _translate("MainWindow", "System Setting"))
#import member_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
