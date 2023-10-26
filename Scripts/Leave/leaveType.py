import os
import time
from datetime import *
import sys
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
from Leave import leaveApproval,leaveBalance
import utils
from PyQt5 import QtCore, QtGui, QtWidgets



class Leave(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        #self.formLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 330, 160, 691, 331)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayoutWidgets = utils.widgetDrawer(self.tab,220, 60, 353, 285)
        # self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 18 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 9 , True , 75)

        '''Frame - Line'''
        self.separatingLine = utils.frameDrawer(self.tab, 170, 10, 21, 1001,"VLine","Sunken")
        '''Form Layout'''
        self.gridLayout = utils.gridLayoutDrawer(self.gridLayoutWidgets)
        #self.formLayoutAddDevice = utils.formLayoutDrawer(self.formLayoutAddDeviceWidget)
       
        '''Labels'''
        self.labelLeaveTypeName = utils.labelDrawers(self.gridLayoutWidgets, 510, 40, 271, 51, "Leave Type Name")
        self.labelAnnualLeave = utils.labelDrawers(self.gridLayoutWidgets, 510, 80, 271, 51, "Annual Leave")
        self.labelWOPayLeave = utils.labelDrawers(self.gridLayoutWidgets, 510, 120, 271, 51, "Leave Without Pay")
        self.labelSpecialLeave = utils.labelDrawers(self.gridLayoutWidgets, 510, 160, 271, 51, "Special Leave With Pay")
        self.labelMaternityLeave = utils.labelDrawers(self.gridLayoutWidgets, 510, 200, 271, 51, "Maternity Leave")
        self.labelPMLeave = utils.labelDrawers(self.gridLayoutWidgets, 510, 240, 271, 51, "Leave For Personal Matters")
        self.labelPaternityLeave = utils.labelDrawers(self.gridLayoutWidgets, 510, 280, 271, 51, "Paternity Leave")
        self.labelMourningLeave = utils.labelDrawers(self.gridLayoutWidgets, 510, 320, 271, 51, "Mourning Leave")
        self.labelSpecialLeave = utils.labelDrawers(self.gridLayoutWidgets, 510, 360, 271, 51, "Special Leave")


        '''Buttons'''
        self.buttonEditAnnualLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 810, 80, 81, 31, "Edit" , "")
        self.buttonDeleteAnnualLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 900, 80, 81, 31, "Delete" , "")
        self.buttonEditWOPayLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 810, 120, 81, 31, "Edit" , "")
        self.buttonDeleteWOPayLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 900, 120, 81, 31, "Delete" , "")
        self.buttonEditSpecialLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 810, 160, 81, 31, "Edit" , "")
        self.buttonDeleteSpecialLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 900, 160, 81, 31, "Delete" , "")
        self.buttonEditMaternityLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 810, 200, 81, 31, "Edit" , "")
        self.buttonDeleteMaternityLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 900, 200, 81, 31, "Delete" , "")
        self.buttonEditPMLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 810, 240, 81, 31, "Edit" , "")
        self.buttonDeletePMLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 900, 240, 81, 31, "Delete" , "")
        self.buttonEditPaternityLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 810, 280, 81, 31, "Edit" , "")
        self.buttonDeletePaternityLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 900, 280, 81, 31, "Delete" , "")
        self.buttonEditMourningLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 810, 320, 81, 31, "Edit" , "")
        self.buttonDeleteMourningLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 900, 320, 81, 31, "Delete" , "")
        self.buttonEditSpecialLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 810, 360, 81, 31, "Edit" , "")
        self.buttonDeleteSpecialLeave = utils.pushButtonDrawers(self.gridLayoutWidgets, 900, 360, 81, 31, "Delete" , "")
        self.buttonLeaveType = utils.pushButtonDrawers(self.tab, 40, 60, 130, 120, "Leave Type" , "")
        self.buttonLeaveBalance = utils.pushButtonDrawers(self.tab, 40, 190, 130, 120, "Leave Balance" , "")
        self.buttonLeaveApproval = utils.pushButtonDrawers(self.tab, 40, 320, 130, 120, "Leave Approval" , "")
        '''Set Fonts'''
        # self.labelDeviceSettings.setFont(self.fontHeader)
        # self.labelDeviceTime.setFont(self.fontNormal)
        # self.labelBuildVersion.setFont(self.fontNormal)
        # self.labelCameraOpen.setFont(self.fontNormal)
        # self.labelBiometricType.setFont(self.fontNormal)
        # self.labelFaceVersion.setFont(self.fontNormal)
        # self.labelFaceOpen.setFont(self.fontNormal)
        # self.labelFingerprintOpen.setFont(self.fontNormal)
        # self.labelMacAddress.setFont(self.fontNormal)
        # self.labelSerialNumber.setFont(self.fontNormal)
        # self.labelPlatform.setFont(self.fontNormal)
        # self.labelSoftwareVersion.setFont(self.fontNormal)
        # self.labelVendor.setFont(self.fontNormal)

        '''Set Widget'''
        self.gridLayout.addWidget(self.labelLeaveTypeName, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.labelAnnualLeave, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.labelWOPayLeave, 2, 0, 1, 1)
        self.gridLayout.addWidget(self.labelSpecialLeave, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.labelMaternityLeave, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.labelPMLeave, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.labelPaternityLeave, 6, 0, 1, 1)
        self.gridLayout.addWidget(self.labelMourningLeave, 7, 0, 1, 1)
        self.gridLayout.addWidget(self.labelSpecialLeave, 8, 0, 1, 1)
        self.gridLayout.addWidget(self.buttonEditAnnualLeave, 1, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonDeleteAnnualLeave, 1, 3, 1, 1)
        self.gridLayout.addWidget(self.buttonEditWOPayLeave, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonDeleteWOPayLeave, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.buttonEditSpecialLeave, 3, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonDeleteSpecialLeave, 3, 3, 1, 1)
        self.gridLayout.addWidget(self.buttonEditMaternityLeave, 4, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonDeleteMaternityLeave, 4, 3, 1, 1)
        self.gridLayout.addWidget(self.buttonEditPMLeave, 5, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonDeletePMLeave, 5, 3, 1, 1)
        self.gridLayout.addWidget(self.buttonEditPaternityLeave, 6, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonDeletePaternityLeave, 6, 3, 1, 1)
        self.gridLayout.addWidget(self.buttonEditMourningLeave, 7, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonDeleteMourningLeave, 7, 3, 1, 1)
        self.gridLayout.addWidget(self.buttonEditSpecialLeave, 8, 2, 1, 1)
        self.gridLayout.addWidget(self.buttonDeleteSpecialLeave, 8, 3, 1, 1)


        '''Setting Widgets as Central Widgets'''
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Leave")

        "Button Events"
        

        self.buttonLeaveBalance.clicked.connect(lambda x: leaveBalanceEvent(AdminDashBoard))
        self.buttonLeaveApproval.clicked.connect(lambda x: leaveApprovalEvent(AdminDashBoard))
        
        # QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.tab


       
def leaveBalanceEvent(MainWindow):
    leaveBalanceUi = leaveBalance.Leave()
    leaveBalanceUi.setupUi(MainWindow)
    MainWindow.setCentralWidget(leaveBalanceUi.centralwidget)
    MainWindow.show()
    return leaveBalanceUi
    




def leaveApprovalEvent(MainWindow):
    leaveApprovalUi = leaveApproval.Leave()
    leaveApprovalUi.setupUi(MainWindow)
    MainWindow.setCentralWidget(leaveApprovalUi.centralwidget)
    MainWindow.show()
    return leaveApprovalUi

