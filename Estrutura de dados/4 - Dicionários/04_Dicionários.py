# DICIONÁRIOS são um conjunto com relação de chave:valor
# Eles criam uma espécie de banco de dados
# Existem algumas maneiras de criar um dicionário

# usando chaves e os dois pontos
escola = {"nome": "Carlos", "turma": "A", "série": "quarta"}
# usando dict
escola2 = dict(nome="Carlos", turma="A", serie="quarta")
# para acrescentar um valor em um dicionário já existente
escola["Idade"] = 10

print(f"{escola}\n{escola2}")
# escola tem acrescentado a idade

print("\n\nFAzendo Aninhamento\n")
# Podemos fazer um dentro do outro fazendo aninhação, aqui vira um processo de BD
alunos = {
    "aluno1@teste.com" : {"nome": "Carlos", "turma": "A"},
    "aluno2@teste.com" : {"nome": "Ana", "turma": "B"},
    "aluno3@teste.com" : {"nome": "Alexis", "turma": "c"},
    "aluno4@teste.com" : {"nome": "Alexis", "turma": "c", "notas":{10,9,10,8}}
}

# dicionário criado, agora podemos pegar dados dali
print(alunos["aluno1@teste.com"])#vai imprimir o que tem entro desse dicionario
print(alunos["aluno2@teste.com"]["nome"])#vai pegar só o nome desse aluno
print(alunos["aluno4@teste.com"]["notas"])#só as notas, que é um dicionário dentro do outro

# aqui acrescentei dados no aluno 3 e pedi para imprimir
alunos["aluno3@teste.com"]["notas"] = {5,10,9,7} 
print(alunos["aluno3@teste.com"]["notas"])

# para faze iteração, puxar os itens do diconário
print("\n\nImprimindo todo o dicionário\n")
for lista_aluno in alunos:
    print(lista_aluno, alunos[lista_aluno])

# ou usando método itens()
print("\n\nImprimindo com itens\n")
for chave, valor in alunos.items():
    print(chave, valor)