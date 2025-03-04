# Listas
# podem ser escritas usando [], o mais comum
# pode tbm usar a função list() e irá transformar o que tem dentro em itens de lista.
# para escolher separadamente itens da lista pode ser posição 0,1,2 (esquerda para direita)
# ou -1,-2(que vai do último par o primeiro)

frutas =["laranja","limão","maça"]
print(frutas[1]) #limão
print(frutas[-1]) #maça

# vale qualquer item, não precisa ser da mesma classe
carro = ["ferrari" , "vermelho" , 245000 , 2950.50, 2020]
#marca, cor, valor, ipva valor, ano

# matriz é uma lista com lista dentro
matriz = [
    ["a", 25, "carro"],
    ["b", 45, "anão"],
    ["c", 30, "cachorro"]
]

# para selecionar o item primeiro colchete é a linha e segundo a coluna
print(matriz[0]) #vai a primeira lista toda
print(matriz[1][0])#primerio item da segunda linha

# fatiar lista - [de quando : até quando]
fatiar = list("alexispincowscy") #função list() vai transformar em letra por letra

print(fatiar[0:3])#vai imprimir do item 0 até o 3 (a,l,e)
print(fatiar[4:]) #vai imprimir do quarto elemento (i) para frente
print(fatiar[:3])#vai do 0 até o terceiro item (igual primeiro exemplo)
print(fatiar[::])#vai tudo separado
print(fatiar[::-1])#tudo invertido

# itinerar (imprimir todos os itens em ordem)
# usar o FOR
carros = ["gol", "palio", "celta"]
for lista_carro in carros:
    print(lista_carro)

# para imprimir enumerando
# for com enumerate
# vai imprimir a posição e o item da lista da posição

carros = ["gol", "palio", "celta"]
for indice, lista_carro in enumerate(carros):
    print(f"{indice} - {lista_carro}")

# python permite o metódo comprehension, escrever um for em uma linha

numeros = [1 ,10, 50, 12, 24, 50, 4356, 213]
# para saber se é par, um for (percorre item por item e faz funçaõ apend, para adicionar na lista)
numeros_pares = []

for numero_par in numeros:
    if numero_par % 2 == 0: #consição apra testar se é par (o resto da divisão tem que ser 0)
        numeros_pares.append(numero_par) #usar o append para acrscentar o número da lista pares

print(numeros_pares)

# pode ser tudo numa linha só

numeros2 = [1 ,10, 50, 12, 24, 50, 4356, 213]
numeros_pares2 = [numero_par2 for numero_par2 in numeros2 if numero_par2 % 2 == 0] #primerio o que retorna, depois a mesma lógica do for só que em 1 linha
print(numeros_pares2)

# exemplo 2
numeros = [1 ,10, 50, 12, 24, 50, 4356, 213]
num_ao_quadrado = [resultado **2 for resultado in numeros] # vai ir de número em número, fazendo a exponenciação de 2 e acrscentando na lista
print(num_ao_quadrado)