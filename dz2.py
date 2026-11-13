from tkinter import *

window = Tk()
window.title("Калькулятор")
window.geometry("600x500")

img = PhotoImage(file="school.png")
label = Label(window, image=img)
label.pack()
e1 = Entry(window, font=("Arial", 25))
e1.place(x=60, y=120, width=180, height=50)

e2 = Entry(window, font=("Arial", 20))
e2.place(x=300, y=120, width=180, height=50)

l1 = Label(window, text="Результат",
           font=("Arial", 24, "bold"),
           bg="green", fg="red")
l1.place(x=35, y=360)

def dodaty():
    a = float(e1.get())
    b = float(e2.get())
    l1.config(text=f"{a:g} + {b:g} = {a+b:g}")
def vidnyaty():
    a = float(e1.get())
    b = float(e2.get())
    l1.config(text=f"{a:g} - {b:g} = {a-b:g}")
def pomnozhyty():
    a = float(e1.get())
    b = float(e2.get())
    l1.config(text=f"{a:g} * {b:g} = {a*b:g}")
def podilyty():
    a = float(e1.get())
    b = float(e2.get())
    l1.config(text=f"{a:g} / {b:g} = {a/b:g}")

b1 = Button(window, text="+", font=("Arial", 30),
            bg="red", fg="white", command=dodaty)
b1.place(x=25, y=210, width=130, height=95)
b2 = Button(window, text="-", font=("Arial", 30),
            bg="red", fg="white", command=vidnyaty)
b2.place(x=160, y=210, width=130, height=95)
b3 = Button(window, text="*", font=("Arial", 30),
            bg="red", fg="white", command=pomnozhyty)
b3.place(x=295, y=210, width=130, height=95)
b4 = Button(window, text="/", font=("Arial", 30),
            bg="red", fg="white", command=podilyty)
b4.place(x=430, y=210, width=130, height=95)
window.mainloop()