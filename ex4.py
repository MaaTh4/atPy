import random

def rollDice(qntDados, numFaces):
    primeiroDado = random.randint(1,6)
    segundoDado = random.randint(1,6)

sumDados = primeiroDado + segundoDado

if sumDados == 7 or sumDados == 11:
    print('Natural!!! Você ganhou!')
elif sumDados == 2 or sumDados == 3 or sumDados == 12:
    print('Craps!!! Você perdeu!')
else:
    print('Ponto')
