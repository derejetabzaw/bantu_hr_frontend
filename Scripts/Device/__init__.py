import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import time
from datetime import *
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))

import utils
sys.path.append(os.getcwd())
from .Area import AreaTabs
from .AddDevice import addDevice
from .DeviceManagement import DeviceManagementTabs
# from WorkCode import *

class DeviceTabs(object):
    def setupUi(self, AdminDashBoard):
        AdminDashBoard.setObjectName("AdminDashBoard")
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
        area = AreaTabs().setupUi(AdminDashBoard)
        addDevices = addDevice.AddDevice().setupUi(AdminDashBoard)
        deviceManagement = DeviceManagementTabs().setupUi(AdminDashBoard)
        #alertSetting = alertSettings.AlertSettings().setupUi(AdminDashBoard)
        #companySetting = companySettings.CompanySettings().setupUi(AdminDashBoard)
        
        '''Add Pages as Tab'''
        self.tabWidget.addTab(area, "")
        self.tabWidget.addTab(addDevices, "")
        self.tabWidget.addTab(deviceManagement, "")
        self.tabWidget.setCurrentIndex(0)
        '''Add Tab Text'''
        self.tabWidget.setTabText(self.tabWidget.indexOf(area), "Area")
        self.tabWidget.setTabText(self.tabWidget.indexOf(addDevices), "Add Device")
        self.tabWidget.setTabText(self.tabWidget.indexOf(deviceManagement), "Device Management")


        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.centralwidget






# if __name__ == "__main__":
#     import sys
#     os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
#     app = QtWidgets.QApplication(sys.argv)
#     app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     AdminDashBoard = QtWidgets.QMainWindow()
#     ui = DeviceTabs()
#     ui.setupUi(AdminDashBoard)
#     AdminDashBoard.show()
#     sys.exit(app.exec_())
