def get_todos(filepath="todos.txt"):
    """ Returns the list of todo items
    from the text file.
    """
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()

    return todos

def write_todos(todos_args, filepath="todos.txt"):
    """ Writes the list of todo items
    to the text file.
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_args)
