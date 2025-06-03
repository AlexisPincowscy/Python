# para criar funções só digitar a palvra DEF
# para usar vaiáveis globais dentro da função é necessário usar GLOBAL antes da função
# dá para chamr uma função pela outra

def salario_com_bonus (salario,bonus):
    salario += bonus
    return salario

print(salario_com_bonus(5000,250))


############################


def soma (a,b):
    return a+b

def sub (a,b):
    return a-b

def conta_soma (a,b,conta):
   resultado = conta (a,b)
   print(f"O resultado da soma é = {resultado}") 

def conta_sub (a,b,conta):
    resultado = conta(a,b)
    print(f"O resultado da subtração é = {resultado}")

conta_soma(152,520,soma)
conta_sub(450,85,sub)