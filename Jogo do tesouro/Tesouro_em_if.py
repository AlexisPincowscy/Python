print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vind@ a sua caça ao tesouro perdido.")
print("Sua missão é encontrar o tesouro perdido há milhoes de anos.")

print("para começar você precisa decidir para que lado você vai, mas cuidado, existem perigos escondidos por ai..")
lado = input("E então, você vai para esquerda [E] ou direita [D] ").upper()
if lado == "E":
    print("Ahá!! Muito bem, agora vamos escolher seu próximo desafio!\nVocê agora tem que escolher se vai nadar para chegar à ilha ou não")
    nado = input("Aventureiro, oq eu você quer fazer: nadar [N] ou esperar [E] ").upper()
    if nado == "E":
        print("Olha só, sabia decisão!! Vamos agora para a próxima fase!")
        print("Chegamos a sua decisão final! Está vendo essas portas à sua frente, uma delas te leva ao tesouro...mas QUAL??")
        porta = input("A da vermelha [V], a amarela [A] ou a azul [B], qual será sua escolha? ").upper()
        if porta == "A":
            print("Você achou!! Ai está o seu tesouro!! Parabéns marujo!!")
        elif porta == "V":
            print("Você está em chamas HAHAHA...GAME OVER!!")
        elif porta == "B":
            print("Você foi devorado por leões famintos!!...GAME OVER!!")
        else:
            print("Essa porta não existe...escolha a letra certa")
    elif nado == "N":
        print("Ihhh!! Você acabou sendo atacado por um tubarão...GAME OVER!!")
    else:
        print("Digitou errado de novo...tsc tsc")
elif lado == "D":
    print("A sua caça ao tesouro teve um final trágico, você caiu em um buraco enorme...GAME OVER!!")
else:
    print("Você precisa digitar uma das opções, meu jovem...")