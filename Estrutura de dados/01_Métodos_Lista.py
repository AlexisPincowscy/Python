# Métodos da lista já interno do Python
# append - acrscenta itens na lista
print("Falando de APPEND:\n")
lista1 = []

lista1.append(1)
lista1.append(["python", 150])
lista1.append(["Banana, maça"])

print(f"O que tem na lista1 é: {lista1}")

# método CLEAR, como o nome diz, limpa a lista

lista1.clear()
print(f"O que tem na lista1 agora é: {lista1}")

# método COPY, copia para outra lista, mas são objetos diferentes, o que faz em um, não passa para o outro
# a não ser que faça no outro tbm. Novos comandos feitos nas listas não afetam as outras.
print("\n\n Falando de COPY:\n")
lista1 = []

lista1.append(1)
lista1.append(["python", 150])
lista1.append(["Banana, maça"])

lista2 = lista1.copy()
print(f"O que tem na lista1 é: {lista1} \ne na lista2 {lista2} também!")

lista1.append("java")
print(f"O que tem na lista1 agora é: {lista1}")

lista2[1] = "Macaco Louco"
print(f"Mas a lista2 agora é : {lista2}")

# método COUNT, conta quantas vezes um objeto aparece em determinada lista
# o parâmetro é o obejto e o resultado vai ser int
print("\n\n Falando de COUNT:\n")
lista3 = ["vermelho", "azul", "vermelho", "verde", "vermelho", "azul"]
print(f"Têm {lista3.count("vermelho")} vezes essa cor")
print(f"Têm {lista3.count("azul")} vezes essa cor")
print(f"Têm {lista3.count("verde")} vezes essa cor")

# método EXTEND, acrescenta os valores no final da lista
# esses valores podem ser repetidos
print("\n\n Falando de EXTEND:\n")
carros = ["ferrari", "volks", "fiat"]

carros.extend(["ferrari", "alfa romeo", "fiat"])
print(carros)

# método INDEX, serve para mostrar a PRIMEIRA ocorrência do item na lista
print("\n\n Falando de INDEX:\n")
print(f"O Fiat aparece, pela primeria vez, na posição: {carros.index("fiat")}")
print(f"O Fiat aparece, pela primeria vez, na posição: {carros.index("alfa romeo")}")

# método POP, exclúi os items em forma de pilha (o último a entrar é o primeiro a sair)
print("\n\n Falando de POP:\n")
print(carros)
print(carros.pop()) # forma padrão vai remover o último
print(carros.pop())
print(carros.pop(0)) # você pode delimitar qual item escolher
print(carros)

# método REMOVE, exclúi a primeira ocorrência do item descrito
print("\n\n Falando de REMOVE:\n")
linguagens = ["python", "c", "java", "c", "go lang"]

print(linguagens)
linguagens.remove("c")
print(linguagens)

# método REVERSE, ele coloca a lista ao contrátio
print("\n\n Falando de REVERSE:\n")
linguagens2 = ["python", "c", "java", "go lang"]

print(linguagens2)
linguagens2.reverse()
print(linguagens2)

# método SORT, ordena a lista, por padrão vao ordenar em alfabético
print("\n\n Falando de SORT:\n")
linguagens3 = ["python", "c", "java", "go lang", "csharp"]
linguagens3.sort() # ordem alfabética
print(linguagens3)

linguagens3.sort(reverse=True) #vai trazer de traz para frente, mantendo a ordem alfabética
print(linguagens3)

linguagens3.sort(key=lambda x: len(x)) #vai trazer do menor para o maior, funão interna lambda
print(linguagens3)

linguagens3.sort(key=lambda x: len(x), reverse=True) #vai trazer do menor para o maior tamanho na ordem invertida
print(linguagens3)

# método LEN, serve para pegar o tamanho da lista, item etc
print("\n\n Falando de LEN:\n")
linguagens2 = ["python", "c", "java", "go lang"]
print(f"Essa lista tem {len(linguagens2)} itens!")

# método SORTED, faz exatamente a mesma coisa do SORT, mas é uma função built in, só a chamada que é diferente
print("\n\n Falando de SORTED:\n")
linguagens3 = ["python", "c", "java", "go lang", "csharp"]
print(sorted(linguagens3)) # ordem alfabética, a escrita fica sorted(lista cmo parâmetro)
print(sorted(linguagens3, key=lambda x:len(x))) # mostrando a diferença na escrita