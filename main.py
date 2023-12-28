from machine import Pin
import time

led = Pin('LED', Pin.OUT)  # Pico W では、内蔵LEDの指定はGPIO番号ではなく"LED"を指定

while True:
    led.on()
    time.sleep(0.1)
    led.off()
    time.sleep(0.5)
