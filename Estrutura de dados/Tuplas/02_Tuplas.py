# Tuplas (TUPLES) é uma lista só que constante, a lista é uma variável
# Para definir podemos usar (item,item,item,) com essa última vírgula ou
# var = tuple(valor)

tupla1 = ("carro", "casa", "apt",)
tupla2 = tuple(["java", "kotlin"])
tupla3 = tuple("só um valor") # nesse caso transforma cada caracter um item
tupla4 = ("brasil",)
print(f"Valores da tupla1 = {tupla1}\n Valores da tupla2 = {tupla2}\n Valor da tupl3 = {tupla3}\n Valor da tupla4 = {tupla4}")

# Acesso direto das tuplas é igual ao lista
obj1 = tupla1[0]
print(f"O primeiro item da tupla1 é: {obj1}")

obj2 = tupla2[-1]
print(f"O último item da tupla2 é: {obj2}")

# Tuplas aninhadas, vira matriz igual lista
print("\n\nFALANDO DE ANINHAMENTO\n\n")
matriz = (
    (1, "a", 2),
    (3, "carro", 5),
    ("alibaba", 20, "céu"),
)

print(matriz[0]) # toda a primeria tupla
print(matriz[1][2]) # tupla 2, item 3
print(matriz[0][2]) # tupla 1 , item 3
print(matriz[2][-1]) #tupla 3, último item

# Fatiamento é igual
print("\n\nFALANDO DE FATIAMENTO\n\n")
fatiar = tuple("alexispincowscy") #vai separar cada letra em um item

print(fatiar[0:3]) #imprime a priameira até a terceira letra
print(fatiar[4:]) #da quarta em diante
print(fatiar[:3]) #até a terceira
print(fatiar[::]) #todas
print(fatiar[::-1])# todas invertido

# itinerar (imprimir todos os itens em ordem)
# usar o FOR
print("\n\nFALANDO DE ITERAÇÃO\n\n")
carros = ("gol", "palio", "celta",)
for lista_carro in carros:
    print(lista_carro)


# para imprimir enumerando
# for com enumerate
# vai imprimir a posição e o item da lista da posição

carros = ("gol", "palio", "celta",)
for indice, lista_carro in enumerate(carros):
    print(f"{indice} - {lista_carro}")

