from tkinter import *


def clear():
    input_text.set("")


def enter(value):
    text = input_text.get()
    input_text.set(text + str(value))


def result():
    answer = eval(input_text.get())
    input_text.set(answer)


root = Tk()
root.geometry("330x400")
root.maxsize(330, 400)
root.minsize(330, 400)
root.title("Calculator")
root.configure(bg="black")

input_text = StringVar()
input_entry = Entry(root, textvariable=input_text, font="courier 30 bold", justify="right")
input_entry.pack(fill="x", pady=10, padx=10)
f1 = Frame(root, background="black")
f1.pack()
b1 = Button(f1, text="C", font="courier 25 bold", command=clear).pack(side="left", padx=10, pady=5)
b2 = Button(f1, text="%", font="courier 25 bold", command=lambda: enter('%')).pack(side="left", padx=10, pady=5)
b3 = Button(f1, text="*", font="courier 25 bold", command=lambda: enter('*')).pack(side="left", padx=10, pady=5)
b4 = Button(f1, text="/", font="courier 25 bold", command=lambda: enter('/')).pack(side="left", padx=10, pady=5)
f2 = Frame(root, background="black")
f2.pack()
b4 = Button(f2, text="7", font="courier 25 bold", command=lambda: enter('7')).pack(side="left", padx=10, pady=5)
b5 = Button(f2, text="8", font="courier 25 bold", command=lambda: enter('8')).pack(side="left", padx=10, pady=5)
b6 = Button(f2, text="9", font="courier 25 bold", command=lambda: enter('9')).pack(side="left", padx=10, pady=5)
b7 = Button(f2, text="-", font="courier 25 bold", command=lambda: enter('-')).pack(side="left", padx=10, pady=5)

f3 = Frame(root, background="black")
f3.pack()
b8 = Button(f3, text="4", font="courier 25 bold", command=lambda: enter('4')).pack(side="left", padx=10, pady=5)
b9 = Button(f3, text="5", font="courier 25 bold", command=lambda: enter('5')).pack(side="left", padx=10, pady=5)
b10 = Button(f3, text="6", font="courier 25 bold", command=lambda: enter('6')).pack(side="left", padx=10, pady=5)
b11 = Button(f3, text="+", font="courier 25 bold", command=lambda: enter('+')).pack(side="left", padx=10, pady=5)

f4 = Frame(root, background="black")
f4.pack()
b12 = Button(f4, text="1", font="courier 25 bold", command=lambda: enter('1')).pack(side="left", padx=10, pady=5)
b13 = Button(f4, text="2", font="courier 25 bold", command=lambda: enter('2')).pack(side="left", padx=10, pady=5)
b14 = Button(f4, text="3", font="courier 25 bold", command=lambda: enter('3')).pack(side="left", padx=10, pady=5)
b15 = Button(f4, text="=", font="courier 25 bold", command=result).pack(side="left", padx=10, pady=5)

root.mainloop()
