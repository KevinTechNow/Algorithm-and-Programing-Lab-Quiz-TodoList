import os

run = True

while run:
    try:
        user_input = input("Enter [add/show/done/del/exit] [task/id]: ")
        if user_input == "exit":
            run = False
        elif user_input == "show":
            if os.path.exists("todos.txt"):
                with open("todos.txt", "r") as todo_file:
                    for i, line in enumerate(todo_file.readlines(), 1):
                        print(f"{i}. {line.strip()}")
        else:
            cmd, val = user_input.split(maxsplit=1)
            if cmd == "add":
                with open("todos.txt", "a+") as todo_file:
                    todo_file.write(f"TODO | {val}\n")
            elif cmd == "done":
                idx = int(val) - 1
                with open("todos.txt", "r") as todo_file:
                    lines = todo_file.readlines()
                lines[idx] = lines[idx].replace("TODO", "DONE", 1)
                with open("todos.txt", "w") as todo_file:
                    todo_file.writelines(lines)
            elif cmd == "del":
                idx = int(val) - 1
                with open("todos.txt", "r") as todo_file:
                    lines = todo_file.readlines()
                lines.pop(idx)
                with open("todos.txt", "w") as todo_file:
                    todo_file.writelines(lines)
            else:
                print("Input Properly!")
                
    except (ValueError, IndexError):
        print("Input Properly!")
    except KeyboardInterrupt:
        print("Exiting")
        run = False