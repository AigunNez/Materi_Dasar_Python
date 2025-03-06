from tkinter import *

root = Tk()
root.title("Button Example")
root.geometry("200x100")

entry = Entry(root, background="black", foreground="white", show="*")
entry.pack()

def buttonClick():
    print("Input dari entry adalah " + entry.get())

def buttonDelete():
    entry.delete(0, END)

def buttonInsert():
    entry.insert(5, "Hello World")

button = Button(root, text="Button Pertama", command=buttonClick)
button.pack()

button_delete = Button(root, text="Delete", command=buttonDelete)
button_delete.pack()

button_insert = Button(root, text="Insert", command=buttonInsert)
button_insert.pack()

root.mainloop()