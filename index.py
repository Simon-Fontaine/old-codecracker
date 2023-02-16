from time import *
from gpiozero import *
from signal import pause

print("Ready !")

led = LED(21)
btn1 = Button(20)

compteur = 0

def pressed1():
  global compteur
  if compteur == 0:
    print('LED Eteinte')
    led.off()
  elif compteur == 1:
    print('LED Allumée')
    led.on()
  elif compteur == 2:
    print('LED clignote')
    led.blink()
  elif compteur == 3:
    compteur = -1
  compteur += 1

btn1.when_pressed = pressed1

pause()