from machine import Pin
from time import sleep
sensora = Pin(13, Pin.IN)
sensorb = Pin(15, Pin.IN)
sensorx = Pin(20, Pin.IN)
sensory = Pin(17, Pin.IN)
ledbg = Pin(21, Pin.OUT)
ledbr = Pin(14, Pin.OUT)
ledar = Pin(16, Pin.OUT)
ledag = Pin(18, Pin.OUT)
while True:
    if(sensora.value() == 0):
        while(sensorb.value() == 1):
            if(sensorb.value() == 0):
                #while sensora.value() == 0 and sensorb.value()==0:
                    ledbr.value(1)
                    ledbg.value(0)
                    ledar.value(0)
                    ledag.value(1)
                    sleep(5)
                    break
        ledbr.value(0)
        ledag.value(0)
    elif(sensorb.value() == 0):
        while(sensora.value() == 1):
            if(sensora.value() == 0):
                #while sensora.value() == 0 and sensorb.value()==0:
                    ledbg.value(1)
                    ledbr.value(0)
                    ledar.value(1)
                    ledag.value(0)
                    sleep(5)
                    break
        ledbg.value(0)
        ledar.value(0)
    elif(sensorx.value() == 0):
       while(sensory.value() == 1):
            if(sensory.value() == 0):
                #while sensorx.value() == 0 and sensory.value()==0:
                    ledag.value(0)
                    ledar.value(1)
                    ledbr.value(0)
                    ledbg.value(1)
                    sleep(5)
                    break
       ledbg.value(0)
       ledar.value(0)
    elif(sensory.value() == 0):
        while(sensorx.value() == 1):
            if(sensorx.value() == 0):
                #while sensorx.value() == 0 and sensory.value()==0:
                    ledag.value(1)
                    ledar.value(0)
                    ledbg.value(0)
                    ledbr.value(1)
                    sleep(5)
                    break
        ledag.value(0)
        ledbr.value(0)
    else:
        ledbr.value(0)
        ledbg.value(0)
        ledar.value(0)
        ledag.value(0)