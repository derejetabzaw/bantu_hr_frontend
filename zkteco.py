
# from socket import *
# soc = socket(AF_INET, SOCK_STREAM)
# soc.connect(('192.168.1.105', 4370))
# data = "ack"
# soc.send(data.encode())
# # with open("http-response.txt", "w") as respfile:
# response = soc.recv(1024)  # <--- Use select.epoll or asyncore instead!
# print(soc)
# print("connected", response.decode('latin-1') == '')

from fpmachine.devices import ZMM220_TFT

# create a device with ip, port and encoding
dev = ZMM220_TFT("192.168.1.105", 4370, "latin-1")
dev.connect(0)
users = dev.get_users()

id = 1
for item in users:
    print(item.id)
    print(item.name)
    print(item.password)

# print((dev.get_user_face(str(id))).decode())
# # print(list(users))

dev.reboot()
