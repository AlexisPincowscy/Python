from art import logo
import string
print(logo)

alphabet = list(string.ascii_lowercase)


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
        
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]



    print(f"Aqui está a mensagem: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
game_over = False
while game_over is not True:
    direction = input("Escreve 'encode' para embaralhar, e 'decode' para desvendar:\n").lower()
    text = input("Escreva sua mensagem:\n").lower()
    shift = int(input("Escreva o número para embaralhar:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    choice = int(input("Quer fazer de novo? Sim[1] ou Não[2]?\n"))
    if choice == 2:
        game_over = True
        print("Ok, até a próxima!")
    else:
        game_over = False
