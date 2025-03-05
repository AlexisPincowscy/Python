# a função F string serve para interpolar (misturar) tipos de dados na string.

nome = "Alex"
idade = 36
profissao = "estudante"
altura = 1.8023

print(f"{nome} tem {idade} anos e trabalha na função de {profissao}")
print(f"{nome} tem {altura:.2f} de altura") #exemplo para colcoar 2 casa decimais
print(f"{nome} tem {altura:10.2f} de altura")#o primeiro nome antes do .2f seria a quantidade de casas a esquerda
# existem outrso métodos, que são antigos como % e .format, mas já não são utilizados