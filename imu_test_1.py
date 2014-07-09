import Adafruit_BBIO.ADC as ADC
import Adafruit_BBIO.PWM as PWM
import time

sensor_pin = 'P9_40'
led_pin = 'P9_14'
ADC.setup()
PWM.start(led_pin, 0)


while True:
	

	reading = ADC.read(sensor_pin)
	brightness = abs(reading-0.9)*70

	print reading
	#PWM.set_duty_cycle(led_pin, brightness)
	time.sleep(0.01)
	

