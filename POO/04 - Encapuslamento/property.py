class Foo:
    def __init__(self, valor):
        self._valor = valor
    
    @property # transforma o método em atributo
    def x(self):
        return self._valor or 0
    
    @x.setter # criar o setter com o mesmo nome, para conseguir alterar o valor do atributo
    def x(self, valor):
        self._valor = valor

    @x.deleter # pode ser para apagar ou settar um valor que sirva como um "delete"
    def x(self):
        self._valor = 0 #chamando o atributo del ele vai zerar o valor


foo = Foo(10)
print(foo.x) # tendo usando o property eu posso chamar o x como atributo e não método

del foo.x
print(foo.x)


foo.x = 40 # dessa maneira não será possível de alterar o valor, é necessário criar o setter
print(foo.x) # agora valor alterado para 40