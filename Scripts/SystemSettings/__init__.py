import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import time
from datetime import *
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))

import utils
sys.path.append(os.getcwd())
from .User import UserSetting
from . import alertSettings , companySettings

class SystemSettingsTab(object):
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
        userSetting = UserSetting().setupUi(AdminDashBoard)
        alertSetting = alertSettings.AlertSettings().setupUi(AdminDashBoard)
        companySetting = companySettings.CompanySettings().setupUi(AdminDashBoard)
        
        '''Add Pages as Tab'''
        self.tabWidget.addTab(userSetting, "")
        self.tabWidget.addTab(alertSetting, "")
        self.tabWidget.addTab(companySetting, "")
        self.tabWidget.setCurrentIndex(0)
        '''Add Tab Text'''
        self.tabWidget.setTabText(self.tabWidget.indexOf(userSetting), "User")
        self.tabWidget.setTabText(self.tabWidget.indexOf(alertSetting), "Alert Settings")
        self.tabWidget.setTabText(self.tabWidget.indexOf(companySetting), "Company Settings")

        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.centralwidget






# if __name__ == "__main__":
#     import sys
#     os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
#     app = QtWidgets.QApplication(sys.argv)
#     app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     AdminDashBoard = QtWidgets.QMainWindow()
#     ui = SystemSettingsTab()
#     ui.setupUi(AdminDashBoard)
#     AdminDashBoard.show()
#     sys.exit(app.exec_())
