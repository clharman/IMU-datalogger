import time
import LSM303D as m
import lowpass as lp

bus = m.bus_init()
a_gain = m.a_init(bus)
gain = m.m_init(bus)
last = [0,0,0]

while(1):
	mag = m.m_get(bus, gain)

	print str(round(lp.simple(mag[0], last[0])/1000,2)) + '\t' + str(round(lp.simple(mag[1], last[1])/1000,2)) + '\t' + '\t' + str(round(lp.simple(mag[2], last[2])/1000,2))
	last = mag
	time.sleep(0.1)
