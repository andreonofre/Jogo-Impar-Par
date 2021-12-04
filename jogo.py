from random import randint

vitoria = 0
while True:
    jogador = int(input("Digite um valor:"))
    computador = randint(1, 11)
    total = jogador + computador
    tipo = " "
    while tipo not in "PI":
        tipo = input("O que você escolhe? [P/I]: ").upper().strip()[0]
    print(f"Você jogou {jogador} e o computador jogou {computador}, totalizando {total},", end=" ")
    print("DEU PAR!" if total % 2 == 0 else "DEU ÍMPAR!" )
    if tipo == "P":
        if total % 2 == 0:
            print("Você GANHOU")
            vitoria += 1
        else:
            print("Você PERDEU")
            break
    elif tipo == "I":
        if total % 2 == 0:
             print("Você VENCEU")
             vitoria += 1
        else:
            print("Você PERDEU")
        break
    print("Vamos jogar novamente...")
print(f"GAME OVER! Você venceu {vitoria} vezes.")