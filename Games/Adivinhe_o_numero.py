import random
import time

def jogar ():
    print ("********************************")
    print ("Bem vindo ao jogo de Adivinhação \nAdivinhe um numero entre 0 e 50")
    print ("********************************\n")


    numero_secreto = random.randrange(0,51) 
    rodada = 1

    print("Em qual nível deseja jogar?")
    print("(1) Fácil, (2) Médio, (3) Difícil")

    nivel = int(input("Defina seu nível: "))

    if nivel == 1:
        total_de_tentativas = 15
    elif nivel == 2:
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5    


    for rodada in range (1,total_de_tentativas +1):
        print ("\nTentativa {} de {}" .format (rodada, total_de_tentativas))
        chute = int(input("Adivinhe o número: "))

        if chute < 0 or chute > 50:
            print ("Você digitou um numero inválido\n")
            continue

        if numero_secreto == chute:
            print ("Muito bem! Você acertou")
            resultado = True
            break
        else:
            if numero_secreto > chute:
                print ("Você errou, Seu numero foi baixo, tente um número maior")
                resultado = False
            elif numero_secreto < chute:
                print ("Você errou! Seu numero foi mais alto, tente um número menor")
                resultado = False
                
            
    if resultado == False:
        imprime_mensagem_perdedor(numero_secreto)

    numero_secreto

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print ("")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(numero_secreto):
    print ("\nO número era {} " .format (numero_secreto))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    print ("")
    print("***************************")
    print("******** GAME OVER ********")
    print("***************************")

if __name__ == "__main__":
    jogar()
    time.sleep(3)
    exit()
    