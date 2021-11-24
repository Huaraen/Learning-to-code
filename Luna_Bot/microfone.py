import speech_recognition as sr
from commands import Audio, Server
from gatilho import Verifica_voz
from random import randrange
verify_voice = Verifica_voz()
server = Server()
audio = Audio()

class Mic:
    def __init__(self, name_bot):
        self.__name_bot = name_bot
        self.reconhecimento = sr.Recognizer()

    def power (self, is_power):
        if is_power: return Power_on().mic_on(self, is_power)
        else: return Power_off().mic_on(self, is_power)

    @property
    def name_bot(self):
        return self.__name_bot

class Power_on:
    '''se sistema se encontra ligado, identifica a voz
    e executa função.'''
    def __init__(self):
        self.__trig_turn_off = ["turn off", "vai pra casa", "dormir", "boa noite"]
    
    def mic_on(self, Miic, is_power):
        print ("\n｡◕‿◕｡")
        voice = Mic_turn_on().reconhecimento_mic(is_power)
        if Miic.name_bot == voice: verify_voice.voz_bot ()
        elif Miic.name_bot in voice:
            for command_voice in self.__trig_turn_off:
                if command_voice in voice: self._sleep()
            voice = voice.replace((Miic.name_bot+" "), "")
            return verify_voice.realiza_comandos(voice)
        else:
            return verify_voice.just_voice (voice)

    def _sleep(self):
        roll4 = randrange(1,4)
        if roll4 == 1: audio.toca_audios("go_to_sleep_6", "bot")
        else: audio.toca_randomic_audio("go_to_sleep_", 5)

class Power_off:
    '''se sistema se encontra desligado, identifica a voz
    e se tiver o comando de ligar, liga o sistema.'''
    def __init__(self):
        self.__trig_turn_on = ["turn on", " ligar", "acorde", "bom dia", "boa tarde", "boa noite", "despert"]

    def mic_on(self, Miic, is_power):
        voice = Mic_turn_on().reconhecimento_mic(is_power)
        if Miic.name_bot in voice:
            for command_voice in self.__trig_turn_on:
                if command_voice in voice:
                    audio.toca_randomic_audio("bot_greetings_", 5)
                    server.server_notification("Oláa!!", Miic.name_bot.title())
                    return True
            return self.__sleeping()
        else: return self.__sleeping()

    def __sleeping(self):
        server.server_notification(texto="Sleeping...", cardinal="Luna") 
        roll20 = randrange(1, 20)
        if roll20 <= 15: audio.toca_audios("go_to_sleep_2", "bot")
        return False

class Mic_turn_on(Mic):
    def reconhecimento_mic(self, power):
        with sr.Microphone() as mic:
            reconhecimento_do_mic = self.reconhecimento.listen(mic)
            try:
                voice = self.reconhecimento.recognize_google(reconhecimento_do_mic,language= "pt-BR")
                voice = voice.lower()
                print (">>: {}".format(voice))
                return voice
            except sr.UnknownValueError:
                if power: return self.__power_on_unknownvalue_exception()
                else: return self.__power_off_unknownvalue_exception()     
            except sr.RequestError as e:
                if power: return self.__power_on_requesterror_exception(e)
                else: return self.__power_off_requesterror_exception(e)

    def __power_on_unknownvalue_exception(self):
        server.server_notification ("não consegui entender o que você disse", self.name_bot.title())
        roll20 = randrange(1,20)
        if roll20 > 13: audio.toca_randomic_audio("beep_", 9)
        return "unknown command" 
    def __power_on_requesterror_exception(self, e):
        print (self.name_bot.title(), ":  Error, Error. . .; {0}".format(e))
        audio.toca_audios("Hello_Monkeys")
        return "unknown command"

    def __power_off_unknownvalue_exception(self):        
        server.server_notification (":  Não estou em casa, deixe seu recado e eu vejo quando voltar", (self.name_bot.title()))
        return False
    def __power_off_requesterror_exception(self, e):    
        '''Não foi possivel requisitar resultados de Google Speech Recognition service'''
        server.server_notification (":  Error, Error. . . {0}".format(e)), (self.name_bot.title())
        return False


if "__main__" == __name__:
    power = True
    while True:
        x = Mic_turn_on().reconhecimento_mic(power)
        if x == "sair": exit ()
