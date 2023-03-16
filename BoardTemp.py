import utime
from machine import I2C,Pin
import struct

class Board_temp:
    def __init__(self):
        self.i2c = I2C(0,sda=Pin(20),scl=Pin(21),freq=400000)
        self.TEMP = 'b'
        self.devices = self.i2c.scan()
        
    def read_temp(self):
        while True:
            try:
                TEMPDAT = struct.unpack(self.TEMP,self.i2c.readfrom(self.devices[0],1))[0]
                print('%s:%.1f'%('Celsius',TEMPDAT))
                utime.sleep(0.1)
            except:
                TEMPDAT = 0
#                 print('%s:%f'%('Celsius',0.0))
                utime.sleep(0.1)
            break
        return TEMPDAT

if __name__=='__main__':
    Board_temp().read_temp()            
