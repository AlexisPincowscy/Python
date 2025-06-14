class Animal:
    def __init__(self, cor):
        self.cor = cor

    def __str__(self):
        return f"{self.__class__.__name__}: {(', '.join(f'{chave} = {valor}' for chave,valor in self.__dict__.items()))}"

class Mamifero(Animal):
    def __init__(self, n_patas, **kw):
        super().__init__(**kw)
        self.n_patas = n_patas

class Aves(Animal):
    def __init__(self, bico, **kw):
        super().__init__(**kw)
        self.bico = bico

class Ornitorrinco (Aves, Mamifero):
    pass

# uso de KW para acrescnetar na classe pai os atribvutos misturados, código fica confuso com as travas
ornitorrinco = Ornitorrinco(bico='amarelo', cor='marrom', n_patas=4)
print(ornitorrinco)