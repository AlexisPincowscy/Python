class Veiculo:
    def __init__(self, cor, placa, n_rodas):
        self.cor = cor
        self.place = placa
        self.n_rodas = n_rodas
    
    def ligar():
        pass



class Moto(Veiculo):
    def __init__(self, cor, placa, n_rodas, motor):
        super().__init__(cor, placa, n_rodas)
        self.motor = motor

    def ligar(self):
        print('Motor ligado' if self.motor == True else "Motor desligado")

    def __str__(self):
        super().__str__()
        return f"{self.__class__.__name__}: {(', '.join (f'{chave} = {valor}' for chave, valor in self.__dict__.items()))}"
    

moto = Moto('vermelha','abc-009',2,False)
moto.ligar()
moto.motor = True
moto.ligar()
print(moto)

# class Carro(Veiculo):
#     pass

# class Caminhao(Veiculo):
#     pass