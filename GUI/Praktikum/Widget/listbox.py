from tkinter import *

root = Tk()
root.title("Button Example")
root.geometry("300x300")

listbox = Listbox(root, height=5, width=15, selectmode=MULTIPLE)
listbox.pack()

items = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
for item in items:
    listbox.insert(END, item)

def showSelection():
    selected_items = listbox.curselection()  # Mendapatkan item yang dipilih
    for item in selected_items:
        print(listbox.get(item))  # Menampilkan item yang dipilih

button = Button(root, text="Show Selection", command=showSelection)
button.pack()

root.mainloop()