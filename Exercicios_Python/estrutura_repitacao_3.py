opcao = -1
while opcao != 0:
    opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato \n[0] Sair: "))
    if opcao == 1:
       print("sacando...")
    elif opcao == 2:
        print("Exibindo o extrato da conta...")
    else:
        print("obrigado por utilizar nosso sistema. Encerrando o programa.")    