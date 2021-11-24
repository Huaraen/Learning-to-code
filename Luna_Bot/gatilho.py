from commands import Utility, Datahora, Audio, Server, Browser, App
from random import randrange
from time import sleep

utility = Utility()
dh  = Datahora()
audio = Audio()
server = Server()
browser = Browser()
app = App("Atalhos")


class Body:
    def __init__(self, prox_comando=None):
        self.__bot = "luna"
        self.__prox_comando = prox_comando

    def proximo_comando_a_ser_executado (self, voice):
        '''retorna string'''
        if self.__prox_comando is None:
            return ''
        else:
            return self.__prox_comando.check(voice)
    
    @property
    def bot (self):
        '''retorna string do bot'''
        return self.__bot
    @property
    def bot_name(self):
        '''retorna string do bot formatado'''
        return self.__bot.title()

    def procura_em_lista_e_executa_programa (self, self_lista, comando_de_voz):
        for frase in self_lista:
            if frase in comando_de_voz:
                sett.check_comando_executado("comando executado")
                return True
        return False


class Set_up:
    def __init__(self):
        self.__tolerance = 2
        self.__anger = 0 # pegar em um arquivo e transformar em int para que o mesmo sempre fique salvo.
        self.algum_comando_foi_executado = Comando_nao_executado()
        self.executaaadoooo = False
        
    @property
    def mood (self):
        '''check quantidade de raiva'''
        return self.__anger
    @property
    def tolerance(self):
        return self.__tolerance

    def check_comando_executado(self, comando):
        return self.algum_comando_foi_executado.check_comando_executado(self, comando)
    def comando_executado (self):
        self.algum_comando_foi_executado.comando_executado(self)
    def comando_nao_executado (self):
        self.algum_comando_foi_executado.comando_nao_executado(self)


class Comando_ja_executado:
    def check_comando_executado (self, Setup, comando):
        if comando == "startando comandos":
            self.comando_nao_executado(Setup)
        elif comando == "comando foi executado":
            return True            
    def comando_executado (self, Setup):
        server.server_notification("comando já foi executado")
    def comando_nao_executado (self, Setup):
        Setup.algum_comando_foi_executado = Comando_nao_executado()
        Setup.executaaadoooo = False

class Comando_nao_executado:
    def check_comando_executado (self, Setup, comando):
        if comando == "comando executado":
            self.comando_executado(Setup)
        elif comando == "comando foi executado":
            return False
    def comando_executado (self, Setup):
        Setup.algum_comando_foi_executado = Comando_ja_executado()
        Setup.executaaadoooo = True
    def comando_nao_executado (self, Setup):
        server.server_notification("comando ainda não foi executado")


class Angry:
    def angry (self):
        '''retorna True caso ela esteja brava'''
        roll20 = randrange(1,21)
        if roll20 <= sett.mood:
            audio.toca_randomic_audio("angry_", 6)
            just__voice._change_mood(1)
            return True
        else: return False


class Just_voice:
    def _change_mood(self, anger):
        '''soma raiva atual com a causa'''
        sett.__anger += anger
        if sett.mood < 0: sett.__anger = 0

    def check(self, voz):
        # audios, mudar de lugar.
        if angry.angry(): return "angry"
        elif sett.mood >= 9 and "desculp" in voz:
            x = audio.toca_randomic_audio("angry_mood_sorry_", stop=4)
            if x == 1: self._change_mood (-4)
            else: self._change_mood (-2)
            return "still angry "
        else:
            if   "fogo" in voz or "fire" in voz:
                server.server_notification("Fogoo!!", body.bot_name)
                audio.toca_audios("fire_fire")
                return "audio "
            elif "macaco" in voz or "trol" in voz:
                server.server_notification("\n.   _/﹋\_\n    (҂`_´)\n    <,︻╦̵̵̿╤─ ҉     ~  •", Body().bot_name)
                audio.toca_audios("hello_monkeys")
                return "audio "
            elif "é um robo" in voz:
                audio.toca_randomic_audio("are_you_a_bot_", 6)
                return "audio "
            elif "*" in voz:
                audio.toca_randomic_audio("been_rude_with_bot_", 2)
                self._change_mood (4)
                return "audio "
            elif "sentido da vida" in voz:
                audio.toca_audios("meaning_of_life", "bot")
                self._change_mood (-1)
                return "audio "
            elif "sobre você" in voz:
                audio.toca_randomic_audio("tell_me_something_about_yourself_", 4)
                return "audio "
            elif "você é d" in voz or "você veio d" in voz or "nasceu" in voz:
                audio.toca_randomic_audio("where_are_you_from_", 8)
                self._change_mood (-1)
                return "audio "
            elif "vinho" in voz:
                audio.toca_audios("osmanthus_wine_taste_the_same_as_I_remember","bot")
                self._change_mood (-1)
                return "audio "
            elif "você é solteir" in voz:
                audio.toca_audios("are_you_single","bot")
                return "audio "
            return "sem audio "


