# Conjuntos (comando SET) serve para retirar valores repetidos, podendo ser os números e/ou letras.
# a ordem não é garantida, os valores não são duplicados, mas ele não vai ordenar de padrão

# Exemplos

numeros = set([1,2,3,1,4,5,1,3,4,1])
print(numeros)
# pode ser escrito assim ou só abrindo e fechando chaves

letras = set("alexispincowscy")
print(sorted(letras)) #aqui usei o método SORTED  que, por padrão, coloca em ordem alfabética

carros = set(["palio", "gol", "palio", "celta", "polo"])
print(carros)

# para pordemos pegar um item específico ou fatiar, precisamos transformar o conjunto em lista

numeros2 = {1,2,4,5,3,6,4,1,3,5,6}
# print(numeros2[1]) #erro pq set não é subescrevível
numeros2 = list(numeros2)
print(numeros2[2]) #aqui já funciona


# para iterar, ir de um a um
# usando for igual lista e tupla
carros = set(["palio", "gol", "palio", "celta", "polo"])
for modelo in carros:
    print(modelo) #vai imprimir sem colcoar palio 2x

# para saber indíce usar o enumerate
for indice, modelo in enumerate(carros):
    print(f"{indice} - {modelo}")