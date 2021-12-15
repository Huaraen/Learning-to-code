class Data:
	def comm_data(self, voz):
		print ("realizando commnd data")
		if "data" in voz:
			print ("data enviada")

class Hora:
	def comm_hora(self, voz):
		print ("realizando commnd hora")
		if "hora" in voz:
			print ("hora enviada")

class Comandos_procedural:
	def realiza_comando(self, voz, comando):
		if comando == "hora":
			comando_realizado = hora.comm_hora(voz)
		if comando == "data":
			comando_realizado = dia.comm_data(voz)
		print ("Comandos_procedural_realizado")
		return comando_realizado


class Voz:
	def mic(self):
		x = input(">>>: ")
		return x

voz = Voz()
dia = Data()
hora = Hora()
cmd_prcd = Comandos_procedural()
voice = "a hora da dona joana é curta"
cmd_prcd.realiza_comando(voice, "hora")
cmd_prcd.realiza_comando(voice, "data")

class Data_cmd:
	def cmd(self, voz):
		print ("realizando commnd data")
		if "data" in voz:
			print ("data enviada")
class Hora_cmd:
	def cmd(self, voz):
		print ("realizando commnd hora")
		if "hora" in voz:
			print ("hora enviada")

class Comandos:
	def realiza_comando(self, voz, estrategia_que_reprezenta_o_comando):
		comando_realizado = estrategia_que_reprezenta_o_comando.cmd(voz)

voice = "que data você vai ganhar um novo plaixtaichan"

Comandos().realiza_comando(voice, Hora_cmd())
Comandos().realiza_comando(voice, Data_cmd())

class Controle_de_voz_versao_01:
	def cmd(self, voz):
		if "batata" in voz:
			return "batata"
		elif "pera" in voz:
			return "pera"

''' eliminando Ifs '''

class Comando_batata:
	def cmd(self, voz):
		if "batata" in voz:
			return "batata"
		else: return "comando_invalido"
class Comando_pera:
	def cmd(self, voz):
		if "pera" in voz:
			return "pera"
		else: return "comando_invalido"

class Controle_de_voz_versao_02:
	def cmd(self, voz):
		comando = Comando_pera().cmd(voz)
		if comando == "comando_invalido":
			comando = Comando_batata().cmd(voz)
		return comando

'''---------------------------- ------------------------'''

class Comando_banana:
	'''realizando cadeia do construtor'''
	def __init__(self, proximo_comando):
		self.__proximo_comando = proximo_comando
	def cmd(self, voz):
		if "banana" in voz:
			print ("banana")
			return "banana"
		else: return self.__proximo_comando.cmd(voz)
class Comando_melancia:
	'''realizando cadeia do construtor'''
	def __init__(self, proximo_comando):
		self.__proximo_comando = proximo_comando
	def cmd(self, voz):
		if "melancia" in voz:
			print ("melancia")
			return "melancia"
		else: return self.__proximo_comando.cmd(voz)
class Comando_sem_fruta:
	def cmd(self, voz):
		return "sem fruta"

class Controle_de_voz_versao_03:
	'''Chain of Responsability, realizando cadeia do construtor'''
	def cmd(self, voz):
		comando = Comando_banana(Comando_melancia(Comando_sem_fruta())).cmd(voz)
		return comando

voice = "salada de fruta com melancia não é nada comparado a banana salada de fruta"
controle = Controle_de_voz_versao_03()
comando_realizado = controle.cmd(voice)

print ()
print ()
print ()

class Cor_maister:
	def __init__ (self, outra_cor=None):
		self.__outra_cor = outra_cor
	def chamando_outra_cor(self, voz):
		if self.__outra_cor is None: return ''
		return self.__outra_cor.que_cor_eh_esse(voz)
	

from abc import ABCMeta, abstractmethod
class Cores(Cor_maister):
	__metaclass__ = ABCMeta
	def que_cor_eh_esse(self, voz):
		if self.verifica_se_tem_cor(voz):
			return self.tem_cor(voz) + self.chamando_outra_cor(voz)
		else: return self.nao_tem_cor(voz) + self.chamando_outra_cor(voz)
	@abstractmethod
	def verifica_se_tem_cor(self, voz):
		pass
	@abstractmethod
	def tem_cor (self, voz):
		pass
	@abstractmethod
	def nao_tem_cor (self, voz):
		pass
class Preta(Cores):
	def verifica_se_tem_cor(self, voz):
		return "preta" in voz
	def tem_cor (self, voz):
		return ("tem a cor {}. ".format ("preta"))
	def nao_tem_cor (self, voz):
		return "não tem cor. "
class Branca(Cores):
	def verifica_se_tem_cor(self, voz):
		return "branca" in voz
	def tem_cor (self, voz):
		return ("tem a cor {}. ".format ("branca"))
	def nao_tem_cor (self, voz):
		return "não tem cor. "
class Rosa(Cores):
	def verifica_se_tem_cor(self, voz):
		return "rosa" in voz
	def tem_cor (self, voz):
		return ("tem a cor {}. ".format ("rosa"))
	def nao_tem_cor (self, voz):
		return "não tem cor. "
class Amarela(Cores):
	def verifica_se_tem_cor(self, voz):
		return "amarela" in voz
	def tem_cor (self, voz):
		return ("tem a cor {}. ".format ("amarela"))
	def nao_tem_cor (self, voz):
		return "não tem cor. "

class Controle_de_voz_versao_04:
	def cmd(self, voz, cores):
		comando = cores.que_cor_eh_esse(voz)
		print (comando)

poema = "as cores brancas em meu pomar são puras, pretas, rosas amarelas e lilas"
x = Controle_de_voz_versao_04()
todas_as_cores = Branca(Rosa(Amarela(Preta())))
x.cmd(poema, todas_as_cores)

class Anime(object):

	Isekai 	 = 1
	Romance  = 2
	Aventura = 3
	Fantasia = 4

	def __init__(self):
		self.genero_anime = 1

	def informa_genero(self):
		if self.genero_anime == Anime.Isekai:
			print ("genero *Isekai* é muito bom!!")
		elif self.genero_anime == Anime.Romance:
			print ("genero *Romance* é muito bom!!")			
		elif self.genero_anime == Anime.Aventura:
			print ("genero *Aventura* é muito bom!!")
		elif self.genero_anime == Anime.Fantasia:
			print ("genero *Fantasia* é muito bom!!")

if __name__ == "__main__":
	batata = Anime()
	batata.informa_genero()
	batata.genero_anime = Anime.Aventura
	batata.informa_genero()
	batata = Anime()
	batata.informa_genero()