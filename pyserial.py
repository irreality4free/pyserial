from time import sleep
import serial
ser = serial.Serial('COM6', 9600) # Establish the connection on a specific port
counter = 32 # Below # 32 everything in ASCII is gibberish
p = "FF AE 00 0C AE 11 34 56 00 00"
# def make_packet():
#     pack = ""
#     pack += chr(0xff)+chr(0xae)
#     pack +=

def pack2str(p):
    return " ".join(["%x"%c for c in p])

def str2pack(s):
    return [chr(eval("0x%s"%l)) for l in s.split()]
ser.write(p.encode('utf-8'))#
while True:

     counter +=1
      # Convert the decimal number to ASCII then send it to the Arduino
     # ser.write(counter)
     print(pack2str(ser.readline())) # Read the newest output from the Arduino
     sleep(1) # Delay for one tenth of a second
     if counter == 255:
        counter = 32

# print(str(0x10))