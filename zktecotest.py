from cv2 import add
from fpmachine.devices import ZMM220_TFT

ip = "192.168.1.105"

def con():
    # create a device with ip, port and encoding
    # connection with device with ip
    dev = ZMM220_TFT("192.168.1.105", 4370, "latin-1")
    dev.connect(0)
    print("connected")


def delete_user(ip, userId):
    dev = ZMM220_TFT(ip, 4370, "latin-1")
    dev.connect(0)
    dev.del_user(userId)
    print("User Deleted Successfully")

# delete_user(ip, 1)

def device_info(ip):
    dev = ZMM220_TFT(ip, 4370, "latin-1")
    dev.connect(0)
    print("Connected")

    print("Device Time: ", dev.device_time)
    print("Build Version: ", dev.build_version)
    print("Camera Open: ", dev.camera_open == '1')
    print("Biometric type: ", dev.biometric_type)
    print("Face Version: ", dev.zk_face_version)
    print("Face Open: ", dev.face_fun_on == '1')
    print("Fingerprint Version: ", dev.fp_version)
    print("Fingerprint Open: ", dev.finger_fun_on == '1')
    print("Mac Address: ", dev.mac_address)
    print("Serial Number: ", dev.serial_number)
    print("Platform: ", dev.platform)
    print("Software Version: ", dev.software_version)
    print("Vendor: ", dev.vendor)
    

# device_info(ip)