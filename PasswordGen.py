import random,string
from tkinter import *

def generator():
    size = int(password_len.get())
    combinations = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(combinations) for _ in range(size))
    print(password)

    popup = Toplevel()
    popup.title("Password Generator")
    popup.geometry("250x100")
    popup.configure(bg="cyan")

    label = Label(popup,text=password,bg="cyan",font="timesnewroman 15 bold")
    label.pack(pady=20)

root= Tk()
root.geometry("400x300")
root.maxsize(400,300)
root.minsize(400,300)
root.title("Password Generator")
root.configure(bg="cyan")


l1 = Label(root, text="Enter The Length Of Your Password",font="timesnewroman 15 bold", bg="cyan")
l1.pack(pady=15)
password_txt = IntVar()
password_len = Entry(root,textvariable=password_txt,font="timesnewroman 20 bold", justify="center")
password_len.pack(pady=10)
b1 = Button(root,text="Generate",font="timesnewroman 15 bold",command=generator)
b1.pack(pady=15)


root.mainloop()