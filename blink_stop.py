import time
import gpiozero

# Definindo o GPIO
led_pin = 2

# Definindo o LED
led_red = gpiozero.LED(led_pin)

while(True):
	# Manter o LED aceso
	led_red.on()
