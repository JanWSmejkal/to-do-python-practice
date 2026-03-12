while input != "quit":
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open("files/todos.txt", "w")
            file.writelines(todos)
            file.close()
        case "show":
            file = open("files/todos.txt", "r")
            todos = file.readlines()
            file.close()

            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.capitalize()}"
                print(row)
        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            todos[number] = new_todo = input("enter new todo: ")
        case "complete":
            number = int(input("Number of the todo to complete: "))
            todos.pop(number)
        case "exit":
            break

print("Bye!")