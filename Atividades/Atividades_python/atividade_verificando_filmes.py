class Filme():
    '''armazena titulo e diretor, imprimindo formatado quando chamado pelo mesmo'''
    def __init__(self, titulo, diretor = ''):
        self.titulo = titulo
        self.diretor = diretor
    def __str__(self):
        return self.titulo + ' - ' + self.diretor
    def __eq__(self, outro_filme):
        return self.titulo == outro_filme.titulo

a = Filme("A Teoria de Tudo", "James Marsh")
b = Filme("La La Land", "Damien Chazelle")
c = Filme("O Poderoso Chefão", "Francis Ford Coppola")

def pega_todos_os_filmes():
    '''return list'''
    babaduba = [b, c, a]
    return babaduba

def tenho_o_filme(filme_procurado):
    '''return True or False'''
    meus_filmes = pega_todos_os_filmes()
    return filme_procurado in meus_filmes
    

if __name__ == "__main__":
    for filmes in pega_todos_os_filmes():
        print (filmes)
    
    filme_procurado = Filme('A Teoria de Tudo')
    if tenho_o_filme(filme_procurado):
        print('Tenho o filme!')
    else:
        print('Não tenho :(')