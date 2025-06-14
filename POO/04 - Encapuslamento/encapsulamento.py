class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo
        
    def depositar(self):
        pass

    def sacar(self):
        pass
    
    def mostrar_saldo(self):
        return self._saldo

conta = Conta(100)
print(conta._saldo) # não é correto, o python não garante a privacidade, mas por convenção _ antes traz uma variável no códgio
print(conta.mostrar_saldo()) # aplicação correta de encapsulamento em Python