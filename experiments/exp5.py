todos = []

while input != "quit":
    user_action = input("Type add, show, edit, complete, length or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item.capitalize()}"
                print(row)
            print(f"Length is {index+1}")
        case "length":
            print("Length is", len(todos))
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