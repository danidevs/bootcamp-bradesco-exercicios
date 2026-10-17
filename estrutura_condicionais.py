import sys


opcao = int(input("Informe uma opção: [1] Sacar \n[2] Extrato:"))
if opcao == 1:
    valor = float(input("Informe o valor que deseja sacar: "))
    # ...
elif opcao == 2:
    print("Exibindo o extrato da conta...")
else:
    sys.exit("Opção inválida. Encerrando o programa.")    