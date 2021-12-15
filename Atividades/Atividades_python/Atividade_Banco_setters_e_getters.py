

class Conta:
    def __init__(self, numero, titular, saldo, limite):
         # Atributos e atributos privados
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

         # métodos e métodos privados
    def depositar(self, valor):
        self.__saldo += valor 

    def __valor_disponivel(self, valor_a_sacar):
        valor_disponivel = self.saldo + self.limite
        return valor_a_sacar <= valor_disponivel

    def sacar(self, valor):
        if self.__valor_disponivel(valor):
            self.__saldo -= valor
        else:
            print ("Seu saldo é de {}, sendo insuficiente para o saque de {}." .format (self.__saldo, valor))

    def extrato(self):
        print("Saldo {}".format(self.__saldo))

    def transferir (self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)

            # propriedades #
        ## setters e getters ##

    @property
    def titular (self): # def get_titular (self):
        return self.__titular

    @property    
    def saldo (self): # def get_saldo (self):
        return self.__saldo 
    
                # Tornando os Sintaxes Amigaveis.. #

    @property # dessa forma, ao invez de fazer "get_limite", apenas por "conta.limite" eu consigo pegar o valor.
    def limite (self): # antes sendo def get_limite (self):
        return self.__limite

    @limite.setter # com a propriedade limite criado acima, podemos alterar o "set_limite" para um ".setter" conseguindo alterar a conta com "conta.limite = x"
    def limite (self, limite): # antes sendo "def set_limite (self, limite):"
        self.limite = limite 

    @staticmethod
    def codigos_bancos(): #chamando "Conta.codigo_banco()" a gente consegue chamar esse método sem que tenhamos um objeto criado.
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}



##Além desse princípio de responsabilidade única existem outras que foram definidos através do Robert C. Martin no início dos anos 2000 e são conhecidos pelo acrônimo SOLID:

'''
S - Single responsibility principle
O - Open/closed principle
L - Liskov substitution principle
I - Interface segregation principle
D - Dependency inversion principle
'''

huara = Conta("01", "huara", 0, 2000)
huara.depositar (500)
print (huara.saldo)

rafa = Conta('2', 'rafa', 0, 5000)
rafa.depositar(1000)
print (rafa.saldo)

huara.transferir (200, rafa)
print (huara.saldo)
print (rafa.saldo)

