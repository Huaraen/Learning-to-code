from commands import Command, Datahora
from os import remove

cmd = Command()
dh  = Datahora()

class Body:
    def __init__(self):
        '''lista usado de acordo com entendimento de voz.'''
        # trig = trigger
        self.__bot_name             = ("Luna")
        self.__trig_dia             = ["data de hoje", "dia é hoje"]
        self.__trig_hour            = ["que horas são", "diga as hora"]
        self.__trig_musica          = ["anime", "bad apple"]
        self.__trig_browser         = ["google", "navegador", "discord", "youtube", "allura", "alura", "curso", "whatsapp", "anime"]
        self.__trig_programas       = ["bloco de notas", "sul", "league of legends", "spotify", "gerenciador de tarefas"]
        self.__trig_serie_assistir  = ["peaky blinders"]
        self.__trig_turn_off        = ["desligue", "desligar", "desativar", "desative"]
        self.__trig_power_off       = ["vai pra casa", "até mais", "boa noite", "vai dormir"]

    def __procura_em_lista_e_executa_programa (self, self_lista, frase_recebida_de_voz,  palavra_comando, loop_Value = False):
        '''pega uma palavra ou frase de uma lista e executa comando com palavra_comando se existente dentro da lista.
        ** self_lista              == self.__trig_lista
        ** frase_recebida_de_voz   == trigger
        ** palavra_comando         == palavra > aqui é usado "data", "hora" .. que será executado no comando
        ** Loop_Value = True > palavra_comando += " item_loop" se necessario para executar no comando.'''
        for frase in self_lista:
            if frase in frase_recebida_de_voz:
                if loop_Value == True:
                    palavra_comando += " {}".format(frase)
                self.__executa_comandos (frase_recebida_de_voz, palavra_comando)
                return False
            else: return True

    def check_trigger(self, trigger):
        '''Filtro de comandos. Verifica comando recebido e retorna execução do comando'''
        comando_invalido = True

        if "dia" in trigger or "data" in trigger:
            check = self.__procura_em_lista_e_executa_programa(self.__trig_dia, trigger, "data")
            if check != None: comando_invalido = check
        if "hora" in trigger:
            check = self.__procura_em_lista_e_executa_programa(self.__trig_hour, trigger, "hora")
            if check != None: comando_invalido = check
           
        if "toca" in trigger or "tocar" in trigger:
            check = self.__procura_em_lista_e_executa_programa(self.__trig_musica, trigger, "tocar")
            if check != None: comando_invalido = check

        if "abrir" in trigger:
            check = self.__procura_em_lista_e_executa_programa(self.__trig_browser, trigger, "abrir", True)
            if check != None: comando_invalido = check
            check = self.__procura_em_lista_e_executa_programa(self.__trig_programas, trigger, "abrir", True)
            if check != None: comando_invalido = check

        if "procura" in trigger and "no youtube" in trigger:
            procurar = trigger.replace ("procura ","")
            procurar = procurar.replace ("no youtube", "")
            cmd.procurar_youtube(procurar)

        if "fechar" in trigger:
            check = self.__procura_em_lista_e_executa_programa(self.__trig_programas, trigger, "fechar", True)
            if check != None: comando_invalido = check

        if "mutar" in trigger:
            comando_invalido = False
            self.__executa_comandos (trigger, "mute") 

        if "assistir" in trigger and "anime" in trigger:
            comando_invalido = False
            self.__executa_comandos (trigger, ("abrir anime"))
        elif "assistir" and "série" in trigger:
            '''
            print ("qual série você deseja assistir?")
            series = []
            for serie in self.__trig_serie_assistir:
                serie.append(series+"\n")
            comprimento_series = len(series)
            for serie in range (0: comprimento_series):
                print ("{} -  {}".format(serie, series[serie]))
            ouvir_em_audio_serie_ah_assistir = input("qual filme deseja assistir? >>")
            if ouvir_em_audio_serie_ah_assistir == 1:
                cmd.internet("abrir_google")
                print ("colar url do peaky blindes.")
            '''
            cmd.server_notification("Em Construção. .")
            path = "Audios/"
            audio = "Audio_Temporario"
            cmd.cria_audio("Comando não finalizado.", audio)
            remove(path+"{}.mp3".format (audio))
            comando_invalido = False
            pass

        self.__procura_em_lista_e_executa_programa(self.__trig_turn_off, trigger, "tchau")
        power_on = self.__procura_em_lista_e_executa_programa(self.__trig_power_off, trigger, "power off")
        if power_on != None: return power_on
        
        if comando_invalido == True:
            self.__executa_comandos (trigger, "comando invalido")
            return True

        else: return True
        

    def __executa_comandos (self, trigger, comando):
        '''recebe comando, verifica e executa'''
        if comando == "data":
            dh.dia
        elif comando == "hora":
            dh.hora
        
            #  playlist.
        elif "tocar" in comando:
            for musica in self.__trig_musica:
                if musica in trigger:
                    cmd.playlist (musica)
                    break

            #  Browser
        elif "abrir" in comando:
            for browser in self.__trig_browser:
                if browser in comando:
                    cmd.abrir_aba_navegador(comando)
            for jogo in self.__trig_programas:
                if jogo in comando:
                    if comando == "abrir league of legends":
                        cmd.abrir_aplicativo("League_of_Legends")
                    elif comando == "abrir sul":
                        cmd.abrir_aplicativo("osu!")
                    elif comando == "abrir spotify":
                        cmd.abrir_aplicativo("spotify")
                    elif comando == "abrir gerenciador de tarefas":
                        cmd.abrir_programa("taskmgr")
                    elif comando == "abrir bloco de notas":
                        cmd.abrir_programa("notepad")

        elif "fechar" in comando:
            if comando == "fechar league of legends":
                cmd.fechar_aplicativo("LeagueClient")
            elif comando == "fechar sul":
                cmd.fechar_aplicativo("osu!")
            elif comando == "fechar navegador":
                cmd.fechar_aplicativo("msedge")
            elif comando == "fechar spotify":
                cmd.fechar_aplicativo("spotify")

        elif comando == "mute":
            cmd.mute(trigger)

        elif comando == "assistir":
            cmd.server_notification("Em Construção")

        elif comando == "tchau":
            cmd.toca_audios("megumu_yamerooo")
            sleep(1)
            exit()

        elif comando == "power off":
            cmd.toca_randomic_audio("beep_boop_0", 11)

        else:
            cmd.comando_invalido (trigger)


    def check_voice (self, trigger):
         # audios, mudar de lugar.
        if "fogo" in trigger or "fire" in trigger:
            cmd.server_notification("Fogoo!!", self.__bot_name)
            cmd.toca_audios("fire_fire")
        elif "macaco" in trigger:
            cmd.server_notification("", self.__bot_name)
            cmd.toca_audios("hello_monkeys")

    def paciencia(self, trigger):
        if "definir paciência em" in trigger:
            x = cmd.separar_numeros_da_frase(trigger)
            if   x ==   0: return x
            elif x ==   2: return x
            elif x ==   4: return x
            elif x ==   9: return x
            elif x ==  20: return x
            elif x == 100: return x
            else: cmd.server_notification("Paciência configurada para numeros 0, 2, 4, 9, 20 e 100.")
            return None


if __name__ == "__main__":   
    from time import sleep
    print ("Arquivo somente auxiliar.")
    for count in range (0,3):
        cmd.server_notification ("Fechando em {} sec".format ((3-count)))
        sleep(1)
    exit()