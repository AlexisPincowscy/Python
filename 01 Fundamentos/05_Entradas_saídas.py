# entrada e saída de dados
# entrada de dados vem da função builtin chamada input, recebendo em formato string
nome = input('Qual o seu nome: ')
idade = input('Qual a sua idade: ')

print(nome, idade)
print(nome, idade, end="...\n")
print(f"Seu nome é {nome} e você tem {idade} anos.")
print(nome, idade, sep=" # ")
