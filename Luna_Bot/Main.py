from commands import Command, Datahora
from gatilho  import Body as cmmd
import microfone     as mic
# import microfone_off as mic

cmd = Command()
dh = Datahora()
bot = "Luna"
    
def main ():
    checkin = iniciar()
    intro(checkin)
    power = False
    paciencia = 0
    while True:
        if power == True:
            trigger = mic.mic_on(power, paciencia)
            if bot.lower() == trigger:
                cmd.toca_audios("nya_button")
            elif not "unknown command" in trigger:
                if "Just Voice" in trigger:
                    cmmd().check_voice(trigger.replace("Just Voice", ""))
                elif "definir paciencia" in trigger:
                    x = int (cmmd().paciencia())
                    if x != None: paciencia = x
                else: 
                    x = cmmd().check_trigger(trigger)
                    if x != None:
                        power = x

        elif power == False:
            power = mic.mic_on(power)
        else: pass


def iniciar ():
    print ("\nIniciando . . \n")
    checkin = input ("Por Favor, informe nick: ")
    cmd.toca_audios("link_start")
    return checkin

def intro (checkin):
    print ("{}: Bom dia {}" .format (bot, checkin))
    cmd.toca_randomic_audio("bot_greetings_0", 5)
    print ("{}: Hoje é dia {}" .format (bot, dh.data))



if __name__ == "__main__":
    main()

'''
Bandeira de Mood, tendo uma com "angry" e certas palavras fazem descer o humor.
usar boolean enquanto não impor inteligencia artificial nela.
'''