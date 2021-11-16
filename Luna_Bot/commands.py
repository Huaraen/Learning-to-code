import webbrowser    as browser
import playsound     as ps
from datetime        import datetime
from os              import remove, system as os_system
from gtts            import gTTS
from time            import sleep
from random          import randrange

bot_name = "Luna"

class Datahora:
    '''Dia a dia'''  
    def _data_agora(self):
        return datetime.now().strftime("%d/%m")    
    def _hora_agora(self):
        return datetime.now().strftime("%H:%M")
        # ("%H:%M:%S") Para segundos também.
    def _data_hora():
        return datetime.now().strftime("%d/%m/%Y %H:%M")

    @property
    def dia(self):
        '''imprime, cria e reproduz audio com a data atual'''
        data = ("hoje é dia {}".format (self._data_agora()))
        print (data)
        Command().cria_audio (data, "data_atual")
    
    @property
    def hora(self):
        '''imprime, cria e reproduz audio com as horas'''
        horas = ("agora são, {}".format (self._hora_agora()))
        print (horas)
        Command().cria_audio (horas, "hora_atual")

    @property
    def data (self):
        '''retorna data atual em texto'''
        return self._data_agora()

class Command:
    def __init__ (self):
        self.__path = "Audios/"

    def server_notification(self, texto, cardinal = "Cardinal"):
        '''imprime a mensagem do sistema'''
        print("{}: {}".format(cardinal, texto))
        
    def cria_audio(self, texto, nome_audio):
        '''Cria audio com base em texto'''
        tts = gTTS(texto, lang="pt-br")
        tts.save('{}{}.mp3'.format (self.__path, nome_audio))
        self.toca_audios(nome_audio)
        sleep (1)
        remove('{}{}.mp3'.format (self.__path, nome_audio))

    def toca_audios (self, nome, fonte="audios"):
        '''reproduz audio.mp3, fonte "audios" ou "bot'''
        if fonte == "audios":
            path = self.__path
        elif fonte == "bot":
            path = "Audios/bot_sound/"
        else: path = fonte
        ps.playsound('{}{}.mp3'.format (path, nome))

    def toca_randomic_audio(self,nome_audio, stop=2):
        random = str(randrange(1,stop+1))
        self.toca_audios(nome_audio+random, fonte="bot")

    def playlist (self, album):
        '''toca musica'''
        if album == "bad apple":
            browser.open("https://open.spotify.com/track/3urItfkvXw8tPjwNs2lXdd?si=06f4bc2e97174db7")
        elif album == "anime":
            browser.open("https://open.spotify.com/playlist/3lsfveO1cBycWxcjbQ54Gw?si=d7fcc215816747ac")

    def abrir_aba_navegador (self, http):
        '''abre browser selecionado'''
        if http == "abrir whatsapp":
            browser.open ("https://web.whatsapp.com/")
        elif http == "abrir google" or http == "abrir navegador":
            browser.open ("https://www.google.com.br/")
        elif http == "abrir youtube":
            browser.open ("https://www.youtube.com/")
        elif http == "abrir alura" or http == "abrir curso":
            browser.open ("https://cursos.alura.com.br/category/data-science")
        elif http == "abrir anime":
            browser.open ("https://animesonline.cc/episodio/")
        elif http == "abrir discord":
            browser.open ("https://discord.com/channels/490586921664512001/708076678924206170")

    def procurar_youtube (self, search):
        '''procura no youtube'''
        search = search.replace(" ", "+")
        browser.open ("https://www.youtube.com/results?search_query={}".format(search))

    def abrir_aplicativo (self, app):
        '''Abre aplicativo pelo atalho.lnk dentro da pasta Atalhos'''
        path = "Atalhos"
        os_system ("start /d {} {}.lnk".format(path, app))
    
    def abrir_programa(self, app):
        '''Abre programa direto'''
        os_system ("start {}".format(app))

    def fechar_aplicativo (self, app):
        '''Fecha aplicativo.exe'''
        try:        
            os_system('taskkill /f /im {}.exe'.format(app))
        except:
            self.server_notification ("{}: Aplicativo não encontrado na barra de tarefas" .format (bot_name))
            self.cria_audio("Arquivo não encontrado", 'fechar_aplicativo')
        '''
        /f : Specifies that process(es) be forcefully terminated.
        /im (ImageName ): Specifies the image name of the process to be terminated.
        For more info regarding TaskKill --> 
        https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-xp/bb491009(v=technet.10)?redirectedfrom=MSDN
        '''

    def separar_numeros_da_frase (self, trigger):
        '''recebe texto, mantem e retorna somente numeros em inteiro'''
        apenas_digitos = ("")
        for caractere in trigger:
            if caractere.isdigit():
                apenas_digitos += caractere
        apenas_digitos = int(apenas_digitos)
        return apenas_digitos
            
    def mute(self, trigger):
        '''Mute'''
        tempo = self.separar_numeros_da_frase(trigger)
        if tempo != int: tempo = 30
        mute_alert = [5, 15, 35, 55, 75, 95] 
        for sec in range (0,tempo):
            sleep (1)
            if sec in mute_alert:               
                self.server_notification ("Muted for {} Seconds" .format(tempo - sec))
        self.server_notification ("Unmuter!")
        self.toca_audios("nya_button")
    
    def comando_invalido (self, trigger):
        '''alerta na tela e audio de comando invalido'''
        self.toca_audios("what")
        self.server_notification('Comando  ==> {} <== Não Existente'.format(trigger))

    

if __name__ == "__main__":
    Command().server_notification("Arquivo de propriedade extensão")
    for time in range (0,3):
        Command().server_notification(("Programa se desligando em {}".format(3-time)))
        sleep(1)
    exit()