import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao PyGerador de Senhas!")
nr_letters = int(input("Quantas letras você quer na senha?\n"))
nr_symbols = int(input(f"Quantos símbolos você quer na senha?\n"))
nr_numbers = int(input(f"Quantos números você quer na senha?\n"))


psw = []
for psw_letters in range(0,nr_letters):
    psw.append(random.choice(letters))

for psw_symbols in range(0,nr_symbols):
    psw.append(random.choice(symbols))

for psw_numb in range(0,nr_numbers):
    psw.append(random.choice(numbers))

random.shuffle(psw)
psw_final = ''.join(psw)
print(f"Sua senha é:\n{psw_final}")