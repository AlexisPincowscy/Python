import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



escolha = [pedra, papel, tesoura]

print("Vamos ver quem ganha, você ou o PC!! Pedra, Papel e Tesoura!!!\n")
eu = int(input("Escolha 0 para Pedra, 1 para Papel e 2 para Tesoura:\n"))
if eu >= 0 and eu <= 2:
    print(f"Você escolheu:\n{escolha[eu]}")
    pc = random.randint(0,2)
    print(f"O PC escolheu:\n{escolha[pc]}")
    if eu == 0 and pc == 2:
        print("Você ganhou!!")
    elif pc == 0 and eu == 2:
        print("Você perdeu!!")
    elif pc > eu:
        print("Você perdeu!!")
    elif eu > pc:
        print("Você ganhou!!")
    elif eu == pc:
        print("Empate!")
else:
    print("Escolha inválida, você perdeu!")