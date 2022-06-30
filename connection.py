import mysql.connector as mysql
from datetime import date
from pymysql import MySQLError
# from tabulate import tabulate

# Change the below config code to make it connect with your database
# Change the user and password with your mysql configuration
config = {
    "host": "localhost",
    "user": "root",
    "database": "bantu-hr-db",
    "password": 'wutangclan',
    # "password": "Sa@654321",
    "port": 3306,
    "auth_plugin": "mysql_native_password",
}

try:
    bantudb = mysql.connect(**config)
    print("Connection Opened Successfully!")
    try:
        mycursor = bantudb.cursor()
        mycursor.execute("use `bantu-hr-db`;")

        def viewDepartment():
            mycursor.execute(
                "SELECT * FROM Department ORDER BY Department_Id;")
            # Get all records
            records = mycursor.fetchall()
            # REMOVE LINE 30 - 41, Later while cleaning code
            # Print the number of Rows
            # count = mycursor.rowcount
            # print("Number of Rows: ", count)
            # # Print each row
            # tableData = tabulate(
            #     records,
            #     headers=["Department_Id", "Department_name", "Parent_Department"],
            #     tablefmt="fancy_grid",
            # )
            # print(tableData)

            return records

        def addDepartment(dep_id, dep_name, par_dep):
            mycursor.execute(
                """INSERT INTO Department (Department_id, Department_name, Parent_Department)
                                    VALUES (%s, %s, %s)""",
                (dep_id, dep_name, par_dep),
            )
            bantudb.commit()
            print("Department Added Successfully!")
            viewDepartment()

        def editDepartment(dep_id, dep_name, par_dep):
            mycursor.execute(
                """UPDATE Department SET Department_name=%s, Parent_Department=%s
                                          WHERE Department_id=%s""",
                (dep_name, par_dep, dep_id),
            )
            bantudb.commit()
            print("Department Updated Successfully!")
            viewDepartment()

        def deleteDepartment(dep_id):
            mycursor.execute(
                "DELETE FROM Department WHERE Department_id=%s", (dep_id,))
            bantudb.commit()
            print("Department Deleted Successfully!")
            viewDepartment()

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
                """INSERT INTO personel
                  (personel_id,devicePersonel_id,Gender,Department,Employee_type,Employment_date,full_name,job_title,paygrade,image,fingerprint)
                              VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)""",
                (
                    personel["personel_id"],
                    personel["devicePersonel_id"],
                    personel["Gender"],
                    personel["Department"],
                    personel["Employee_type"],
                    personel["Employment_date"],
                    personel["full_name"],
                    personel["job_title"],
                    personel["paygrade"],
                    personel["image"],
                    personel["fingerprint"],
                ),
            )
            bantudb.commit()
            print("Personnel Added Successfully!")

        def viewPersonel():
            mycursor.execute(
                "SELECT personel_id, full_name, fingerprint FROM personel;")
            # Get all records
            records = mycursor.fetchall()

            return records

        def fingerprint_device_id():
            finger_print = {}
            mycursor.execute(
                "SELECT devicePersonel_id ,fingerprint FROM personel where fingerprint = 0;"
            )
            for temp in mycursor:
                finger_print[temp[0]] = temp[1]

            return finger_print

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

    except Exception as e:
        print("MySQL Query Error!")

    # finally:
    #       if bantudb.is_connected():
    #             bantudb.close()
    #             print("Connection Closed Successfully!")

except Exception as e:
    print("MySQL Error! Cannot Connect to the Database.")
