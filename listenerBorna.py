import socket

UDP_IP="10.223.204.201"
UDP_PORT=7800
#self.transport.getHandle().setsockopt(socket.SOL_SOCKET, 25, "ens192")
sock = socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.bind((UDP_IP,UDP_PORT))
msg=b"Hello"
while True:
    data, addr=sock.recvfrom(1024)
    print("Poruka: {}".format(data))
    sock.sendto(msg,addr)