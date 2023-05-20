import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils



class CompanySettings(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.formLayoutWidgets = utils.widgetDrawer(self.tab,30, 100, 381, 557)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 12 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)

        '''Form Layout'''
        self.formLayout = utils.formLayoutDrawer(self.formLayoutWidgets)
       
        '''Labels'''
        self.labelCompanyName = utils.labelDrawers(self.formLayoutWidgets, 0, 0, 1, 1, "Company Name")
        self.labelEstdID = utils.labelDrawers(self.formLayoutWidgets, 1, 0, 1, 1, "Estd ID")
        self.labelShowinReport = utils.labelDrawers(self.formLayoutWidgets, 2, 0, 1, 1, "Show in Report")
        self.labelAgentID = utils.labelDrawers(self.formLayoutWidgets, 3, 0, 1, 1, "Agent ID")
        self.labelCurrency = utils.labelDrawers(self.formLayoutWidgets, 4, 0, 1, 1, "Currency")
        self.labelEmail = utils.labelDrawers(self.formLayoutWidgets, 5, 0, 1, 1, "Email")
        self.labelPhoneNumber = utils.labelDrawers(self.formLayoutWidgets, 6, 0, 1, 1, "Phone Number")
        self.labelNationality = utils.labelDrawers(self.formLayoutWidgets, 6, 0, 1, 1, "Phone Number")
       
        '''Line Edits'''
        self.labelCompanyLogoPH = utils.labelDrawers(self.tab, 440, 100, 151, 31, "Company Logo")
        self.lineEditCompanyName = utils.lineEditDrawers(self.formLayoutWidgets, 0, 1, 1, 1)
        self.lineEditShowinReport = utils.lineEditDrawers(self.formLayoutWidgets, 1, 1, 1, 1)
        self.lineEditAgentID = utils.lineEditDrawers(self.formLayoutWidgets, 2, 1, 1, 1)
        self.lineEditCurrency = utils.lineEditDrawers(self.formLayoutWidgets, 3, 1, 1, 1)
        self.lineEditEmail = utils.lineEditDrawers(self.formLayoutWidgets, 4, 1, 1, 1)
        self.lineEditPhoneNumber = utils.lineEditDrawers(self.formLayoutWidgets, 5, 1, 1, 1)
        self.lineEditNationality = utils.lineEditDrawers(self.formLayoutWidgets, 6, 1, 1, 1)
        '''set fonts'''
        LineEdit_List=[self.labelCompanyLogoPH, self.lineEditCompanyName, self.lineEditShowinReport,self.lineEditAgentID ,
                       self.lineEditCurrency, self.lineEditEmail, self.lineEditPhoneNumber, self.lineEditNationality]
        for line in LineEdit_List:
            utils.widgetEditStyle(line ,["border :1px solid #000000" , "border-radius:0px"])
            line.setMinimumSize(QtCore.QSize(20, 20))

        '''Buttons'''
        self.buttonBrowse = utils.pushButtonDrawers(self.tab, 420, 170, 165, 27, "Browse" , "")
        self.buttonOkay = utils.pushButtonDrawers(self.tab, 530, 590, 165, 27, "Okay" , "")
        '''Check Boxes'''
        self.checkBoxShowinReport = utils.checkBoxDrawers(self.tab, 740, 89, 251, 51, "Show in Report")
        '''Combo Boxes'''
        self.comboBoxEstdID = utils.comboBoxDrawers(self.formLayoutWidgets, 1, 1, 1, 1,["Yes" , "No"])
        '''Set Fonts'''
        self.labelCompanyName.setFont(self.fontHeader)
        self.labelEstdID.setFont(self.fontHeader)
        self.labelShowinReport.setFont(self.fontHeader)
        self.labelAgentID.setFont(self.fontHeader)
        self.labelCurrency.setFont(self.fontHeader)
        self.labelEmail.setFont(self.fontHeader)
        self.labelPhoneNumber.setFont(self.fontHeader)
        self.labelNationality.setFont(self.fontHeader)
        self.labelCompanyLogoPH.setFont(self.fontHeader)
        self.lineEditCompanyName.setFont(self.fontHeader)
        self.lineEditShowinReport.setFont(self.fontHeader)
        self.lineEditAgentID.setFont(self.fontHeader)
        self.lineEditCurrency.setFont(self.fontHeader)
        self.lineEditEmail.setFont(self.fontHeader)
        self.lineEditPhoneNumber.setFont(self.fontHeader)
        self.lineEditNationality.setFont(self.fontHeader)
        self.comboBoxEstdID.setFont(self.fontHeader)
        self.checkBoxShowinReport.setFont(self.fontHeader)
        self.buttonBrowse.setFont(self.fontHeader)
        self.buttonOkay.setFont(self.fontHeader)



        '''Set Style'''
        utils.widgetEditStyle(self.buttonOkay,["background-color:#fff","color:#0076bd","border-top:1px solid #fff","border-bottom:1px solid #0076bd","padding-bottom:0px"])
        utils.widgetEditStyle(self.buttonBrowse,["background-color:#fff","color:#0076bd","border-top:1px solid #fff","border-bottom:1px solid #0076bd","padding-bottom:0px"])

        '''Set Widget'''

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelCompanyName)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelEstdID)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelShowinReport)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelAgentID)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelCurrency)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelEmail)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelPhoneNumber)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelNationality)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEditCompanyName)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.comboBoxEstdID)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEditShowinReport)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEditAgentID)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEditCurrency)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEditEmail)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEditPhoneNumber)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEditNationality)

        '''Setting Widgets as Central Widgets'''
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Company Settings")
        
        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.tab

      

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = CompanySettings()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
