"""
Lista de exercícios 2
Exemplo de média com formatação na saída
Criado por: Carlos Jr
15/02/25
"""

#Entrada - Solicia para o usuário digitar as notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

#Processamento - Calcula a média aritmética
media = (nota1 + nota2 + nota3) / 3.0

#Saída - Exibe a média aritmética
print(f"A média aritimética das notas é: {media:.2}")