FILEPATH = 'todo_list.txt'


def get_todo_list(filepath=FILEPATH):
    """
    Read a text file and returns a list of todo_items
    :param filepath:
    :return:
    """
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
        return todo_local


def write_todo_list(todo_arg, filepath=FILEPATH):
    """
           Write the todo_list into the text file
           """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_arg)


if __name__ == '__main__':
    print('This is a function')
