from commands import Audio, Server
from gatilho import Verifica_voz
from random import randrange

audio = Audio()
server = Server()
verify_voice = Verifica_voz()

class Mic():
    def __init__(self, name_bot):
        self.__name_bot = name_bot

    @property
    def name_bot(self):
        return self.__name_bot

    def power (self, is_power):
        if is_power: return Power_on().mic_on(self)
        else: return Power_off().mic_on(self)


class Power_on():
    '''se sistema se encontra ligado, identifica a voz
    e executa função.'''
    def __init__(self):
        self.__trig_turn_off = ["turn off", "vai pra casa", "dormir", "boa noite"]
    
    def mic_on(self, Miic):
        voice = input("... ")
        if Miic.name_bot == voice: 
            return verify_voice.voz_bot ()
        elif Miic.name_bot in voice:
            for command_voice in self.__trig_turn_off:
                if command_voice in voice:
                     return self._sleep()
            voice = voice.replace((Miic.name_bot+" "), "")
            return verify_voice.realiza_comandos(voice)
        else:
            return verify_voice.just_voice (voice)

    def _sleep(self):
        roll4 = randrange(1,4)
        if roll4 == 1: audio.toca_audios("go_to_sleep_6", "bot")
        else: audio.toca_randomic_audio("go_to_sleep_", 5)
        return "sleep"

class Power_off():
    '''se sistema se encontra desligado, identifica a voz
    e se tiver o comando de ligar, liga o sistema.'''
    def __init__(self):
        self.__trig_turn_on = ["turn on", " ligar", "acorde", "bom dia", "boa tarde", "boa noite", "despert"]

    def mic_on(self, Miic):
        voice = input("... ")
        if Miic.name_bot in voice:
            for command_voice in self.__trig_turn_on:
                if command_voice in voice:
                    server.server_notification("Oláa!!", Miic.name_bot.title())
                    audio.toca_randomic_audio("bot_greetings_", 5)
                    return True
            return self.__sleeping()
        else: return self.__sleeping()

    def __sleeping(self):
        server.server_notification(texto="Sleeping...", cardinal="Luna") 
        roll20 = randrange(1, 20)
        if roll20 <= 15: audio.toca_audios("go_to_sleep_2", "bot")
        return False
        
