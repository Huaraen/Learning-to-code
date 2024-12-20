# -*- coding: UTF-8 -*-

'''
Para evitarmos o uso de if, criamos classes mães e filhas.. :

def aplica_desconto_extra(self):
    if (self.estado_atual == Orcamento.EM_APROVACAO):
        self.__desconto_extra+= self.valor * 0.05
    elif(self.estado_atual == Orcamento.APROVADO):
        self.__desconto_extra+= self.valor * 0.02
    elif(self.estado_atual == Orcamento.REPROVADO):
        raise Exception('Orçamentos reprovados não recebem desconto extra')
    elif(self.estado_atual == Orcamento.FINALIZADO):
        raise Exception('Orcamentos finalizados não recebem desconto extra')
        
'''

from abc import ABCMeta, abstractmethod

class Estado_de_um_orcamento(object):
    __metaclass__ = ABCMeta
    def __init__(self):
        self.desconto_aplicado = False
    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass
    @abstractmethod
    def aprova(self, orcamento):
        pass
    @abstractmethod
    def reprova(self, orcamento):
        pass
    @abstractmethod
    def finaliza(self, orcamento):
        pass

class Em_aprovacao(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        if (not self.desconto_aplicado):
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
            self.desconto_aplicado = True    
        else:
            raise Exception('Desconto já aplicado')
    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()
    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()
    def finaliza(self, orcamento):
        raise Exception('Orcamento em aprovação não podem ir para finalizado diretamente')
    
class Aprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        if (not self.desconto_aplicado):
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')
    def aprova(self, orcamento):
        raise Exception('Orçamento já está em estado de aprovação')
    def reprova(self, orcamento):
        raise Exception('Orçamento está em estado de aprovação e não pode ser reprovado')
    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()

class Reprovado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')
    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser aprovado')
    def reprova(self, orcamento):
        raise Exception('Orçamento já está em estado de reprovação')
    def finaliza(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser finalizado')

class Finalizado(Estado_de_um_orcamento):
    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orcamentos finalizados não recebem desconto extra')
    def aprova(self, orcamento):
        raise Exception('Orçamento finalizado já foi aprovado')
    def reprova(self, orcamento):
        raise Exception('Orçamento já finalizado não pode ser reprovado')
    def finaliza(self, orcamento):
        raise Exception('Orçamento já foi finalizado')


class Orcamento(object):

    def __init__(self):
        self.__itens = []
        # começa com o estado em aprovação 
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0

   # nova implementação de aplica_desconto_extra
    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)
    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto
    def aprova(self):
        self.estado_atual.aprova(self)
    def reprova(self):
        self.estado_atual.reprova(self)
    def finaliza(self):
        self.estado_atual.finaliza(self)

    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra

    # retornamos uma tupla, já que não faz sentido alterar os itens de um orçamento
    def obter_itens(self):
        return tuple(self.__itens)

    # perguntamos para o orçamento o total de itens
    @property
    def total_itens(self):
        return len(self.__itens)

    def adiciona_item(self, item):
        self.__itens.append(item)

# um item criado não pode ser alterado, suas propriedades são somente leitura
class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        return self.__valor

    @property
    def nome(self):
        return self.__nome

if __name__ == '__main__':
    orcamento = Orcamento()
    orcamento.adiciona_item(Item('Item A', 100.0))
    orcamento.adiciona_item(Item('Item B', 50.0))
    orcamento.adiciona_item(Item('Item C', 400.0))
    orcamento.aplica_desconto_extra() 
    print (orcamento.valor) # imprime 522.5 porque descontou 5% de 550.0
    
    orcamento.aprova()
    orcamento.aplica_desconto_extra() 
    print (orcamento.valor) # imprime 512.05 porque descontou 2% de 522.5
    
    orcamento.finaliza()
    # orcamento.aplica_desconto_extra() # lança exceção, porque não pode aplica desconto em um orçamento finalizado