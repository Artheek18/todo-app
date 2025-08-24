from functions import get_todos, write_todos
import time


while True:
    action = input("Type add, show, edit, complete or quit: ")
    action = action.strip().lower()
    if action.startswith("add"):
        todo = action[4:]

        todos_list = get_todos()
        now = time.strftime("%d-%m-%Y")
        todos_list.append(todo.capitalize() + ", " + now + '\n')
        write_todos(todos_list)

    elif action.startswith("show"):
        #print(*todos_list, sep=", ")
        todos_list = get_todos()

        for index, todo in enumerate(todos_list):
            todo = todo.title().strip('\n')
            print(f"{index+1}-{todo}")

    elif action.startswith("edit"):
        number = action[5:]
        try:
            number = int(number) if number else int(input("Enter the number of the To Do to edit: "))

            todos_list = get_todos()
            new_todo = input("Enter new To Do: ")
            todos_list[number - 1] = new_todo + '\n'
            write_todos(todos_list)

            print(f"Updated To Do #{number}: {new_todo}")

        except ValueError:  # invalid integer input
            print("Invalid input: please enter a number.")
            continue

        except IndexError:  # number not within list bounds
            print("Error: That number doesn’t exist in the To Do list.")
            continue

    elif action.startswith("complete"):
        number = action[9:]
        try:
            number = int(number) if number else int(input("Enter the number of the To Do to complete: "))

            todos_list = get_todos()
            removed_todo = todos_list.pop(number - 1)
            write_todos(todos_list)

            print(f"Removed: {removed_todo.strip()}")
            for index, todo in enumerate(todos_list, start=1):
                print(f"{index}-{todo.strip()}")

        except ValueError:
            print("Invalid input: please enter a number.")
            continue

        except IndexError:
            print("Error: That number doesn’t exist in the To Do list.")
            continue

    elif "quit" in action:
        break

    else:
        print("Enter a valid command")

print("Bye")

