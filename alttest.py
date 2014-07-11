import time
import LPS25H as p

bus = b.bus_init()
p.p_init(bus)

while(1):
	alt_out = p.p_get(bus)
	print str(alt_out)
	time.sleep(0.1)
