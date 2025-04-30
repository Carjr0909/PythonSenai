"""
Lista de exercícios 3
Escreva um programa que calcule a média geométrica entre três números informados pelo
usuário. Utilize o tipo de dados double.
Criado por: Carlos Jr
15/02/25
"""

import math as m

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))

media1 = (n1 * n2 * n3)
media2 = m.cbrt(media1)

print(f"A média geométrica dos números digitados é: {media2:.8}")
