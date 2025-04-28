from tkinter import *


window= Tk()
window.geometry("500x500")
window.configure(bg="red")
window.title("My fist app ever!!!")






welcome=Label(window, text ="welcome!!!" ,bg="red",fg="black",font=(""
"Helvetica",20))
welcome.pack()

btn= Button(window, text="click here", bg= "gold")
btn.pack()

entry=Entry(window,bg="white")
entry.pack()

text=Text(window)
text.pack()



window.mainloop()