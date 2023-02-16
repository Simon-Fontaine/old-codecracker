from time import *
from gpiozero import *
from signal import pause


print("Ready !")

led = LED(21)
btn1 = Button(20)
btn2 = Button(16)
btn3 = Button(12)

def pressed1():
  print('LED Eteinte')
  led.off()

def pressed2():
  print('LED Allumée')
  led.on()

def pressed3():
  print('LED clignote')
  led.blink()


btn1.when_pressed = pressed1
btn2.when_pressed = pressed2
btn3.when_pressed = pressed3

pause()