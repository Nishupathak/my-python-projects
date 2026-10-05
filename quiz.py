import random

QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Rome", "Madrid"],
        "answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars",
    },
    {
        "question": "What is 7 x 8?",
        "options": ["54", "56", "58", "64"],
        "answer": "56",
    },
    {
        "question": "Which language is used to style web pages?",
        "options": ["Python", "HTML", "CSS", "Java"],
        "answer": "CSS",
    },
    {
        "question": "How many days are in a leap year?",
        "options": ["364", "365", "366", "367"],
        "answer": "366",
    },
]


def ask(question, number, total):
    print()
    print("Question", number, "of", total)
    print(question["question"])
    options = question["options"][:]
    random.shuffle(options)
    for i, option in enumerate(options, start=1):
        print(i, "-", option)
    while True:
        try:
            choice = int(input("Your answer (1-4): "))
        except ValueError:
            print("Please type a number!")
            continue
        if 1 <= choice <= len(options):
            break
        print("Please pick from 1 to", len(options))
    if options[choice - 1] == question["answer"]:
        print("Correct!")
        return True
    print("Wrong! The answer was:", question["answer"])
    return False


def play():
    questions = QUESTIONS[:]
    random.shuffle(questions)
    score = 0
    for number, q in enumerate(questions, start=1):
        if ask(q, number, len(questions)):
            score += 1
    total = len(questions)
    percent = score * 100 // total
    print()
    print("You got", score, "out of", total, "(" + str(percent) + "%)")
    if percent == 100:
        print("Perfect! You are a genius!")
    elif percent >= 60:
        print("Good job!")
    else:
        print("Keep practicing!")


while True:
    play()
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        print("Thanks for playing!")
        break