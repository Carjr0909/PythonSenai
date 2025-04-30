"""
    DESVIO CONDICIONAL SIMPLES
Apresente a mensagem se o número inteiro é positivo, negativo ou igual a 0
Data: 15/02/25
Criado po: Carlos Jr.
"""

i = float(input("Digite um número: "))

if i < 0:
    print("Esse número é negatio")
elif i > 0:
    print("Número positivo")
else:
    print("Este número é igual a zero")