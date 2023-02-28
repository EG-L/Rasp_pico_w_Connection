import utime
from machine import I2C,Pin
import struct

class Board_temp:
    def __init__(self):
        self.i2c = I2C(0,sda=Pin(20),scl=Pin(21),freq=400000)
        self.TEMP = 'b'
        self.devices = self.i2c.scan()
        print(self.devices)
        
    def read_temp(self):
        while True:
            try:
#                 print(self.i2c.readfrom(self.devices[0],1))
                print('%s:%.1f'%('Celsius',struct.unpack(self.TEMP,self.i2c.readfrom(self.devices[0],1))[0]))
                print('%s:%.1f'%('Fahrenheit',struct.unpack(self.TEMP,self.i2c.readfrom(self.devices[0],1))[0]*9.0/5.0+32.0))
                utime.sleep(1)
            except:
                print('%s:%f'%('Celsius',0.0))
                utime.sleep(1)

Board_temp().read_temp()
                
