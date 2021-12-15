import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import webbrowser as browser
from os import remove


# from request import get ## pega HTTPs da internet.
# from bs4 import BeautifulSoup ## pega um <item> ou <titulo> .. do código da internet

# Ex: Get e BeautifulSoup

'''
def ultimas_noticias():
    site= get('https://news.google.com/news/rss?ned=pt_br&gl=BR&hl=pt')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:2]:
        mensagem = item.title.text
        print (mensagem)
        cria_audio(mensagem)
        playsound('aula/assistente_pessoal/audios/mensagem.mp3')

'''
##### CONFIGURAÇÕES #####
hotword = "morgana"


# obtain audio from the microphone
def monitora_audio():        
    microfone = sr.Recognizer()
    with sr.Microphone() as source:
        
        print("Aguardando o Comando: ")
        audio = microfone.listen(source)
            
        try:
            trigger = microfone.recognize_google(audio,language= "pt-BR")
            trigger = trigger.lower()
            print (trigger)

            if hotword in trigger:
                print ("Comando: ", trigger)
                responde("nya_button")
                executa_comandos(trigger)

        except sr.UnknownValueError:
            responde("what")
            print (hotword.title(), ":  não consegui entender o que você disse")
            main()
        except sr.RequestError as e:
            responde("megumu_yamerooo")
            print (hotword.title(), ":  Não foi possivel requisitar resultados de Google Speech Recognition service; {0}".format(e))
            main()
    return trigger

##### FUNÇÕES PRINCIPAIS #####

def cria_audio(audio, nome):
    tts = gTTS(audio, lang="pt-br")
    tts.save('aula/assistente_pessoal/audios/{}.mp3'.format (nome))
    responde(nome)

def responde (nome):
    playsound('aula/assistente_pessoal/audios/{}.mp3'.format (nome))

def executa_comandos(trigger):
    if "fogo" in trigger:
        fire()
    elif hotword == trigger:
        responde ("Ayaya")
    elif "toca" and "anime" in trigger:
        playlist ("anime")
    elif "toca" and "bad apple" in trigger:
        playlist ("bad_apple")
    else:
        comando_invalido (trigger)


# comandos = 
##### FUNÇÕES COMANDOS #####
def fire ():
    responde("Fire_Fire")

def comando_invalido (trigger):
    mensagem = trigger.strip(hotword)
    print (hotword.title(), ": ", mensagem)
    cria_audio(mensagem, "comando_invalido")
    print('COMANDO INVÁLIDO --', mensagem)
    remove("aula/assistente_pessoal/audios/comando_invalido.mp3")
    responde("megumu_yamerooo")

def playlist (album):
    if album == "bad_apple":
        browser.open("https://open.spotify.com/track/3urItfkvXw8tPjwNs2lXdd?si=06f4bc2e97174db7")
    elif album == "rock":
        browser.open("https://open.spotify.com/track/4PSiPZp8MYMDZzuBhCLgc6?si=b540ec462e9c423a")

def main():
    while True:
        monitora_audio()


if __name__ == "__main__":
    main()