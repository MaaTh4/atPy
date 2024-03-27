salario = int(input('Nos informe seu salario: '))

def calcAumento():
    if salario <= 1500:
        aumento = salario * 0.2
        newSalario = salario + aumento
        print('\nSeu antigo salario era de: ',salario, ' reais')
        print('O aumento foi de 20%')
        print('O valor do aumento foi de: ',aumento, ' reais')
        print('Seu novo salario é de: ',newSalario, ' reais' )
        
        
    elif salario > 1500 and salario <= 2000:
        aumento = salario * 0.15
        newSalario = aumento + salario
        
        print('\nSeu antigo salario era de: ',salario, ' reais')
        print('O aumento foi de 15%')
        print('O valor do aumento foi de: ',aumento, ' reais')
        print('Seu novo salario é de: ',newSalario, ' reais' )
        
    elif salario > 2000 and salario <= 2500: 
        aumento = salario * 0.10
        newSalario = aumento + salario
        
        print('\nSeu antigo salario era de: ',salario, ' reais')
        print('O aumento foi de 10%')
        print('O valor do aumento foi de: ',aumento, ' reais')
        print('Seu novo salario é de: ',newSalario, ' reais' )
        
    elif salario > 2500:
        aumento = salario * 0.05
        newSalario = salario + aumento

        print('\nSeu antigo salario era de: ',salario, ' reais')
        print('O aumento foi de 5%')
        print('O valor do aumento foi de: ',aumento, ' reais')
        print('Seu novo salario é de: ',newSalario, ' reais' )

        
calcAumento()
