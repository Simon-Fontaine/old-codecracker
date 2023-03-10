from gpiozero import RotaryEncoder, RGBLED, Button
from signal import pause
from time import *
from art import tprint
import random
import json
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
tprint("Code Cracker","3d_diagonal")

username = input(f"\n{bcolors.HEADER}{bcolors.BOLD}Entrez votre nom d'utilisateur:{bcolors.ENDC}\n")

print(f"""
{bcolors.OKCYAN}{bcolors.BOLD}Prêt {username}?{bcolors.ENDC}
Essaiez de trouver {bcolors.BOLD}4{bcolors.ENDC} nombres entre {bcolors.UNDERLINE}-30 et 30{bcolors.ENDC} !

{bcolors.OKCYAN}{bcolors.BOLD}Couleurs:{bcolors.ENDC}
{bcolors.OKGREEN}Vert:{bcolors.ENDC} Nombre correcte
{bcolors.FAIL}Rouge:{bcolors.ENDC} Nombre incorrecte
{bcolors.OKBLUE}Bleu:{bcolors.ENDC} Mauvais nombre mais proche du bon
{bcolors.WARNING}Jaune:{bcolors.ENDC} Vous avez cracké le coffre-fort
""")

input(f"\n{bcolors.HEADER}Appuiez sur ENTER pour démarrer votre chrono...{bcolors.ENDC}\n")

print(f"\n{bcolors.WARNING}Le chrono a démarré !{bcolors.ENDC}\n")

# Début du chrono
st = time.time()

# Fonctions
def ledColor(compteur):
  global index
  global code

  if compteur == code[index]:
    led.color = ledcolors.GREEN
  elif abs(compteur) == maxsteps:
    led.color = ledcolors.OFF
  elif compteur < (code[index] - 10):
    led.color = ledcolors.RED
  elif compteur > (code[index] + 10):
    led.color = ledcolors.RED
  else:
    led.color = ledcolors.BLUE

startCompteir = rotor.value * maxsteps
ledColor(startCompteir)

def rotated():
  global index
  global code

  compteur = rotor.value * maxsteps

  ledColor(compteur)

  print(f"Valeur actuelle: {compteur}")

def confirm():
  global index
  global st
  global username

  compteur = rotor.value * maxsteps

  if compteur == code[index]:
    inputs.append(compteur)
    index += 1
    print(f"\n{bcolors.OKGREEN}{compteur} est un nombre correcte !{bcolors.ENDC}\n")
    if len(inputs) == len(code):
      newtime = '%.2f' % (time.time() - st)
      print(f"{bcolors.OKGREEN}Vous avez ouvert le coffre-fort !{bcolors.ENDC}\n{bcolors.OKCYAN}Combinaison:{bcolors.ENDC} {code}\n{bcolors.WARNING}Temps: {bcolors.FAIL}{bcolors.BOLD}{newtime}{bcolors.ENDC}{bcolors.WARNING} secondes{bcolors.ENDC}")
      
      newdata = {'name': username, 'time': newtime}

      def write_json(new_data, filename='scores.json'):
        with open(filename,'r+') as file:
            file_data = json.load(file)
            file_data["players"].append(new_data)
            file.seek(0)
            json.dump(file_data, file, indent = 2)

      write_json(newdata)

      with open('scores.json') as f:
          data = json.load(f)

      sorted_times = sorted(data['players'], key=lambda k: float(k['time']))

      print(f"\n{bcolors.OKCYAN}{bcolors.BOLD}Les 3 meilleurs chronos sont:{bcolors.ENDC}")
      for i in range(3):
          player = sorted_times[i]
          print(f"{i+1}. {player['name']} - {player['time']} secondes")

      exit()
  elif compteur != code[index]:
    print(f"\n{bcolors.FAIL}{compteur} est un nombre incorrecte !{bcolors.ENDC}\n")
  
  ledColor(compteur)

# Event Listener
rotor.when_rotated = rotated
button.when_pressed = confirm

# Petite pause
pause()