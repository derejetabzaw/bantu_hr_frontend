import os
import sys
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils
        

class Device (object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tableWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        AdminDashBoard.setCentralWidget(self.tabWidget)
        return self.tabWidget

