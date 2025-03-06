from tkinter import *

root = Tk()
root.title("Button Example")
root.geometry("200x100")

def buttonClick():
    print("Button clicked")

button = Button(root, text="Button Pertama", command=buttonClick)
button.pack()

root.mainloop()