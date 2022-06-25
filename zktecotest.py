from fpmachine.devices import ZMM220_TFT
from fpmachine.models import UserInfo, MachineState
import pandas as pd
import numpy as np


ip = "192.168.1.105"
dev = ZMM220_TFT(ip, 4370, "latin-1")


def con():
    # create a device with ip, port and encoding
    dev.disconnect()
    dev.connect(0)
    print("connected")


def add_user(**kwargs):
    con()
    new_user = UserInfo("latin-1")
    new_user.name = kwargs["FullName"]
    new_user.password = kwargs["password"]
    new_user.person_id = kwargs["id"]

    dev.set_user(new_user)


def delete_user(userId):
    con()
    dev.del_user(userId)
    print("User Deleted Successfully")


# delete_user(ip, 1)


def device_info():
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


# device_info()


def restartDevice():
    con()
    dev.reboot()


# restartDevice()


def shutdownDevice():
    con()
    dev.shutdown()


def get_users():
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


def get_user_id():
    con()
    device_user_count = 0
    id = []
    if MachineState().user_count == 0:
        return device_user_count
    else:
        users = dev.get_users()
        for user in users:
            id.append(user.person_id)
        return int(id[len(id)-1])

        #users = dev.get_users()


def handleCSV_Import(data_path):
    index = get_user_id()
    full_data = pd.read_csv(data_path)
    isolated_data = full_data['name'].to_list()
    for data in isolated_data:
        index += 1
        add_user(FullName=data, password='', id=str(index))


def get_finger_print(user_id):
    con()
    fps = dev.get_fps()
    for fp in fps:
        if(int(fp.user_id) == user_id):
            pass


# get_finger_print()
print(get_user_id())
