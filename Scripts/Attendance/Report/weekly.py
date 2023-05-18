import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/"))))
import utils



class Weekly(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.formLayoutWidgets = utils.widgetDrawer(self.tab, 10, 0, 621, 398)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 12 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)


       
        '''Labels'''
        self.labelDepartment = utils.labelDrawers(self.tab, 0, 10, 91, 16, "Department")
        self.labelDate = utils.labelDrawers(self.tab, 380, 15, 65, 13, "Select Date")

        

        '''Date Time Edits'''
        self.dateTimeEditDate = utils.dateEditDrawers(self.tab, 380, 30, 110, 16)
        self.dateTimeEditDate.setCalendarPopup(True)
        self.dateTimeEditDate.setDisplayFormat("yyyy-MM-dd")
        self.dateTimeEditDate.setDateTime(QtCore.QDateTime.currentDateTime())

        '''Buttons'''
        self.buttonGenerate = utils.pushButtonDrawers(self.tab, 560, 30, 121, 21, "Generate" , "")

        '''Combo Boxes'''
        self.comboBoxDepartment = utils.comboBoxDrawers(self.tab,  0, 30, 241, 20, ["Select Department" , "Finance" , "IT" , "HR" , "Marketing" , "Sales"])

        '''Table Widget'''
        self.tableWidget = utils.tableWidgetDrawer(self.tab, 0, 60, 560, 421, 2,0,["Employee Name" , "Total Hours"])


        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.tab

     
       
        

      

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = Weekly()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
