class Passaro:
    def voar(self):
        pass

class Pardal (Passaro):
    def voar(self):
        print("Voando")

class Aveztruz (Passaro):
    def voar (self):
        print("Eu não sei voar")


def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
a1 = Aveztruz()

plano_de_voo(p1)
plano_de_voo(a1)