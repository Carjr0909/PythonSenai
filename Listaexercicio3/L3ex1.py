"""
Lista de exercícios 3
Escreva um programa que calcule o delta de uma equação de segundo grau
Δ = b² - 4ac
Criado por: Carlos Jr
15/02/25
"""
import math as m

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = m.pow(b, 2.0) - (4 * a * c)

print(f"O delta dessa equação é igual a: {delta:.4}")