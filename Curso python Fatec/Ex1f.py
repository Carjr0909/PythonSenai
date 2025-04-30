"""
Escreva um programa que leia um número na tela e escreva se ele é par o impar.
Lembrando que para saber a paridade de um número inteiro é preciso calcular o resto
da sua divisão por 2. Se o resto for 0 o número é par, se for 1 o número é impar
"""

n = int(input("Digite um número: "))

c = n % 2

if c >= 1:
    print("Este número é ímpar")
else:
    print("Este número é par")
