"""
Lista de exercícios 3
Crie um programa que solicite ao usuário o valor do raio de uma esfera e calcule o seu volume
Criado por: Carlos Jr
15/02/25
"""

import math as m

r = float(input("Digite o raio da esfera: "))

v = 4 * m.pi * m.pow(r, 3.0) / 3.0

print(f"O volume dessa esfera é igual a: {v:.5}")
