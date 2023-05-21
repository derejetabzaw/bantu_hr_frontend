import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils



class ClockIO(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.formLayoutWidgets = utils.widgetDrawer(self.tab, 10, 0, 621, 398)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 12 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)


       
        '''Labels'''
        self.labelSearchMember = utils.labelDrawers(self.tab, 0, 10, 91, 16, "Search Member")
        self.labelDate = utils.labelDrawers(self.tab, 380, 15, 47, 13, "Date")

       
        '''Line Edits'''
        self.lineEditSearchMember = utils.lineEditDrawers(self.tab, 0, 30, 241, 20)
        
        '''Set Fonts'''
        utils.widgetEditStyle(self.lineEditSearchMember ,["border :1px solid #000000" , "border-radius:0px"])
        self.lineEditSearchMember.setMinimumSize(QtCore.QSize(20, 20))
        

        '''Date Time Edits'''
        self.dateTimeEditDate = utils.dateEditDrawers(self.tab, 380, 28, 110, 16)
        self.dateTimeEditDate.setCalendarPopup(True)
        self.dateTimeEditDate.setDisplayFormat("yyyy-MM-dd")
        self.dateTimeEditDate.setDateTime(QtCore.QDateTime.currentDateTime())

        '''Buttons'''
        self.buttonSearchMember = utils.pushButtonDrawers(self.tab, 260, 30, 75, 23, "Search" , "")
        self.buttonReport = utils.pushButtonDrawers(self.tab, 540, 30, 121, 21, "See Today's Report" , "")

        '''Table Widget'''
        self.tableWidget = utils.tableWidgetDrawer(self.tab, 0, 60, 560, 421, 4,0,["Employee Name" , "Clock In" , "Clock Out" , "Total Hours"])


        '''Set Fonts'''
        
        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.tab


     
       
        

      

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = ClockIO()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
