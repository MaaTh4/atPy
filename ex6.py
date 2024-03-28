notasAluno = []

a = 1
while a >= 0:

    notas = int(input("Digite a nota do aluno: "))
    if notas > 10:
        print('ERROR! A nota não pode ser maior que 10. Insira uma nota válida')
    else:
        notasAluno.append(notas)
        a = notas

notasAluno.pop()

sort = sorted(notasAluno)

print('\nForam lidas ',len(notasAluno), ' notas')
print('Ordem crescente: ', sort)
print('Ordem decrescente na vertical: ')

listaInvertida = sorted(notasAluno, reverse=True)
for item in listaInvertida:
    print(item)
        

soma = sum(notasAluno)
print(f'A soma das notas é: {soma}')

media = soma/len(notasAluno)

print(f'A média das notas é: {media}')

acimaDaMedia = 0
abaixoDeSete = 0

for item in notasAluno:
    if item > media:
        acimaDaMedia += 1 
    elif item < 7:
        abaixoDeSete += 1 


print(f'A quantidade de notas acima da média é: {acimaDaMedia}')
print(f'A quantidade de notas abaixo da 7 é: {abaixoDeSete}')
