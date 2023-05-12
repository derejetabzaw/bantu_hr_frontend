import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys




import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/"))))
import utils



class Attendance(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.formLayoutWidgets = utils.widgetDrawer(self.tab, 10, 0, 621, 398)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 12 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)


       
        '''Labels'''
        self.labelDepartment = utils.labelDrawers(self.tab, 0, 10, 91, 16, "Department")
        self.labelDate = utils.labelDrawers(self.tab, 400, 15, 65, 13, "Date Range")
        self.labelTo = utils.labelDrawers(self.tab, 425, 30, 65, 13, "To")


        '''Date Time Edits'''
        self.dateTimeEditRangeOne = utils.dateEditDrawers(self.tab, 280, 30, 110, 16)
        self.dateTimeEditRangeOne.setCalendarPopup(True)
        self.dateTimeEditRangeOne.setDisplayFormat("yyyy-MM-dd")
        self.dateTimeEditRangeOne.setDateTime(QtCore.QDateTime.currentDateTime())

        self.dateTimeEditRangeTwo = utils.dateEditDrawers(self.tab, 460, 30, 110, 16)
        self.dateTimeEditRangeTwo.setCalendarPopup(True)
        self.dateTimeEditRangeTwo.setDisplayFormat("yyyy-MM-dd")
        self.dateTimeEditRangeTwo.setDateTime(QtCore.QDateTime.currentDateTime())



 

        currentMonth =  datetime.now().strftime("%B")
        

        '''Buttons'''
        self.buttonGenerate = utils.pushButtonDrawers(self.tab, 580, 30, 121, 21, "Generate" , "")

        '''Combo Boxes'''
        self.comboBoxDepartment = utils.comboBoxDrawers(self.tab,  0, 30, 241, 20, ["Select Department" , "Finance" , "IT" , "HR" , "Marketing" , "Sales"])

        '''Table Widget'''
        self.tableWidget = utils.tableWidgetDrawer(self.tab, 0, 60, 560, 421, 2,0,["Employee Name" , "Total Hours"])




     
       
        

      

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = Attendance()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
