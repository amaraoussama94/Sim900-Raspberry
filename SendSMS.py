#SIM900+Raspberry
import serial
import RPi.GPIO as GPIO
import os , time


#init  seriial port com "ttyS0" ou "ttyAMA0 "
port=serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1)

#Transmitting AT Commands to the Modem 'r\n' indicates the Enter Key

port.write('AT'+'\r\n')
rcv=port.read(10)
print(rcv)
time.sleep(1)

#Disable the Echo
port.write('ATE0'+'\r\n')
rcv=port.read(10)
print(rcv)
time.sleep(1)

#select Message format as TEXT mode
port.write('AT+CMGF=1'+'\r\n')
rcv=port.read(10)
print(rcv)
time.sleep(1)

#New  SMS Message Indications
port.write('AT+CNMI=2,1,0,0,0'+'\r\n')
rcv=port.read(10)
print(rcv)
time.sleep(1)


#Sending a message to a particular Number(chose the Number phone you like to send SMS )

port.write('AT+CMGS="+21625576469"'+'\r\n')
rcv=port.read(10)
print(rcv)

#Message text
port.write('Hello User'+'\r\n')
rcv=port.read(10)
print(rcv)

#Enable to send SMS = ctrl+z
port.write("\x1A")
for i in range(10):
    rcv=port.read(10)
    print(rcv)
    
           

