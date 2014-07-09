import time
import LPS25H as b

bus = b.bus_init()
b.alt_init(bus)

while(1):
	alt_out = b.get_alt(bus)
	print str(alt_out[0]) +'\t' + '\t' + str(alt_out[1])
	time.sleep(0.05)