class Set:
    def check (self, voz):
        __config_options = ["defin", "mude", "mudar", "set"]
        if body.procura_em_lista_e_executa_programa(__config_options, voz, "paciência"):
            if "paciência" in voz: self.__paciencia(voz)
            elif "humor"   in voz: self.__irritada (voz)
            
    def __set_anger(self, new_anger):
        sett.__anger = new_anger
        if sett.__anger is None: sett.__anger = 0
    def __set_tolerance(self, new_tolerance):
        sett.__tolerance = new_tolerance
        if sett.__tolerance is None: sett.__tolerance = 2

    def __irritada(self, trigger):
        new_anger = utility.separar_numeros_da_frase(trigger)
        try:
            audio.toca_audios("number_{}".format(new_anger), "bot")
        except:
            raise server.server_notification("Executando..")
        finally:
            for random_number in randrange(1, 5):
                if   random_number == 1:
                    audio.toca_audios("yeah_no_problem", "bot")
                elif random_number == 2:
                    audio.toca_audios("roger_that", "bot")
                elif random_number == 3:
                    audio.toca_audios("jp_wakatta", "bot")
                elif random_number == 4:
                    audio.toca_audios("oky", "bot")
            self.__set_anger (new_anger)

    def __paciencia(self, trigger):
        new_tolerance = utility.separar_numeros_da_frase(trigger)
        try:
            audio.toca_audios("number_{}".format(new_tolerance), "bot")
        except:
            raise server.server_notification("Executando..")
        finally:
            for random_number in randrange(1, 5):
                if   random_number == 1:
                    audio.toca_audios("yeah_no_problem", "bot")
                elif random_number == 2:
                    audio.toca_audios("roger_that", "bot")
                elif random_number == 3:
                    audio.toca_audios("jp_wakatta", "bot")
                elif random_number == 4:
                    audio.toca_audios("oky", "bot")
            self.__set_tolerance (new_tolerance)


class Unknown_command:
    def check(self, voz):
        if not sett.check_comando_executado("comando foi executado"):
            x =  just__voice.check(voz)
            if "sem audio" in x:
                audio.toca_audios("what")
                server.server_notification('Comando  ==> {} <== Não Existente'.format(voz))
                return "comando desconhecido"
            else: return x
        else: return "comando já executado"


class Verifica_voz(Body):
    def realiza_comandos (self, voz):
        sett.check_comando_executado("startando comandos")
        lista_de_comandos = Dia(Hora(Musica(Navegador(Programas_abrir(Programas_fechar
        (Algo_youtube(Mute(Desligar(Unknown_command())))))))))
        return lista_de_comandos.check(voz)
    
    def command_voice(self, voz):
        '''retorna set config, unknown command ou lista de comandos'''
        config_options = ["defin", "mude", "mudar"]
        for gatilho in config_options:
            if gatilho in voz: return sett.check(voz)
        if "unknown command" in voz: return unknown__commando.check()
        else: 
            print ("executando comando com bot")
            return self.proximo_comando_a_ser_executado(voz)
    
    def voz_bot(self):
        '''executa comando de voz ao chamar pelo bot'''
        audio.toca_audios("nya_button")
    def just_voice(self, voz):
        '''executa comando quandos solicitado somente voz'''
        return just__voice.check(voz)


class Base_Comandos(Body):
    def check(self, voz):
        if self.tem_palavra_chave_e_comando(voz):
            return self.executa_comando(voz)
        else: return self.nao_tem_comando_ir_ao_proximo_da_lista(voz)

    def tem_palavra_chave_e_comando (self, voz):
        pass
    def executa_comando (self, voz):
        pass
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        pass


class Dia(Base_Comandos):
    __trig_dia = ["data de hoje", "dia é hoje"]
    def tem_palavra_chave_e_comando (self, voz):
        if "dia" in voz or "data" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_dia, voz)
        else: return False
    def executa_comando (self, voz):
        dh.dia
        return "dia " + self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)
        

