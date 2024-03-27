from unidecode import unidecode
import re




# Exemplo de uso:
minha_string = input("digita algo: ")

nova = re.sub(",", "", minha_string)
novissima =  nova.replace(".", "")
novapracaralho = novissima.replace(" ", "")
print(novapracaralho)
