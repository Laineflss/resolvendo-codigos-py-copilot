# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita o primeiro número do usuário e converte para float
numero1 = float(input("Digite o primeiro número: "))

# Solicita o segundo número do usuário e converte para float
numero2 = float(input("Digite o segundo número: "))

# Realiza uma operação simples (neste caso, soma)
resultado_soma = numero1 + numero2
resultado_subtracao = numero1 - numero2
resultado_multiplicacao = numero1 * numero2
resultado_divisao = numero1 / numero2 if numero2 != 0 else "Divisão por zero não permitida"

# Exibe os resultados das operações
print("O resultado da soma é:", resultado_soma)
print("O resultado da subtração é:", resultado_subtracao)
print("O resultado da multiplicação é:", resultado_multiplicacao)
print("O resultado da divisão é:", resultado_divisao)
