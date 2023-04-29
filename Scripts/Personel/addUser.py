import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time


parent_dir = os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/")))
icons_dir = os.path.join(parent_dir, "Assets/icons/").replace("\\","/")


class Personel(object):
    def setupUi(self, AdminDashBoard):
        self.centralwidget = QtWidgets.QWidget(AdminDashBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1000))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color:#000")
        self.tabWidget.setIconSize(QtCore.QSize(20, 40))
        self.tabWidget.setObjectName("tabWidget")

        self.personel = QtWidgets.QWidget()
        self.personel.setObjectName("personel")
        self.stackedWidget = QtWidgets.QStackedWidget(self.personel)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1921, 1011))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setFont(font)
        self.stackedWidget.setStyleSheet("background-color:#fff\n""")
        self.stackedWidget.setObjectName("stackedWidget")
        self.adduser = QtWidgets.QWidget()
        self.adduser.setObjectName("adduser")
        self.frame = QtWidgets.QFrame(self.adduser)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1361, 821))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.innerstackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.innerstackedWidget.setGeometry(QtCore.QRect(0, -20, 1920, 1000))
        self.innerstackedWidget.setFont(font)

        '''Widget Functions'''
        def lineDraw(widget,orientation,x, y, length, width):
            line = QtWidgets.QFrame(widget)
            line.setGeometry(QtCore.QRect(x, y, length, width))
            if orientation == "horizontal":
                line.setFrameShape(QtWidgets.QFrame.HLine)
            else:
                line.setFrameShape(QtWidgets.QFrame.VLine)
            line.setFrameShadow(QtWidgets.QFrame.Sunken)
            return line
            
        
        def labelDrawers(widget, x, y,length,width, text):
            label = QtWidgets.QLabel(widget)
            label.setGeometry(QtCore.QRect(x, y, length, width))
            label.setText(text)
            return label  
        def lineEditDrawers(widget, x, y, length, width):
            lineedit = QtWidgets.QLineEdit(widget).setGeometry(QtCore.QRect(x, y, length, width))
            return lineedit
        def dateEditDrawers(widget, x, y, length, width):
            dateedit = QtWidgets.QDateEdit(widget).setGeometry(QtCore.QRect(x, y, length, width))
            return dateedit
        def plainEditDrawers(widget, x, y, length, width):
            plainedit = QtWidgets.QPlainTextEdit(widget).setGeometry(QtCore.QRect(x, y, length, width))
            return plainedit
        def comboBoxDrawers(widget, x, y, length, width , comboitems):
            combobox = QtWidgets.QComboBox(widget)
            combobox.setGeometry(QtCore.QRect(x, y, length, width))
            for i,items in enumerate (comboitems):
                combobox.addItem(items)
                combobox.setItemText(i, items)
            return combobox
        def pushButtonDrawers(widget, icon ,x, y, length, width, text):
            pushbutton = QtWidgets.QPushButton(widget)
            pushbutton.setGeometry(QtCore.QRect(x, y, length, width))
            pushbutton.setText(text)
            if len(icon) != 0:
                pushbutton.setStyleSheet("background:url(" + icons_dir  + icon + ");\n"
                                        "background-repeat:no-repeat;\n"
                                        "height:12px;\n"
                                        "text-align:bottom;")
            if len(icon) == 0 and text == "Browse":
                pushbutton.setStyleSheet("border:1px solid #fff;\n"
                                         "border-radius:25px;\n"
                                         "background-color:#0076bd;\n"
                                         "color:#fff")

            if len(icon) == 0 and (x,y,length,width) == (0,0,0,0):
                if text == 'Cancel':
                    pushbutton.setStyleSheet("background-color:#fff;\n"
                                         "color:#ff0000;\n"
                                         "border: 1px solid #fff;\n"
                                         "border-radius:12px;\n"
                                         "text-decoration: underline;\n"
                                         "font-family:monospace;\n"
                                         "font-size:20px\n"
                                         "")
                else:
                    pushbutton.setStyleSheet("background-color:#fff;\n"
                                            "color:#0076bd;\n"
                                            "border: 1px solid #0076bd;\n"
                                            "border-radius:12px;\n"
                                            "font-family:monospace;\n"
                                            "font-size:20px\n"
                                            "")
                    
            return pushbutton
        
        
        

        '''Defining Stacked Widgets - Section I'''
        self.innerWidget = QtWidgets.QWidget()
        self.stackedWidget.addWidget(self.adduser)
        self.line_upper_bound = lineDraw(self.innerWidget,"horizontal",240, 330, 521, 16)
        self.line_divider = lineDraw(self.innerWidget,"horizontal",220, 730, 911, 16)
        self.line_vertical_divider = lineDraw(self.innerWidget,"vertical",170, 10, 21, 1001)
        self.line_lower_bound = lineDraw(self.innerWidget,"horizontal",240, 110, 521, 16)
        
        
        self.innerWidget = QtWidgets.QWidget()
        self.bottomButtonLayoutWidgets = QtWidgets.QWidget(self.innerWidget)
        self.bottomButtonLayoutWidgets.setGeometry(QtCore.QRect(540, 650, 571, 61))
        self.bottomButtonLayout = QtWidgets.QHBoxLayout(self.bottomButtonLayoutWidgets)
        self.bottomButtonLayout.setContentsMargins(0, 0, 0, 0)


        '''Defining Labels/LineEdit/ComboBoxes - Section I'''
        '''Buttons'''
        self.addUserButton = pushButtonDrawers(self.innerWidget, "iconmonstr-user-8-120.png",10, 40, 158, 141, "Add User")
        self.viewUserButton = pushButtonDrawers(self.innerWidget, "iconmonstr-list-lined-120.png",10, 190, 158, 141, "View User")
        self.positionManagementButton = pushButtonDrawers(self.innerWidget, "iconmonstr-flag-3-120.png",10, 340, 158, 141, "Position Management")        
        self.browseButton = pushButtonDrawers(self.innerWidget, "",940, 420, 111, 51, "Browse")
        self.okayButton = pushButtonDrawers(self.bottomButtonLayoutWidgets, "",0,0 ,0 ,0 , "Okay")
        self.cancelButton = pushButtonDrawers(self.bottomButtonLayoutWidgets, "",0,0 ,0 ,0 ,"Cancel")
        self.importFromExcelButton = pushButtonDrawers(self.bottomButtonLayoutWidgets,"" ,0,0 ,0 , 0, "Import From Excel")
        self.syncFPButton = pushButtonDrawers(self.bottomButtonLayoutWidgets, "", 0 ,0 ,0 ,0 , "Sync Fingerprint")
        
        '''Add Button Widget to Layout'''
        self.bottomButtonLayout.addWidget(self.okayButton)
        self.bottomButtonLayout.addWidget(self.cancelButton)
        self.bottomButtonLayout.addWidget(self.importFromExcelButton)
        self.bottomButtonLayout.addWidget(self.syncFPButton)
        

        '''Title Font and Label'''
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.addPersonelLabel = labelDrawers(self.innerWidget, 235, 50, 231, 61, "Add Personel")
        self.addPersonelLabel.setFont(font)

        '''Label'''
        
        self.employeeCodeLabel = labelDrawers(self.innerWidget, 240, 138, 81, 16, "Employee Code")
        self.fullNameLabel = labelDrawers(self.innerWidget, 240, 168, 51, 16, "Full Name")
        self.birthDateLabel = labelDrawers(self.innerWidget, 240, 198, 51, 16, "Birth Date")
        self.birthPlaceLabel = labelDrawers(self.innerWidget, 240, 228, 61, 16, "Birth Place")
        self.bloodTypeLabel = labelDrawers(self.innerWidget, 240, 258, 61, 16, "Blood Type")
        self.genderLabel = labelDrawers(self.innerWidget, 240, 288, 39, 11, "Gender")
        self.religionLabel = labelDrawers(self.innerWidget, 550, 138, 71, 16, "Religion")
        self.maritalStatusLabel = labelDrawers(self.innerWidget, 550, 168, 61, 16, "Marital Status")
        self.employeTypeLabel = labelDrawers(self.innerWidget, 550, 198, 71, 16, "Employee Type")
        self.drivingLicenseLabel = labelDrawers(self.innerWidget, 550, 228, 111, 16, "Driving License Grade")
        self.remarksLabel = labelDrawers(self.innerWidget, 550, 288, 39, 11, "Remarks")
        self.userPhotoLabel = labelDrawers(self.innerWidget, 880, 210, 241, 201, "<html><head/><body><p><img src=\"" + icons_dir + "iconmonstr-user-14-240.png\"/></p></body></html>")




        '''LineEdit'''
        self.employeeCodeEdit = lineEditDrawers(self.innerWidget, 330, 138, 113, 20)
        self.fullNameEdit = lineEditDrawers(self.innerWidget, 330, 168, 113, 20)
        self.birthDateEdit = dateEditDrawers(self.innerWidget, 330, 198, 111, 22)
        self.birthPlaceEdit = lineEditDrawers(self.innerWidget, 330, 228, 113, 20)
        self.bloodTypeEdit = lineEditDrawers(self.innerWidget, 330, 258, 113, 20)
        self.drivingLicenseEdit = lineEditDrawers(self.innerWidget, 670, 228, 113, 20)
        self.remarksEdit = plainEditDrawers(self.innerWidget, 660, 258, 104, 64)

        '''ComboBox'''
        self.genderComboBox = comboBoxDrawers(self.innerWidget, 330, 290, 111, 22,["Male" , "Female"])
        self.maritalStatusComboBox = comboBoxDrawers(self.innerWidget, 660, 170, 111, 22,["Single" , "Married"])
        self.employeTypeComboBox = comboBoxDrawers(self.innerWidget, 660, 200, 111, 22,["Permanent" , "Contract"])
        self.religionComboBox = comboBoxDrawers(self.innerWidget, 660, 140, 111, 22,["Orthodox" ,"Muslim" , "Protestant" , "Adventist" , "Others"])



        '''Defining Labels/LineEdit/ComboBoxes - Section II'''
        '''Labels'''
        self.hiredDateLabel = labelDrawers(self.innerWidget, 240, 360, 51, 16, "Hired Date")
        self.payrollTypeLabel = labelDrawers(self.innerWidget, 240, 400, 71, 16, "Payroll Type")
        self.contractEndDateLabel = labelDrawers(self.innerWidget, 240, 430, 91, 16, "Contract End Date")
        self.positionLabel = labelDrawers(self.innerWidget, 240, 460, 71, 16, "Position")
        self.memberLabel = labelDrawers(self.innerWidget, 240, 490, 61, 16, "Member")
        self.locationLabel = labelDrawers(self.innerWidget, 240, 520, 71, 16, "Location")
        self.stationLabel = labelDrawers(self.innerWidget, 240, 560, 71, 16, "Station")
        self.orgUnitLabel = labelDrawers(self.innerWidget, 240, 590, 61, 16, "Org. Unit")  
        self.subOfficeLabel = labelDrawers(self.innerWidget, 240, 620, 71, 16, "Sub Office")
        self.supervisorPositionLabel = labelDrawers(self.innerWidget, 240, 648, 101, 16, "Supervisor Position")
        self.supervisorNameLabel = labelDrawers(self.innerWidget, 240, 678, 91, 16, "Supervisor Name")
        self.sciGradeLabel = labelDrawers(self.innerWidget, 240, 708, 71, 16, "SCI Grade")
        self.salaryLabel = labelDrawers(self.innerWidget, 550, 360, 71, 16, "Salary")
        self.accountNumberLabel = labelDrawers(self.innerWidget, 550, 390, 91, 16, "Account Number")
        self.bankAreaLabel = labelDrawers(self.innerWidget, 550, 420, 71, 16, "Bank Area")
        self.natureOfAssignment = labelDrawers(self.innerWidget, 550, 450, 111, 16, "Nature of Assignment")
        self.projectAttachmentLabel = labelDrawers(self.innerWidget, 550, 480, 111, 16, "Project Attachment")
        self.taxCodeLabel = labelDrawers(self.innerWidget, 550, 510, 71, 16, "Tax Code")
        self.pensionCodeLabel = labelDrawers(self.innerWidget, 550, 540, 81, 16, "Pension Code")
        self.statusLabel = labelDrawers(self.innerWidget, 550, 570, 81, 16, "Status")

        '''LineEdit'''
        self.salaryEdit = lineEditDrawers(self.innerWidget, 660, 360, 113, 20)
        self.accountNumberEdit = lineEditDrawers(self.innerWidget, 660, 390, 113, 20)
        self.bankAreaEdit = lineEditDrawers(self.innerWidget, 660, 420, 113, 20)
        self.taxCodeEdit = lineEditDrawers(self.innerWidget, 660, 510, 113, 20)
        self.pensionCodeEdit = lineEditDrawers(self.innerWidget, 660, 540, 113, 20)
        self.hiredDateEdit = dateEditDrawers(self.innerWidget, 350, 360, 111, 22)
        self.contractEndDateComboBox = dateEditDrawers(self.innerWidget, 350, 430, 111, 22)

        '''ComboBox'''
        self.payrollTypeComboBox = comboBoxDrawers(self.innerWidget, 350, 400, 111, 22,["Permanent" , "Contract"])
        self.positionComboBox = comboBoxDrawers(self.innerWidget, 350, 460, 111, 22,["" , ""])
        self.memberComboBox = comboBoxDrawers(self.innerWidget, 350, 490, 111, 22,["Bantu" , ""])
        self.locationComboBox = comboBoxDrawers(self.innerWidget, 350, 520, 111, 22,["Addis Ababa" , ""])
        self.stationComboBox = comboBoxDrawers(self.innerWidget, 350, 560, 111, 22,["Addis Ababa" , ""])
        self.orgUnitComboBox = comboBoxDrawers(self.innerWidget, 350, 590, 111, 22,["Admin & IT" , ""])
        self.subOfficeComboBox = comboBoxDrawers(self.innerWidget, 350, 620, 111, 22,["Addis Ababa" , ""])
        self.supervisorPositionComboBox = comboBoxDrawers(self.innerWidget, 350, 648, 111, 22,["Accountability" , ""])
        self.supervisorNameComboBox = comboBoxDrawers(self.innerWidget, 350, 678, 111, 22,["" , ""])
        self.sciGradeComboBox = comboBoxDrawers(self.innerWidget, 350, 708, 111, 22,["1" , "2"])
        self.natureOfAssignmentComboBox = comboBoxDrawers(self.innerWidget, 660, 450, 111, 22,["Managerial" , ""])
        self.projectAttachmentComboBox = comboBoxDrawers(self.innerWidget, 660, 480, 111, 22,["Program" , ""])
        self.statusComboBox = comboBoxDrawers(self.innerWidget, 660, 570, 111, 22,["Active" , ""])
        self.userResignationComboBox = comboBoxDrawers(self.innerWidget, 10, 510, 161, 91,["Resignation" , ""])


        self.innerstackedWidget.addWidget(self.innerWidget)
        self.tabWidget.addTab(self.personel, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.personel), "Personnel")
        self.stackedWidget.setCurrentIndex(1)
        
        AdminDashBoard.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.innerWidget


# if __name__ == "__main__":
#     import sys
#     os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
#     app = QtWidgets.QApplication(sys.argv)
#     app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     AdminDashBoard = QtWidgets.QMainWindow()
#     ui = Personel()
#     ui.setupUi(AdminDashBoard)
#     AdminDashBoard.show()
#     sys.exit(app.exec_())