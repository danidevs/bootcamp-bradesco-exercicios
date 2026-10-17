texto = input("Digite um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(f"{letra} é uma vogal.")
    else:
        print(f"{letra} não é uma vogal.")
        print("Fim do programa.")