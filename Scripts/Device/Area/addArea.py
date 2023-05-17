import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/"))))
import utils

class Area (object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        AdminDashBoard.setCentralWidget(self.tabWidget)
        self.labelAddArea = utils.labelDrawers(self.tab, 20, 30, 441, 51, "Add Area")
        self.fonts = utils.fontSpecifier("Yu Gothic UI Semibold", 16 , True , 75)
        self.labelAddArea.setFont(self.fonts)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), "Add Area")
        return self.tabWidget
    
