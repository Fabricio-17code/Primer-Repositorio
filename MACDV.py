import random

def valorInicial():
  return random.randint(0,1)

def recibirInput():
  adv = input("¿Cruz o Cara?: ")
  adv = adv.lower()
  if adv == "cruz":
    return 1
  elif adv == "cara":
    return 0
  else:
    return -1

def iniciarJuego():
  result = valorInicial()
  adv = recibirInput()
  while adv == -1:
    print("Error.") 
    adv = recibirInput()
  if adv == result:
    print("¡Ganaste el Juego!")
  else:
    print("Perdiste")

def procesarInp(inp):
  if inp == "y" or inp == "yes" or inp == "n" or inp == "not":
    return True
  else:
    return False

def reset():
  inp = input("¿Quieres jugar de nuevo? (y/n): ").lower()
  print()
  inpValida = procesarInp(inp)
  while inpValida == False:
    inp = input("Error. ¿Quieres jugar de nuevo? (y/n): ").lower()
    inpValida = procesarInp(inp)   
  if inp == "y" or inp == "yes":
    return True
  elif inp == "n" or inp == "not":
    return False 
    
playAgain = True
while playAgain:
  iniciarJuego()
  playAgain = reset()