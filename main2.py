todos = []

while input != "quit":
    todo = input("Type add or show ")
    todo = todo.capitalize()
    todos.append(todo)
    print(todos)
