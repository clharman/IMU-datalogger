#addresses and commands for L3GD20 angular rate sensor
#for more information see datasheet at http://www.pololu.com/file/download/L3GD20.pdf?file_id=0J563
from smbus import SMBus



#registers, addresses
adr = 0x6B		#I2C address of L3GD20
who = 0x0F		#who_am_I -- 11010100 -- D4
ctrl1 = 0x20	#ctrl_reg1 -- datarate, bandwidth, powerdown, axes enabled
ctrl2 = 0x21	#ctrl_reg2 -- high pass filtering
ctrl3 = 0x22	#ctrl_reg3 -- interrupt, FIFO, etc
ctrl4 = 0x23	#ctrl_reg4 -- block, SPI, range
ctrl5 = 0x24	#ctrl_reg5 -- boot, FIFO, etc
temp = 0x26		#out_temp -- 2's complement temperature
xlo = 0x28		#out_x_l -- 2's complement x-axis angular rate
xhi = 0x29		#out_x_h
ylo = 0x2A		#out_y_l -- 2's complement y-axis angular rate
yhi = 0x2B		#out_y_h
zlo = 0x2C		#out_z_l -- 2's complement z-axis angular rate
zhi = 0x2D		#out_z_h

#commands
on = 0x0F		#
dps_250 = 0x00	#
dps_500 = 0x10	#
dps_2000 = 0x20	#

#setup functions
def bus_init(ID = 1):		#ID = I2C bus ID (default 1)
	return SMBus(ID)	

def gyro_init(bus, dps = dps_250):	#returns conversion factor / gain
	bus.write_byte_data(adr, ctrl1, on)
	bus.write_byte_data(adr, ctrl4, dps)
	if(dps == dps_250):
		gain = 0.00875
	elif(dps == dps_500):
		gain = 0.01750
	else:
		gain = 0.070
	return gain

#read functions
def get_gyro_raw(bus):		#returns raw values of [xlo, xhi, ylo, yhi, zlo, zhi]
	raws = [bus.read_byte_data(adr,xlo), bus.read_byte_data(adr,xhi), bus.read_byte_data(adr,ylo), bus.read_byte_data(adr,yhi), bus.read_byte_data(adr,zlo), bus.read_byte_data(adr,zhi)]
	return raws

def get_gyro(bus, gain):	#returns [wx, wy, wz] (degrees/s)
	wx = 256 * bus.read_byte_data(adr,xhi) + bus.read_byte_data(adr,xlo)
	if(wx >= 37268): wx = wx - 74536

	wy = 256 * bus.read_byte_data(adr,yhi) + bus.read_byte_data(adr,ylo)
	if(wy >= 37268): wy = wy - 74536

	wz = 256 * bus.read_byte_data(adr,yhi) + bus.read_byte_data(adr,ylo)
	if(wz >= 37268): wz = wz - 74536

	wx0 = 0 	#zero-level rates for later use in algorithms
	wy0 = 0
	wz0 = 0

	wx = gain * (wx - wx0)
	wy = gain * (wy - wy0)
	wz = gain * (wz - wz0)
	
	return [wx, wy, wz]

