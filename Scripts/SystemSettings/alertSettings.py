import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils



class AlertSettings(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        #self.formLayoutAddDeviceWidget = utils.widgetDrawer(self.tab, 330, 160, 691, 331)
        self.tabWidget.addTab(self.tab, "")
        self.formLayoutUpperWidgets = utils.widgetDrawer(self.tab,20, 60, 891, 241)
        self.formLayoutLowerWidgets = utils.widgetDrawer(self.tab, 30, 250, 881, 232)
        # self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        # self.gridLayout.setContentsMargins(0, 0, 0, 0)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 12 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)

        '''Form Layout'''
        self.formUpperLayout = utils.formLayoutDrawer(self.formLayoutUpperWidgets)
        self.formLowerLayout = utils.formLayoutDrawer(self.formLayoutLowerWidgets)
        #self.formLayoutAddDevice = utils.formLayoutDrawer(self.formLayoutAddDeviceWidget)
       
        '''Labels'''
        self.labelMailSetting = utils.labelDrawers(self.tab, 30, 0, 179, 58, "Mail Settings")
        self.labelAlertSetting = utils.labelDrawers(self.tab, 30, 185, 179, 58, "Alert Settings")
        self.labelApprovalAlert = utils.labelDrawers(self.tab, 30, 380, 179, 58, "Approval Alert")
        
        
        self.labelEmailSendingServer = utils.labelDrawers(self.formLayoutUpperWidgets, 0, 0, 1, 1, "Email Sending Server")
        self.labelServerPort = utils.labelDrawers(self.formLayoutUpperWidgets, 1, 0, 1, 1, "Server Port")
        self.labelEmailAccount = utils.labelDrawers(self.formLayoutUpperWidgets, 2, 0, 1, 1, "Email Account")
        self.labelPassword = utils.labelDrawers(self.formLayoutUpperWidgets, 3, 0, 1, 1, "Password")
        self.labelEmailAddress = utils.labelDrawers(self.formLayoutUpperWidgets, 4, 0, 1, 1, "Email Address")
        self.labelLateExceed = utils.labelDrawers(self.formLayoutLowerWidgets, 0, 0, 1, 1, "Late Leave Exceed")
        self.labelEarlyExceed = utils.labelDrawers(self.formLayoutLowerWidgets, 1, 0, 1, 1, "Early Leave Exceed")
        self.labelAbsentExceed = utils.labelDrawers(self.formLayoutLowerWidgets, 2, 0, 1, 1, "Absent Exceed")
        self.labelEmailSendingFrequency = utils.labelDrawers(self.formLayoutLowerWidgets, 3, 0, 1, 1, "Email Sending Frequency")
        self.labelEmailAlert = utils.labelDrawers(self.formLayoutLowerWidgets, 4, 0, 1, 1, "Email Alert")
       
        '''Line Edits'''
        self.lineEditEmailSendingServer = utils.lineEditDrawers(self.formLayoutUpperWidgets, 0, 1, 1, 1)
        self.lineEditServerPort = utils.lineEditDrawers(self.formLayoutUpperWidgets, 1, 1, 1, 1)
        self.lineEditEmailAccount = utils.lineEditDrawers(self.formLayoutUpperWidgets, 2, 1, 1, 1)
        self.lineEditPassword = utils.lineEditDrawers(self.formLayoutUpperWidgets, 3, 1, 1, 1)
        self.lineEditEmailAddress = utils.lineEditDrawers(self.formLayoutUpperWidgets, 4, 1, 1, 1)
        self.lineEditLateExceed = utils.lineEditDrawers(self.formLayoutLowerWidgets, 0, 1, 1, 1)
        self.lineEditEarlyExceed = utils.lineEditDrawers(self.formLayoutLowerWidgets, 1, 1, 1, 1)
        self.lineEditAbsentExceed = utils.lineEditDrawers(self.formLayoutLowerWidgets, 2, 1, 1, 1)

        '''Buttons'''
        self.buttonOkay = utils.pushButtonDrawers(self.tab, 530, 590, 165, 27, "Okay" , "")
        '''Check Boxes'''
        self.checkBoxEmailAlert = utils.checkBoxDrawers(self.tab, 50, 420, 251, 51, "Email Alert")
        self.checkBoxPopAlert = utils.checkBoxDrawers(self.tab, 270, 420, 251, 51, "Pop Alert")
        '''Combo Boxes'''
        self.comboBoxEmailSendingFrequency = utils.comboBoxDrawers(self.formLayoutLowerWidgets, 3, 1, 1, 1, ["Daily","Weekly","Monthly"])
        self.comboBoxEmailAlert = utils.comboBoxDrawers(self.formLayoutLowerWidgets, 4, 1, 1, 1, ["Yes","No"])

        '''Set Fonts'''

        self.labelMailSetting.setFont(self.fontHeader)
        self.labelAlertSetting.setFont(self.fontHeader)
        self.labelApprovalAlert.setFont(self.fontHeader)
        self.labelEmailSendingServer.setFont(self.fontNormal)
        self.labelServerPort.setFont(self.fontNormal)
        self.labelEmailAccount.setFont(self.fontNormal)
        self.labelPassword.setFont(self.fontNormal)
        self.labelEmailAddress.setFont(self.fontNormal)
        self.labelLateExceed.setFont(self.fontNormal)
        self.labelEarlyExceed.setFont(self.fontNormal)
        self.labelAbsentExceed.setFont(self.fontNormal)
        self.labelEmailSendingFrequency.setFont(self.fontNormal)
        self.labelEmailAlert.setFont(self.fontNormal)

        
 

        '''Set Style'''
        utils.widgetEditStyle(self.labelMailSetting , ["color:#0076bd"])
        utils.widgetEditStyle(self.labelAlertSetting , ["color:#0076bd"])
        utils.widgetEditStyle(self.labelApprovalAlert , ["color:#0076bd"])
        utils.widgetEditStyle(self.lineEditEmailSendingServer ,["border :1px solid #0076bd", "border-radius:10px"])
        #self.lineEditEmailSendingServer.setMinimumSize(QtCore.QSize(20, 40))

        
        #utils.widgetEditStyle(self.buttonOkay,["background-color:#fff","color:#0076bd","border-top:1px solid #fff","border-bottom:1px solid #0076bd","padding-bottom:0px"])

        '''Set Widget'''
        self.formUpperLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelEmailSendingServer)
        self.formUpperLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelServerPort)
        self.formUpperLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelEmailAccount)
        self.formUpperLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.formUpperLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelEmailAddress)
        self.formLowerLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelLateExceed)
        self.formLowerLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelEarlyExceed)
        self.formLowerLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelAbsentExceed)
        self.formLowerLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelEmailSendingFrequency)
        self.formLowerLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelEmailAlert)
        self.formUpperLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditEmailSendingServer)
        self.formUpperLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditServerPort)
        self.formUpperLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditEmailAccount)
        self.formUpperLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.formUpperLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditEmailAddress)
        self.formLowerLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditLateExceed)
        self.formLowerLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEditEarlyExceed)
        self.formLowerLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditAbsentExceed)
        self.formLowerLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.comboBoxEmailSendingFrequency)
        self.formLowerLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.comboBoxEmailAlert)


        '''Setting Widgets as Central Widgets'''
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Alert Settings")
        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.tab
        


      

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = AlertSettings()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
