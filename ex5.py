from unidecode import unidecode

minha_string = input("digita algo: ")

nova = minha_string.replace(",", "")
novissima =  nova.replace(".", "")
novapracaralho = novissima.replace(" ", "")
bolsonaro = unidecode(novapracaralho)


def inverter_string(string):
    return string[::-1]

StringDefifinitiva = bolsonaro.lower()
string_invertida = inverter_string(StringDefifinitiva)
print(StringDefifinitiva)
print(string_invertida)
if StringDefifinitiva == string_invertida:
    print("É um palindromo")
else:
    print('Não é palindromo')
