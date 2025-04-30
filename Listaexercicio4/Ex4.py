"""
Faça um programa que leia calcule o frete com base no peso informado pelo usuário.
Obs. A empresa de entregas cobra frete de acordo com o peso da mercadoria. Se o peso for até
5 kg, o frete é R$ 20,00. Se o peso for acima de 5 kg e até 10 kg, o frete é R$ 40,00. Para pesos
acima de 10 kg, o frete é R$ 60,00.
Data: 15/02/25
Criado por: Carlos Jr
"""

peso = int(input("Digite o peso do produto: "))

if peso <= 5:
    print("O frete custa: R$20,00")
elif peso <= 10:
    print("O frete custa R$40,00")
else:
    print("O frete custa R$60,00")
