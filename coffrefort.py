from time import *
from gpiozero import RotaryEncoder, RGBLED, Button
from signal import pause
import random

rotor = RotaryEncoder(17, 27)
button = Button(22)
led = RGBLED(red=10, green=9, blue=11)
led.color = (1, 0, 0)

counter = 0

code = [0, 0, 0, 0]
inputs = []
index = 0

for i in range(len(code)):
    code[i] = random.randint(-30,30)

print("Code: ", code)

print("Ready ?\n\nTry to find numbers between -30 and 30 !\nThere are 4 numbers to find !\n\nColors:\nGreen: Correct number\nRed: Wrong number\nBlue: Wrong number but close to the correct one\nYellow: You have opened the safe !\n\n")

def rotatedRight():
    global counter
    counter += 1
    if len(inputs) == len(code):
        led.color = (1, 1, 0.2)
        print("You have opened the safe !")
    elif counter < (code[index] - 10):
        led.color = (1, 0, 0)
    elif counter > (code[index] + 10):
        led.color = (1, 0, 0)
    elif counter == code[index]:
        led.color = (0, 1, 0)
    else :
        led.color = (0, 0, 1)
    print("Current Value: ", counter)

def rotatedLeft():
    global counter
    counter -= 1
    if len(inputs) == len(code):
        led.color = (1, 1, 0.2)
        print("You have opened the safe !")
    elif counter < (code[index] - 10):
        led.color = (1, 0, 0)
    elif counter > (code[index] + 10):
        led.color = (1, 0, 0)
    elif counter == code[index]:
        led.color = (0, 1, 0)
    else :
        led.color = (0, 0, 1)
    print("Current Value: ", counter)

def confirm():
    global index
    global counter
    global code
    
    if len(inputs) == len(code):
        led.color = (1, 1, 0.2)
        print("You have opened the safe !")
    elif counter == code[index]:
        led.color = (1, 0, 0)
        print("Your Input: ", counter)
        print("Correct Guess !")
        inputs.append(counter)
        print('Your inputs: ', inputs)
        index += 1

        if len(inputs) == len(code):
            led.color = (1, 1, 0.2)
            print("You have opened the safe !")
    elif counter != code[index]:
        led.color = (1, 0, 0)
        print("Your Input: ", counter)
        print("Incorrect Guess !\nTry again !")
    

rotor.when_rotated_clockwise = rotatedLeft

rotor.when_rotated_counter_clockwise = rotatedRight

button.when_pressed = confirm

pause()