# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loginpage.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import adminDashboard

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1923, 1000)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:#0076bd\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(570, 180, 691, 651))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("background-color:#0076bd;\n"
"border:4px solid #fff;\n"
"border-radius:22px;\n"
"box-shadow: 10px 10px 5px 0px rgba(0,118,189,0.75);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(90, 200, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#fff;\n"
"border:1px solid #0076bd;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#fff;\n"
"border:1px solid #0076bd;")
        self.label_2.setObjectName("label_2")
        self.LoginBtn = QtWidgets.QPushButton(self.frame)
        self.LoginBtn.setGeometry(QtCore.QRect(260, 380, 171, 61))
        self.LoginBtn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.LoginBtn.setStyleSheet("background-color:#0076bd;\n"
"border-radius:28px;\n"
"border:1px solid #fff;\n"
"cursor:pointer;\n"
"color:#ffffff;\n"
"font-family:Arial;\n"
"font-size:17px;\n"
"padding:16px 31px;\n"
"QPushButton::hover{\n"
"    background-color:#fff\n"
"}\n"
"   ")
        self.LoginBtn.setFlat(False)
        self.LoginBtn.setObjectName("LoginBtn")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(280, 80, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#fff;\n"
"border:1px solid #0076bd;\n"
"")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(250, 210, 301, 31))
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 20))
        self.lineEdit.setStyleSheet("border:1px solid #fff;\n"
"border-radius:8px;\n"
"border:1px solid #fff;\n"
"color:#fff;\n"
"font-family: monospace;\n"
"font-size:15px;")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(250, 270, 301, 31))
        self.lineEdit_2.setMinimumSize(QtCore.QSize(300, 20))
        self.lineEdit_2.setStyleSheet("border:1px solid #fff;\n"
"border-radius:8px;\n"
"border:1px solid #fff;\n"
"color:#fff;\n"
"font-family: monospace;\n"
"font-size:15px;")
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(800, 110, 401, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#0076bd;\n"
"\n"
"")
        
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.LoginBtn.clicked.connect(lambda x:self.click_event(MainWindow))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Username"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.LoginBtn.setText(_translate("MainWindow", "Login"))
        self.label_4.setText(_translate("MainWindow", "G!ZE"))
        self.label_3.setText(_translate("MainWindow", "G!ZE"))
        
    def click_event(self,MainWindow):
        self.adminWindow = adminDashboard.Ui_AdminDashBoard()
        
        self.adminWindow.setupUi(MainWindow)
        MainWindow.show()


if __name__ == "__main__":
    import sys    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
