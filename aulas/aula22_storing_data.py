
while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    match user_action:
        case "add":
            todo = input("Enter a todo: ") + "\n"

            file = open("todos.txt", "r")
            todos = file.readlines()
            file.close()

            todos.append(todo)

            ## Storing datas in file .txt
            file = open("todos.txt", "w") # ele sobrescreve os dados
            file.writelines(todos)
            file.close()


        case "show":
            for index, item in enumerate(todos):
                row = f"{index + 1}-{item}"
                print(row)

        case "edit":
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            new_todo = input("Enter a new todo: ")
            # existing_todo = todos[number]
            todos[number] = new_todo

        case "complete":
            number = int(input("Number od the todo to complete: "))
            todos.pop(number - 1)

        case "exit":
            break

print("Bye")

"""
countries = ["Brazil", "EUA", "Canada", "Japan", "Germany"]

#for country in countries:
#    print(country)


for index, country in enumerate(countries):
    print(f"{index + 1}° {country}")

"""

### How to store data in files .txt / .svl / .sql
# "file.txt", "r" - read   "w" - write
