import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.append(os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/"))))
import utils

class AreaSetting (object):
    def setupUi(self, AdminDashBoard):
        #self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        #self.tabWidget.addTab(self.tab, "")
        #AdminDashBoard.setCentralWidget(self.tabWidget)
        
        '''Font Specifier'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 16 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)
        self.fontButton = utils.fontSpecifier("Yu Gothic UI Semibold", 10 , True , 75)
        
        '''Labels'''
        self.labelAreaSettings = utils.labelDrawers(self.tab, 20, 0, 201, 51, "Area Settings")
        self.labelSearch = utils.labelDrawers(self.tab, 0, 50 , 91, 31, "Search")
        self.labelAreaCode = utils.labelDrawers(self.tab, 90, 40 , 141, 41, "Area Code")
        self.labelAreaName = utils.labelDrawers(self.tab, 450, 40 , 101, 31, "Area Name")

        '''Line Edits'''
        self.lineEditAreaCode = utils.lineEditDrawers(self.tab, 190, 40, 250, 30)
        self.lineEditAreaName = utils.lineEditDrawers(self.tab, 560, 40, 250, 30)

        '''Buttons'''
        self.buttonSearch = utils.pushButtonDrawers(self.tab, 820, 40, 93, 28, "Search" ,  "")
        self.buttonClear = utils.pushButtonDrawers(self.tab, 940, 40, 93, 28, "Clear" ,  "")
        
        '''Table Widgets'''
        self.tableWidgetAreaSetting = utils.tableWidgetDrawer(self.tab, 0, 100, 671, 551,5,0,["Area Code","Area Name","Parent Area","Remarks","Related Operation"])

        '''List Widget'''
        self.listWidgetAreaSetting = utils.listWidgetDrawer(self.tab, 670, 100, 521, 551,["Area"])

        '''Set Fonts'''
        self.labelAreaSettings.setFont(self.fontHeader)
        self.labelSearch.setFont(self.fontNormal)
        self.labelAreaCode.setFont(self.fontNormal)
        self.labelAreaName.setFont(self.fontNormal)
        self.buttonSearch.setFont(self.fontButton)
        self.buttonClear.setFont(self.fontButton)



        
        #self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Area Settings")
        return self.tab
    

# if __name__ == "__main__":
#     import sys
#     os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
#     app = QtWidgets.QApplication(sys.argv)
#     app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     AdminDashBoard = QtWidgets.QMainWindow()
#     ui = AreaSetting()
#     ui.setupUi(AdminDashBoard)
#     AdminDashBoard.show()
#     sys.exit(app.exec_())