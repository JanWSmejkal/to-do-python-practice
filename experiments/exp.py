todos = []

while input != "quit":
    user_action = input("Type add, show or exit: ")
    user_action = user_action.strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case "show" | "display" | "print":
            for item in todos:
                item = item.title()
                print(item)
        case "exit":
            break
        case x:
            print("Sorry, Unknown command.")



print("Bye!")