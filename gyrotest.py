import time
import L3GD20 as g

bus = g.bus_init()
gain = g.gyro_init(bus)

while(1):
	rates = g.get_gyro(bus, gain)
	print str(rates[0]-4.2) +'\t'+ '\t' + str(rates[1]-1.3) +'\t'+ '\t' + str(rates[2]-1.3)
	time.sleep(0.1)

