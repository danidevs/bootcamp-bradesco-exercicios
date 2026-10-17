MAIOR_IDADE = 18

idade = int(input("Digite a sua idade: "))
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a carteira de motorista.")
else:
    print("Menor de idade, não pode tirar a carteira de motorista.")