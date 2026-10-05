import random

WORDS = ["python", "banana", "elephant", "computer", "guitar",
         "rocket", "pizza", "cricket", "monkey", "window",
         "keyboard", "school"]


def show_word(word, guessed):
    shown = ""
    for letter in word:
        if letter in guessed:
            shown += letter + " "
        else:
            shown += "_ "
    return shown


def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = set()
    lives = 6

    while lives > 0:
        print()
        print(show_word(word, guessed))
        print("Lives left:", lives)
        if wrong:
            print("Wrong letters:", " ".join(sorted(wrong)))

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please type just one letter!")
            continue
        if guess in guessed or guess in wrong:
            print("You already tried that!")
            continue

        if guess in word:
            guessed.add(guess)
            print("Yes!")
            if all(letter in guessed for letter in word):
                print()
                print(show_word(word, guessed))
                print("You won! The word was", word)
                return
        else:
            wrong.add(guess)
            lives -= 1
            print("Nope!")

    print()
    print("Game over! The word was", word)


while True:
    play()
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        print("Bye!")
        break