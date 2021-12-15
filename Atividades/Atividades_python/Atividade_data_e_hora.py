from datetime import datetime
import time


def dataNow():
    return datetime.now().strftime("%d/%m/%Y")

def hourNow():
    return datetime.now().strftime("%H:%M:%S")


data_atual = dataNow()
hora_atual = hourNow()

def teste ():
        
    for counter in range (0,80):
        print (counter)
        hora = hourNow()
        print (hora)
        time.sleep (1)

def main ():
    checkin = input ("Por Favor, informe nome: ")
    intro(checkin)

def intro (checkin):
    print ("Bom dia {}" .format (checkin))
    print ("\nEste arquivo é sobre as aulas de python, vamos rever algumas coisas?")
    print ("Alias, o dia de hoje é {} certo? \nAgora são {} Horas." .format (dataNow(), hourNow()))




if __name__ == "__main__":
    main ()