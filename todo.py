tasks = []

def show_tasks():
    if len(tasks) == 0:
        print("Nothing to do!")
    else:
        for number, task in enumerate(tasks, start=1):
            print(number, "-", task)

def add_task():
    text = input("What do you want to do? ")
    tasks.append(text)
    print("Added!")

def remove_task():
    show_tasks()
    number = int(input("Which number is done? "))
    tasks.pop(number - 1)
    print("Removed!")

while True:
    print()
    print("1 = show, 2 = add, 3 = done, 4 = quit")
    choice = input("Pick: ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Bye!")
        break