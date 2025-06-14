class Cachorro:
    def __init__(self, nome, raca, cor):
        # inicialziando a classe
        self.nome = nome
        self.raca = raca
        self.cor = cor

    def latir(self):
        print("Au au")

    def __del__(self):
        print("Removendo a instância da classe")
    
        
c = Cachorro('rocky', 'frenhcie', 'preto')
c.latir()
print(c.nome)
# ele sempre vai executar e depois removar a instância no final.
# caso queira que essa instÂcia seja deletada antes
# digitar 'del e o nome da instância", nesse caso seria 'del c' 