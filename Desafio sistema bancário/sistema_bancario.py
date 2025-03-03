menu = """"

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


    

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("Quanto você quer depositar?\n"))
        if deposito >= 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
        else:
            print ("Não podemos fazer depósito negativo!")

    elif opcao == "s":
        saque = float(input("Quanto você quer sacar?\n"))
        
        excedeu_saldo = saque > saldo
        excedeu_limite = saque > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente!")
            
        elif excedeu_limite:
            print("Operação falhou! Você não tem limite suficiente!")
        
        elif excedeu_saques:
            print("Operação falhou! Número de saques do dia excedidos!")

        elif saque > 0:
            saldo -= saque
            extrato += f"Saque: R${saque:.2f}\n"
            numero_saques += 1
        else:
            print ("Operação inválida!")

    elif opcao == "e":
        print("\n########Extato########")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("#########################")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")