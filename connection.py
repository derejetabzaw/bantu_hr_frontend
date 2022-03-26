import mysql .connector as mysql
from datetime import date

#Used to connect to the database
# Change the user and password with your mysql configuration for the file to connect with the database
bantudb = mysql.connect(
      host='localhost',
      user='root',
      database='bantu-hr-db',
      password='Sa@654321', 
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

def addPersonel(personel_id, Gender, Department, Employee_type, pasword, first_name, last_name, job_title, paygrade, image, deviceId):
      mycursor.execute( """INSERT INTO 
                        personel (`personel_id`,`Gender`,`Department`,`Employee_type`,`Employemnet_date`,`pasword`,`first_name`,`last_name`,`job_title`,`paygrade`,`image`,`deviceId`) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                        (personel_id, Gender, Department, Employee_type, date.today(), pasword, first_name, last_name, job_title, paygrade, image, deviceId))
      bantudb.commit()
      print("Personel Added Successfully!")
      viewPersonel()

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

# addDepartment(12, 'ZX', 'XZ')
#editDepartment(12, 'AS', 'TU')
#deleteDepartment(12)

#addAreas(3, 100, 'Add', 'Ethio', 'old' )
#editAreas(3,'ASDF', 'QWERTY' ,'GHJKL')
#deleteAreas(3)

#addDevice(12, 'Sams', '123456789', '128.52.11.90', '75', '2')
#editDevice(12, 'Samsung', '11.12.13.14', 123, 1 )
#deleteDevice(12)

# addPersonel(3, 'Male', 1, 'Temporary', 'QWERTY', 'Kebe', 'Abe', 'Guide', 222, None, 1)
# editPersonel(3, 'Lead', 'Permanent', 'ASDFGH', 'New', 555.55, None, 1)
#deletePersonel(3)
