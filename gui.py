import functions
import FreeSimpleGUI as fsgui

label = fsgui.Text("Type a to-do")
input_box = fsgui.InputText(tooltip="Enter a to-do")
add_button = fsgui.Button("Add to-do")

window = fsgui.Window("To-Do App", layout=[[label], [input_box, add_button]])
window.read()
window.close()
