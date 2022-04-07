from tkinter import *

window = Tk()
window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.pack()
#my_label.place(x=0, y=0)
#my_label.grid(column=0, row=0)

#button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command=button_clicked)
button.pack()

#entry
input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()