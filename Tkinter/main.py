import tkinter

window = tkinter.Tk()

window.title("My first GUI Program")
window.minsize(width=500, height=300)

my_label = tkinter.Label(text='I am a Label', font=("Arial", 24, "bold"))
my_label.pack()

my_label.config(text='New Label')


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()


input = tkinter.Entry(width=10)
input.pack()
print(input.get())

window.mainloop()
