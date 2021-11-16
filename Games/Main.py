import Adivinhe_o_numero
import Forca_League_of_Legends


print ("********************")
print ("  Escolha seu jogo  ")
print ("********************")

print ("\n (1) Jogo da forca\n (2) Jogo da Adivinhação")

jogo = int(input("\nQual jogo deseja jogar? "))

if jogo == 1:
    print ("\nIniciando Jogo da forca \n")
    Forca_League_of_Legends.jogar()
elif jogo == 2:
    print ("\niniciando jogo de Adivinhação\n")
    Adivinhe_o_numero.jogar()























