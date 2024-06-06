# https://microcontrollerslab.com/dc-motor-l298n-driver-raspberry-pi-pico-tutorial/
# using L298N

from machine import Pin, PWM
from time import sleep

IN1 = Pin(1, Pin.OUT)
IN2 = Pin(2, Pin.OUT)

speed = PWM(Pin(3))
speed.freq(1000)


speed.duty_u16(10000)
IN1.low()  #spin forward
IN2.high()
sleep(2)

IN1.low()  #stop
IN2.low()
sleep(1)

speed.duty_u16(20000)
IN1.high()  #spin backward
IN2.low()
sleep(2)

IN1.low()  #stop
IN2.low()
sleep(1)

speed.duty_u16(30000)
IN1.low()  #spin forward
IN2.high()
sleep(2)

IN1.low()  #stop
IN2.low()
sleep(1)

speed.duty_u16(40000)
IN1.high()  #spin backward
IN2.low()
sleep(2)

IN1.low()  #stop
IN2.low()
sleep(1)

