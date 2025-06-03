# # FOR
# # no python ele vai, FOR, andar em obejtos interável, andando de unidade em unidade da lista
# texto = input("Informe um texto: ")
# VOGAIS = "AEIOU"

# for letra in texto:
#     if letra.upper() in VOGAIS: #função upper vai transformar as letra em maiúsculas
#         print(letra.upper(), end=" ")
# else:
#     print() #adiciona uma quebrade linha no final

# # for com range (começo, final, de quanto tem quanto)
# print("A tabuada do 5 é:")
# for tabuada_do_5 in range(0,51,5):
#     print(tabuada_do_5, end=" ")


# WHILE

# executar, repetir um pedaço de código, até que algo aconteça

opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar\n[2] Extrato\n[0] Sair\n"))
    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo o extrato...")


# comando BREAK serve para dar parar a execução do programa, parar o loop
# pode ser usado em qualquer loop (for e while)
# comando CONTINUE ele pula para próxima etapa do código