# Como entrada, receba um número inteiro e verifique se ele é par ou ímpar. 

# Solicita um número inteiro do usuário
numero = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print("O número", numero, "é par.")
else:
    print("O número", numero, "é ímpar.")
