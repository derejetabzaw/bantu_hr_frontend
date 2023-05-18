import os
import sys
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils



class Personel(object):
    def setupUi(self, AdminDashBoard):
        self.centralwidget = utils.widgetDrawer(None,0,0,0,0)
        self.font = utils.fontSpecifier("Yu Gothic UI Semibold", 9, True, 75)
        self.fontAddUser = utils.fontSpecifier("Yu Gothic UI Semibold", 12, True, 75)

        self.tabWidget = utils.tabWidgetDrawer(self.centralwidget, 0, 0, 1920, 1000)
        self.tabWidget.setFont(self.font)
        self.tabWidget.setStyleSheet("color:#000")

        self.personel = utils.widgetDrawer(None,0,0,0,0)
        self.stackedWidget = utils.stackedWidgetDrawer(self.personel, 0, 0, 1921, 1011)
        self.stackedWidget.setFont(self.font)
        self.stackedWidget.setStyleSheet("background-color:#fff\n""")
        
        self.adduser = utils.widgetDrawer(None,0,0,0,0)
        self.frame = utils.frameDrawer(self.adduser, 0, 0, 1361, 821,"StyledPanel","Raised")
        self.innerstackedWidget = utils.stackedWidgetDrawer(self.frame, 0, -20, 1920, 1000)
        self.innerstackedWidget.setFont(self.font)


        '''Defining Stacked Widgets - Section I'''
        self.innerWidget = utils.widgetDrawer(None,0,0,0,0)
        self.stackedWidget.addWidget(self.adduser)
        self.line_upper_bound = utils.lineDrawer(self.innerWidget,"horizontal",240, 330, 521, 16)
        self.line_divider = utils.lineDrawer(self.innerWidget,"horizontal",220, 730, 911, 16)
        self.line_vertical_divider = utils.lineDrawer(self.innerWidget,"vertical",170, 10, 21, 1001)
        self.line_lower_bound = utils.lineDrawer(self.innerWidget,"horizontal",240, 110, 521, 16)
        
        
        self.innerWidget = utils.widgetDrawer(None,0,0,0,0)
        self.bottomButtonLayoutWidgets = utils.widgetDrawer(self.innerWidget,540, 650, 571, 61)
        self.bottomButtonLayout = utils.horizontalLayoutDrawer(self.bottomButtonLayoutWidgets)


        '''Defining Labels/LineEdit/ComboBoxes - Section I'''
        '''Buttons'''
        self.addUserButton = utils.pushButtonDrawers(self.innerWidget,10, 40, 158, 141, "Add User", "iconmonstr-user-8-120.png")
        self.viewUserButton = utils.pushButtonDrawers(self.innerWidget,10, 190, 158, 141, "View User", "iconmonstr-list-lined-120.png")
        self.positionManagementButton = utils.pushButtonDrawers(self.innerWidget,10, 340, 158, 141, "Position Management", "iconmonstr-flag-3-120.png")        
        self.browseButton = utils.pushButtonDrawers(self.innerWidget,940, 420, 111, 51, "Browse", "")
        self.okayButton = utils.pushButtonDrawers(self.bottomButtonLayoutWidgets,0,0 ,0 ,0 , "Okay", "")
        self.cancelButton = utils.pushButtonDrawers(self.bottomButtonLayoutWidgets,0,0 ,0 ,0 ,"Cancel", "")
        self.importFromExcelButton = utils.pushButtonDrawers(self.bottomButtonLayoutWidgets,0,0 ,0 , 0, "Import From Excel","" )
        self.syncFPButton = utils.pushButtonDrawers(self.bottomButtonLayoutWidgets, 0 ,0 ,0 ,0 , "Sync Fingerprint", "")
        
        '''Add Button Widget to Layout'''
        self.bottomButtonLayout.addWidget(self.okayButton)
        self.bottomButtonLayout.addWidget(self.cancelButton)
        self.bottomButtonLayout.addWidget(self.importFromExcelButton)
        self.bottomButtonLayout.addWidget(self.syncFPButton)
        

        '''Title Font and Label'''
        self.addPersonelLabel = utils.labelDrawers(self.innerWidget, 235, 50, 231, 61, "Add Personel")
        self.addPersonelLabel.setFont(self.fontAddUser)

        '''Labels'''
        self.employeeCodeLabel = utils.labelDrawers(self.innerWidget, 240, 138, 81, 16, "Employee Code")
        self.fullNameLabel = utils.labelDrawers(self.innerWidget, 240, 168, 51, 16, "Full Name")
        self.birthDateLabel = utils.labelDrawers(self.innerWidget, 240, 198, 51, 16, "Birth Date")
        self.birthPlaceLabel = utils.labelDrawers(self.innerWidget, 240, 228, 61, 16, "Birth Place")
        self.bloodTypeLabel = utils.labelDrawers(self.innerWidget, 240, 258, 61, 16, "Blood Type")
        self.genderLabel = utils.labelDrawers(self.innerWidget, 240, 288, 39, 11, "Gender")
        self.religionLabel = utils.labelDrawers(self.innerWidget, 550, 138, 71, 16, "Religion")
        self.maritalStatusLabel = utils.labelDrawers(self.innerWidget, 550, 168, 61, 16, "Marital Status")
        self.employeTypeLabel = utils.labelDrawers(self.innerWidget, 550, 198, 71, 16, "Employee Type")
        self.drivingLicenseLabel = utils.labelDrawers(self.innerWidget, 550, 228, 111, 16, "Driving License Grade")
        self.remarksLabel = utils.labelDrawers(self.innerWidget, 550, 288, 39, 11, "Remarks")
        self.userPhotoLabel = utils.labelDrawers(self.innerWidget, 880, 210, 241, 201, "<html><head/><body><p><img src=\"" + utils.icons_dir + "iconmonstr-user-14-240.png\"/></p></body></html>")

        '''LineEdits'''
        self.employeeCodeEdit = utils.lineEditDrawers(self.innerWidget, 330, 138, 113, 20)
        self.fullNameEdit = utils.lineEditDrawers(self.innerWidget, 330, 168, 113, 20)
        self.birthDateEdit = utils.dateEditDrawers(self.innerWidget, 330, 198, 111, 22)
        self.birthPlaceEdit = utils.lineEditDrawers(self.innerWidget, 330, 228, 113, 20)
        self.bloodTypeEdit = utils.lineEditDrawers(self.innerWidget, 330, 258, 113, 20)
        self.drivingLicenseEdit = utils.lineEditDrawers(self.innerWidget, 670, 228, 113, 20)
        self.remarksEdit = utils.plainEditDrawers(self.innerWidget, 660, 258, 104, 64)

        '''ComboBoxes'''
        self.genderComboBox = utils.comboBoxDrawers(self.innerWidget, 330, 290, 111, 22,["Male" , "Female"])
        self.maritalStatusComboBox = utils.comboBoxDrawers(self.innerWidget, 660, 170, 111, 22,["Single" , "Married"])
        self.employeTypeComboBox = utils.comboBoxDrawers(self.innerWidget, 660, 200, 111, 22,["Permanent" , "Contract"])
        self.religionComboBox = utils.comboBoxDrawers(self.innerWidget, 660, 140, 111, 22,["Orthodox" ,"Muslim" , "Protestant" , "Adventist" , "Others"])



        '''Defining Labels/LineEdit/ComboBoxes - Section II'''
        '''Labels'''
        
        self.hiredDateLabel = utils.labelDrawers(self.innerWidget, 240, 360, 51, 16, "Hired Date")
        self.payrollTypeLabel = utils.labelDrawers(self.innerWidget, 240, 400, 71, 16, "Payroll Type")
        self.contractEndDateLabel = utils.labelDrawers(self.innerWidget, 240, 430, 91, 16, "Contract End Date")
        self.positionLabel = utils.labelDrawers(self.innerWidget, 240, 460, 71, 16, "Position")
        self.memberLabel = utils.labelDrawers(self.innerWidget, 240, 490, 61, 16, "Member")
        self.locationLabel = utils.labelDrawers(self.innerWidget, 240, 520, 71, 16, "Location")
        self.stationLabel = utils.labelDrawers(self.innerWidget, 240, 560, 71, 16, "Station")
        self.orgUnitLabel = utils.labelDrawers(self.innerWidget, 240, 590, 61, 16, "Org. Unit")  
        self.subOfficeLabel = utils.labelDrawers(self.innerWidget, 240, 620, 71, 16, "Sub Office")
        self.supervisorPositionLabel = utils.labelDrawers(self.innerWidget, 240, 648, 101, 16, "Supervisor Position")
        self.supervisorNameLabel = utils.labelDrawers(self.innerWidget, 240, 678, 91, 16, "Supervisor Name")
        self.sciGradeLabel = utils.labelDrawers(self.innerWidget, 240, 708, 71, 16, "SCI Grade")
        self.salaryLabel = utils.labelDrawers(self.innerWidget, 550, 360, 71, 16, "Salary")
        self.accountNumberLabel = utils.labelDrawers(self.innerWidget, 550, 390, 91, 16, "Account Number")
        self.bankAreaLabel = utils.labelDrawers(self.innerWidget, 550, 420, 71, 16, "Bank Area")
        self.natureOfAssignment = utils.labelDrawers(self.innerWidget, 550, 450, 111, 16, "Nature of Assignment")
        self.projectAttachmentLabel = utils.labelDrawers(self.innerWidget, 550, 480, 111, 16, "Project Attachment")
        self.taxCodeLabel = utils.labelDrawers(self.innerWidget, 550, 510, 71, 16, "Tax Code")
        self.pensionCodeLabel = utils.labelDrawers(self.innerWidget, 550, 540, 81, 16, "Pension Code")
        self.statusLabel = utils.labelDrawers(self.innerWidget, 550, 570, 81, 16, "Status")

        '''LineEdits'''
        self.salaryEdit = utils.lineEditDrawers(self.innerWidget, 660, 360, 113, 20)
        self.accountNumberEdit = utils.lineEditDrawers(self.innerWidget, 660, 390, 113, 20)
        self.bankAreaEdit = utils.lineEditDrawers(self.innerWidget, 660, 420, 113, 20)
        self.taxCodeEdit = utils.lineEditDrawers(self.innerWidget, 660, 510, 113, 20)
        self.pensionCodeEdit = utils.lineEditDrawers(self.innerWidget, 660, 540, 113, 20)
        self.hiredDateEdit = utils.dateEditDrawers(self.innerWidget, 350, 360, 111, 22)
        self.contractEndDateComboBox = utils.dateEditDrawers(self.innerWidget, 350, 430, 111, 22)

        '''ComboBoxes'''
        self.payrollTypeComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 400, 111, 22,["Permanent" , "Contract"])
        self.positionComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 460, 111, 22,["" , ""])
        self.memberComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 490, 111, 22,["Bantu" , ""])
        self.locationComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 520, 111, 22,["Addis Ababa" , ""])
        self.stationComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 560, 111, 22,["Addis Ababa" , ""])
        self.orgUnitComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 590, 111, 22,["Admin & IT" , ""])
        self.subOfficeComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 620, 111, 22,["Addis Ababa" , ""])
        self.supervisorPositionComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 648, 111, 22,["Accountability" , ""])
        self.supervisorNameComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 678, 111, 22,["" , ""])
        self.sciGradeComboBox = utils.comboBoxDrawers(self.innerWidget, 350, 708, 111, 22,["1" , "2"])
        self.natureOfAssignmentComboBox = utils.comboBoxDrawers(self.innerWidget, 660, 450, 111, 22,["Managerial" , ""])
        self.projectAttachmentComboBox = utils.comboBoxDrawers(self.innerWidget, 660, 480, 111, 22,["Program" , ""])
        self.statusComboBox = utils.comboBoxDrawers(self.innerWidget, 660, 570, 111, 22,["Active" , ""])
        self.userResignationComboBox = utils.comboBoxDrawers(self.innerWidget, 10, 510, 161, 91,["Resignation" , ""])

        '''Setting Widgets as Central Widgets'''
        self.innerstackedWidget.addWidget(self.innerWidget)
        self.tabWidget.addTab(self.personel, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.personel), "Personnel")
        self.stackedWidget.setCurrentIndex(1)
        
        AdminDashBoard.setCentralWidget(self.centralwidget)
        return self.innerWidget


