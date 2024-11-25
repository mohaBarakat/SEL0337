import time
import gpiozero

led_pin = 2

led_red = gpiozero.LED(led_pin)

while(True):
	led_red.on()
