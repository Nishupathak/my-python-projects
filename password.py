import secrets
import string

SYMBOLS = "!@#$%^&*()-_=+?"

COMMON = ["password", "123456", "12345678", "qwerty", "abc123",
          "iloveyou", "admin", "welcome", "letmein", "password1"]


def generate_password(length, use_upper, use_digits, use_symbols):
    pools = [string.ascii_lowercase]
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(SYMBOLS)

    chars = [secrets.choice(pool) for pool in pools]
    everything = "".join(pools)
    while len(chars) < length:
        chars.append(secrets.choice(everything))

    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def check_password(password):
    score = 0
    tips = []

    if password.lower() in COMMON:
        return 0, ["This is one of the most common passwords. Never use it!"]

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters.")
    if len(password) >= 12:
        score += 1
    else:
        tips.append("12 or more characters is even better.")

    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append("Add small letters.")
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append("Add CAPITAL letters.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append("Add numbers.")
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        tips.append("Add symbols like ! or @.")

    return score, tips


def rating(score):
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Medium"
    if score == 5:
        return "Strong"
    return "Very strong"


def ask_yes(question):
    return input(question + " (y/n): ").lower().strip() == "y"


def generator_screen():
    try:
        length = int(input("How long? (6-64): "))
    except ValueError:
        print("Please type a number!")
        return
    if length < 6 or length > 64:
        print("Please pick a length from 6 to 64.")
        return
    use_upper = ask_yes("Include CAPITAL letters?")
    use_digits = ask_yes("Include numbers?")
    use_symbols = ask_yes("Include symbols?")
    password = generate_password(length, use_upper, use_digits, use_symbols)
    print()
    print("Your password:", password)
    score, tips = check_password(password)
    print("Strength:", rating(score), "(" + str(score) + "/6)")


def checker_screen():
    password = input("Type a password to check: ")
    if password == "":
        print("You didn't type anything.")
        return
    score, tips = check_password(password)
    print()
    print("Strength:", rating(score), "(" + str(score) + "/6)")
    for tip in tips:
        print("-", tip)
    if not tips:
        print("Great password!")


while True:
    print()
    print("1 = make a password, 2 = check a password, 3 = quit")
    choice = input("Pick: ")
    if choice == "1":
        generator_screen()
    elif choice == "2":
        checker_screen()
    elif choice == "3":
        print("Bye!")
        break
    else:
        print("Please pick 1 to 3.")