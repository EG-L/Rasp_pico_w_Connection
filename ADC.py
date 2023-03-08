import time
from machine import ADC,Pin

class MUX:
    def __init__(self):
        self.SELA = 0
        self.SELB = 0
        self.SELC = 0
        self.DSPON = 1
        self.TRXON = 1
        self.TRXCON = 1
       
        self.sela = Pin(10,mode=Pin.OUT,value=self.SELA)
        self.selb = Pin(11,mode=Pin.OUT,value=self.SELB)
        self.selc = Pin(12,mode=Pin.OUT,value=self.SELC)
    
    def MUX_CHECK(self,outputV=0.0,limit=0.0,Err_check=0):#Err_check : 0 data_read, 1 err
        
        self.err_check = Err_check
        self.MNT = ADC(26)
        
        if self.err_check == 0:
            self.dspon = Pin(6,mode=Pin.OUT,value=self.DSPON)
            self.trxon = Pin(7,mode=Pin.OUT,value=self.TRXON)
            self.trxcon = Pin(8,mode=Pin.OUT,value=self.TRXCON)
            DSPEN = 0
            TRXPSEN = 0
            TRXCSEN = 0
            DC12VMNT = 0
            time.sleep(0.5)
            while True:
                self.MNTIN = (3.3/65536)*self.MNT.read_u16()
                if self.MNTIN>=outputV:
                    DATA = ADC(28)
                    DSPEN = (3.3/65536)*DATA.read_u16()
                    if DSPEN>=limit:
                        self.Break_DT()
                        DSPEN,TRXPSEN,TRXCSEN,DC12VMNT,self.err_check = 0,0,0,0,1
                        break
                    time.sleep(0.1)
                    Pin(10,mode=Pin.OUT,value=1)
                    TRXPSEN = (3.3/65536)*DATA.read_u16()
                    if TRXPSEN>=limit:
                        self.Break_DT()
                        DSPEN,TRXPSEN,TRXCSEN,DC12VMNT,self.err_check = 0,0,0,0,1
                        break
                    time.sleep(0.1)
                    DATA = ADC(27)
                    TRXCSEN = (3.3/65536)*DATA.read_u16()
                    if TRXCSEN>=limit:
                        self.Break_DT()
                        DSPEN,TRXPSEN,TRXCSEN,DC12VMNT,self.err_check = 0,0,0,0,1
                        break
                    Pin(11,mode=Pin.OUT,value=1)
                    time.sleep(0.1)
                    DC12VMNT = (3.3/65536)*DATA.read_u16()
                break #### 브레이크 들여쓰기 수정 필요
            
            return DSPEN,TRXPSEN,TRXCSEN,DC12VMNT,self.MNTIN,self.err_check
        else:
            while True:
                self.MNTIN = (3.3/65536)*self.MNT.read_u16()
                if self.MNTIN>=outputV:
                    break
                time.sleep(0.5)
            return 0,0,0,0,self.MNTIN,1
        
    def Break_DT(self):
        stop_dat = [self.dspon,self.trxon,self.trxcon]
        
        for i in stop_dat:
            i.value(0)
                
if __name__=='__main__':
    print(MUX().MUX_CHECK())
