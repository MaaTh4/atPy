inteiros = [1,2,3,4,5,6,7,8,9,10]

cubosDosInt = {}

for item in inteiros:
    cubo = item ** 3
    cubosDosInt[f'Cubo do {item}'] = cubo
    
print(cubosDosInt)
