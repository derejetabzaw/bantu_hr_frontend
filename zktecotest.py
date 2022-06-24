
from fpmachine.devices import ZMM220_TFT
from fpmachine.models import UserInfo

dev = ZMM220_TFT("192.168.1.105", 4370, "latin-1")
def con():
    # create a device with ip, port and encoding
    
    dev.connect(0)
    print("connected")

def conn(ip):
    # create a device with ip, port and encoding
    dev.connect(0)
    print("connected")
    
def add_user(**kwargs):
    con()
    new_user = UserInfo("latin-1")
    new_user.name = kwargs['FullName']
    new_user.password = kwargs['password']
    new_user.person_id = kwargs['id'] #need to sync with database  , one or more checks need to be made and photo and the fingerprint record is not required
    dev.set_user(new_user)
ip = "192.168.1.105"

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
    

def get_users():
    con()
    userdata = {}
    username = {}
    id = []
    
    users = dev.get_users()
    for usr in users:
        userdata[usr.person_id] = [usr.name,usr.password]
    return userdata
    # user_data = []
    
    # id = []
    # users = dev.get_users()
    # for usr in users:
    #     user_data.append(usr.person_id)
    #     user_data.append(usr.name)
    #     user_data.append(usr.password)

get_users()
        
