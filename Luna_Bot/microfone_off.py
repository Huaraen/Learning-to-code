from commands import Command
from time import sleep
cmd = Command()

bot = ("luna")
        
def mic_on (power=False, time=4):
    sleep(int(time))

    voice = input("comando>> ")
    if power == True:
        if bot == voice:
            return bot
        elif bot in voice:
            return voice.replace((bot+" "), "")
        else:
            retorno = "Just Voice "
            retorno += voice
            return retorno

    if power == False:
        if bot in voice:
            trig_turn_on = ["turn on", "ligar", "acorde", "bom dia", "boa tarde", "boa noite", "desperte"]
            for command_voice in trig_turn_on:
                if command_voice in voice:
                    return True
        else: return False