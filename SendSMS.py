#SIM900+Raspberry
import serial
import RPi.GPIO as GPIO
import os , time

GPIO.setmode(GPIO.BOARD)
#init  seriial port com "ttyS0" or "ttyAMA0 "
port=serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1)

#Transmitting AT Commands to the Modem 'r\n' indicates the Enter Key
#ser.write(str.encode('allon'))   or use ser.write(serialcmd.encode()) else error: unicode strings are not supported, please encode to bytes:
port.write(str.encode('AT\r\n'))
rcv=port.read(10)
print(rcv)
time.sleep(1)

#Disable the Echo
#port.write(str.encode('ATE0'+'\r\n'))
#rcv=port.read(10)
#print(rcv)
#time.sleep(1)

#select Message format as TEXT mode
port.write(str.encode('AT+CMGF=1\r\n'))
rcv=port.read(10)
print(rcv)
time.sleep(1)

#New  SMS Message Indications
port.write(str.encode('AT+CNMI=2,1,0,0,0\r\n'))
rcv=port.read(10)
print(rcv)
time.sleep(1)


#Sending a message to a particular Number(chose the Number phone you like to send SMS )

port.write(str.encode('AT+CMGS="25576469"\r\n'))
rcv=port.read(10)
print(rcv)

#Message text
port.write(str.encode('Hello User\r\n'))
rcv=port.read(10)
print(rcv)

#Enable to send SMS = ctrl+z
port.write(str.encode("\x1A"))
for i in range(10):
    rcv=port.read(10)
    print(rcv)
    
           

