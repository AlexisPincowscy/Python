# testa se está utilziando a mesma região de memória
# comando IS para ver se ocupa e IS NOT para ver se não ocupa

valor = 1000
nome = "Carlos"
Conta = valor
Aluno = nome

print(Aluno is nome)

print(Conta is valor)

print(Conta is Aluno)

print(Aluno is not Conta)