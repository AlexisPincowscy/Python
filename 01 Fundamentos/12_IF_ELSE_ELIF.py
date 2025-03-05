# # exemplo de IF e ELSE e ELIF(elseif do python)

idade = int(input("Qual a sua idade?\n"))
idade_especial = 12
if idade >= 18:
    print("Você está pronto para tirar a carteira!!")
else:
    print("Calma, pequeno gafanhoto! Seu tempo há de chegar =)")


if idade >= 18:
    print("Você está pronto para tirar a carteira!!")
elif idade == idade_especial:
    print("Você já é crescido, pode começar as aulas teoricas, mas as práticas só com 18.")
else:
    print("Calma, pequeno gafanhoto! Seu tempo há de chegar =)")




# # Exemplo de IF aninhado (um dentro do outro)

saldo = 5000
cheque_especial = 1000
saque = int(input("Quanto vc quer sacar?\n"))
tipo_conta = int(input("Qual seu tipo de conta:\nConta normal: 1\nConta universitária: 2\n"))

if tipo_conta == 1:
    if saldo >= saque: 
        print("Saque realizado!")
        saldo -= saque
        print(f"Saldo atual: R${saldo}")
    elif saque > (saldo + cheque_especial):
        saldo += cheque_especial
        saldo -= saque
        print("Saque realizado utilizando cheque especial, fique atento!")
        print(f"Seu saldo está negativo: R${saldo}.")
    else:
        print("Não é possível realizar o saque.")
elif tipo_conta == 2:
    if saldo >= saque: 
        print("Saque realizado!")
    else:
        print("Você não possui saldo, nem cheque especial.")




# Exemplo de IF ternário (em três partes dentro de uma mesma linha)
# fica var = SUCESSO + if e condição + FRACASSO

carro = input("Qual marca do seu carro?\n")

bom = "carrão" if carro == "BMW" else "carrinho"
print(f"Você tem um {bom}!")
