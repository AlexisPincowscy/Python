class Bicileta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("Trim, trim")
    
    def parar(self):
        print("Freeeia")

    def correr(self):
        print("Pedalando rápidooo")

    #def __str__(self): #__str__ para retornar os valores específicos
        #return f"cor: {b1.cor}, model: {b1.modelo}, ano: {b1.ano} e valor: {b1.valor}"
    
   # def __str__(self):
       # return f"{self.__class__.__name__}" #traz o nome da classe, nesse caso Bicileta

    def __str__(self): # sequancia que puxa dinâmicamente o nome da classe e seus atributos em chave valor usando op dicionário
        return f"{self.__class__.__name__}: {', '. join(f'{chave} = {valor}' for chave, valor in self.__dict__.items())}"
    
b1 = Bicileta("azul", "Caloi", 2020, 2350.50)

print(f"Foi vendida a {b1}")
b1.buzinar()