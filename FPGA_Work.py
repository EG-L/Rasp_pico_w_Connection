from machine import Pin
import utime

while True:
    pin = Pin(9,mode=Pin.IN)
    try:
        if pin.value() == 0:
            print('Close')
        else:
            print('Open')
    except:
        print('Error')
    utime.sleep(0.1)

