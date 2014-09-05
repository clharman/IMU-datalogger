#balance on two points using two propellers across from eachother, divided by the axis of rotation

import motors
import LSM303D as accel
import time
import lowpass as lp

bus = accel.bus_init()
gain = accel.a_init(bus)

zero = motors.init()
#motors.test()

p_gain = 1.8
d_gain = 40

m1 = zero
m2 = zero
m3 = zero
m4 = zero
axl = [0,0,0,0,0];

time.sleep(2)

print('Go!')

for x in xrange(0,400):

	axl.insert(0, accel.a_get(bus, gain)[1]/1000)
	axl.pop()

	axl_filt = lp.simple(axl)

	dvt = deriv(axl)

	

	if axl_filt > 0.4: axl_filt = 0.4

	if dvt > 0.05: dvt = 0.05

	print(str(axl))
	m2 = zero + 1.3 + (axl_filt * p_gain) - dvt * d_gain
	m3 = zero + 1.3 - (axl_filt * p_gain) + dvt * d_gain

	motors.set_all(m1, m2, m3, m4)

	time.sleep(0.001)

motors.term()