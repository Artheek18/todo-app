import functions
import FreeSimpleGUI as fs

label = fs.Text("Type a to-do")
input_box = fs.InputText(tooltip="Enter a to-do", key="todo")
add_button = fs.Button("Add To-Do")

window = fs.Window("To-Do App",
                      layout=[[label], [input_box, add_button]],
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

        case fs.WINDOW_CLOSED:
            break

window.close()
