import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/"))))
import utils


class Reboot(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.formLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 10, 120, 311, 61)
        self.horizontalLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 10, 180, 311, 41)
        self.page = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.pageOne = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.stackedWidget = utils.stackedWidgetDrawer(self.tab, 140, 0, 1920, 1000)
        self.verticalLayoutWidget = utils.widgetDrawer(self.tab, 400, 200, 741, 321)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI", 16 , True , 75)


        '''Form Layout'''
        self.verticalLayoutRestart = utils.verticalLayoutDrawer(self.verticalLayoutWidget)
        '''Labels'''
        self.labelRestartDevice = utils.labelDrawers(self.tab, 410, 0, 701, 171, "Restarting device may result in loss of unsaved work!")
        self.labelRestartDevice.setGeometry(QtCore.QRect(410, 0, 701, 171))
        self.labelRestartDevice.setStyleSheet("color:red")      

        '''Push Buttons'''
        self.buttonrestart = utils.pushButtonDrawers(self.verticalLayoutWidget, 20, 30, 50, 50, "Restart", "iconmonstr-power-on-off-10-240.png")
        self.buttonrestart.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonrestart.setStyleSheet("background-color:#fff;\n"
"border-bottom:2px solid red;\n"
"color:#0076bd;\n"
"font-family:monospace;\n"
"font-size:20px")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/restarticon/iconmonstr-power-on-off-10-240.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonrestart.setIcon(icon)
        self.buttonrestart.setIconSize(QtCore.QSize(50, 50))
        

        '''Set Fonts'''
        self.labelRestartDevice.setFont(self.fontHeader)


        '''Set Widget'''
        self.verticalLayoutRestart.addWidget(self.buttonrestart)


        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.tab

        




if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = Reboot()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
