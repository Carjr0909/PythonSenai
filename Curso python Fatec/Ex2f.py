"""
Escreva um programa que leia dois números inteiros e msotre na tela
apenas o menor dos dois. Se ambos forem iguais mostre qualquer um deles.
"""

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("DIgite o segundo número: "))

if n1 <= n2:
     print(f"O menor número é: {n1}")
else:
     print(f"O maior número é: {n2}")
