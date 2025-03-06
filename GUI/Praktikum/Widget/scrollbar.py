from tkinter import *

root = Tk()
root.title("Pack Example")
root.geometry("200x100")

# Membuat Listbox
listbox = Listbox(root, height=5, width=30)
listbox.pack(side=LEFT)

# Menambahkan beberapa item ke Listbox
items = ["Apple", "Banana", "Orange", "Grapes", "Mango", "Pineapple", "Peach", "Plum"]
for item in items:
    listbox.insert(END, item)

# Membuat Scrollbar vertikal
scrollbar = Scrollbar(root, orient=VERTICAL, command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Menghubungkan Scrollbar dengan Listbox
listbox.config(yscrollcommand=scrollbar.set)

root.mainloop()