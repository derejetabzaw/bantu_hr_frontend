from fpmachine.devices import ZMM220_TFT
from fpmachine.models import UserInfo



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
    new_user.person_id = kwargs[
        "id"
    ]  # need to sync with database  , one or more checks need to be made and photo and the fingerprint record is not required
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
