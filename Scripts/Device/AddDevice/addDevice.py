import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/"))))
import utils



class AddDevice(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.formLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 10, 50, 431, 256)
        self.horizontalLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 10, 330, 541, 80)
        self.tabWidget.addTab(self.tab, "")
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 12 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)

        self.labelAddDevice = utils.labelDrawers(self.tab, 10, 10, 201, 51, "Add Device")

        '''Form Layout'''
        self.formLayoutAddDevice = utils.formLayoutDrawer(self.formLayoutAddDeviceWidget)
        self.horizontalLayoutAddDevice = utils.horizontalLayoutDrawer(self.horizontalLayoutAddDeviceWidget)
       
        '''Labels'''
        self.labelAddId = utils.labelDrawers(self.formLayoutAddDeviceWidget, 10, 70, 201, 51, "Area ID")        
        self.labelDeviceName = utils.labelDrawers(self.formLayoutAddDeviceWidget, 10, 70, 201, 51, "Device Name")
        self.labelSerialNumber = utils.labelDrawers(self.formLayoutAddDeviceWidget, 10, 70, 201, 51, "Serial Number")
        self.labelIPAddress = utils.labelDrawers(self.formLayoutAddDeviceWidget, 10, 70, 201, 51, "IP Address")
        self.labelPortNumber = utils.labelDrawers(self.formLayoutAddDeviceWidget, 10, 70, 201, 51, "Port Number")
        self.labelArea = utils.labelDrawers(self.formLayoutAddDeviceWidget, 10, 70, 201, 51, "Area")
        '''Line Edits'''
        self.lineEditAreaId = utils.lineEditDrawers(self.formLayoutAddDeviceWidget, 10, 10, 20, 30)
        self.lineEditDeviceName = utils.lineEditDrawers(self.formLayoutAddDeviceWidget, 10, 50, 20, 30)
        self.lineEditSerialNumber = utils.lineEditDrawers(self.formLayoutAddDeviceWidget, 10, 100, 20, 30)
        self.lineEditIPAddress = utils.lineEditDrawers(self.formLayoutAddDeviceWidget, 10, 150, 20, 30)
        self.lineEditPortNumber = utils.lineEditDrawers(self.formLayoutAddDeviceWidget, 10, 200, 20, 30)
        
        '''Combo Box'''
        self.comboBoxArea = utils.comboBoxDrawers(self.formLayoutAddDeviceWidget, 20, 30, 20, 30, ["Area 1", "Area 2", "Area 3", "Area 4", "Area 5"])

        '''Buttons'''
        self.buttonSave = utils.pushButtonDrawers(self.tab, 20, 30, 20, 30, "Save and New", "")
        self.buttonOkay = utils.pushButtonDrawers(self.tab, 20, 30, 20, 30, "Okay", "")
        self.buttonCancel = utils.pushButtonDrawers(self.tab, 20, 30, 20, 30, "Cancel", "")

        '''Set Fonts'''
        self.labelAddDevice.setFont(self.fontHeader)
        self.labelAddId.setFont(self.fontNormal)
        self.labelDeviceName.setFont(self.fontNormal)
        self.labelSerialNumber.setFont(self.fontNormal)
        self.labelIPAddress.setFont(self.fontNormal)
        self.labelPortNumber.setFont(self.fontNormal)
        self.labelArea.setFont(self.fontNormal)




        '''Set Style'''
        self.lineEditAreaId = utils.widgetEditStyle(self.lineEditAreaId , ["border:1px solid #0076bd" , "border-radius:10px"])
        self.lineEditDeviceName = utils.widgetEditStyle(self.lineEditDeviceName , ["border:1px solid #0076bd" , "border-radius:10px"])
        self.lineEditSerialNumber = utils.widgetEditStyle(self.lineEditSerialNumber , ["border:1px solid #0076bd" , "border-radius:10px"])
        self.lineEditIPAddress = utils.widgetEditStyle(self.lineEditIPAddress , ["border:1px solid #0076bd" , "border-radius:10px"])
        self.lineEditPortNumber = utils.widgetEditStyle(self.lineEditPortNumber , ["border:1px solid #0076bd" , "border-radius:10px"])
        self.comboBoxArea = utils.widgetEditStyle(self.comboBoxArea , ["border:1px solid #0076bd" , "border-radius:10px"])
        self.buttonSave = utils.widgetEditStyle(self.buttonSave , ["background-color:#fff" ,"color:#0076bd", "border-top:1px solid #fff","border-bottom:1px solid #0076bd","padding-bottom:0px"])
        self.buttonOkay = utils.widgetEditStyle(self.buttonOkay , ["background-color:#fff" ,"color:#0076bd", "border-top:1px solid #fff","border-bottom:1px solid #0076bd","padding-bottom:0px"])
        self.buttonCancel = utils.widgetEditStyle(self.buttonCancel , ["background-color:#fff" , "color:#ff0000" , "border-top:1px solid #fff" , "border-bottom:1px solid #ff0000" , "padding-bottom:0px"])



        
        '''Set Widget'''
        self.formLayoutAddDevice.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelAddId)
        self.formLayoutAddDevice.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelDeviceName)
        self.formLayoutAddDevice.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelSerialNumber)
        self.formLayoutAddDevice.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelIPAddress)
        self.formLayoutAddDevice.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelPortNumber)
        self.formLayoutAddDevice.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelArea)
        self.formLayoutAddDevice.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditAreaId)
        self.formLayoutAddDevice.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditDeviceName)
        self.formLayoutAddDevice.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditSerialNumber)
        self.formLayoutAddDevice.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditIPAddress)
        self.formLayoutAddDevice.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditPortNumber)
        self.formLayoutAddDevice.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBoxArea)
    
        self.horizontalLayoutAddDevice.addWidget(self.buttonSave)
        self.horizontalLayoutAddDevice.addWidget(self.buttonOkay)
        self.horizontalLayoutAddDevice.addWidget(self.buttonCancel)






if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = AddDevice()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
