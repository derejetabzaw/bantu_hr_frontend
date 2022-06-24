
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
    new_user = UserInfo("latin-1")
    new_user.name = kwargs['FullName']
    new_user.password = kwargs['password']
    new_user.person_id = kwargs['id'] #need to sync with database  , one or more checks need to be made and photo and the fingerprint record is not required
    dev.set_user(new_user)
