import random
import hangman_words
import hangman_art

word_list = hangman_words.word_list
vidas = 6


logo = hangman_art.logo
print(logo)
chosen_word = random.choice(word_list)


placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("\n\nQual é a palavra: " + placeholder)

game_over = False
correct_letters = []
guesses = []
while not game_over:

    
    print(f"****************************{vidas}/6 VIDAS RESTANTES****************************")
    guess = input("Escolha uma letra: ").lower()

    
    if guess in correct_letters:
        print("Você já escolheu essa letra, tente outra.")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            guesses.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            guesses.append(guess)

    print("Palavra para adivinhar: " + display)

    

    if guess not in chosen_word:
        vidas -= 1
        print (f"Você chutou {guess} e ele não está na palavra. Perdeu uma vida")

        if vidas == 0:
            game_over = True

           
            print(f"**************************A PALAVRA ERA: {chosen_word}! VOCÊ PERDEU!!**********************")

    if "_" not in display:
        game_over = True
        print("****************************VOCÊ GANHOU!!****************************")

    print(hangman_art.stages[vidas])