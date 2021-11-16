import speech_recognition as sr
from commands import Command as cmd
from time import sleep
name_bot = ("luna")

# obtain audio from the microphone
def mic_on(power=False, time=4):      
    reconhecimento = sr.Recognizer()
    sleep(int(time))
    with sr.Microphone() as mic:
        
        print(">>>: ")
        reconhecimento_do_mic = reconhecimento.listen(mic)
        
        if power == True:
            try:
                voice = reconhecimento.recognize_google(reconhecimento_do_mic,language= "pt-BR")
                voice = voice.lower()
                print (voice)

                if name_bot == voice:
                    return name_bot
                elif name_bot in voice:
                    return voice.replace((name_bot+" "), "")

            except sr.UnknownValueError:
                print (name_bot.title(), ":  não consegui entender o que você disse")
                return "unknown command"        
            except sr.RequestError as e:
                print (name_bot.title(), ":  Não foi possivel requisitar resultados de Google Speech Recognition service; {0}".format(e))
                cmd().toca_audios("Hello_Monkeys")
                return "unknown command"
            else:
                x = "Just Voice "
                x += voice
                return x

        if power == False:
            try:
                voice = reconhecimento.recognize_google(reconhecimento_do_mic,language= "pt-BR")
                voice = voice.lower()
                print (voice)


                if name_bot in voice:
                    trig_turn_on = ["turn on", "ligar", "acorde", "bom dia", "boa tarde", "boa noite", "desperte"]
                    for command_voice in trig_turn_on:
                        if command_voice in voice:
                            return True
                else: return False

            except sr.UnknownValueError:
                print (name_bot.title(), ":  não consegui entender o que você disse")
                return False
            except sr.RequestError as e:
                print (name_bot.title(), ":  Não foi possivel requisitar resultados de Google Speech Recognition service; {0}".format(e))
                return False
        return False
    
if __name__ == "__main__":
    while True:
        sair = mic_on()
        print (sair)
        if sair == "sair" or sair == "fechar":
            cmd().server_notification("Fechando Programa")
            exit ()