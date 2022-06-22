
from fpmachine.devices import ZMM220_TFT

def con():
    # create a device with ip, port and encoding
    dev = ZMM220_TFT("192.168.1.105", 4370, "latin-1")
    dev.connect(0)
    print("connected")

def conn(ip):
    # create a device with ip, port and encoding
    dev = ZMM220_TFT(ip, 4370, "latin-1")
    dev.connect(0)
    print("connected")
