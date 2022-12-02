from calendar import c
from fpmachine.devices import ZMM220_TFT
from fpmachine.models import UserInfo
import pandas as pd
import connection as dbcon
from datetime import datetime


ip = "192.168.1.105"
dev = ZMM220_TFT(ip, 4370, "latin-1")


def con():
    # create a device with ip, port and encoding
    # dev = ZMM220_TFT("192.168.1.105", 4370, "latin-1")
    dev.disconnect()
    dev.connect(0)
    print("Connected")


def disconnect():
    
    dev.disconnect()
    print("Disconnected from: ", ip)


def connectByIp(ip):
    # create a device with ip, port and encoding
    dev = ZMM220_TFT(ip, 4370, "latin-1")
    dev.disconnect()
    dev.connect(0)
    print("Connected to: ", ip)

    return dev


def add_user(**kwargs):
    #adds user
    con()
    new_user = UserInfo("latin-1")
    new_user.name = kwargs["FullName"]
    new_user.person_id = kwargs["id"]

    dev.set_user(new_user)


def delete_user(userId):
    #deletes user
    con()
    dev.del_user(userId)
    print("User Deleted Successfully")





def device_info():

    #returns device information
    con()

    listInfo = [
        dev.device_time,
        dev.build_version,
        (dev.camera_open == "1"),
        dev.biometric_type,
        dev.zk_face_version,
        (dev.face_fun_on == "1"),
        dev.fp_version,
        (dev.finger_fun_on == "1"),
        dev.mac_address,
        dev.serial_number,
        dev.platform,
        dev.software_version,
        dev.vendor,
    ]
    return listInfo


def addMachine(ip):
    #adds machine
    con()
    port = 4370
    dbcon.addMachine(dev.platform, dev.serial_number,
                     ip, port, dev.mac_address)


def restartDevice():
    #restarts the device
    con()
    dev.reboot()


def get_users():
    #returns user list
    con()
    users = dev.get_users()

    userList = []
    for user in users:
        temp = []
        temp.append(user.person_id)
        temp.append(user.name)
        temp.append(user.password)

        userList.append(temp)
    return userList


# this only returns the last taken ID be sure to increment at addition of new user


def get_user_id():
    #returns user id
    con()
    inc = 0
    id = []
    try:
        users = dev.get_users()
        for user in users:
            id.append(user.person_id)

        return int(id[(int(len(id))) - 1])

    except:
        return 0

        # users = dev.get_users()


def handleCSV_Import(data_path):
    index = get_user_id()
    full_data = pd.read_csv(data_path)
    isolated_data = full_data["name"].to_list()
    isoalted_id_col = full_data["id"].tolist()
    itr = 0
    for data in isolated_data:
        index += 1
        add_user(FullName=data, password="", id=str(index))
        # dbcon.addPersonel(
        #     personel_id=isoalted_id_col[itr], devicePersonel_id=isoalted_id_col[itr], devicePersonel_id=index, Gender='Gender',)
        dbcon.addPersonel(
            personel_id=isoalted_id_col[itr],
            devicePersonel_id=index,
            Gender=None,
            Department=None,
            Employee_type=None,
            Employment_date=None,
            full_name=isolated_data[itr],
            job_title=None,
            paygrade=None,
            image=None,
            fingerprint=0,
        )
        itr += 1


# use get_fps() to get  information about all the finger prints on the device
def sync_finger_print():
    con()
    print("in callback")
    unregistered_finger_prints = dbcon.fingerprint_device_id()
    list_user = dev.get_fps()

    for data in list_user:
        print("data:", data.user_id)
        for device_fp in unregistered_finger_prints:
            print("data12:", data.user_id)
            print("unreg", device_fp)
            if (data.user_id == device_fp):
                print('list', device_fp)
                dbcon.editPersonelFingerprint(
                    fingerprint=1, devicePersonel_id=data.user_id
                )
                print("match found at ", data.user_id)


# this function is resource demanding
def attendance_logs(id):
    con()
    att = dev.get_att_logs()
    attendance_data = []
    for data in att:
        if(int(data.person_id) == id):
            attendance_data.append(data.att_time)
    return attendance_data


def time_diffrence(start, end):
    t1 = datetime.strptime(start, "%H:%M:%S")
    t2 = datetime.strptime(end, "%H:%M:%S")
    return t2-t1


def Sychronizing_attendance():
    registed_users = dbcon.get_registered_users()
    for id in registed_users:
        logs = attendance_logs(id)
        check_in, check_out = str(logs[0]), str(logs[1])
        check_in_time = check_in.split(" ")[1]
        date = check_in.split(" ")[0]
        check_out_time = check_out.split(" ")[1]

        worked_hours = time_diffrence(check_in_time, check_out_time)
        dbcon.attendance(id, date, check_in_time, check_out_time, worked_hours)

       # print("success")
        


