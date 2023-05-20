import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils



class PayrollRegistration(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayoutWidgets = utils.widgetDrawer(self.tab,220, 60, 353, 285)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 18 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 9 , True , 75)

       
        '''Labels'''
       
        self.labelYear = utils.labelDrawers(self.tab, 10, 30, 71, 16, "Payroll Year")
        self.labelPayrollIndex = utils.labelDrawers(self.tab, 330, 30, 71, 16, "Payroll Index")
        self.labelFieldOffice = utils.labelDrawers(self.tab, 10, 60, 61, 16, "Field Office")
        self.labelPayrollType = utils.labelDrawers(self.tab, 330, 60, 71, 16, "Payroll Type")
        '''Line Edits'''
        self.lineEditPayrollIndex = utils.lineEditDrawers(self.tab, 410, 30, 111, 20)
        '''line style'''
        utils.widgetEditStyle(self.lineEditPayrollIndex ,["border :1px solid #000000" , "border-radius:0px"])
        self.lineEditPayrollIndex.setMinimumSize(QtCore.QSize(20, 20))
        '''Combo Boxes'''
        self.comboBoxYear = utils.comboBoxDrawers(self.tab, 80, 30, 91, 22, ["2022"])
        self.comboBoxFieldOffice = utils.comboBoxDrawers(self.tab, 80, 60, 91, 22, ["Addis Ababa" , "Bahir Dar"])
        self.comboBoxPayrollType = utils.comboBoxDrawers(self.tab, 410, 60, 69, 22, ["Regular" , "Contract"])


        '''Buttons'''
        self.buttonGeneratePDF = utils.pushButtonDrawers(self.tab, 220, 90, 75, 23, "Generate" , "")
       
        '''Table Widget'''
        self.tableWidgetPayroll = utils.tableWidgetDrawer(self.tab, 10, 130, 621, 311, 11,6,["Employee Name" , "Position" , "Work Day" , "Daily Salary" , "Overtime" , "Transport Allowance" , "Time" , "Date" , "Comission" , "Total Salary" , "Net Salary"])
        
        '''Set Fonts'''
        # self.labelDeviceSettings.setFont(self.fontHeader)
        # self.labelDeviceTime.setFont(self.fontNormal)
        # self.labelBuildVersion.setFont(self.fontNormal)


        '''Setting Widgets as Central Widgets'''
        self.tabWidget.addTab(self.tab, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Payroll Registration")
        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.tab


       


       
      

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = PayrollRegistration()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
