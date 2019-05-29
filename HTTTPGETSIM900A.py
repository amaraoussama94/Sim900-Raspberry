import serial
import RPi.GPIO as gpio     
import os, time

gpio.setmode(gpio.BOARD)    

# Enable Serial Communication
port = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write(str.encode('AT'+'\r\n'))
rcv = port.read(10)
print (rcv)
time.sleep(1)

#Disable the Echo
port.write(str.encode('ATE0'+'\r\n'))
rcv=port.read(10)
print(rcv)
time.sleep(1)

#Verify wather the SiM card is ready
ser.write(str.encode("AT+CPIN?\r"))
msg=ser.read(128)
print(msg)
time.sleep(3)

#SHUT all existing communication
ser.write(str.encode("AT+CIPSHUT\r"))
msg=ser.read(128)
print(msg)
time.sleep(3)

#Configure bearer profile 1 
port.write(str.encode("AT+SAPBR=3,1,\"CONTYPE\",\"GPRS\""));  #Connection type GPRS 
rcv = port.read(128)
print (rcv)
time.sleep(3)

port.write(str.encode("AT+SAPBR=3,1,\"internet.ooredoo.tn\",\"\""));  # APN of the provider 
rcv = port.read(128)
print (rcv)
time.sleep(3)

port.write(str.encode("AT+SAPBR=1,1")); # Open GPRS context 
rcv = port.read(10)
print (rcv)
time.sleep(3)

port.write(str.encode("AT+SAPBR=2,1")); #Query the GPRS context 
rcv = port.read(128)
print (rcv)
time.sleep(3)

port.write(str.encode("AT+HTTPINIT"));  #Initialize HTTP service 
rcv = port.read(128)
print (rcv)
time.sleep(3)

port.write(str.encode("AT+HTTPPARA=\"CID\",1"));  #Set parameters for HTTP session 
rcv = port.read(128)
print (rcv)
time.sleep(3)
 
port.write(str.encode("AT+HTTPPARA=\"URL\",\"api.thingspeak.com/update\""));  # Set parameters for HTTP session */
rcv = port.read(10)
print (rcv)
time.sleep(3)

port.write(str.encode("AT+HTTPDATA=50,20000")); #POST data of size 50 Bytes with maximum latency time of 20seconds for inputting the data
rcv = port.read(128)
print (rcv)
time.sleep(3)
#Data to be sent
tmp=5
#buf = "A = %d\n , B= %s\n" % (a, b)

postUrl= "update?api_key=OFBYXE9CG5KMUKJD&field1=%f" %tmp
port.write(str.encode(postUrl))
rcv = port.read(128)
print (rcv)
time.sleep(3)
 
port.write(str.encode("AT+HTTPACTION=1"));  #Start POST session 
rcv = port.read(128)
print (rcv)
time.sleep(3)

port.write(str.encode("AT+HTTPTERM"));  #Terminate HTTP service 
rcv = port.read(10)
print (rcv)
time.sleep(3)

port.write(str.encode("AT+SAPBR=0,1")); #Close GPRS context 
rcv = port.read(128)
print (rcv)
time.sleep(3)
