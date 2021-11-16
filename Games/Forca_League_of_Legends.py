import random
import time

def jogar ():

    mensagem_de_abertura()
    palavra_secreta = carrega_palavra_secreta()        
    
    palavra_acertada = inicializa_letras_acertadas(palavra_secreta) 
    print (palavra_acertada)
    print ("")

    enforcou = False
    acertou = False
    erros = 0

    
    while(not enforcou and not acertou):
        # while true
        
        chute = jogada ()

        if chute in palavra_secreta:
            marca_chute_correto(palavra_secreta, palavra_acertada, chute)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in palavra_acertada
        print (palavra_acertada)
       
    if acertou :
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

       
    print("\n\nFim do jogo\n \n")


def mensagem_de_abertura(): 
    print ("********************************")
    print ("   Bem vindo ao jogo da Forca   ")
    print ("********************************\n")

def carrega_palavra_secreta ():
    arquivo = open("campeoes.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()   

    numero_random = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero_random].upper()
    return palavra_secreta  

def inicializa_letras_acertadas (palavra):
    return ["_" for letra in palavra]
    '''Mesma coisa que exemplo abaixo, porém, compacto
    Ex 1 
    palavra_acertada = []
    for letra in palavra_secreta:
    palavra_acertada.append("_")'''

def jogada ():
    chute = input("Informe uma letra: ")
    chute = chute.strip().upper()
    return chute

def marca_chute_correto(palavra_secreta, palavra_acertada, chute):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            palavra_acertada [posicao] = letra
        posicao += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
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

if __name__ == "__main__":
    jogar()
    time.sleep(3)
    exit()
    