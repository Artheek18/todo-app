FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Returns the list of todos
    from the text file.
    """
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()

    return todos

def write_todos(todos_args, filepath=FILEPATH):
    """ Writes the list of todos
    to the text file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)
