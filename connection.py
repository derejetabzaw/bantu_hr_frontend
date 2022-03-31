import mysql.connector as mysql
from datetime import date

#Used to connect to the database
# Change the user and password with your mysql configuration for the file to connect with the database
bantudb = mysql.connect(
      host='localhost',
      user='root',
      database='bantu-hr-db',
      password='wutangclan', 
      port=3306,
      auth_plugin = 'mysql_native_password'
)

mycursor = bantudb.cursor()
mycursor.execute("use `bantu-hr-db`;")

def viewDepartment():
      mycursor.execute("SELECT * FROM Department;")
      for temp in mycursor:
            print(temp)
      bantudb.close()

def addDepartment(dep_id, dep_name, par_dep):
      mycursor.execute( """INSERT INTO Department (Department_id, Department_name, Parent_Department) 
                        VALUES (%s, %s, %s)""", (dep_id, dep_name, par_dep))
      bantudb.commit()
      print("Department Added Successfully!")
      viewDepartment()

def editDepartment(dep_id, dep_name, par_dep):
      mycursor.execute( """UPDATE Department SET Department_name=%s, Parent_Department=%s 
                              WHERE Department_id=%s""", (dep_name, par_dep, dep_id))
      bantudb.commit()
      print("Department Updated Successfully!")
      viewDepartment()

def deleteDepartment(dep_id):
      mycursor.execute( "DELETE FROM Department WHERE Department_id=%s", (dep_id,))
      bantudb.commit()
      print("Department Deleted Successfully!")
      viewDepartment()

def viewAreas():
      mycursor.execute("SELECT * FROM Areas;")
      for temp in mycursor:
            print(temp)
      bantudb.close()

def addAreas(area_id, area_code, area_name, par_area, remark):
      mycursor.execute( """INSERT INTO areas (areaId, areaCode, areaName, parentArea, remarks) 
                        VALUES (%s, %s, %s, %s, %s)""", (area_id, area_code, area_name, par_area, remark))
      bantudb.commit()
      print("Area Added Successfully!")
      viewAreas()
      
def addPersonel(**personel):
      mycursor.execute( """INSERT INTO personel (personel_id,Gender,Department,Employee_type,Employemnet_date,pasword,first_name,last_name,job_title,paygrade,image) 
                  VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s)""", 
                  (personel["personel_id"],personel["Gender"],personel["Department"],personel["Employee_type"],personel["Employemnet_date"],personel["pasword"],personel["first_name"],personel["last_name"],personel["job_title"],personel["paygrade"],personel["image"]))
      bantudb.commit()
      bantudb.close()
      print("Area Added Successfully!")
            

def editAreas(area_id, area_name, par_area, remark):
      mycursor.execute( """UPDATE areas 
                              SET areaName=%s, parentArea=%s, remarks=%s
                              WHERE areaId=%s""", (area_name, par_area, remark, area_id))
      bantudb.commit()
      print("Area Updated Successfully!")
      viewAreas()

def deleteAreas(area_id):
      mycursor.execute( "DELETE FROM areas WHERE areaId=%s", (area_id,))
      bantudb.commit()
      print("Area Deleted Successfully!")
      viewAreas()

def viewDevices():
      mycursor.execute("SELECT * FROM device;")
      for temp in mycursor:
            print(temp)
      bantudb.close()

def addDevice(deviceId, deviceName, serialNumber, ipAddress, portNumber, area_id):
      mycursor.execute( """INSERT INTO device (deviceId, deviceName, serialNumber, ipAddress, portNumber, areaId) 
                        VALUES (%s, %s, %s, %s, %s, %s)""", (deviceId, deviceName, serialNumber, ipAddress, portNumber, area_id))
      bantudb.commit()
      print("Device Added Successfully!")
      viewDevices()

def editDevice(deviceId, deviceName, ipAddress, portNumber, area_id):
      mycursor.execute( """UPDATE device 
                              SET deviceName=%s, ipAddress=%s, portNumber=%s, areaId=%s
                              WHERE deviceId=%s""", (deviceName, ipAddress, portNumber, area_id, deviceId))
      bantudb.commit()
      print("Device Updated Successfully!")
      viewDevices()

def deleteDevice(deviceId):
      mycursor.execute( "DELETE FROM device WHERE deviceId=%s", (deviceId,))
      bantudb.commit()
      print("Device Deleted Successfully!")
      viewDevices()

def viewPersonel():
      mycursor.execute("SELECT * FROM personel;")
      for temp in mycursor:
            print(temp)
      bantudb.close()



def editPersonel(personel_id, Department, Employee_type, pasword, job_title, paygrade, image, deviceId):
      mycursor.execute( """UPDATE personel 
                              SET Department=%s, Employee_type=%s, pasword=%s, job_title=%s, paygrade=%s, image=%s, deviceId=%s
                              WHERE personel_id=%s""", (Department, Employee_type, pasword, job_title, paygrade, image, deviceId, personel_id))
      bantudb.commit()
      print("Personel Updated Successfully!")
      viewPersonel()

def deletePersonel(personel_id):
      mycursor.execute( "DELETE FROM personel WHERE personel_id=%s", (personel_id,))
      bantudb.commit()
      print("Personel Deleted Successfully!")
      viewPersonel()
      
def add_holiday(*args):
      mycursor.execute( """INSERT INTO holiday (holiday_id, hoiday_name, min_unit, unit, round_off, symbol_in_report) 
                        VALUES (%s, %s, %s, %s, %s, %s)""", (args[0], args[1], args[2], args[3], args[4], args[5]))
      bantudb.commit()
      print("holiday Added Successfully!")
      
      
      
