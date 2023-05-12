import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils



class Payroll(object):
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

       
        '''Labels'''
       
        self.labelYear = utils.labelDrawers(self.tab, 20, 30, 47, 13, "Year")
        self.labelPayrollIndex = utils.labelDrawers(self.tab, 20, 60, 71, 16, "Payroll Index")
        self.labelFieldOffice = utils.labelDrawers(self.tab, 400, 30, 61, 16, "Field Office")

        '''Line Edits'''
        self.lineEditPayrollIndex = utils.lineEditDrawers(self.tab, 110, 60, 113, 20)

        '''Combo Boxes'''
        self.comboBoxYear = utils.comboBoxDrawers(self.tab, 100, 30, 69, 22, ["2022"])
        self.comboBoxFieldOffice = utils.comboBoxDrawers(self.tab, 470, 30, 90, 22, ["Addis Ababa" , "Bahir Dar"])



        '''Buttons'''
        self.buttonGenerateExcel = utils.pushButtonDrawers(self.tab, 384, 60, 91, 23, "Generate Excel" , "")
        self.buttonGeneratePDF = utils.pushButtonDrawers(self.tab, 490, 60, 75, 23, "Generate PDF" , "")
       
        '''Set Fonts'''
        # self.labelDeviceSettings.setFont(self.fontHeader)
        # self.labelDeviceTime.setFont(self.fontNormal)
        # self.labelBuildVersion.setFont(self.fontNormal)


       


       
      

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = Payroll()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
