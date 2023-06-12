#Scripts\utils.py
import os
from PyQt5 import QtCore, QtGui, QtWidgets 
"""importing packages used for python gui"""

parent_dir = os.path.dirname(os.getcwd().replace("\\","/"))
icons_dir = os.path.join(parent_dir, "Assets/icons/").replace("\\","/")
images_dir = os.path.join(parent_dir, "Assets/images/").replace("\\","/")
"""specfies the location for the image files"""
""" this module has function that allows the user to customize and draw differernt types of widgets  """
IMAGES = [str(images_dir) + "1.jpg", str(images_dir) + "2.jpg",
            str(images_dir) + "3.jpg", str(images_dir) + "4.jpg", str(images_dir) + "5.jpg"]

def fontSpecifier(Family , PointSize , Bold , Weight):
    """_this function specfies our fonts for the objects _

    Args:
        Family (_string _): _representing the font family_
        PointSize (_int_): _font size_
        Bold (_Bool_): _true if we want it to be bold else false_
        Weight (_int _): _sets how thick or thin characters in text should be displayed._

    Returns:
        _object_: it returns the customized object that calls it__
    """    
    font = QtGui.QFont()
    font.setFamily(Family)
    font.setPointSize(PointSize)
    font.setBold(Bold)
    font.setWeight(Weight)
    
    return font

