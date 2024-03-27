Turma = []

a = 1
while a >= 0:

    NotasDaTurma = int(input("Digite a nota do aluno: "))
    Turma.append(NotasDaTurma)
    a = NotasDaTurma

Turma.pop()

sort = sorted(Turma)

print('Foram lidas ',len(Turma), ' notas')
print('Ordem crescente: ', sort)

# reverseSort = sorted(Turma, reverse=True)

# for i in range (len(reverseSort)):
#     for x in reverseSort:
#         print(x[i], end=' ')
