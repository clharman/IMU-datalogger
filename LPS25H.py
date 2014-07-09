#addresses and commands for LPS25H barometer/altitude sensor
#for more information see datasheet at http://www.pololu.com/file/download/LPS25H.pdf?file_id=0J761
from smbus import SMBus

#registers, addresses
adr = 0x5D		#I2C address of LPS25H
rpxl = 0x08		#ref_p_xl
rplo = 0x09		#ref_p_l
rphi = 0x0A		#ref_p_h
who = 0x0F		#who_am_I -- 10111101 -- 0xBD
pxl = 0x08		#press_out_xl
plo = 0x09		#press_out_l
phi = 0x0A		#press_out_h
tlo = 0x2B		#temp_out_l
thi = 0x2C		#temp_out_h
ctrl1 = 0x20	#ctrl_reg1 -- datarate, bandwidth, powerdown
ctrl2 = 0x21	#ctrl_reg2 -- FIFO, I2C, boot
ctrl3 = 0x22	#ctrl_reg3 -- interrupt, drain
ctrl4 = 0x23	#ctrl_reg4 -- interrupt
temp = 0x26		#out_temp -- 2's complement temperature
yhi = 0x2B		#out_y_h
zlo = 0x2C		#out_z_l -- 2's complement z-axis angular rate
zhi = 0x2D		#out_z_h

#commands
on = 0xA0		#7hz updates
reset = 0x00	#reset ctrl2, ctrl3

pgain = 1.0 / 4096.0
tgain = 1.0 / 480.0

#setup functions
def bus_init(ID = 1):		#ID = I2C bus ID (default 1)
	return SMBus(ID)	

def alt_init(bus):	#returns conversion factor / gain
	bus.write_byte_data(adr, ctrl1, on)
	bus.write_byte_data(adr, ctrl2, reset)

#read functions
def get_alt_raw(bus):		#returns raw values of [pxl, plo, phi, tlo, thi]
	raws = [bus.read_byte_data(adr,pxl), bus.read_byte_data(adr,plo), bus.read_byte_data(adr,phi), bus.read_byte_data(adr,tlo), bus.read_byte_data(adr,thi)]
	return raws

def get_alt(bus):	#returns [press, temp] (hPa, dec C)
	press = 65536 * bus.read_byte_data(adr, phi) + 256 * bus.read_byte_data(adr, plo) + bus.read_byte_data(adr, pxl)
	temp = 256 * bus.read_byte_data(adr,thi) + bus.read_byte_data(adr,tlo)


	press = pgain * press
	temp = tgain * temp
	
	return [press, temp]
