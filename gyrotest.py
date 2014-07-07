import time
import L3GD20

bus = bus_init()
gain = gyro_init(bus)

while(1):
	rates = get_gyro(bus, gain)
	print rates(1) + '\t' + rates(2) + '\t' + rates(3)
	time.sleep(0.1)

