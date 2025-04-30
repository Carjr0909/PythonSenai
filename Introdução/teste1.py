print("Área de login")

email = input("Digite seu email ")
email_correto = "carlospontecianojr@gmail.com"

if email == email_correto:
  print("\n" * 130)
  print("Digite sua senha ")
elif email != email_correto:
  print("Email não cadastrado... tente novamente")
else:
  print("email não cadastrado")
  exit()

senha = input("senha ")
senha_correta = "12345"

if senha == senha_correta:
  print("\n" * 130)
  print("Login realizado com sucesso")
  print("Seja bem-vindo ao sistema ")
  print("Carregando")
  print()
  print("Carregando..")
  print("Carregando...\n\nMenu\n")

Opcoes_correta1 = "1"
Opcoes_correta2 = "2"
print("1 - Calculadora\n\n2 - Sair\n")

if Opcoes_correta1:
  print("\n" * 130)
  print("Selecione a operação desejada")
  print("S - Soma\nM - Multiplicação\n")
  input("Digite A inicial da opção desejada: ")

conta_correta1 = "S"
conta_correta1 = "s"

if conta_correta1:
  print("\n" * 130)
  num1 = float(input("\nDigite o primeiro número: "))
  num2 = float(input("\nDigite o segundo número: "))

  resultado1 = num1 * num2

  print("O resultado dessa multiplicação é: ", resultado1)
else:
  print("\n" * 130)
  num3 = float(input("\nDigite o primeiro número: "))
  num4 = float(input("\nDigite o segundo número: "))

  resultado2 = num3 + num4

  print("O resultado dessa soma é: ", resultado2)