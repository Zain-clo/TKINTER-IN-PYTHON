from tkinter import *


# Main Window
window = Tk()
window.title("Simple To-Do List")
window.geometry("300x400")

# Entry Box
entry =Entry(window, bg="red")
entry.pack()

# Add Button
btn =Button(window, text="Add Task", width=20, )
btn.pack()


# Delete Button
btn = Button(window, text="Delete Selected Task", width=20)
btn.pack()

# Run App
window.mainloop()
