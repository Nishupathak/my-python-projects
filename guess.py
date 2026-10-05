import random
def load_best():
    try:
        with open("highscore.txt", "r") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return None

def save_best(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))
def play():
    secret = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number from 1 to 100.")
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Please type a number!")
            continue
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print("You got it in", attempts, "tries!")
            return attempts
best = load_best()
if best is not None:
    print("Best score so far:", best, "tries")

while True:
    score = play()
    best = load_best()
    if best is None or score < best:
        save_best(score)
        print("New high score!")
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        print("Bye!")
        break