def lineDrawer(widget, orientation, x, y, length, width):
    """_draws the specfic widget and sytles it with the specfied arguments_
    example   self.line_lower_bound = utils.lineDrawer(self.innerWidget,"horizontal",240, 110, 521, 16)
    Args:
        widget (_object _): _the qwwidget object_
        orientation (_string_): _horizontal /vertical_
        x (_int_): _the point  of the x-axis where we begin_
        y (_int_): _the point of the y-axis where we bbegin_
        length (_int_): _the length of the line on the the y axis_
        width (_int_): _the length of the line on the x axis_

    Returns:
        _object_: _the line objecct_
    """    
    line = QtWidgets.QFrame(widget)
    """ QFrame class is the base class of widgets that can have a frame"""
    if orientation == "Horizontal":
        line = QtWidgets.QFrame(widget)
        line.setGeometry(QtCore.QRect(x, y, length, width))
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        """The frame style is specified by a frame shape and a shadow style that is used to visually separate the frame from surrounding widgets."""
        line.setStyleSheet("")
    if orientation == "Vertical":
        line = QtWidgets.QFrame(widget)
        line.setGeometry(QtCore.QRect(x, y, length, width))
        line.setFrameShape(QtWidgets.QFrame.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setStyleSheet("")

    return line


def labelDrawers(widget, x, y,length,width, text):
    """_here we use QLabel for displaying text and images for the widget that calls this method_

    Args:
        widget (_objecct_): _object of widget classes_
        x (_int_): _the starting point on the x-axis_
        y (_int_): _the starting point on the x-axis_
        length (_int_): _the vertical distance_
        width (_int_): _the horizontal distance_
        text (_string_): _the text we want to display_

    Returns:
        _the object_: _the customized label_
    """    
    label = QtWidgets.QLabel(widget)
    label.setGeometry(QtCore.QRect(x, y, length, width))
    label.setText(text)
    return label  
def lineEditDrawers(widget, x, y, length, width):
    """_The QLineEdit widget is a one-line text editor this function allows us to create a customzied  widget_

    Args:
        widget (_object_): _the object we are gonna customize_
          x (_int_): _the starting point on the x-axis_
         y (_int_): _the starting point on the x-axis_
         length (_int_): _the vertical distance_
         width (_int_): _the horizontal distance_
       
    Returns:
        _object_: _the customized widget object_
    """    
    if (x,y,length,width) != (0,0,0,0):
        
        lineedit = QtWidgets.QLineEdit(widget)
        lineedit.setGeometry(QtCore.QRect(x, y, length, width))
    else:
        """ if the values are not given we just creted a lineeditable widget with the default value"""
        lineedit = QtWidgets.QLineEdit(widget)

    return lineedit

def widgetEditStyle(widget , attributes):
    """_for example utils.widgetEditStyle(self.buttonSave , ["background-color:#fff" ,"color:#0076bd", "border-top:1px solid #fff"])
    we use the function to style the widgets_

    Args:
        widget (_object _): _the object we are gonna customize_
        attributes (_string_): _list of the attributes_

    Returns:
        _object_: _the customized object_
    """    
    style = []
    for attribute in (attributes):
        style.append(str(attribute + ';\n'))
    """ we add the styles present in the arguments and we add them to our css  """
    stylelist = '\n'.join(style)
    widget.setStyleSheet(stylelist)
    return widget
def dateEditDrawers(widget, x, y, length, width):
    """ QDateTimeEdit allows the user to edit dates by using the keyboard or the arrow keys to increase and decrease date and time values."""
    """_we use this function to create  editable datatimedrawers in the position we want_

    Returns:
        _object_: _returns the the customized obj_
    """    
    dateedit = QtWidgets.QDateEdit(widget)
    dateedit.setGeometry(QtCore.QRect(x, y, length, width))
    return dateedit
def plainEditDrawers(widget, x, y, length, width):
    "this function creates editabletext plain in the position and size given by the argumen"
    plainedit = QtWidgets.QPlainTextEdit(widget).setGeometry(QtCore.QRect(x, y, length, width))
    return plainedit
def comboBoxDrawers(widget, x, y, length, width , comboitems):
    """_draws the combo box int the x and y positions specfied and then populates the items to the combobox_

    Args:
         widget (_object_): _combox object_
         x (_int_): _the starting point on the x-axis_
         y (_int_): _the starting point on the x-axis_
         length (_int_): _the vertical distance_
         width (_int_): _the horizontal distance_
       comboitems (_string_): _the string we wish to populate the combobox with_

    Returns:
        _object_: _combobox object_
    """    
    combobox = QtWidgets.QComboBox(widget)
    combobox.setGeometry(QtCore.QRect(x, y, length, width))
    for i,items in enumerate (comboitems):
                 
        combobox.addItem(items) 
        """using  a loop to populate the combobox"""  
        combobox.setItemText(i, items)
    return combobox

def checkBoxDrawers(widget, x, y, length, width, text):
    """_draws the check box int the x and y positions specfied and then sets the text on the checkbox_

    Args:
         widget (_object_): _checkbox object_
         x (_int_): _the starting point on the x-axis_
         y (_int_): _the starting point on the x-axis_
         length (_int_): _the vertical distance_
         width (_int_): _the horizontal distance_
        text (int):_the text for the checkbox_

    Returns:
        _object_: _checkboxobject_
    """ 
    checkbox = QtWidgets.QCheckBox(widget)
    checkbox.setGeometry(QtCore.QRect(x, y, length, width))
    checkbox.setText(text)
    return checkbox
def pushButtonDrawers(widget,x, y, length, width, text , icon):
    
           
    """_pushbuttton to draw it on the specfied position and inserting the text or the icon (image) into  the pushbutton_

    Returns:
        _object_: _returns the customized object_
    """       
    
    pushbutton = QtWidgets.QPushButton(widget)
    pushbutton.setGeometry(QtCore.QRect(x, y, length, width))
    pushbutton.setText(text)
    """if the text arguemnt is given to us we will use that if we are given an image we will use that and then using css to style the button"""
    if len(icon) != 0:
        """ if we have an image in the argument"""
        pushbutton.setStyleSheet("background:url(" + icons_dir  + icon + ");\n"
                                "background-repeat:no-repeat;\n"
                                "height:12px;\n"
                                "text-align:bottom;")
    if len(icon) == 0 and text == "Browse":
        """if we have no image but have an argument with the value browse"""
        pushbutton.setStyleSheet("border:1px solid #fff;\n"
                                    "border-radius:25px;\n"
                                    "background-color:#0076bd;\n"
                                    "color:#fff")

    if len(icon) == 0 and (x,y,length,width) == (0,0,0,0):
        if text == 'Cancel':
            """text argument with value cancel no other argument provided"""
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

def frameDrawer(widget ,x, y, length, width, FrameShape, FrameShadow):
    """_to make a frame with the specfied arguments for example frameDrawer(self.scrollAreaWidgetContents, 0, 500, 1271, 41, "HLine", "Sunken")_

   
    """    
    frame = QtWidgets.QFrame(widget)
    frame.setEnabled(True)
    frame.setGeometry(QtCore.QRect(x, y, length, width))
    frame.setStyleSheet("")
    if FrameShape == "StyledPanel":
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
    if FrameShape == "HLine":
        frame.setFrameShape(QtWidgets.QFrame.HLine)
    if FrameShape == "VLine":
        frame.setFrameShape(QtWidgets.QFrame.VLine)
    if FrameShadow == "Raised":
        frame.setFrameShadow(QtWidgets.QFrame.Raised)
        """the frame and contents appear raised; draws a 3D raised line using the light and dark colors of the current color group"""
    if FrameShadow == "Sunken":
        """ 	the frame and contents appear sunken; draws a 3D sunken line using the light and dark colors of the current color group"""
        frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        
    return frame
def widgetDrawer(widget, x, y, length, width):
    if widget is None:
    
        widget = QtWidgets.QWidget() 
  
   
        if (x,y,length,width) != (0,0,0,0):
            widget.setGeometry(QtCore.QRect(x, y, length, width))
    else:
        widget = QtWidgets.QWidget(widget)
        if (x,y,length,width) != (0,0,0,0):
            widget.setGeometry(QtCore.QRect(x, y, length, width))
    """ for example widgetDrawer(None,0,0,0,0) if no object is provided for the first argument then we will just draw the default widget if provided we use"""
    return widget
def scrollAreaDrawer(widget, x, y, length, width):
    """_it draws the scroll area with the specfied arguments_

    Args:widget (_object_): _the object we are gonna customize_
          x (_int_): _the starting point on the x-axis_
         y (_int_): _the starting point on the x-axis_
         length (_int_): _the vertical distance_
         width (_int_): _the horizontal distance_
        

    Returns:
        _object_: 
    """    
    scrollArea = QtWidgets.QScrollArea(widget)
    scrollArea.setGeometry(QtCore.QRect(x, y, length, width))
    scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
    scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
    scrollArea.setWidgetResizable(True)
    return scrollArea
def stackedWidgetDrawer(widget, x, y, length, width):
    stackedWidget = QtWidgets.QStackedWidget(widget)
    stackedWidget.setGeometry(QtCore.QRect(x, y, length, width))
    return stackedWidget
def tableWidgetDrawer(widget, x, y, length, width, columnCount, rowCount, Texts):
    """_for example tableWidgetDrawer(self.tab, 0, 60, 560, 421, 2,0,["Employee Name" , "Total Hours"])_
       sets up a table with the values given via the argument and poputaltes the table with the data in text
   
    Returns:
        _object_: 
    """    
    tableWidget = QtWidgets.QTableWidget(widget)
    tableWidget.setGeometry(QtCore.QRect(x, y, length, width))
    tableWidget.setColumnCount(columnCount)
    tableWidget.setRowCount(rowCount)
    item = []
    for i in range(len(Texts)):
        item.append(QtWidgets.QTableWidgetItem())
    for i, Text in enumerate(Texts):
        tableWidget.setHorizontalHeaderItem(i, item[i])
        """loop to populate the the column and the row"""
        item[i].setText(Text)
    return tableWidget
def tabWidgetDrawer(widget, x, y, length, width):
    tabWidget = QtWidgets.QTabWidget(widget)
    tabWidget.setGeometry(QtCore.QRect(x, y, length, width))
    tabWidget.setIconSize(QtCore.QSize(20,20))
    return tabWidget

def formLayoutDrawer(widget):
    """_draws ot_

    Args:
        widget (_type_): _description_

    Returns:
        _type_: _description_
    """    
    formLayout = QtWidgets.QFormLayout(widget)
    formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
    """that can be used to control the way in which the form's fields grow."""
    formLayout.setContentsMargins(0, 0, 0, 0)
    """Sets the left, top, right, and bottom margins to use around the layout."""
    return formLayout

def horizontalLayoutDrawer(widget):
    """
The QHBoxLayout class lines up widgets horizontally"""
    horizontalLayout = QtWidgets.QHBoxLayout(widget)
    horizontalLayout.setContentsMargins(0, 0, 0, 0)
    return horizontalLayout
def verticalLayoutDrawer(widget):
    verticalLayout = QtWidgets.QVBoxLayout(widget)
    verticalLayout.setContentsMargins(0, 0, 0, 0)
    return verticalLayout


def treeWidgetDrawer(widget, x, y, length, width):
    """The QTreeWidget class is a convenience class that provides a standard tree widget with a classic item-based interface similar to that used by the QListView """
    treeWidget = QtWidgets.QTreeWidget(widget)
    treeWidget.setGeometry(QtCore.QRect(x, y, length, width))
    return treeWidget

def gridLayoutDrawer(widget):
    """QGridLayout takes the space made available to it (by its parent layout or by the parentWidget() ), 
    divides it up into rows and columns, and puts each widget it manages into the correct cell."""
    gridLayout = QtWidgets.QGridLayout(widget)
    gridLayout.setContentsMargins(0, 0, 0, 0)
    return gridLayout
def listWidgetDrawer(widget, x, y, length, width,Texts):
    """QListWidget is a convenience class that provides a list view similar to the one supplied by QListView,
    but with a classic item-based interface for adding and removing items."""
    listWidget = QtWidgets.QListWidget(widget)
    listWidget.setGeometry(QtCore.QRect(x, y, length, width))
    item = QtWidgets.QListWidgetItem()
    item = []
    for i in range(len(Texts)):
        item.append(QtWidgets.QListWidgetItem())
    for i, Text in enumerate(Texts):
        listWidget.addItem(item[i])
        item[i].setText(Text)    
    listWidget.setSortingEnabled(True)
    return listWidget




