from gpiozero import RotaryEncoder, RGBLED, Button
from signal import pause
from time import *
import random
import time

# Variables
code = [0, 0, 0, 0]
maxsteps = 30
inputs = []
index = 0

# Couleurs
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class ledcolors:
    YELLOW = (1, 1, 0.2)
    GREEN = (0, 1, 0) 
    BLUE = (0, 0, 1)
    RED = (1, 0, 0)
    OFF = (0, 0, 0)

# GPIO setup
rotor = RotaryEncoder(17, 27, max_steps=maxsteps)
led = RGBLED(red=10, green=9, blue=11)
button = Button(22)

# Génération du code
for i in range(len(code)):
    code[i] = random.randint(-maxsteps,maxsteps)

# Initialisation de la partie
print("Code: ", code)

print(f"""
{bcolors.HEADER}{bcolors.BOLD}Prêt ?{bcolors.ENDC}
Essaie de trouver {bcolors.BOLD}4{bcolors.ENDC} nombres entre {bcolors.UNDERLINE}-30 et 30{bcolors.ENDC} !

{bcolors.OKCYAN}Couleurs:{bcolors.ENDC}
{bcolors.OKGREEN}Vert:{bcolors.ENDC} Nombre correcte
{bcolors.FAIL}Rouge:{bcolors.ENDC} Nombre incorrecte
{bcolors.OKBLUE}Bleu:{bcolors.ENDC} Mauvais nombre mais proche du bon
{bcolors.WARNING}Jaune:{bcolors.ENDC} Vous avez cracké le coffre-fort

{bcolors.UNDERLINE}{bcolors.BOLD}Ton chrono commence maintenant !{bcolors.ENDC}
""")

# Début du chrono
st = time.time()

# Fonctions
def ledColor(compteur):
  global index
  global code

  if len(inputs) == len(code):
    led.color = ledcolors.YELLOW
  elif compteur == code[index]:
    led.color = ledcolors.GREEN
  elif abs(compteur) == maxsteps:
    led.color = ledcolors.OFF
  elif compteur < (code[index] - 10):
    led.color = ledcolors.RED
  elif compteur > (code[index] + 10):
    led.color = ledcolors.RED
  else:
    led.color = ledcolors.BLUE

def rotated():
  global index
  global code

  compteur = rotor.value

  ledColor(compteur)

  print(f"Valeur actuelle: {compteur}")

def confirm():
  global index
  global st

  compteur = rotor.value

  ledColor(compteur)

  if len(inputs) == len(code):
    print(f"""
    {bcolors.WARNING}Vous avez déjà ouvert le coffre-fort !{bcolors.ENDC}
    """)
  elif compteur == code[index]:
    inputs.append(compteur)
    index += 1
    print(f"""
    {bcolors.OKGREEN}{compteur} est un nombre correcte !{bcolors.ENDC}
    """)
    if len(inputs) == len(code):
      print(f"""
      {bcolors.OKGREEN}Vous avez ouvert le coffre-fort !{bcolors.ENDC}
      {bcolors.OKCYAN}Combinaison:{bcolors.ENDC} {code}
      {bcolors.WARNING}Temps: {bcolors.BOLD}{time.time() - st}{bcolors.ENDC} secondes{bcolors.ENDC}
      """)
  elif compteur != code[index]:
    print(f"{bcolors.FAIL}{compteur} est un nombre incorrecte !{bcolors.ENDC}")

# Event Listener
rotor.when_rotated = rotated
button.when_pressed = confirm

# Petite pause 
pause()
