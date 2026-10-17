def sacar ( valor):
    saldo = 1000
    if valor <= saldo:
        print("valor sacdo com sucesso")
        print("retire o seu dinheiro na boca do caixa")
    print("Obrigado por utilizar o nosso caixa eletrônico. \n")

def depositar (valor):
    saldo = 1000
    saldo += valor
    print(f"valor de r${valor} depositado com sucesso! \n")

sacar(200)
depositar(500)