import time
import LSM303D as a
import lowpass as lp

bus = a.bus_init()
gain = a.a_init(bus)
last = [0,0,0]

while(1):
	axl = a.get_a(bus, gain)

	print str(round(lp.simple(axl[0], last[0])/1000,2)) + '\t' + str(round(lp.simple(axl[1], last[1])/1000,2)) + '\t' + '\t' + str(round(lp.simple(axl[2], last[2])/1000,2))
	last = axl
	time.sleep(0.1)
