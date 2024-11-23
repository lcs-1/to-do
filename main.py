# from functions import get_todos,update_todos
import function
import time
now = time.strftime("%B %d, %Y %I:%M:%S %p")
print("It is", now)

while True:
    userinput = input("Please enter add or show or complete or edit or exit: ")
    userinput = userinput.lower().strip()

    if userinput.startswith("add"):
        todo = userinput[4:]

        todos = function.get_todos()

        todos.append(todo + "\n")

        function.update_todos(todos)

    elif userinput.startswith("show"):
        todos = function.get_todos('todos.txt')

        for index, task in enumerate(todos, start=1):
            print(f"Task {index}: {task.capitalize().strip()}")

    elif userinput.startswith("edit"):
        try:
            number = userinput[5:]
            number = int(number) - 1

            todos = function.get_todos()

            edited_text = input("Please enter the corrected task: ")
            todos[number] = edited_text + "\n"

            function.update_todos(todos)
            
        except Exception:
            print("Please enter the tasknumber with edit or enter correct tasknumber ")
            continue

    elif userinput.startswith("complete"):
        try:
            number = userinput[9:]
            number = int(number) - 1

            todos = function.get_todos()

            print(f"{(todos[number]).strip('\n')} has been completed")

            todos.pop(number)

            function.update_todos(todos)
            
        except Exception:
            print("Please enter tasknumner next to complete or valid tasknumber")
            continue
    elif userinput.startswith("exit"):
        break

    else:
        print("Please enter a valid input ")

print("Bye!")
