from BoardTemp import Board_temp as Bt
from FPGA_Work import FPGA_
from UART import Uart_CONN as Conn
from ADC import MUX
import time

err_check = 0
while True:
    DSPEN,TRXPSEN,TRXCSEN,DC12VMNT,MNTIN,err_check = MUX().MUX_CHECK(outputV=0,limit=3.3,Err_check=err_check)
    err_check = err_check
    BoardTemp = Bt().read_temp() # 0 : error Data
    Working_check = FPGA_().FPGA_Check() # 0 : close , 1 : open, 2 : error
    ENVTEMP,Depth = Conn().RS485READ() # 0 : error Data

    Conn().RS232WRITE(DSPEN=DSPEN,TRXEN=TRXPSEN,TRXCSEN=TRXCSEN,DC12VMNT=DC12VMNT,MNTIN=MNTIN,BDTEMP=BoardTemp,ENVTEMP=ENVTEMP,DEPTH=Depth,FPGAWORKING=Working_check)

