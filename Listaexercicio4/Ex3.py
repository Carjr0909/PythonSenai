"""
Faça um programa que leia as notas de duas provas, calcule a média aritmética simples, e
informe se o aluno foi aprovado (média maior ou igual a 6) ou reprovado (média menor que 6).
Data: 15/02/25
Criado por: Carlos Jr
"""

n1 = int(input("Digite a primeira nota: "))
n2 = int(input("Digite a segunda nota: "))

media = (n1 + n2) / 2.0

if media >= 6:
    print('Média:', media, '\nAprovado')
else:
    print('Média:', media, '\nReprovado')
