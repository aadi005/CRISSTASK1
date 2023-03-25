import socket

serverIP = "172.17.29.11"

serverPORT = 6000

serveraddress = (serverIP,serverPORT)

bufferSize = 1024

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

message = "HI My name is Aaditya Goel 2022B3PS0417P"

bytesToSend = str.encode(message)
UDPClientSocket.sendto(bytesToSend, serveraddress)


for i in message:
    bytesToSend = str.encode(i)
    UDPClientSocket.sendto(bytesToSend, serveraddress)
