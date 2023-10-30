import tkinter
   
root = tkinter.Tk()
root.configure(bg='lightyellow')
root.title('To-Do List Manager')
root.geometry('320x290')
tasks = []

#Functions for the features of the app
def update_listbox():
    clear_listbox()
    #update the Listbox after every operation
    for task in tasks:
        lb_tasks.insert("end", task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    # Get the task name for text input field
    task = txt_input.get()
    # add it to Listbox 
    if task != '':
        tasks.append(task)
        update_listbox()
    else:
        display['text'] = "Please enter a task!"
    txt_input.delete(0,'end')

def delete():
    task = lb_tasks.get('active')#stores the selected task from the Listbox
    if task in tasks:
        tasks.remove(task)
    # call update function to re-print the Listbox
    update_listbox()
    display['text'] = "Task deleted!"

def delete_all():
    
    global tasks
    # Clear the list
    tasks = []
    update_listbox()

def number_of_task():
    number_of_tasks = len(tasks)
    msg = "Number of tasks : %s" %number_of_tasks
    display['text'] = msg

def exit():
    quit()
    
#Creatin Buttons and Textfields

title = tkinter.Label(root, text = "TO-DO LIST", bg='yellow')
title.grid(row=0,column=1)

add_task_msg = tkinter.Label(root,text="Enter the task name",bg='sky blue')
add_task_msg.grid(row=2,column=0)

display = tkinter.Label(root, text = "", bg='white')
display.grid(row=1,column=1)

txt_input = tkinter.Entry(root, width=15)
txt_input.grid(row=2,column=1)

btn_add_task = tkinter.Button(root, text = "Add Task", fg = 'green', bg = None, command = add_task)
btn_add_task.grid(row=8,column=0)

btn_delete = tkinter.Button(root, text = "Delete", fg = 'red', bg = None, command = delete)
btn_delete.grid(row=9,column=0)

btn_delete_all = tkinter.Button(root, text = "Delete All", fg = 'red', bg = None, command = delete_all)
btn_delete_all.grid(row=8,column=3)

btn_number_of_task = tkinter.Button(root, text = "Number of Tasks", fg = 'blue', bg = None, command = number_of_task)
btn_number_of_task.grid(row=8,column=1)

btn_close = tkinter.Button(root, text = "Exit", fg = 'black', bg = None, command = exit)
btn_close.grid(row=9,column=3)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=3,column=1,rowspan=3)

root.mainloop()