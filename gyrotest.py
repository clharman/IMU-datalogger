import time
import L3GD20 as g
import lowpass as lp

bus = g.bus_init()
gain = g.w_init(bus)
last = 0

while(1):
	rates = g.w_get(bus, gain)

	print str(rates[0]) +'\t' + '\t' + str(lp.simple(rates[0], last))
	last = rates[0]
	time.sleep(0.05)

