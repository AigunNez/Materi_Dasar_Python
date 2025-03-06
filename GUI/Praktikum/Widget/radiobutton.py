from tkinter import *

root = Tk()
root.title("Button Example")
root.geometry("300x300")

select = StringVar()

radiobutton1 = Radiobutton(root, text="Option 1", value="Anda memilih Option 1", variable=select)
radiobutton1.pack()

radiobutton2 = Radiobutton(root, text="Option 2", value="Anda memilih Option 2", variable=select)
radiobutton2.pack()

radiobutton3 = Radiobutton(root, text="Option 3", value="Anda memilih Option 3", variable=select)
radiobutton3.pack()

def showSelection():
    print(f"Selected Option: {select.get()}")

button = Button(root, text="Show Selection", command=showSelection)
button.pack()

root.mainloop()