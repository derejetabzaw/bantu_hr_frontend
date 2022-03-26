import mysql .connector as mysql

#Used to connect to the database
bantudb = mysql.connect(
      host='localhost',
      user='root',
      database='bantu-hr-db',
      password='Sa@654321', # Change the user and password with your mysql configuration for the file to connect with the database
      port=3306,
      auth_plugin = 'mysql_native_password'
)

mycursor = bantudb.cursor()
mycursor.execute("use `bantu-hr-db`;")

def viewDepartment():
      mycursor.execute("SELECT * FROM `bantu-hr-db`.department;")
      for dep in mycursor:
            print(dep)
      bantudb.close()

def addDepartment(dep_id, dep_name, par_dep):
      mycursor.execute( """INSERT INTO department (Department_id, Department_name, Parent_Department) 
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
      mycursor.execute( "DELETE FROM Department WHERE Department_id=%s", (dep_id))
      bantudb.commit()
      print("Department Deleted Successfully!")
      viewDepartment()

# addDepartment(112, 'ZX', 'XZ')
#editDepartment(12, 'AS', 'TU')
# deleteDepartment(12)
