import time
import L3GD20 as g

bus = g.bus_init()
gain = g.gyro_init(bus)

while(1):
	rates = g.get_gyro(bus, gain)
	print rates(1) + '\t' + rates(2) + '\t' + rates(3)
	time.sleep(0.1)

