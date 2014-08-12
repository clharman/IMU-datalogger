import time
import L3GD20 as g
import lowpass as lp

bus = g.bus_init()
gain = g.w_init(bus)
last = 0
xcache = []
ycache = []
zcache = []

for x in xrange(0,100):
	rates = g.w_get(bus, gain)
	xcache.append(rates[0])
	ycache.append(rates[1])
	zcache.append(rates[2])
	time.sleep(0.001)

x0 = sum(xcache) / float(len(xcache))
y0 = sum(ycache) / float(len(ycache))
z0 = sum(zcache) / float(len(zcache))

while(1):
	rates = g.w_get(bus, gain, x0, y0, z0)

	print str(rates[0]) +'\t' + str(rates[1]) + '\t' + str(rates[2])
	time.sleep(0.05)

