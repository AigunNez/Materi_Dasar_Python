from tkinter import *

root = Tk()
root.title("Button Example")
root.geometry("300x300")

frame1 = Frame(root, bg="lightblue", width=300, height=300, borderwidth=2, relief="solid")
frame1.place(x=0, y=0)

label = Label(frame1, text="Label Pertama")
label.pack()

frame2 = Frame(root, bg="blue", borderwidth=2,)
frame2.pack(side=RIGHT)

label2 = Label(frame2, text="Label Kedua")
label2.pack()

root.mainloop()