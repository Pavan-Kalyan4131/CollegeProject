from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
import freesans20
import writer
from time import sleep
import dht 
#import time
i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

#from machine import Pin

#sensor = dht.DHT22(Pin(14))
sensor = dht.DHT11(Pin(15))
#led = Pin(16, Pin.OUT)
buz = Pin(14, Pin.OUT)
buz.value(0)
#led.value(0)
threshold_temp = 45
threshold_humid = 2
cnt = 0
while cnt < 10:
  try:
    sleep(2)
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()
    print('Temperature: %3.1f C' %temp)
    print('Humidity: %3.1f %%' %hum)
    if hum > threshold_humid:
        if temp < threshold_temp:
            #led.value(1)
            #display.text("ALERT!!!", 30, 0)
            font = writer.Writer(display, freesans20)
            #display.text("OVER FOG DETECTED", 0, 18)
            font.set_textpos(28, 0)
            font.printstring(str("ALERT!!!"))
            font.set_textpos(15, 20)
            font.printstring(str("OVER FOG"))
            font.set_textpos(15,40)
            font.printstring(str("DETECTED"))
            display.show()
            display.fill(0)
            #buz.value(1)
            sleep(0.5)
            buz.value(0)
            #led.value(0)
    else:
        #led.value(0)
        display.fill(0)
        buz.value(0)
  except OSError as e:
    print('Failed to read sensor.')
  cnt += 1