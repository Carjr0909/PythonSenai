"""
Faça um programa que pergunte a idade do usuário e informe se ele pode ou não se aposentar.
Obs. Uma pessoa só pode se aposentar quando atingir 60 anos (idade mínima).
Data: 15/02/25
Criado por: Carlos Jr
"""

i = float(input("Digite sua idade: "))

if i >= 60:
    print("Você pode se aposentar!")
else:
    print("Você ainda precisa trabalhar!")