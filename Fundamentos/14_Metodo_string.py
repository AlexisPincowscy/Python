# métodos de manipulação de STRINGS

nome = input("Qual seu nome: ")

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!   "

print(texto)
print(texto.strip()) #tira os espaços em branco
print(texto.rstrip() + ".") #tira os espaços da R direita 
print(texto.lstrip() + ".") #tira os espaços da L esquerda

menu = "Python"

print(menu.center(20)) #centraliza o texto com o número de caracteres informado
print(menu.center(20,"#"))#centraliza e preenche os espaços em branco com o caracter informado
print("-".join(menu)) #colcoa o caracter entre os obejtos da lista, nmesse caso o "-" entre cada lettra