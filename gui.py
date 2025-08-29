import functions
import FreeSimpleGUI as fs

label = fs.Text("Type a to-do to add")
input_box = fs.InputText(tooltip="Enter a to-do", key="todo")
add_button = fs.Button("Add To-Do")

label_for_edit = fs.Text("Edit a To-Do")
list_box = fs.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(40, 20))
edit_button = fs.Button("Edit To-Do")

window = fs.Window("To-Do App",
                      layout=[[label], [input_box, add_button], [label_for_edit], [list_box, edit_button]],
                      font=("Helvetica bold", 10))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add To-Do":
            todos = functions.get_todos()
            added = values['todo'] + "\n"
            todos.append(added)
            functions.write_todos(todos)

        case "Edit To-Do":
            edit_todo = values['todos'][0]
            new = values['todo']

            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values['todos'][0])


        case fs.WINDOW_CLOSED:
            break

window.close()
