from BoardTemp import Board_temp as Bt
from FPGA_Work import FPGA_
from UART import Uart_CONN as Conn

BoardTemp = Bt().read_temp() # 0 : error Data
Working_check = FPGA_().FPGA_Check() # 0 : close , 1 : open, 2 : error
ENVTEMP,Pressure = Conn().RS485READ() # 0 : error Data

Conn().RS232WRITE(BDTEMP=BoardTemp,ENVTEMP=ENVTEMP,PRESSURE=Pressure,FPGAWORKING=Working_check)

