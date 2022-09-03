import mysql.connector as mysql
# from datetime import date
# import datetime
# from pymysql import MySQLError
import itertools

#from zktecotest import sync_finger_print

# from tabulate import tabulate

# Change the below config code to make it connect with your database
# Change the user and password with your mysql configuration
config = {
    "host": "localhost",
    "user": "root",
    "database": "bantu-hr-db",
     "password": 'wutangclan',
    #"password": "Sa@654321",
    "port": 3306,
    "auth_plugin": "mysql_native_password",
}

try:
    bantudb = mysql.connect(**config)
    print("Connection Opened Successfully!")
    try:
        mycursor = bantudb.cursor()
        mycursor.execute("use `bantu-hr-db`;")

      

        # def editDepartment(dep_id, dep_name, par_dep):
        #     mycursor.execute(
        #         """UPDATE Department SET Department_name=%s, Parent_Department=%s
        #                                   WHERE Department_id=%s""",
        #         (dep_name, par_dep, dep_id),
        #     )
        #     bantudb.commit()
        #     print("Department Updated Successfully!")
        #     viewDepartment()

        def deleteDepartment(dep_id):
            mycursor.execute(
                "DELETE FROM Department WHERE Department_id=%s", (dep_id,))
            bantudb.commit()
            print("Department Deleted Successfully!")
            # viewDepartment()

        def get_departments():
            sql = "select Department_name from Department"
            cursor = mycursor.execute(sql)
            department_names = mycursor.fetchall()
            bantudb.commit()
            return list(itertools.chain(*department_names))


        def viewAreas():
            mycursor.execute("SELECT * FROM Areas;")
            for temp in mycursor:
                print(temp)

        def addAreas(area_id, area_code, area_name, par_area, remark):
            mycursor.execute(
                """INSERT INTO areas (areaId, areaCode, areaName, parentArea, remarks)
                                    VALUES (%s, %s, %s, %s, %s)""",
                (area_id, area_code, area_name, par_area, remark),
            )
            bantudb.commit()
            print("Area Added Successfully!")
            viewAreas()

        def addPersonel(**personel):
            mycursor.execute(
                """INSERT INTO personelInfo
                  (employeeCode, full_name, birthDate, birthPlace, bloodType, gender, religion, maritalStatus, employmentType, drivingLicenceGrade, remarks,image, hiredDate, payrollType, contractEndDate, position, _member, location, station, orgUnit, subOffice, supervisorPosition, supervisorName,sciGrade, salary, accountNumber, bankArea, natureOfAssignment, projectAttachement, taxCode, pensionCode, _status)
                              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                              %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                              %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    personel["employeeCode"],
                    personel["full_name"],
                    personel["birthDate"],
                    personel["birthPlace"],
                    personel["bloodType"],
                    personel["gender"],
                    personel["religion"],
                    personel["maritalStatus"],
                    personel["employmentType"],
                    personel["drivingLicenceGrade"],
                    personel["remarks"],
                    personel["image"],
                    personel["hiredDate"],
                    personel["payrollType"],
                    personel["contractEndDate"],
                    personel["position"],
                    personel["_member"],
                    personel["location"],
                    personel["station"],
                    personel["orgUnit"],
                    personel["subOffice"],
                    personel["supervisorPosition"],
                    personel["supervisorName"],
                    personel["sciGrade"],
                    personel["salary"],
                    personel["accountNumber"],
                    personel["bankArea"],
                    personel["natureOfAssignment"],
                    personel["projectAttachement"],
                    personel["taxCode"],
                    personel["pensionCode"],
                    personel["_status"]
                ),
            )
            bantudb.commit()
            print("Personnel Info Added Successfully!")

        def viewPersonel():
            mycursor.execute(
                "SELECT personel_id, full_name, fingerprint FROM personel;")
            # Get all records
            records = mycursor.fetchall()

            return records

        def fingerprint_device_id():

            mycursor.execute(
                "SELECT devicePersonel_id FROM personel where fingerprint = 0;"
            )
            registeredusers = mycursor.fetchall()
            bantudb.commit()
            fp = list(itertools.chain(*registeredusers))
            print(fp)
            return fp

        def editPersonel(
            personel_id,
            Department,
            Employee_type,
            fingerprint,
            job_title,
            paygrade,
            image,
        ):
            mycursor.execute(
                """UPDATE personel
                                          SET Department=%s, Employee_type=%s, fingerprint=%s, job_title=%s, paygrade=%s, image=%s
                                          WHERE personel_id=%s""",
                (
                    Department,
                    Employee_type,
                    fingerprint,
                    job_title,
                    paygrade,
                    image,
                    personel_id,
                ),
            )
            bantudb.commit()
            print("Personel Updated Successfully!")
            viewPersonel()

        def editPersonelFingerprint(**personel):
            fp = personel["fingerprint"]
            deviceid = personel["devicePersonel_id"]
            sql = f"UPDATE personel SET fingerprint = {fp} WHERE devicePersonel_id = {deviceid}"
            mycursor.execute(sql)
            bantudb.commit()
            print("Fingerprint Updated Successfully!")
            viewPersonel()

        def deletePersonel(personel_id):
            mycursor.execute(
                "DELETE FROM personel WHERE personel_id=%s", (personel_id,)
            )
            bantudb.commit()
            print("Personel Deleted Successfully!")
            viewPersonel()

        def editAreas(area_id, area_name, par_area, remark):
            mycursor.execute(
                """UPDATE areas
                                          SET areaName=%s, parentArea=%s, remarks=%s
                                          WHERE areaId=%s""",
                (area_name, par_area, remark, area_id),
            )
            bantudb.commit()
            print("Area Updated Successfully!")
            viewAreas()

        def deleteAreas(area_id):
            mycursor.execute("DELETE FROM areas WHERE areaId=%s", (area_id,))
            bantudb.commit()
            print("Area Deleted Successfully!")
            viewAreas()

        def viewDevices():
            mycursor.execute("SELECT * FROM device;")
            for temp in mycursor:
                print(temp)

        def addDevice(
            deviceId, deviceName, serialNumber, ipAddress, portNumber, area_id
        ):
            # addDevice(**deviceId)
            mycursor.execute(
                """INSERT INTO device (deviceId, deviceName, serialNumber, ipAddress, portNumber, areaId)
                                    VALUES (%s, %s, %s, %s, %s, %s)""",
                (deviceId, deviceName, serialNumber,
                 ipAddress, portNumber, area_id),
            )
            bantudb.commit()
            print("Device Added Successfully!")
            viewDevices()

        def editDevice(deviceId, deviceName, ipAddress, portNumber, area_id):
            mycursor.execute(
                """UPDATE device
                                          SET deviceName=%s, ipAddress=%s, portNumber=%s, areaId=%s
                                          WHERE deviceId=%s""",
                (deviceName, ipAddress, portNumber, area_id, deviceId),
            )
            bantudb.commit()
            print("Device Updated Successfully!")
            viewDevices()

        def deleteDevice(deviceId):
            mycursor.execute(
                "DELETE FROM device WHERE deviceId=%s", (deviceId,))
            bantudb.commit()
            print("Device Deleted Successfully!")
            viewDevices()

        def add_holiday(*args):
            mycursor.execute(
                """INSERT INTO holiday (holiday_id, hoiday_name, min_unit, unit, round_off, symbol_in_report)
                                    VALUES (%s, %s, %s, %s, %s, %s)""",
                (args[0], args[1], args[2], args[3], args[4], args[5]),
            )
            bantudb.commit()
            print("holiday Added Successfully!")

        def viewMachines():
            mycursor.execute("SELECT * FROM machine;")
            # Get all records
            records = mycursor.fetchall()

            return records

        def viewMachinesByIP(machineId):
            mycursor.execute(
                f"SELECT ipAddress FROM machine WHERE machineNumber = {machineId} "
            )
            # Get all records
            record = mycursor.fetchone()

            return record[0]

        def addMachine(deviceName, serialNumber, ipAddress, portNumber, macAddress):
            # insert into machine (deviceName, serialNumber, ipAddress, portNumber) values ("Zkteco", "AZ76890Y", "192.168.1.200", 4370);
            mycursor.execute(
                """INSERT INTO machine (deviceName, serialNumber, ipAddress, portNumber, macAddress)
                                    VALUES (%s, %s, %s, %s, %s)""",
                (deviceName, serialNumber, ipAddress, portNumber, macAddress),
            )
            bantudb.commit()
            print("Machine Added Successfully!")
            viewMachines()

        def viewAttendance():
            mycursor.execute("SELECT * FROM attendance_log;")
            # Get all records
            records = mycursor.fetchall()

            for temp in records:
                print(temp)

            return records

        def attendance(devicePersonel_id, check_date, check_in, check_out, worked_hours):
            mycursor.execute(
                f"SELECT full_name FROM personel WHERE devicePersonel_id = {devicePersonel_id} "
            )
            full_name = mycursor.fetchone()

            mycursor.execute(

                """INSERT INTO attendance_log (devicepersonel, full_name, check_date, check_in, check_out, worked_hours)
                                    VALUES (%s, %s, %s, %s, %s, %s)""",
                (devicePersonel_id, full_name[0], check_date,
                 check_in, check_out, worked_hours),
            )

            bantudb.commit()
            viewAttendance()

    except Exception as e:
        print("MySQL Query Error!")

    def get_registered_users():
        sql = 'select devicePersonel_id from personel where fingerprint = 1'
        mycursor.execute(sql)
        registeredusers = mycursor.fetchall()
        bantudb.commit()
        out = list(itertools.chain(*registeredusers))
        return out
    #department operations
    def viewDepartment():
        #on the current logic this seems useless but keep in case requiremnent changes
        mycursor.execute(
            "SELECT * FROM Department ORDER BY Department_Id;")
        # Get all records
        records = mycursor.fetchall()

        return records

    def addDepartment(dep_id, dep_name, par_dep):
        mycursor.execute(
                """INSERT INTO Department (Department_id, Department_name, Parent_Department)
                                    VALUES (%s, %s, %s)""",
                (dep_id, dep_name, par_dep),
            )
        bantudb.commit()
        
    def get_top_level_parents():
        #this module is for getting departements with no parent i.e top level departments
        sql_query = "select DISTINCT Department_name from Department where Parent_Department is null"
        mycursor.execute(sql_query)
        department_names = mycursor.fetchall()
        department_names=(list(itertools.chain(*department_names)))
        bantudb.commit()
        if len(department_names) == 0:
            return 0
        else:
            return department_names
        
    def get_department_children(department):
        sql_query = f"select Department_name from Department where Parent_Department = '{department}'"
        mycursor.execute(sql_query)
        child_departments = mycursor.fetchall()
        return list(itertools.chain(*child_departments))
            
        


    # finally:
    #       if bantudb.is_connected():
    #             bantudb.close()
    #             print("Connection Closed Successfully!")

except Exception as e:
    print("MySQL Error! Cannot Connect to the Database.")

print(get_top_level_parents())