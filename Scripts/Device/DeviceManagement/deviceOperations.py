import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/"))))
import utils


class DeviceManagement(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.formLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 10, 120, 311, 61)
        self.horizontalLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 10, 180, 311, 41)
        self.page = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.pageOne = utils.widgetDrawer(None, 0, 0, 0, 0)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 14 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)
        self.fontStackedWidget = utils.fontSpecifier("Yu Gothic UI Semibold", 9 , True , 75)
        '''Stacked Widget'''

        self.stackedWidget = utils.stackedWidgetDrawer(self.tab, 140, 0, 1920, 1000)
        #self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))

#         self.stackedWidget.setStyleSheet("background-color:#fff\n"
# "")

        '''Form Layout'''
        self.formLayoutAddDevice = utils.formLayoutDrawer(self.formLayoutAddDeviceWidget)
        self.horizontalLayoutAddDevice = utils.horizontalLayoutDrawer(self.horizontalLayoutAddDeviceWidget)

        '''Labels'''
        self.labelAddDevice = utils.labelDrawers(self.tab, 10, 70, 111, 28, "Add Device")
        self.labelDeviceList = utils.labelDrawers(self.pageOne, 220, 30, 161, 28, "Device List")
        self.labelIPAddress = utils.labelDrawers(self.formLayoutAddDeviceWidget, 20, 100, 111, 28, "IP Address")

        '''Line Edits'''
        self.lineEditIPAddress = utils.lineEditDrawers(self.formLayoutAddDeviceWidget, 0, 0, 0, 0)
#         self.lineEdit_58 = QtWidgets.QLineEdit(self.formLayoutWidget_16)
#         self.lineEdit_58.setMinimumSize(QtCore.QSize(20, 30))
#         self.lineEdit_58.setStyleSheet("border :1px solid #0076bd;\n"
# "border-radius:10px;\n"
# "")
#         self.lineEdit_58.setObjectName("lineEdit_58")

        '''Push Buttons'''
        self.buttonSave = utils.pushButtonDrawers(self.tab, 20, 30, 20, 30, "Save", "")
        self.buttonCancel = utils.pushButtonDrawers(self.tab, 20, 30, 20, 30, "Cancel", "")
        
#         self.dev_okbtn_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_31)
#         font = QtGui.QFont()
#         font.setFamily("Yu Gothic UI Semibold")
#         font.setPointSize(11)
#         font.setBold(True)
#         font.setWeight(75)
#         self.dev_okbtn_3.setFont(font)
#         self.dev_okbtn_3.setStyleSheet("background-color:#fff;\n"
# "color:#0076bd;\n"
# "border-top:1px solid #fff;\n"
# "border-bottom:1px solid #0076bd;\n"
# "padding-bottom:0px")
#         self.dev_okbtn_3.setObjectName("dev_okbtn_3")

        '''TableWidget'''
        self.tableWidgetDeviceList = utils.tableWidgetDrawer(self.pageOne, 220, 60, 881, 311,6,0,["Device ID","Device Name" , "Serial Number", "IP Address", "Port Number", "MAC Address"])
        

        '''Set Fonts'''
        self.labelAddDevice.setFont(self.fontHeader)
        self.labelDeviceList.setFont(self.fontHeader)
        self.labelIPAddress.setFont(self.fontNormal)
        self.stackedWidget.setFont(self.fontStackedWidget)



        '''Set Widget'''
        self.formLayoutAddDevice.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelIPAddress)
        self.formLayoutAddDevice.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditIPAddress)
        self.horizontalLayoutAddDevice.addWidget(self.buttonSave)
        self.horizontalLayoutAddDevice.addWidget(self.buttonCancel)
        self.stackedWidget.addWidget(self.pageOne)
        




if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = DeviceManagement()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
