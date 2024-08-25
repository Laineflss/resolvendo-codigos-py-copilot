#  Vamos testar se uma palavra é um palíndromo?! 

# Solicita uma palavra do usuário
palavra = input("Digite uma palavra: ")

# Inverte a palavra usando slicing
palavra_invertida = palavra[::-1]

# Verifica se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")
