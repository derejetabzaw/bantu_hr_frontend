import os
from PyQt5 import QtCore, QtWidgets
import sys
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils

parent_dir = os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/")))
icons_dir = os.path.join(parent_dir, "Assets/icons/").replace("\\","/")

class Department(object):
    def setupUi(self, AdminDashBoard):
        self.centralwidget = utils.widgetDrawer(AdminDashBoard, 0,0,0,0)

        self.tabWidget = utils.tabWidgetDrawer(self.centralwidget, 0, 0, 1920, 1000)
        self.font = utils.fontSpecifier("Yu Gothic UI Semibold", 9 , True , 75)
        self.tabWidget.setFont(self.font)
        self.tabWidget.setStyleSheet("color:#000")
        self.tabWidget.setIconSize(QtCore.QSize(20, 40))
        self.department = utils.widgetDrawer(None,0,0,0,0)
        self.stackedWidget = utils.stackedWidgetDrawer(self.department, 0, 0, 1920, 1000)
        self.addDepartment = utils.widgetDrawer(None,0,0,0,0)
        self.frame = utils.frameDrawer(self.addDepartment , 740, 160, 421, 191, "StyledPanel", "Raised")
        self.formLayoutWidget = utils.widgetDrawer(self.frame , 0, 30, 421, 160)
        self.formLayout = utils.formLayoutDrawer(self.formLayoutWidget)



        '''Add Department Title'''
        self.addDepartmentLabel = utils.labelDrawers(self.addDepartment, 20, 20, 200, 30, "Add Department")
        self.fontTitle = utils.fontSpecifier("Yu Gothic UI Semibold", 12 , True , 75)
        self.addDepartmentLabel.setFont(self.fontTitle)
        '''Label'''
        self.fontLabels = utils.fontSpecifier("Yu Gothic UI Semibold", 14 , True , 75)
        self.departmentIdLabel = utils.labelDrawers(self.formLayoutWidget, 20, 20, 200, 30, "Department ID")
        self.departmentIdLabel.setFont(self.fontLabels)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.departmentIdLabel)
        self.departmentNameLabel =  utils.labelDrawers(self.formLayoutWidget, 20, 20, 200, 30, "Department Name")
        self.departmentNameLabel.setFont(self.fontLabels)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.departmentNameLabel)

        '''Line Edit'''
        self.departmentIdLineEdit = utils.lineEditDrawers(self.formLayoutWidget, 0, 0, 0, 0)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.departmentIdLineEdit)
        self.departmentNameLineEdit = utils.lineEditDrawers(self.formLayoutWidget, 0, 0, 0, 0)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.departmentNameLineEdit)
        '''line sytle'''
        LineEdit_list= [self.departmentIdLineEdit , self.departmentNameLineEdit]
        for line in LineEdit_list:
            utils.widgetEditStyle(line ,["border :1px solid #000000" , "border-radius:0px"])
            line.setMinimumSize(QtCore.QSize(20, 20))

        '''Tree Widget'''
        self.treeWidget = utils.treeWidgetDrawer(self.addDepartment, 200, 60, 531, 501)
        self.treeWidget.headerItem().setText(0, "1")

        '''Divider Line'''
        self.line = utils.lineDrawer(self.addDepartment, "Vertical",180, -30, 21, 1001)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)

        '''Buttons'''
        self.addStaffButton = utils.pushButtonDrawers(self.addDepartment, 10, 20, 141, 131, "Add Staff", "staff.png")
        self.editDepartmentButton = utils.pushButtonDrawers(self.addDepartment, 20, 150, 131, 141, "Edit Department", "Edit.png")
        self.settingDepartmentButton = utils.pushButtonDrawers(self.addDepartment, 20, 300, 131, 131, "Setting", "setting.png")
        self.deleteDepartmentButton = utils.pushButtonDrawers(self.addDepartment, 20, 440, 131, 141, "Delete Department", "delete.png")
        self.checkDepartmentButton = utils.pushButtonDrawers(self.addDepartment, 20, 590, 131, 141, "Active Department", "Active.png")
        self.addDepartmentButton = utils.pushButtonDrawers(self.addDepartment, 790, 100, 171, 26, "Add Department", "")
        self.addDepartmentButton.setStyleSheet("background-color:#fff;\n"
                                   "color:#0076bd;\n"
                                   "border: 1px solid #0076bd;\n"
                                   "border-radius:12px;\n"
                                   "font-family:monospace;\n"
                                   "font-size:20px\n""")
        self.buttonFonts = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)
        self.okayButton = utils.pushButtonDrawers(self.formLayoutWidget, 0, 0, 0, 0, "Okay", "")
        self.okayButton.setFont(self.buttonFonts)
        self.okayButton.setStyleSheet("background-color:#fff;\n"
                                      "color:#0076bd;\n"
                                      "border-top:1px solid #fff;\n"
                                      "border-bottom:1px solid #0076bd;\n"
                                      "padding-bottom:0px")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.okayButton)
        self.cancelButton = utils.pushButtonDrawers(self.formLayoutWidget, 0, 0, 0, 0, "Cancel", "")
        self.cancelButton.setFont(self.buttonFonts)
        self.cancelButton.setStyleSheet("background-color:#fff;\n"
                                         "color:#ff0000;\n"
                                         "border-top:1px solid #fff;\n"
                                         "border-bottom:1px solid #0076bd;\n"
                                         "padding-bottom:0px")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cancelButton)






        '''Setting Widgets as Central Widgets'''
        self.stackedWidget.addWidget(self.addDepartment)
        self.tabWidget.addTab(self.department, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.department), "Personnel")
        self.stackedWidget.setCurrentIndex(2)
        
        AdminDashBoard.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.addDepartment


