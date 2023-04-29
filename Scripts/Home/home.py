import os
import sys
sys.path.append(os.path.dirname(os.getcwd().replace("\\","/")))
import utils


class Home(object):
     state = 0
     clickedItem = ""
       
     def setupUi(self, AdminDashBoard):
        '''This function is used to setup the UI for the Home Page Dashboard'''

        AdminDashBoard.setObjectName("AdminDashBoard")
        AdminDashBoard.resize(1922, 1080)
        #AdminDashBoard.setMaximumSize(QtCore.QSize(16777215, 16777215))
        AdminDashBoard.setStyleSheet("background-color:#fff")
        '''Fonts'''
        self.fontHomeTab = utils.fontSpecifier("Yu Gothic UI Semibold", 9 , True , 75)
        self.fontstatusbar = utils.fontSpecifier("Yu Gothic UI Semibold", 14 , True , 75)
        '''Define Central Widget and Tab Widget'''
        self.centralwidget = utils.widgetDrawer(AdminDashBoard, 0, 0, 0, 0)
        self.hometabWidget = utils.tabWidgetDrawer(self.centralwidget, 0, 0, 1920, 1000)
        self.hometabWidget.setFont(self.fontHomeTab)
        self.hometabWidget.setStyleSheet("color:#000")
        #self.hometabWidget.setIconSize(QtCore.QSize(20, 40))
        
        '''Define Components of the Home Page'''
        self.homepage = utils.widgetDrawer(None,0,0,0,0)
        self.frame = utils.frameDrawer(self.homepage, 0, 0, 1920, 1000, "StyledPanel", "Raised")
        self.scrollArea = utils.scrollAreaDrawer(self.frame, 0, 0, 1920, 1000)
        self.scrollAreaWidgetContents = utils.widgetDrawer(None, 0, 0, 1901, 998)
        self.tableWidget = utils.tableWidgetDrawer(self.scrollAreaWidgetContents, 0, 570, 1261, 261,2,0,["Device Status","Message"])
        self.devicestatusbar_label = utils.labelDrawers(self.scrollAreaWidgetContents, 10, 530, 161, 28, "Device Status Bar")
        self.imageslabel = utils.labelDrawers(self.scrollAreaWidgetContents, -1, 0, 1921, 361, "")
        self.separatingLine = utils.frameDrawer(self.scrollAreaWidgetContents, 0, 500, 1271, 41, "HLine", "Sunken")
      
        
        '''Buttons for Homepage Image Slider'''
        '''NEXT BUTTON'''
        self.nextButton = utils.pushButtonDrawers(self.scrollAreaWidgetContents, 480, 400, 101, 101, "" , "next.png")
        self.nextButton.clicked.connect(lambda x: self.nextImage())
        '''PREVIOUS BUTTON'''
        self.previousButton = utils.pushButtonDrawers(self.scrollAreaWidgetContents, 380, 400, 101, 101,"","back.png")
        self.previousButton.clicked.connect(lambda x: self.prevImage())

        '''Setting Widgets as Central Widgets'''
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.hometabWidget.addTab(self.homepage, "")
        AdminDashBoard.setCentralWidget(self.centralwidget)
        self.hometabWidget.setCurrentIndex(0)
        self.hometabWidget.setTabText(self.hometabWidget.indexOf(self.homepage), "Home")
        #QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.scrollArea

     
     def nextImage(self):
        '''Button Click Functions - Next'''
        if(self.state == len(utils.IMAGES)-1):
                self.state=0
                self.imageslabel.setStyleSheet(f"background:url({utils.IMAGES[self.state]})")
                self.state+=1
        else:
                self.imageslabel.setStyleSheet(f"background:url({utils.IMAGES[self.state]})")
                self.state+=1
     def prevImage(self):
        '''Button Click Functions - Previous'''
        if(self.state == 0):
                self.state=len(utils.IMAGES)-1
                self.imageslabel.setStyleSheet(f"background:url({utils.IMAGES[self.state]})")
                self.state-=1
        else:
                self.imageslabel.setStyleSheet(f"background:url({utils.IMAGES[self.state]})")
                self.state-=1


