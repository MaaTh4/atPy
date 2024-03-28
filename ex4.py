import random

def rollDice(qntDados, numFaces):
    return sum(random.randint(1, numFaces) for x in range(qntDados))
  
def jogarCraps():  
    qntDados = 2
    numFaces = 6
    
    results = rollDice(qntDados, numFaces)   
    

    if results == 7 or results == 11:
        print(f'Natural!!! Você ganhou! Tirou: {results}')
    elif results == 2 or results == 3 or results == 12:
        print(f'Craps!!! Você perdeu! Tirou: {results}')
    else:
        print('Ponto', results)
        ponto = results
        while True:
            segundaJogada = rollDice(qntDados,numFaces)
            print(f'Sua segunda jogada foi: {segundaJogada}')
            if segundaJogada == ponto:
                print('SUA SEGUNDA JOGADA FOI PONTO!!! Você ganhou!')
                break
            elif segundaJogada == 7:
                print('Você tirou 7! Você perdeu!')
                break
        
        
jogarCraps()
