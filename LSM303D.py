#addresses and commands for LSM303D angular rate sensor
#for more information see datasheet at http://www.pololu.com/file/download/LSM303D.pdf?file_id=0J703
from smbus import SMBus

#registers, addresses
adr = 0x1D		#I2C address of LSM303D
who = 0x0F		#who_am_I -- 01001001 -- 49

a_xlo = 0x28		#out_x_l_a
a_xhi = 0x29		#out_x_h_a
a_ylo = 0x2A		#out_y_l_a
a_yhi = 0x2B		#out_y_h_a
a_zlo = 0x2C		#out_z_l_a
a_zhi = 0x2D		#out_z_h_a

m_xlo = 0x08		#out_x_l_m
m_xhi = 0x09		#out_x_h_m
m_ylo = 0x0A		#out_y_l_m
m_yhi = 0x0B		#out_y_h_m
m_zlo = 0x0C		#out_z_l_m
m_zhi = 0x0D		#out_z_h_m

ctrl0 = 0x1F	#
ctrl1 = 0x20	#ctrl_reg1 -- datarate, bandwidth, powerup/down, axes enabled
ctrl2 = 0x21	#ctrl_reg2 -- high pass filtering
ctrl3 = 0x22	#ctrl_reg3 -- interrupt, FIFO, etc
ctrl4 = 0x23	#ctrl_reg4 -- block, SPI, range
ctrl5 = 0x24	#ctrl_reg5 -- mag resolution, datarate, temp enable, latching
ctrl6 = 0x25	#ctrl_reg6 -- mag full-scale
ctrl7 = 0x26	#

#COMMANDS
#	Accelerometer
a_on = 0xA7		#power_on @ 1.6 kHz sampling, continuous update, 3 axes enabled @ ctrl1

a_FS_2g = 0x00	#Full scale & 773 Hz Anti-alias filter bandwidth @ ctrl2
a_FS_4g = 0x08	#^
a_FS_6g = 0x10	#^
a_FS_8g = 0x18	#^
a_FS_16g = 0x20	#^

#Magnetometer
m_on = 0x70		#power_on @ 100 Hz sampling, high magnetic resolution @ ctrl5

m_FS_2g = 0x00	#Full scale.  g = gauss. @ ctrl6
m_FS_4g = 0x20	#
m_FS_8g = 0x40	#
m_FS_12g = 0x60	#

#setup functions
def bus_init(ID = 1):		#ID = I2C bus ID (default 1)
	return SMBus(ID)	

def a_init(bus, a_FS = a_FS_8g):	#returns conversion factor = gain (output will be mille-g's)
	bus.write_byte_data(adr, ctrl1, a_on)
	bus.write_byte_data(adr, ctrl2, a_FS)
	if(a_FS == a_FS_8g):
		a_gain = 0.244
	elif(a_FS == a_FS_2g):
		a_gain = 0.061
	elif(a_FS == a_FS_4g):
		a_gain = 0.122
	elif(a_FS == a_FS_6g):
		a_gain = 0.183
	else:	#(a_FS_16g)
		a_gain = 0.732
	return a_gain		

def m_init(bus, m_FS = m_FS_4g):	#returns conversion factor = gain (output will be mille-gauss)
	bus.write_byte_data(adr, ctrl5, m_on)
	bus.write_byte_data(adr, ctrl6, m_FS)
	if(m_FS == m_FS_4g):
		m_gain = 0.160
	elif(m_FS == m_FS_2g):
		m_gain = 0.080
	elif(m_FS == m_FS_8):
		m_gain = 0.320
	else:	#(m_FS_12g)
		m_gain = 0.479
	return m_gain	


#read functions

def get_a(bus, a_gain):	#returns [a_x, a_y, a_z] (mg)
	a_x = 256 * bus.read_byte_data(adr,a_xhi) + bus.read_byte_data(adr,a_xlo)
	if(a_x >= 32768): a_x = a_x - 65536

	a_y = 256 * bus.read_byte_data(adr,a_yhi) + bus.read_byte_data(adr,a_ylo)
	if(a_y >= 32768): a_y = a_y - 65536

	a_z = 256 * bus.read_byte_data(adr,a_zhi) + bus.read_byte_data(adr,a_zlo)
	if(a_z >= 32768): a_z = a_z - 65536

	a_x = a_gain * a_x
	a_y = a_gain * a_y
	a_z = a_gain * a_z
	
	return [a_x, a_y, a_z]

def get_m(bus, m_gain):	#returns [m_x, m_y, m_z] (mgauss)
	m_x = 256 * bus.read_byte_data(adr,m_xhi) + bus.read_byte_data(adr,m_xlo)
	if(m_x >= 65536): m_x = m_x - 131072

	m_y = 256 * bus.read_byte_data(adr,m_yhi) + bus.read_byte_data(adr,m_ylo)
	if(m_y >= 65536): m_y = m_y - 131072

	m_z = 256 * bus.read_byte_data(adr,m_zhi) + bus.read_byte_data(adr,m_zlo)
	if(m_z >= 65536): m_z = m_z - 131072

	m_x = m_gain * m_x
	m_y = m_gain * m_y
	m_z = m_gain * m_z
	
	return [m_x, m_y, m_z]
