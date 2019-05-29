#SIM900+Raspberry
import serial
import RPi.GPIO as GPIO
import os , time

GPIO.setmode(GPIO.BOARD)

#Enable SErial Communication
ser=serial.Serial("/dev/ttyS0",baudrate=9600,timeout=1)

#Transmitting AT commands to the Modem '\r\n' indicates the Enter Key

ser.write('AT'+'\r\n')
rcv=ser.read(10)
print(rcv)
time.sleep(1)

#Verify wather the SiM card is ready
ser.write("AT+CPIN?\r")
msg=ser.read(128)
print(msg)
time.sleep(3)

#SHUT all existing communication
ser.write("AT+CIPSHUT\r")
msg=ser.read(128)
print(msg)
time.sleep(3)

#configures the device for a single IP connection
ser.write("AT+CIPMUX=0\r")
msg=ser.read(128)
print(msg)
time.sleep(3)

#Activate GPRS service
#ser.write("AT+CIPMUX=0\r")
#msg=ser.read(128)
#print(msg)
#time.sleep(3)

#sets the PDP context parameters (APN of your phone ope)
command="AT+CGDCONT=1"+","+'"IP"'+","+"'internet.ooredoo.tn'\r" 
ser.write(command.encode())
msg=ser.read(128)
print(msg)
time.sleep(3)

#connect to GPRS with APN=yours phone ope usernme="" and password=""
ser.write('AT+CSTT="internet.ooredoo.tn","",""\r')
msg=ser.read(128)
print(msg)
time.sleep(3)




