class Hora(Base_Comandos):
    __trig_hour = ["que horas são", "diga as hora"]
    def tem_palavra_chave_e_comando (self, voz):
        if "hora" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_hour, voz)
        return False            
    def executa_comando (self, voz):
        dh.hora
        return "horas " + self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Musica(Base_Comandos):
    __trig_musica = ["anime", "bad apple"]
    def tem_palavra_chave_e_comando (self, voz):
        if "toca" in voz or "tocar" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_musica, voz)
        else: return False
    def executa_comando (self, voz):
        for musica in self.__trig_musica:
            if musica in voz:
                audio.playlist (musica)
        return "tocando musica " + self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)
        

class Navegador(Base_Comandos):
    __trig_browser = ["google", "navegador", "discord", "youtube", "allura", "alura", "curso", "whatsapp", "anime"]
    def tem_palavra_chave_e_comando (self, voz):
        if "abrir" in voz or "abre" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_browser, voz)
        return False
    def executa_comando (self, voz):
        for aba_browser in self.__trig_browser:
            if aba_browser in voz:
                browser.abrir_aba_navegador(aba_browser)
        return "abrir navegador " + self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Programas_abrir(Base_Comandos):
    __trig_programas = ["bloco de notas", "sul", "league of legends", "navegador", "spotify", "gerenciador de tarefas"]
    def tem_palavra_chave_e_comando (self, voz):
        if "abrir" in voz or "abre" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_programas, voz)
        else: return False
    def executa_comando (self, voz):
        if "league" in voz or "legends" in voz:
            app.abrir_aplicativo("League_of_Legends")
        elif "spotify" in voz:
            app.abrir_aplicativo("spotify")
        elif "sul" in voz:
            app.abrir_aplicativo("osu!")
        elif "bloco de notas" in voz:
            app.abrir_programa("notepad")
        elif "gerenciador de tarefas" in voz:
            app.abrir_programa("taskmgr")
        return "programa aberto " + self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Programas_fechar(Programas_abrir):
    __trig_programas = ["bloco de notas", "sul", "league of legends", "navegador", "spotify"]
    def tem_palavra_chave_e_comando (self, voz):
        if "fecha" in voz:
            return self.procura_em_lista_e_executa_programa(self.__trig_programas, voz)
        else: return False
    def executa_comando (self, voz):
        if "navegador" in voz:
            app.fechar_aplicativo("msedge")
        elif "league" in voz or "legends" in voz:
            app.fechar_aplicativo("LeagueClient")
        elif "spotify" in voz:
            app.fechar_aplicativo("spotify")
        elif "sul" in voz:
            app.fechar_aplicativo("osu!")
        elif "bloco de notas" in voz:
            app.fechar_aplicativo("notepad")
        return "fechando app " + self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Algo_youtube(Base_Comandos):
    def tem_palavra_chave_e_comando (self, voz):
        if  "procur" in voz and " no youtube" in voz or "pesquis" in voz and " no youtube" in voz:
            return True
        else: return False
    def executa_comando (self, voz):
        pesquisar_sobre = self.formatacao_para_pesquisar(voz)
        browser.procurar_youtube(pesquisar_sobre)
        sett.check_comando_executado("comando executado")
        return "youtube " + self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)

    def formatacao_para_pesquisar(self, voz):
        __filtro_de_palavras = ["procurar", "procure", "procura", "sobre", "no youtube", "pesquisar", "pesquise", "pesquisa", "pra mim", "para mim"]
        for palavras in __filtro_de_palavras:
            if palavras in voz:
                voz = voz.replace (palavras+' ', "")
                voz = voz.replace (' '+palavras, "")
        return voz

class Desligar(Base_Comandos):
    __trig_turn_off = ["desligue", "desligar", "desativar", "desative"]
    def tem_palavra_chave_e_comando (self, voz):
        return self.procura_em_lista_e_executa_programa(self.__trig_turn_off, voz)
    def executa_comando (self, voz):
        audio.toca_randomic_audio("beep_boop_", 11)
        sleep(1)
        exit()
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)


class Mute(Base_Comandos):    
    __trig_mute = ["mutar", "mute", "silenci", "quiet"]
    def tem_palavra_chave_e_comando (self, voz):
        return self.procura_em_lista_e_executa_programa(self.__trig_mute, voz)
    def executa_comando (self, voz):
        server.mute(voz)
        return "muted " + self.proximo_comando_a_ser_executado (voz)
    def nao_tem_comando_ir_ao_proximo_da_lista (self, voz):
        return self.proximo_comando_a_ser_executado (voz)

body              = Body()
angry             = Angry()
sett              = Set_up()
just__voice       = Just_voice()
unknown__commando = Unknown_command()

if __name__ == "__main__": 
    while True:
        voice = (input(">> "))
        Verifica_voz().realiza_comandos(voice)
        if voice == "sair":
            exit()
