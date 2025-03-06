from tkinter import *

root = Tk()
root.title("Pack Example")
root.geometry("200x100")

label1 = Label(root, text="Label Pertama")
# label.pack(side="left", padx=10, pady=10)
# label.grid(row=0, column=0, padx=10, pady=10)
label1.place(x=30, y=10)

label2 = Label(root, text="Label Kedua")
# label2.grid(row=0, column=1, padx=10, pady=10)
label2.place(x=40, y=10)

root.mainloop()