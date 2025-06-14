from abc import ABC, abstractmethod
# importar biblioteca para transformar a classe em abstrata

class Controle(ABC):

    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractmethod
    def marca(self):
        pass

class ControleTV(Controle):
    #como a classe Contole é abstrata, Interface, eu sou obrigado a construir (polimorfismo) os métodos
    def ligar(self):
        print("Ligando")

    def desligar(self):
        print("Desligar")

    @property
    def marca(self):
        return "LG"
    

c1 = ControleTV()
c1.ligar()
c1.desligar()
print(c1.marca)