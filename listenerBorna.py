#!/usr/bin/env python

################ UDP SERVER ################################

import socket

ip = '10.223.204.201'           # this is local host
port = 7800    # start port here

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    try:
        # server must bind to an ip address and port
        sock.bind((ip, port))
        print("Listening on Port:", port)
        break
    except Exception:
        print("ERROR: Cannot connect to Port:", port)
        port += 1

try:
    while True:
        message, addr = sock.recvfrom(1024)  # OK someone pinged me.
        print(f"received from {addr}: {message}")
        sock.sendto(b"ACK", addr)
except KeyboardInterrupt:
    pass
finally:
    sock.close()
