 #  Orientação e Objetos


class Programas:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def dar_like(self):
        self._likes += 1

    @property
    def likes (self):
        return self._likes

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome (self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return ("Nome: {} - Ano: {}, likes: {}." .format (self._nome, self.ano, self._likes))


class Filme(Programas):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao

    def __str__(self):
        return ("Nome: {} - Ano: {}, {} Minutos, - likes: {}." .format (self._nome, self.ano, self.duracao, self._likes))


class Serie(Programas):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas

    def __str__(self):
        return ("Nome: {} - Ano: {}, {} Temporadas, - likes: {}." .format (self._nome, self.ano, self.temporadas, self._likes))


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas  = programas

         # Duck Typing > brincadeira da comunidade. "Se comporta como um".

    def __getitem__ (self, item):
        return self._programas [item]


          ## Duck Typing ##
         # com isso eu não preciso me preocupar em herdar uma classe built-in como (list)p ara deixar essa classe "Playlist" como um iteravel,
          ## Se eu sei que ela é, (ou a brincadeira da comunidade, se ela fala como um pato, anda como um pato e se parece como um pato, ele é um pato.)
          ## e é por isso que existe esses "Magic Methods", esses aspéctos mais indiomáticos da sintaxe do python, esses métodos com "dois underlines( __ )"

    @property
    def listagem(self):
        return self._programas

    def __len__(self):
        return len(self._programas)

vingadores = Filme("vingadores - Guerra Infinita", 2019, 160)
atlanta = Serie("atlanta", 2018, 2)
tmep = Filme("Todo mundo em panico", 1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
tmep.dar_like()
demolidor.dar_like()
vingadores.dar_like()
atlanta.dar_like()
tmep.dar_like()
vingadores.dar_like()
demolidor.dar_like()
tmep.dar_like()
vingadores.dar_like()
demolidor.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
atlanta.dar_like()
vingadores.dar_like()
atlanta.dar_like()
tmep.dar_like()
atlanta.dar_like()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print ("Tamanho da listagem: {}".format (len(playlist_fim_de_semana)))

for programa in playlist_fim_de_semana:
   print(programa)








































