alunos = {
    "aluno1@teste.com" : {"nome": "Carlos", "turma": "A"},
    "aluno2@teste.com" : {"nome": "Ana", "turma": "B"},
    "aluno3@teste.com" : {"nome": "Alexis", "turma": "c"},
    "aluno4@teste.com" : {"nome": "Alexis", "turma": "c", "notas":{10,9,10,8}}
}

# COPY ele copia, criando outro dicionário!
print("\nCopy\n")
alunos2 = alunos.copy()
for chave,valor in alunos2.items():
    print(chave,valor)

# CLEAR ele limpa
print("\nClear\n")
alunos.clear()
print(alunos) #agora vazio
for chave,valor in alunos.items():
    print(chave,valor)
# dict aluno vazio

# FROMKEYS serve para criar chaves com valor none(vazio) ou com valor padrão
print("\nFROMKEYS\n")
exe1 = dict.fromkeys(["nome", "telefone"])
print(exe1) #aqui valor nulo

exe2 = dict.fromkeys(["nome","telefone"], "vazio")
print(exe2) #aqui valor padrão é "vazio"

# se usar ele em um já existente, ele sobre escreve tudo, serve para criar um novo dicionário

# GET outra forma de acessar valor dentro do dicionário
# reescrevi alunos, pois tinha dado clear antes
alunos = {
    "aluno1@teste.com" : {"nome": "Carlos", "turma": "A"},
    "aluno2@teste.com" : {"nome": "Ana", "turma": "B"},
    "aluno3@teste.com" : {"nome": "Alexis", "turma": "c"},
    "aluno4@teste.com" : {"nome": "Alexis", "turma": "c", "notas":{10,9,10,8}}
}
print("\nGET\n")
print(alunos.get("aluno1@teste.com"))#pega o primeiro aluno
print(alunos.get("aluno2@teste.com", {}))#retorna o segundo e senão encontrasse ia retonar dict vazio
print(alunos.get("aluno", "não encontrado"))#não encontra a chave e retorna o valor "não encontrado"

# ITEMS traz todos itens, funciona bem com o for
print("\nITEMS\n")
print(alunos.items())#sem o for
print("\n")
for chave,valor in alunos.items():#o for, masi organizado
    print(chave,valor)

# KEYS retorna só as chaves, funciona igual o ITEMS
# útil para saber quais são as chaves
# VALEUS retorna os valores, mas sem as chaves
print("\nKEYS e VALUES\n")
print(f"{alunos.keys()}\n")#sem o for
print(f"{alunos.values()}\n")
# POP retorna o valor da chave que ele removeu
# POPITEM vai removendo item por item
print("POP e POPITEM\n")
novo_dic = {"nome":"Alberto", 5:"sala", "turno":2}
novo_dic.pop("nome")
print(novo_dic)

# também passa argumento cvaso não encontre
teste = novo_dic.pop("carro", "arg não existente")
print(teste)
# aqui ele não coloca um argumento no lugar
teste2 = novo_dic.popitem()
print(teste2) #já tinha tirado o nome, aqui tirei o 5, imprime só turno:2

# SETDEFAULT serve para adicionar um chave:valor no dicionário
# caso já exista o valor, nada acontece
print("\nSETDEFAULT\n")
alunos = {
    "aluno1@teste.com" : {"nome": "Carlos", "turma": "A"},
    "aluno2@teste.com" : {"nome": "Ana", "turma": "B"},
    "aluno3@teste.com" : {"nome": "Alexis", "turma": "c"},
    "aluno4@teste.com" : {"nome": "Alexis", "turma": "c", "notas":{10,9,10,8}}
}
alunos["aluno1@teste.com"].setdefault("idade",28) #adicionou a idade nesse dicionário
print(alunos["aluno1@teste.com"])

# UPDATE serve para atualizar o dicionário
# caso já exista a chave, altera o valor para o novo
# caso não exista ele mantêm o antigo e adicona
# uma atualização completa
print("\nUPDATE\n")
alunos.update({"aluno5@teste.com": {"nome": "joão", "idade":20}})
alunos.update({"aluno2@teste.com": {"nome":"Carol"}})
print(alunos["aluno2@teste.com"]) #ele altera para o que o update fez, nesse caso retirou a turma, ficou só o nome novo
print(alunos["aluno5@teste.com"])
for chave,valor in alunos.items():#o for, masi organizado
    print(chave,valor)

# IN técnica de verificação
# Saber se aquele chave existe no dicionário
# Jeito prático de fazer validação
print("\nIN\n")
alunos = {
    "aluno1@teste.com" : {"nome": "Carlos", "turma": "A"},
    "aluno2@teste.com" : {"nome": "Ana", "turma": "B"},
    "aluno3@teste.com" : {"nome": "Alexis", "turma": "c"},
    "aluno4@teste.com" : {"nome": "Alexis", "turma": "c", "notas":{10,9,10,8}}
}

print("aluno1@teste.com" in alunos) #true
print("nome" in alunos["aluno3@teste.com"]) #true
print("sexo" in alunos["aluno4@teste.com"]) #false

# DEL remove objetos do dicionário
print("\nDEL\n")
del alunos["aluno1@teste.com"] #vai excluir o aluno todo
del alunos["aluno4@teste.com"]["notas"]#exclui só as notas do aluno 4
for chave,valor in alunos.items():
    print(chave,valor)