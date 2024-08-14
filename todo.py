from tkinter import *

selected_task = None
tasks = []

files = "tasks.txt"


def save():
    with open(files, 'w') as file:
        for name, var, _ in tasks:
            file.write(f"{name},{var.get()}\n")


def load():
    with open(files, "r") as file:
        for line in file:
            name, value = line.strip().split(',')
            var = IntVar(value=int(value))
            checkbox = Checkbutton(f4, text=name, variable=var)
            checkbox.pack(anchor="w", pady=3)
            checkbox.config(command=lambda cb=checkbox: select(cb))
            tasks.append((name, var, checkbox))


def new_task():
    name = task_val.get().strip()
    if name:
        var = IntVar()
        checkbox = Checkbutton(f4, text=name, variable=var)
        checkbox.pack(anchor="w", pady=3)
        checkbox.config(command=lambda cb=checkbox: select(cb))
        tasks.append((name, var, checkbox))
        task_val.set("")
        global selected_task
        selected_task = None


def select(checkbox):
    global selected_task
    for task_name, var, cb in tasks:
        if cb == checkbox:
            task_val.set(task_name)
            selected_task = (task_name, var, cb)
            break


def update():
    global selected_task
    if selected_task:
        new_name = task_val.get().strip()
        if new_name:
            old_name, var, checkbox = selected_task
            checkbox.config(text=new_name)
            tasks[tasks.index(selected_task)] = (new_name, var, checkbox)
            task_val.set("")
            selected_task = None


def remove():
    global tasks
    complete = [task for task in tasks if task[1].get() == 1]
    for task in complete:
        name, var, checkbox = task
        checkbox.pack_forget()
        tasks.remove(task)


root = Tk()
root.geometry("500x500")
root.maxsize(500, 500)
root.minsize(500, 500)
root.title("To-Do List")

f1 = Frame(root, bg="grey", borderwidth=9, relief=SUNKEN)
f1.pack(fill="x")
l = Label(f1, text="To-Do list", font="timesnewroman 16 bold")
l.pack()

f2 = Frame(root, bg="grey", borderwidth=9, relief=SUNKEN)
f2.pack(side=LEFT, fill="y")
b1 = Button(f2, text="Add Task", borderwidth=2, relief="raised", command=new_task)
b1.pack(fill="x", pady=10)
b2 = Button(f2, text="Edit Task", borderwidth=2, relief="raised", command=update)
b2.pack(fill="x", pady=10)
b3 = Button(f2, text="Mark Complete", borderwidth=2, relief="raised", command=remove)
b3.pack(fill="x", pady=10)

f3 = Frame(root, background="grey", borderwidth=9, relief="sunken")
f3.pack(fill="x")
task = Label(f3, text="Enter Task")
task.pack(side="left", anchor="nw", padx=10)
task_val = StringVar()
taskentry = Entry(f3, textvariable=task_val)
taskentry.pack(side="left", anchor="nw", padx=10)

f4 = Frame(root, background="grey", borderwidth=9, relief="sunken")
f4.pack(fill="both", expand=True, anchor="w")

load()

root.protocol("WM_DELETE_WINDOW", lambda: (save(), root.destroy()))

root.mainloop()
