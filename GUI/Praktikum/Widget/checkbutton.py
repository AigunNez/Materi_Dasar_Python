from tkinter import *

root = Tk()
root.title("Button Example")
root.geometry("300x300")

def checkButton():
    print(f"Option 1: {var1.get()}, Option 2: {var2.get()}, Option 3: {var3.get()}")
    # check1.deselect()
    check1.select()

# Membuat variabel kontrol untuk Checkbuttons
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

# Membuat Checkbuttons
check1 = Checkbutton(root, text="Option 1", variable=var1)
check1.pack()

check2 = Checkbutton(root, text="Option 2", variable=var2)
check2.pack()

check3 = Checkbutton(root, text="Option 3", variable=var3)
check3.pack()

# Tombol untuk menampilkan pilihan yang dipilih
button = Button(root, text="Show Selections", command=checkButton)
button.pack()

root.mainloop()