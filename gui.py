import function
import FreeSimpleGUI as sg

label = sg.Text("Enter a To-do: ")
inputtxt = sg.InputText(tooltip="Enter here", key='to-do')
add_button = sg.Button("Add")
listbox = sg.Listbox(values=function.get_todos(), key='todos',
                     size=[45,10], enable_events=True)
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-do app",
                   layout=[[label],
                           [inputtxt,add_button],
                           [listbox,edit_button,complete_button],
                           [exit_button]],
                   font=("Halvetica",12))

while True:
    event,values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            todos = function.get_todos()
            newTodo = values['to-do'] + "\n"
            todos.append(newTodo)
            function.update_todos(todos)
            window['todos'].update(values = todos)
        case "Edit":
            todoToBeEdited = values['todos'][0]
            new_todo = values['to-do'] + "\n"
            
            todos = function.get_todos()
            index = todos.index(todoToBeEdited)
            todos[index] = new_todo
            function.update_todos(todos)
            window['todos'].update(values = todos)
        case 'todos':
            window['to-do'].update(value = values['todos'][0])
            
        case 'Complete':
            tobecompleted = values['todos'][0]
            todos = function.get_todos()
            todos.remove(tobecompleted)
            function.update_todos(todos)
            window['todos'].update(values = todos)
            window['to-do'].update(value = "")
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
window.close()