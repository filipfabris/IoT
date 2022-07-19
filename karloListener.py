import socket
    
UDP_IP = "10.223.204.201"
UDP_PORT = 7800
   
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))
   
print("pocelo slusanje") 
MESSAGE = "Bok"
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print("received message: %s" % data)
    sock.sendto(MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))
