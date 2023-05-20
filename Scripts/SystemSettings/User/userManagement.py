import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys

import time
from datetime import *
from PyQt5 import QtCore, QtGui, QtWidgets
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/"))))
import utils



class UserManagement(object):
    def setupUi(self, AdminDashBoard):
        self.tabWidget = utils.tabWidgetDrawer(AdminDashBoard, 0, 0, 1920, 1000)
        self.tab = utils.widgetDrawer(None, 0, 0, 0, 0)
        self.tabWidget.addTab(self.tab, "")
        self.formLayoutWidgets = utils.widgetDrawer(self.tab, 10, 0, 621, 398)
        AdminDashBoard.setCentralWidget(self.tabWidget)

        '''Specify Font'''
        self.fontHeader = utils.fontSpecifier("Yu Gothic UI Semibold", 12 , True , 75)
        self.fontNormal = utils.fontSpecifier("Yu Gothic UI Semibold", 11 , True , 75)

        '''Form Layout'''
        self.formLayout = utils.formLayoutDrawer(self.formLayoutWidgets)
       
        '''Labels'''
        self.labelUsername = utils.labelDrawers(self.formLayoutWidgets, 0, 0, 1, 1, "Username")
        self.labelPassword = utils.labelDrawers(self.formLayoutWidgets, 1, 0, 1, 1, "Password")
        self.labelConfirmPassword = utils.labelDrawers(self.formLayoutWidgets, 2, 0, 1, 1, "Confirm Password")
        self.labelAuthorizeDepartment = utils.labelDrawers(self.formLayoutWidgets, 3, 0, 1, 1, "Authorize Department")
        self.labelAuthorizeArea = utils.labelDrawers(self.formLayoutWidgets, 4, 0, 1, 1, "Authorize Area")
        self.labelFirstName = utils.labelDrawers(self.formLayoutWidgets, 5, 0, 1, 1, "First Name")
        self.labelLastName = utils.labelDrawers(self.formLayoutWidgets, 6, 0, 1, 1, "Last Name")
        self.labelEmail = utils.labelDrawers(self.formLayoutWidgets, 6, 0, 1, 1, "Email")
       
        '''Line Edits'''
        self.lineEditUsername = utils.lineEditDrawers(self.formLayoutWidgets, 0, 1, 1, 1)
        self.lineEditPassword = utils.lineEditDrawers(self.formLayoutWidgets, 1, 1, 1, 1)
        self.lineEditConfirmPassword = utils.lineEditDrawers(self.formLayoutWidgets, 2, 1, 1, 1)
        self.lineEditFirstName = utils.lineEditDrawers(self.formLayoutWidgets, 5, 1, 1, 1)
        self.lineEditLastName = utils.lineEditDrawers(self.formLayoutWidgets, 6, 1, 1, 1)
        self.lineEditEmail = utils.lineEditDrawers(self.formLayoutWidgets, 6, 1, 1, 1)


        '''Check Boxes'''
        self.checkBoxStaffStatus= utils.checkBoxDrawers(self.formLayoutWidgets, 740, 89, 251, 51, "Staff Status")
        self.checkBoxSuperStatus = utils.checkBoxDrawers(self.formLayoutWidgets, 740, 89, 251, 51, "Super Status")

        '''Combo Boxes'''
        self.comboBoxAuthorizeDepartment = utils.comboBoxDrawers(self.formLayoutWidgets, 2, 1, 1, 1,["" , ""])
        self.comboBoxAuthorizeArea = utils.comboBoxDrawers(self.formLayoutWidgets, 3, 1, 1, 1,["" , ""])
        '''Set Fonts'''
        self.labelUsername.setFont(self.fontNormal)
        self.labelPassword.setFont(self.fontNormal)
        self.labelConfirmPassword.setFont(self.fontNormal)
        self.labelAuthorizeDepartment.setFont(self.fontNormal)
        self.labelAuthorizeArea.setFont(self.fontNormal)
        self.labelFirstName.setFont(self.fontNormal)
        self.labelLastName.setFont(self.fontNormal)
        self.labelEmail.setFont(self.fontNormal)


     

        '''Set Style'''
        LineEdit_list= [self.lineEditUsername, self.lineEditPassword,  self.lineEditConfirmPassword,self.lineEditFirstName,
                        self.lineEditLastName,  self.lineEditEmail]
        for line in LineEdit_list:
            utils.widgetEditStyle(line,["border :1px solid #000000" , "border-radius:0px"])
            line.setMinimumSize(QtCore.QSize(20, 20))

        '''Set Widget'''

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelUsername)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.labelPassword)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelConfirmPassword)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.labelAuthorizeDepartment)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelAuthorizeArea)
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.labelFirstName)
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.labelLastName)
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.labelEmail)
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.checkBoxStaffStatus)
        self.formLayout.setWidget(0 , QtWidgets.QFormLayout.FieldRole, self.lineEditUsername)
        self.formLayout.setWidget(1 , QtWidgets.QFormLayout.FieldRole, self.lineEditPassword)
        self.formLayout.setWidget(2 , QtWidgets.QFormLayout.FieldRole, self.lineEditConfirmPassword)
        self.formLayout.setWidget(3 , QtWidgets.QFormLayout.FieldRole, self.comboBoxAuthorizeDepartment)
        self.formLayout.setWidget(4 , QtWidgets.QFormLayout.FieldRole, self.comboBoxAuthorizeArea)
        self.formLayout.setWidget(5 , QtWidgets.QFormLayout.FieldRole, self.lineEditFirstName)
        self.formLayout.setWidget(6 , QtWidgets.QFormLayout.FieldRole, self.lineEditLastName)
        self.formLayout.setWidget(7 , QtWidgets.QFormLayout.FieldRole, self.lineEditEmail)
        self.formLayout.setWidget(8 , QtWidgets.QFormLayout.FieldRole, self.checkBoxSuperStatus)
        AdminDashBoard.setWindowTitle("G!ze")
        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.tab

        

      

if __name__ == "__main__":
    import sys
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QtWidgets.QApplication(sys.argv)
    app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    AdminDashBoard = QtWidgets.QMainWindow()
    ui = UserManagement()
    ui.setupUi(AdminDashBoard)
    AdminDashBoard.show()
    sys.exit(app.exec_())
