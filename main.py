import tkinter

window = tkinter.Tk()
window.minsize(50, 50)
window.config(padx=20, pady=20)
window.title("Kilograms to Grams conversion")

label = tkinter.Label(text="Kilograms to Grams conversion", font=("Arial", 20, "bold"))
label.grid(column=1,row=0)

kg = tkinter.Label(text="Kilograms:")
kg.grid(column=0, row=1)
entry = tkinter.Entry(width=7)
entry.grid(column=1, row=1)
kg1 = tkinter.Label(text="Kg")
kg1.grid(column=2, row=1)


gr = tkinter.Label(text="Kilograms:")
gr.grid(column=0, row=3)
g = tkinter.Label()
g.grid(column=1, row=3)
g1 = tkinter.Label(text="g")
g1.grid(column=2, row=3)

def convert():
    k = float(entry.get())
    g.config(text=str(k * 1000))

button = tkinter.Button(text="Convert", command=convert)
button.grid(column=1, row=2)










window.mainloop()