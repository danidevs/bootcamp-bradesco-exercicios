tipo_normal = input("qual o seu tipo de conta?(1 - normal / 2 - universitária): ")
conta_normal = tipo_normal == "1"
conta_universitaria = tipo_normal == "2"
saldo = float(input("Informe o saldo da conta: "))
saque = float(input("Informe o valor que deseja sacar: "))
cheque_especial = float(input("Informe o valor do cheque especial: "))

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
            print("Saque realizado com uso do cheque especial!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente para realizar o saque.")