import time
import LSM303D as a
import lowpass as lp

bus = a.bus_init()
gain = a.gyro_init(bus)
last = [0,0,0]

while(1):
	axl = a.get_a(bus, gain)

	print str(lp.simple(axl[0], last[0])) + '\t' + str(lp.simple(axl[1], last[1])) + '\t' + str(lp.simple(axl[2], last[2]))
	last = axl
	time.sleep(0.1)