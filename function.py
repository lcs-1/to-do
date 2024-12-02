FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Reads from todos file and gives a list of to-dos."""
    with open(filepath, "r") as file_local:
            todos_local = file_local.readlines()
    return todos_local


def update_todos(todos_args,filepath=FILEPATH):
    """ Writes the updated todos in the file."""
    with open(filepath, "w") as file:
            file.writelines(todos_args)
    
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
    print("Hey there!")