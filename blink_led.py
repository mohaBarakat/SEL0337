import time
import gpiozero

led_pin = 2

led_red = gpiozero.LED(led_pin)

while(True):
	led_red.on()
	time.sleep(1)
	led_red.off()
	time.sleep(1)
