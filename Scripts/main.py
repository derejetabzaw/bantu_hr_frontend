"""_This module is where everything is put in order the content of each tab is called_
"""

import os
from PyQt5 import QtCore, QtGui, QtWidgets
"""importing packages used for pyhton Gui """
import os 
"""OS module in Python provides functions for interacting with the operating system.
This module provides a portable way of using operating system dependent functionality."""
import sys
"""It allows operating on the interpreter as it provides access to the variables and 
functions that interact strongly with the interpreter"""
import time
from datetime import *
import utils

sys.path.append(os.getcwd())
"""import tabs which we will execute here"""
from Home import home
from Personel import addUser
from Department import addDepartment
from Device import DeviceTabs
from Leave import leaveType
from Payroll import PayrollTabs
from Attendance import AttendanceTab
from SystemSettings import SystemSettingsTab

      

class Main(object):
    def setupUi(self, AdminDashBoard):
        AdminDashBoard.setObjectName("AdminDashBoard")
        """here  style choices are made for the Admindashboard"""
        AdminDashBoard.resize(1922, 1080)
        AdminDashBoard.setMaximumSize(QtCore.QSize(16777215, 16777215))
        AdminDashBoard.setStyleSheet("background-color:#fff")
        self.centralwidget = QtWidgets.QWidget(AdminDashBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = utils.tabWidgetDrawer(self.centralwidget, 0, 0, 1920, 1000)
        self.font = utils.fontSpecifier("Yu Gothic UI Semibold", 9 , True , 75)
        self.tabWidget.setFont(self.font)
        self.tabWidget.setStyleSheet("color:#000")
        self.tabWidget.setIconSize(QtCore.QSize(20, 40))

        '''Import Pages'''
        Homepage = home.Home().setupUi(AdminDashBoard)
        Personel = addUser.Personel().setupUi(AdminDashBoard)
        Department = addDepartment.Department().setupUi(AdminDashBoard)
        Leave = leaveType.Leave().setupUi(AdminDashBoard)
        SystemSettings = SystemSettingsTab().setupUi(AdminDashBoard)
        Payroll = PayrollTabs().setupUi(AdminDashBoard)
        Attendance = AttendanceTab().setupUi(AdminDashBoard)
        Device = DeviceTabs().setupUi(AdminDashBoard)
        '''Add Pages as Tab'''
        self.tabWidget.addTab(Homepage, "")
        self.tabWidget.addTab(Personel, "")
        self.tabWidget.addTab(Department, "")
        self.tabWidget.addTab(Payroll, "")
        self.tabWidget.addTab(Device, "")
        self.tabWidget.addTab(Leave, "")
        self.tabWidget.addTab(Attendance, "")
        self.tabWidget.addTab(SystemSettings, "")
        self.tabWidget.setCurrentIndex(0)
        '''Add Tab Text'''
        self.tabWidget.setTabText(self.tabWidget.indexOf(Homepage), "Home")
        self.tabWidget.setTabText(self.tabWidget.indexOf(Personel), "Personnel")
        self.tabWidget.setTabText(self.tabWidget.indexOf(Department), "Department")
        self.tabWidget.setTabText(self.tabWidget.indexOf(Payroll), "Payroll")
        self.tabWidget.setTabText(self.tabWidget.indexOf(Device), "Device")
        self.tabWidget.setTabText(self.tabWidget.indexOf(Leave), "Leave")
        self.tabWidget.setTabText(self.tabWidget.indexOf(Attendance), "Attendance")
        self.tabWidget.setTabText(self.tabWidget.indexOf(SystemSettings), "System Settings")

        AdminDashBoard.setWindowTitle("G!ze")
        AdminDashBoard.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)




if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = Main()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
