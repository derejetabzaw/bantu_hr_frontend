
import os
import time
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
parent_dir = os.path.dirname(os.getcwd().replace("\\","/"))
icons_dir = os.path.join(parent_dir, "Assets/icons/").replace("\\","/")


def fontSpecifier(Family , PointSize , Bold , Weight):
    font = QtGui.QFont()
    font.setFamily(Family)
    font.setPointSize(PointSize)
    font.setBold(Bold)
    font.setWeight(Weight)
    return font

def lineDrawer(widget, x, y, length, width):
    line = QtWidgets.QFrame(widget)
    line.setGeometry(QtCore.QRect(x, y, length, width))
    line.setStyleSheet("")
    return line


def labelDrawers(widget, x, y,length,width, text):
    label = QtWidgets.QLabel(widget)
    label.setGeometry(QtCore.QRect(x, y, length, width))
    label.setText(text)
    return label  
def lineEditDrawers(widget, x, y, length, width):
    if (x,y,length,width) != (0,0,0,0):
        lineedit = QtWidgets.QLineEdit(widget).setGeometry(QtCore.QRect(x, y, length, width))
    else:
        lineedit = QtWidgets.QLineEdit(widget)
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
def pushButtonDrawers(widget,x, y, length, width, text , icon):
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

def frameDrawer(widget ,x, y, length, width):
    frame = QtWidgets.QFrame(widget)
    frame.setEnabled(True)
    frame.setGeometry(QtCore.QRect(x, y, length, width))
    frame.setStyleSheet("")
    frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    frame.setFrameShadow(QtWidgets.QFrame.Raised)
    return frame
def widgetDrawer(widget, x, y, length, width):
    widget = QtWidgets.QWidget(widget)
    widget.setGeometry(QtCore.QRect(x, y, length, width))
    return widget
def stackedWidgetDrawer(widget, x, y, length, width):
    stackedWidget = QtWidgets.QStackedWidget(widget)
    stackedWidget.setGeometry(QtCore.QRect(x, y, length, width))
    return stackedWidget
def tableWidgetDrawer(widget, x, y, length, width):
    tableWidget = QtWidgets.QTableWidget(widget)
    tableWidget.setGeometry(QtCore.QRect(x, y, length, width))
    return tableWidget
def tabWidgetDrawer(widget, x, y, length, width):
    tabWidget = QtWidgets.QTabWidget(widget)
    tabWidget.setGeometry(QtCore.QRect(x, y, length, width))
    return tabWidget

def formLayoutDrawer(widget):
    formLayout = QtWidgets.QFormLayout(widget)
    formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
    formLayout.setContentsMargins(0, 0, 0, 0)
    
    return formLayout
def treeWidgetDrawer(widget, x, y, length, width):
    treeWidget = QtWidgets.QTreeWidget(widget)
    treeWidget.setGeometry(QtCore.QRect(x, y, length, width))
    return treeWidget

