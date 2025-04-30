"""
Lista de exercícios 3
Cálculo do área do círculo
Criado por: Carlos Jr
15/02/25
"""
import math as m

raio = float(input("Digite o raio do círculo: "))

area = m.pow(raio, 2.0) * m.pi

print(f"A área do círculo é igual a: {area:.4}")