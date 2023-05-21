import random
from unicodedata import numeric
def jogo_adivinhacao():
    print("********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_tentativas = 3
    rodada = 1

    print(numero_secreto)

    for rodada in range(1, total_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_tentativas))
        chute = input("Digite o seu número: ")
        print("Você digitou ", chute)
        numero = int(chute)

        if numero_secreto == numero:
            print("Você acertou")
            break
        else:
            if (numero > numero_secreto):
                print("Você errou! O seu chute foi maior que o numero correto")
            elif (numero < numero_secreto):
                print("Você errou! O seu chute foi menor que o numero correto")

        rodada = rodada + 1

    print("Fim do jogo!")
