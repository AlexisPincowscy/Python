# Usado para operações matemáticas
# Operação de conjuntos!!

# UNION é a união dos dois conjuntos
print("\nUNION\n")
a = {1,2,3,4}
b = {3,4,5,6}
print(a.union(b)) #imprime sem as repetições

# INTERSECTION valores que existem nos dois
print("\nINTERSECTION\n")
print(a.intersection(b))

# DIFFERENCE tudo de um conjunto sem o outro e os que repetem
print("\nDIFFERENCE\n")
print(a.difference(b)) # só o que tem no A, sem os que repetem e os do b
print(b.difference(a)) # só os que tem no B

# SYMETRIC_DIFFERENCE os que está fora das intersecções
print("\nSYMETRIC_DIFFERENCE\n")
print(a.symmetric_difference(b))
# print(b.symmetric_difference(a)) não faz diferença a ordem

# ISSUBSET saber se o conjunto está ou não contido no outro
print("\nISSUBSET\n")
c = {1,2,3,4,5}
d = {1,2,3,4,5,6,7,8,9}

print(c.issubset(d)) #vai dar TRUE -  c está contindo em d
print(d.issubset(c)) #vai retornar FALSE, pois d não está contido em c

# ISSUPERSET é para saber se um conjutno CONTEM o outro, lógica inversa
print("\nISSUPERSET\n")
print(c.issuperset(d)) #vai dar FALSE -  d não está contindo em c
print(d.issuperset(c)) #vai retornar TRUE, pois c  está contido em c

# ISDISJOINT conferir se um conjuto tem alguma intersecção (joint) com o outro
# verifica só se é true or false
print("\nISDISJOINT\n")
c = {1,2,3,4,5}
d = {1,2,3,4,5,6,7,8,9}
e = {10,11,12,13,14}

print(c.isdisjoint(e)) #true, não tem intersecção
print(c.isdisjoint(d)) #false, tem valores que aparecem nos dois conjuntos

# ADD adiciona um item, mas não o repte caso ele já exista
print("\nADD\n")
e = {10,11,12,13,14}
e.add(3) # vai adicionar o 3
print(e)
e.add(10) #não vai acrescntar outro 10 não
print(e)

# CLEAR serve para limpar a lista toda
print("\nCLEAR\n") 
e.clear() #zera tudo
print(e) #imprime um SET(conjunto) zerado

# COPY, copiar o que tem em um conjunto em outro
print("\nCOPY\n") 
d = {1,2,3,4,5,6,7,8,9}
e # estava vazio depois do clear, lembra?
e = d.copy()
print(e)

# DISCARD descarta um valor, parâmetro, passado
# REMOVE remove o valor que você escolher, parecido com o discard
# a diferença é que se o elemento não existe ele para no erro
# no discard ele não da erro, não remove nada, mas continua a aplicação
print("\nDISCARD e REMOVE\n") 
d = {1,2,3,4,5,6,7,8,9}
d.discard(3) #vai retirar o 3 da lista
d.remove(9) #vai remover o 9
print(d)

# POP retira e retorna o primeiro valor, aqui é diferente!!
print("\nPOP\n") 
d = {1,2,3,4,5,6,7,8,9}
d.add(3) #vai reacrescentar o 3 da lista
print(d)
print(d.pop())#vai retirar/retornar o 1
d.pop()#vai retirar/retornar o 2
d.pop()#vai retirar/retornar o 3
print(d)

# LEN serve para tiar o tamanho do SET, mas sem contar os duplicados
print("\nLEN\n") 
z = {1,4,3,5,6,7,8,9,3,2,4,10,10,11} #14 itens
print(len(z)) #retorna 11, pq os outros 3 são só duplicatas


# IN verificar se aquele valor está dentro daquel conjunto
print("\nLEN\n") 
z = {1,4,3,5,6,7,8,9,3,2,4,10,10,11} 
print(4 in z) #true, tem o elemento 4 no conjunto
print(33 in z) #false