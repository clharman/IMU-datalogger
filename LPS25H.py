#addresses and commands for LPS25H barometer/altitude sensor
#for more information see datasheet at http://www.pololu.com/file/download/LPS25H.pdf?file_id=0J761
from smbus import SMBus

#registers, addresses
adr = 0x5D		#I2C address of LPS25H
r_p_xl = 0x08		#ref_p_xl
r_p_lo = 0x09		#ref_p_l
r_p_hi = 0x0A		#ref_p_h
who = 0x0F		#who_am_I -- 10111101 -- 0xBD
p_xl = 0x28		#press_out_xl
p_lo = 0x29		#press_out_l
p_hi = 0x2A		#press_out_h
t_lo = 0x2B		#temp_out_l
t_hi = 0x2C		#temp_out_h
ctrl1 = 0x20	#ctrl_reg1 -- datarate, bandwidth, powerdown
ctrl2 = 0x21	#ctrl_reg2 -- FIFO, I2C, boot
ctrl3 = 0x22	#ctrl_reg3 -- interrupt, drain
ctrl4 = 0x23	#ctrl_reg4 -- interrupt
temp = 0x26		#out_temp -- 2's complement temperature
yhi = 0x2B		#out_y_h
zlo = 0x2C		#out_z_l -- 2's complement z-axis angular rate
zhi = 0x2D		#out_z_h

#commands
on = 0xC0		#25hz updates	11000000
reset = 0x00	#reset ctrl2, ctrl3

p_gain = 1.0 / 4096.0
t_gain = 1.0 / 480.0

#setup functions
def bus_init(ID = 1):		#ID = I2C bus ID (default 1)
	return SMBus(ID)	

def p_init(bus):	#returns conversion factor / gain
	bus.write_byte_data(adr, ctrl1, on)
	bus.write_byte_data(adr, ctrl2, reset)

#read functions
def p_get(bus):	#returns press (hPa)
	press = 65536 * bus.read_byte_data(adr, p_hi) + 256 * bus.read_byte_data(adr, p_lo) + bus.read_byte_data(adr, p_xl)
	press = p_gain * press
	return press

def t_get(bus):	#returns temp (deg C)
	temp = 256 * bus.read_byte_data(adr,t_hi) + bus.read_byte_data(adr,t_lo)
	temp = t_gain * temp
	return temp
