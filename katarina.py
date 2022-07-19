import socket

UDP_IP = "10.223.204.201"
UDP_PORT = 7800
buffer_size = 1024

sock = socket.socket(socket.AF_INET,
                    socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("Server listening...")
#msg = "Hello world!"
while True:
    data, addr = sock.recvfrom(buffer_size)
    print("received message: %s " % data)
    #sock.sendto(str.encode(msg), (UDP_IP, UDP_PORT))
