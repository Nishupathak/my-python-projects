import json

FILE = "tasks.json"


def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)


def show_tasks(tasks):
    if len(tasks) == 0:
        print("Nothing to do!")
        return
    for number, task in enumerate(tasks, start=1):
        mark = "[x]" if task["done"] else "[ ]"
        print(number, mark, task["text"])


def add_task(tasks):
    text = input("What do you want to do? ").strip()
    if text == "":
        print("Nothing added.")
        return
    tasks.append({"text": text, "done": False})
    save_tasks(tasks)
    print("Added!")


def pick_number(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Which number? "))
        if 1 <= number <= len(tasks):
            return number - 1
    except ValueError:
        pass
    print("Please type a number from the list.")
    return None


def mark_done(tasks):
    index = pick_number(tasks)
    if index is not None:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print("Nice work!")


def delete_task(tasks):
    index = pick_number(tasks)
    if index is not None:
        tasks.pop(index)
        save_tasks(tasks)
        print("Deleted!")


tasks = load_tasks()

while True:
    print()
    print("1 = show, 2 = add, 3 = done, 4 = delete, 5 = quit")
    choice = input("Pick: ")
    if choice == "1":
        show_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Bye!")
        break
    else:
        print("Please pick 1 to 5.")