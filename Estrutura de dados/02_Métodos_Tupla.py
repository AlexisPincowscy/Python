# A Tupla é imutável, então só os métodos que não alteram valores depois são existentes
# método COUNT, conta quantas vezes um objeto aparece em determinada tupla
# o parâmetro é o obejto e o resultado vai ser int
print("\n\n Falando de COUNT:\n")
tupla3 = ("vermelho", "azul", "vermelho", "verde", "vermelho", "azul",)
print(f"Têm {tupla3.count("vermelho")} vezes essa cor")
print(f"Têm {tupla3.count("azul")} vezes essa cor")
print(f"Têm {tupla3.count("verde")} vezes essa cor")

# método INDEX, serve para mostrar a PRIMEIRA ocorrência do item na tupla
print("\n\n Falando de INDEX:\n")
carros = ("ferrari", "volks", "fiat","alfa romeo",)
print(f"O Fiat aparece, pela primeria vez, na posição: {carros.index("fiat")}")
print(f"O Fiat aparece, pela primeria vez, na posição: {carros.index("alfa romeo")}")

# método LEN, serve para pegar o tamanho da tupla, item etc
print("\n\n Falando de LEN:\n")
linguagens2 = ("python", "c", "java", "go lang",)
print(f"Essa tupla tem {len(linguagens2)} itens!")