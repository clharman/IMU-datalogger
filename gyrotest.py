from smbus import SMBus
import time
adr = 0x6B
reg1 = 0x20
reg2 = 0x21
reg3 = 0x22
reg4 = 0x23

xlo = 0x28
xhi = 0x29

ylo = 0x2A
yhi = 0x2B

zlo = 0x2C
zhi = 0x2D

bus = SMBus(1)

bus.write_byte_data(adr, reg1, 0x0F)

while(1):
	print bus.read_byte_data(adr, xlo)
	time.sleep(0.1)

