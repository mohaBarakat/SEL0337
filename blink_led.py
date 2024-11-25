import time
import gpiozero

# Definindo o GPIO
led_pin = 2

# Definindo o LED
led_red = gpiozero.LED(led_pin)

while(True):
	# Ligando e desligando o LED
	led_red.on()
	time.sleep(1)
	led_red.off()
	time.sleep(1)
