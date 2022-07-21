import socket
import psycopg2
from datetime import datetime
import time

localIP = "10.223.204.201"
localPort = 7800
bufferSize = 1024

connection = psycopg2.connect("dbname=student user=postgres password=123")
cursor = connection.cursor()


UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))
print("Uspostavljena veza sa serverom.")
print("IP adresa: ", localIP)
print("Port: ", localPort)


while True:

    message, addr = UDPServerSocket.recvfrom((bufferSize))
    print("Primljena poruka: {0}".format(message))
    UDPServerSocket.sendto(b"ACK", addr)
    message = message.decode("ascii")
    command = message[0:2]
    print(command)
    if command == "02":
        ts = time.time()
        timestamp = datetime.datetime.fromtimestamp(ts).strftime("%d-%m-%Y %H:%M:%S")
        rf = message[2:4]
        device_id = message[4:19]
        report_id = message[19:23]
        car_status = message[23:25]
        sensor_value = message[25:29]
        temperature = message[29:33]
        retry_count = message[33:35]
        transit_seq_no = message[35:37]

        cursor.execute(
            """INSERT INTO car (command, rfqualitycode, imeiid, dataid, carstatusvalue, sensorvalue, temperaturevalue, retrycount, transitsequencenumber,input_datetime)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""",
            (
                command,
                rf,
                device_id,
                report_id,
                car_status,
                sensor_value,
                temperature,
                retry_count,
                transit_seq_no,
                timestamp,
            ),
        )
        if car_status == "00":
            print("Mjesto je slobodno.")
        else:
            print("Mjesto je zauzeto!")

        connection.commit()
    else:
        print("Nije primljena tražena poruka!")
