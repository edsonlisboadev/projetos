user_selection = input('Digite 1 para acessar e 2 para encerrar')
user_right_email = 'admin@admin'
user_right_password = 1234
retry = 0
if user_selection == '2':
    print("Encerrado")
    exit()
elif user_selection != '1':
    print("opção inválida")
    exit()
else:
    user_password = int(input("Digite a sua senha"))
    user_email = input("Digite a sua senha")
    if user_password != user_right_password or user_email != user_right_email and retry <= 3:
        retry += 1
        print(f"Senha inválida, você tem mais { 3 - retry} tentativas")
    