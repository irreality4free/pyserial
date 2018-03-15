from time import sleep


from time import sleep
import serial
ser = serial.Serial('COM6', 9600) # Establish the connection on a specific port
counter = 32 # Below # 32 everything in ASCII is gibberish
    #marker     addr    id   data
#    marker      size    addr    addr    id  ver data        crc
p = "FF AE      00 0C   00      00      01  01  10 12       00 00"
p1= "FF AE      00 0C   00      00      03  01  10          00 00"


def pack2str(p):
    return " ".join(["%02x"%c for c in p])


def str2pack(s):
    # return bytes("".join([chr(eval("0x%s"%l)) for l in s.split()]),'utf-8')
    # return [chr(eval("0x%s"%l)) for l in s.split()]
    #return p1.split()
    return bytearray.fromhex(s)

print(str2pack(p1))
print(pack2str(str2pack(p1)))
ser.write(str2pack(p))
ser.write(str2pack(p))
# for x in str2pack(p1):
#     ser.write(str2pack(p))
# ser.write(p.encode('utf-8'))
#
while True:


      # Convert the decimal number to ASCII then send it to the Arduino
     # ser.write(counter)
     print(ser.readline()) # Read the newest output from the Arduino
     sleep(0.1) # Delay for one tenth of a second
