from machine import Pin, ADC, PWM, I2C  #importing PIN,ADC and PWM
from time import sleep#importing time   
import utime 
from ssd1306 import SSD1306_I2C
import framebuf
import freesans20
import writer

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
display = SSD1306_I2C(128, 64, i2c)

buz = Pin(13, Pin.OUT)
buz.value(0)
xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
# Defining motor pins

#OUT1  and OUT2
In1=Pin(15,Pin.OUT) 
In2=Pin(14,Pin.OUT)  
#EN_A=Pin(8,Pin.OUT)
EN_A=PWM(Pin(18))



#OUT3  and OUT4
In3=Pin(12,Pin.OUT)  
In4=Pin(11,Pin.OUT) 
EN_B=PWM(Pin(19))

  
# Defining frequency for enable pins
EN_A.freq(1500)
EN_B.freq(1500)
# Defining frequency for enable pins

# Forward
def move_forward():
    In1.high()
    In2.low()
    In3.low()
    In4.high()
    
# Backward
def move_backward():
    In1.low()
    In2.high()
    In3.high()
    In4.low()
    
   
#Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()

def alert():
    font = writer.Writer(display, freesans20)
    font.set_textpos(28, 0)
    font.printstring(str("ALERT!!!"))
    font.set_textpos(0, 20)
    font.printstring(str("OVER SPEED"))
    font.set_textpos(15,40)
    font.printstring(str("DETECTED"))
    display.show()
    display.fill(0)
    buz.value(1)
    sleep(0.5)
    buz.value(0)
def dealert():
    display.fill(0)
    display.show()
    buz.value(0)
while True:
    sleep(0.1)
    
    yValue = yAxis.read_u16()
    xValue = xAxis.read_u16()
    #print(yValue)
    #print(xValue)
    
    if yValue >= 32000 and yValue <= 34000 or xValue >= 32000 and xValue <= 34000:

        stop()
    
    if yValue >= 34000:
        duty_cycle = (((yValue-65535/2)/65535)*100)*2
        print("Move backward: Speed " + str(abs(duty_cycle)) + " %")
        if(abs(duty_cycle)) > 60.0:
            alert()
        else:
            dealert()
        #duty_cycle = ((yValue/65535)*100)*650.2
        EN_A.duty_u16(int(duty_cycle))
        EN_B.duty_u16(int(duty_cycle))
        move_backward()

        

    
    elif yValue <= 32000:
        duty_cycle = ((yValue-65535/2)/65535*100)*2
        print("Move Forward: Speed " + str(abs(duty_cycle)) + " %")
        if(abs(duty_cycle)) > 60.0:
            alert()
        else:
            dealert()
        #duty_cycle = abs(duty_cycle)*650.2
        EN_A.duty_u16(int(duty_cycle))
        EN_B.duty_u16(int(duty_cycle))
        move_forward()
       
       
    elif xValue < 32000:
        duty_cycle = (((xValue-65535)/65535)*100)
        print("Move Left: Speed " + str(abs(duty_cycle)) + " %")
        if(abs(duty_cycle)) > 60.0:
            alert()
        else:
            dealert()
        #duty_cycle = abs((duty_cycle)*650.25)

        EN_B.duty_u16(0)
        EN_A.duty_u16(int(duty_cycle))
        move_forward()


    elif xValue > 34000:
        duty_cycle = ((xValue-65535/2)/65535*100)*2
        print("Move Right: Speed " + str(abs(duty_cycle)) + " %")
        if(abs(duty_cycle)) > 60.0:
            alert()
        else:
            dealert()
        #duty_cycle = abs(duty_cycle)*650.2

        EN_B.duty_u16(int(duty_cycle))
        EN_A.duty_u16(0)
        move_forward()