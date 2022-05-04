import random
numero_secreto = random.randint(0, 9)
qtd_tentativa = 0
numero_tentativa = 3
while qtd_tentativa < numero_tentativa:
    print("Jogo da Adivinhação!")
    print("Numero de tentativas: ", numero_tentativa - qtd_tentativa)
    palpite = int(input("Digite um número: "))
    qtd_tentativa += 1
    if palpite == numero_secreto:
        print("Acertou!")
        break
else:
    print("Suas chances acabaram!")
    print(f"O número secreto era: {numero_secreto}")