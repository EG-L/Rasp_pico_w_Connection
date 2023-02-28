import utime
from machine import ADC,Pin
# pin = Pin(10,mode=Pin.OUT)
#pin.value(1)
# adc = ADC(2)
# print(adc.read_u16())
# utime.sleep(1)
# pin.value(0)
# adc = ADC(2)
# print(adc.read_u16())
class MUX:
    def __init__(self):
        self.SELA = 0
        self.SELB = 0
        self.SELC = 0
        self.DSPON = 1
        self.TRXON = 1
        self.TRXCON = 1
        
        self.Break_signal = 0
        
        Pin(10,mode=Pin.OUT,value=self.SELA)
        Pin(11,mode=Pin.OUT,value=self.SELB)
        Pin(12,mode=Pin.OUT,value=self.SELC)
        
        Pin(6,mode=Pin.OUT,value=self.DSPON)
        Pin(7,mode=Pin.OUT,value=self.TRXON)
        Pin(8,mode=Pin.OUT,value=self.TRXCON)
    
    def MUX_CHECK(limit=0):
        while True:
            MNT = ADC(26)
            MNTIN = adc.read_u16()
            if MNTIN>=limit:
                DSP = ADC(28)
                DSPEN = adc.read_u16()
                Pin(10,mode=Pin.OUT,value=1)
                TRXPSEN = adc.read_u16()
                
    
    def b_Sen(self,loc):
        return Pin(loc,mode=Pin.OUT,value=self.Break_signal)
