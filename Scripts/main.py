import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
import time
from datetime import *
import utils

sys.path.append(os.getcwd())
from Home import home
from Personel import addUser
from Department import addDepartment
from Device import addDevice

class Main(object):
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
        Homepage = home.Home().setupUi(AdminDashBoard)
        Personel = addUser.Personel().setupUi(AdminDashBoard)
        Department = addDepartment.Department().setupUi(AdminDashBoard)
        Device = addDevice.Device().setupUi(AdminDashBoard)
        '''Add Pages as Tab'''
        self.tabWidget.addTab(Homepage, "")
        self.tabWidget.addTab(Personel, "")
        self.tabWidget.addTab(Department, "")
        self.tabWidget.setCurrentIndex(0)
        '''Add Tab Text'''
        self.tabWidget.setTabText(self.tabWidget.indexOf(Homepage), "Home")
        self.tabWidget.setTabText(self.tabWidget.indexOf(Personel), "Personnel")
        self.tabWidget.setTabText(self.tabWidget.indexOf(Department), "Department")
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
