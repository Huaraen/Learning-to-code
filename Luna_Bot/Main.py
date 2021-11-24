from commands import Server
from microfone_off import Mic
from gatilho import Audio, Datahora
audio = Audio()
dh = Datahora()


class Main:
    def __init__(self):
        self.__name_bot = "luna"
    @property
    def name_bot (self):
        return self.__name_bot
    def exe(self):
        iniciar.iniciar(self.name_bot)
        while True:
            switch.check_power()


class Iniciar:
    def iniciar (self, bot):
        print ("\nIniciando . . \n")
        checkin = input ("Por Favor, informe nick: ")
        audio.toca_audios("link_start")
        return self.__intro (checkin, bot)

    def __intro (self, checkin, bot):
        print ("{}: olá,  {}" .format (bot, checkin))
        print ("{}: Hoje é dia {}" .format (bot, dh.data))


class Switch:
    def __init__(self):
        self.estado_atual = Power_off()
        self.power = False
        
    def check_power(self):
        self.estado_atual.check_power(self)
    def ligar(self):
        self.estado_atual.ligar(self)
    def desligar(self):
        self.estado_atual.desligar(self)


class Power_on:    
    def check_power(self, Switch):
        voz = mic.power(Switch.power)
        if voz == "sleep":
            return self.desligar(Switch)
        print ("realizando comando: {}".format (voz))
    def ligar(self, Switch):
        server.server_notification ("Programa já em andamento")
    def desligar(self, Switch):
        Switch.estado_atual = Power_off()
        Switch.power = False

class Power_off:
    def check_power(self, Switch):
        if mic.power(Switch.power):
            self.ligar(Switch)
    def ligar(self, Switch):
        Switch.estado_atual = Power_on()
        Switch.power = True
    def desligar(self, Switch):
        server.server_notification ("Programa já se encontra desligado")


if __name__ == "__main__":
    iniciar  = Iniciar()
    switch   = Switch()
    server   = Server()
    main     = Main()
    mic      = Mic(main.name_bot)
    main.exe()
