import os
from PyQt5 import QtCore, QtGui, QtWidgets
import os



parent_dir = os.path.dirname(os.path.dirname(os.getcwd().replace("\\","/")))
icons_dir = os.path.join(parent_dir, "Assets/icons/").replace("\\","/")
images_dir = os.path.join(parent_dir, "Assets/images/").replace("\\","/")

class Home(object):
     images = [str(images_dir) + "1.jpg", str(images_dir) + "2.jpg",
            str(images_dir) + "3.jpg", str(images_dir) + "4.jpg", str(images_dir) + "5.jpg"]
     state = 0
     clickedItem = ""
       
     def setupUi(self, AdminDashBoard):
        '''This function is used to setup the UI for the Home Page Dashboard'''

        AdminDashBoard.setObjectName("AdminDashBoard")
        AdminDashBoard.resize(1922, 1080)
        AdminDashBoard.setMaximumSize(QtCore.QSize(16777215, 16777215))
        AdminDashBoard.setStyleSheet("background-color:#fff")
        self.centralwidget = QtWidgets.QWidget(AdminDashBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.hometabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.hometabWidget.setGeometry(QtCore.QRect(0, 0, 1920, 1000))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.hometabWidget.setFont(font)
        self.hometabWidget.setStyleSheet("color:#000")
        self.hometabWidget.setIconSize(QtCore.QSize(20, 40))
        self.hometabWidget.setObjectName("hometabWidget")
        self.homepage = QtWidgets.QWidget()
        self.homepage.setObjectName("homepage")
        self.frame = QtWidgets.QFrame(self.homepage)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1920, 1000))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1920, 1000))
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1901, 998))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        '''Buttons for Homepage Image Slider'''
        '''NEXT BUTTON'''
        self.nextButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.nextButton.setGeometry(QtCore.QRect(480, 400, 101, 101))
        self.nextButton.setStyleSheet("background:url(" + icons_dir + "next.png)")
        self.nextButton.setText("")
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(lambda x: self.nextImage())
        '''PREVIOUS BUTTON'''
        self.previousButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.previousButton.setGeometry(QtCore.QRect(380, 400, 101, 101))
        self.previousButton.setStyleSheet("background:url(" + icons_dir + "back.png)")
        self.previousButton.setText("")
        self.previousButton.setObjectName("previousButton")
        self.previousButton.clicked.connect(lambda x: self.prevImage())


        self.tableWidget = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 570, 1261, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Device Status")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Messsage")
        self.devicestatusbar_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.devicestatusbar_label.setGeometry(QtCore.QRect(10, 530, 161, 28))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.devicestatusbar_label.setFont(font)
        self.devicestatusbar_label.setObjectName("devicestatusbar_label")
        self.devicestatusbar_label.setText("Device Status Bar")

        
        self.imageslabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.imageslabel.setGeometry(QtCore.QRect(-1, 0, 1921, 361))
        self.imageslabel.setText("")
        self.imageslabel.setObjectName("imageslabel")
        self.separatingLine = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.separatingLine.setGeometry(QtCore.QRect(0, 500, 1271, 41))
        self.separatingLine.setFrameShape(QtWidgets.QFrame.HLine)
        self.separatingLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.separatingLine.setObjectName("separatingLine")
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.hometabWidget.addTab(self.homepage, "")
        AdminDashBoard.setCentralWidget(self.centralwidget)
        self.hometabWidget.setCurrentIndex(0)
        self.hometabWidget.setTabText(self.hometabWidget.indexOf(self.homepage), "Home")

        QtCore.QMetaObject.connectSlotsByName(AdminDashBoard)
        return self.scrollArea

     def nextImage(self):
        if(self.state == len(self.images)-1):
                self.state=0
                self.imageslabel.setStyleSheet(f"background:url({self.images[self.state]})")
                self.state+=1
        else:
                self.imageslabel.setStyleSheet(f"background:url({self.images[self.state]})")
                self.state+=1
     def prevImage(self):
        if(self.state == 0):
                self.state=len(self.images)-1
                self.imageslabel.setStyleSheet(f"background:url({self.images[self.state]})")
                self.state-=1
        else:
                self.imageslabel.setStyleSheet(f"background:url({self.images[self.state]})")
                self.state-=1




# if __name__ == "__main__":
#     import sys
#     os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
#     app = QtWidgets.QApplication(sys.argv)
#     app.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
#     AdminDashBoard = QtWidgets.QMainWindow()
#     ui = Home()
#     ui.setupUi(AdminDashBoard)
#     AdminDashBoard.show()
#     sys.exit(app.exec_())
