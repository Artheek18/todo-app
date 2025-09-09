import functions
import FreeSimpleGUI as fs

#Labels
label = fs.Text("Type a to-do to add")
label_for_edit = fs.Text("Edit a To-Do")

#Input and List boxes
input_box = fs.InputText(tooltip="Enter a to-do", key="todo")
list_box = fs.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=(40, 20))


#Buttons
add_button = fs.Button("Add To-Do")
edit_button = fs.Button("Edit To-Do")
move_up_button = fs.Button("Move Up")
move_down_button = fs.Button("Move Down")
complete_button = fs.Button("Complete")
exit_button = fs.Button("Exit")


window = fs.Window("To-Do App",
                      layout=[
    [label],
    [input_box, add_button],
    [label_for_edit],
    [
        list_box,
        fs.Column([
            [edit_button],
            [complete_button],
            [move_up_button],
            [move_down_button]
        ])
    ],
    [exit_button]
],
                      font=("Helvetica bold", 10))


while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add To-Do":
            todos = functions.get_todos()
            added = values['todo'].strip() + "\n"
            todos.append(added)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit To-Do":
            edit_todo = values['todos'][0]
            new = values['todo']
            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Complete":
            complete_todo = values['todos'][0].strip()
            todos = [t.strip() for t in functions.get_todos()]
            todos.remove(complete_todo)
            functions.write_todos([t + "\n" for t in todos])  # save with newlines
            window['todos'].update(values=todos)
            window['todo'].update(value="")

        case "Move Up":
            todos = functions.get_todos()
            todo_moveUp = values['todos'][0].strip()
            idx = [t.strip() for t in todos].index(todo_moveUp)
            if idx > 0:
                todos[idx], todos[idx - 1] = todos[idx - 1], todos[idx]
                functions.write_todos(todos)
                window['todos'].update(values=[t.strip() for t in todos])
                window['todos'].update(set_to_index=idx - 1)

        case "Move Down":
            todos = functions.get_todos()
            todo_moveDown = values['todos'][0].strip()
            idx = [t.strip() for t in todos].index(todo_moveDown)
            if idx < len(todos)-1:
                todos[idx], todos[idx + 1] = todos[idx + 1], todos[idx]
                functions.write_todos(todos)
                window['todos'].update(values=[t.strip() for t in todos])
                window['todos'].update(set_to_index=idx + 1)

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])


        case fs.WINDOW_CLOSED:
            break

window.close()
