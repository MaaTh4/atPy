from unidecode import unidecode
import re




# Exemplo de uso:
minha_string = input("digita algo: ")

nova = re.sub(",", "", minha_string)
novissima =  nova.replace(".", "")
novapracaralho = novissima.replace(" ", "")
bolsonaro = unidecode(novapracaralho)
print(bolsonaro)


# string_invertida = inverter_string(minha_string)
# print(string_invertida)
