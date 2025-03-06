from tkinter import *

root = Tk()
root.title("Pack Example")
root.geometry("200x100")

# Fungsi untuk menutup aplikasi
def quit_app():
    root.quit()

# Fungsi untuk menampilkan pesan
def show_message():
    print("Menu item selected!")

# Membuat Menu bar
menu_bar = Menu(root)

# Membuat Menu "File"
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=show_message)
file_menu.add_command(label="Save", command=show_message)
file_menu.add_separator()  # Pemisah menu
file_menu.add_command(label="Exit", command=quit_app)

# Membuat Menu "Edit"
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=show_message)
edit_menu.add_command(label="Copy", command=show_message)
edit_menu.add_command(label="Paste", command=show_message)

# Menambahkan menu ke menu bar
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

root.config(menu=menu_bar)
root.mainloop()