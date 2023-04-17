# Número a ser verificado pelo usuário:
num = int(input("Insira um número inteiro para verificar se ele pertence à sequência de Fibonacci: "))

# Variáveis da sequência de Fibonacci
num1 = 0
num2 = 1
fibon = num1 + num2

# Loop para encontrar um número menor ou iqual ao número informado
while fibon < num:
    num1 = num2
    num2 = fibon
    fibon = num1 + num2

# Testando se o número inserido pentence à sequência
if fibon == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")