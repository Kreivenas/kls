from tkinter import *

def pasisveikinti():
    vardas = vardo_laukas.get()
    if vardas:
        rezultatas.configure(text="Labas, {}!".format(vardas))
    else:
        rezultatas.configure(text="Įveskite vardą!")

langas = Tk()
langas.title("Pasveikinimo programa")

uzrasas = Label(langas, text="Įveskite vardą:")
uzrasas.grid(row=0, column=0, sticky=W)
vardo_laukas = Entry(langas)
vardo_laukas.grid(row=0, column=1)

patvirtinimo_mygtukas = Button(langas, text="Patvirtinti", command=pasisveikinti)
patvirtinimo_mygtukas.grid(row=1, columnspan=2, pady=10)


rezultatas = Label(langas)
rezultatas.grid(row=2, columnspan=2)

langas.mainloop()
