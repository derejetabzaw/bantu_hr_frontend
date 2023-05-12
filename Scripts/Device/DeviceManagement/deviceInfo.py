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
        self.formLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 330, 160, 691, 331)
        self.tabWidget.addTab(self.tab, "")
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 18 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 9 , True , 75)

        '''Form Layout'''
        self.formLayoutAddDevice = utils.formLayoutDrawer(self.formLayoutAddDeviceWidget)
       
        '''Labels'''
        self.labelDeviceSettings = utils.labelDrawers(self.tab, 510, 40, 271, 51, "Device Settings")
        self.labelDeviceTime = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 80, 271, 51, "Device Time")
        self.labelBuildVersion = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 120, 271, 51, "Build Version")
        self.labelCameraOpen = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 160, 271, 51, "Camera Open")
        self.labelBiometricType = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 200, 271, 51, "Biometric Type")
        self.labelFaceVersion = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 240, 271, 51, "Face Version")
        self.labelFaceOpen = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 280, 271, 51, "Face Open")
        self.labelFingerprintOpen = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 320, 271, 51, "Fingerprint Open")
        self.labelMacAddress = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 360, 271, 51, "Mac Address")
        self.labelSerialNumber = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 400, 271, 51, "Serial Number")
        self.labelPlatform = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 440, 271, 51, "Platform")
        self.labelSoftwareVersion = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 480, 271, 51, "Software Version")
        self.labelVendor = utils.labelDrawers(self.formLayoutAddDeviceWidget, 510, 520, 271, 51, "Vendor")

        '''Set Fonts'''
        self.labelDeviceSettings.setFont(self.fontHeader)
        self.labelDeviceTime.setFont(self.fontNormal)
        self.labelBuildVersion.setFont(self.fontNormal)
        self.labelCameraOpen.setFont(self.fontNormal)
        self.labelBiometricType.setFont(self.fontNormal)
        self.labelFaceVersion.setFont(self.fontNormal)
        self.labelFaceOpen.setFont(self.fontNormal)
        self.labelFingerprintOpen.setFont(self.fontNormal)
        self.labelMacAddress.setFont(self.fontNormal)
        self.labelSerialNumber.setFont(self.fontNormal)
        self.labelPlatform.setFont(self.fontNormal)
        self.labelSoftwareVersion.setFont(self.fontNormal)
        self.labelVendor.setFont(self.fontNormal)

        '''Set Widget'''
        self.formLayoutAddDevice.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelDeviceTime)
        self.formLayoutAddDevice.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelBuildVersion)
        self.formLayoutAddDevice.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelCameraOpen)
        self.formLayoutAddDevice.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelBiometricType)
        self.formLayoutAddDevice.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelFaceVersion)
        self.formLayoutAddDevice.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelFaceOpen)
        self.formLayoutAddDevice.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelFingerprintOpen)
        self.formLayoutAddDevice.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.labelMacAddress)
        self.formLayoutAddDevice.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.labelSerialNumber)
        self.formLayoutAddDevice.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.labelPlatform)
        self.formLayoutAddDevice.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.labelSoftwareVersion)
        self.formLayoutAddDevice.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.labelVendor)

      

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
