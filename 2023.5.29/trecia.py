from tkinter import *

def pasisveikinti(event=None):
    vardas = vardo_laukas.get()
    if vardas:
        rezultatas.configure(text="Labas, {}!".format(vardas))
        global paskutinis_tekstas
        paskutinis_tekstas = "Labas, {}!".format(vardas)
    else:
        rezultatas.configure(text="Įveskite vardą!")

def istrinti_teksta():
    rezultatas.configure(text="")

def atkurti_teksta():
    rezultatas.configure(text=paskutinis_tekstas)

def uzdaryti_programa():
    langas.quit()

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

langas.bind('<Return>', pasisveikinti)

meniu = Menu(langas)
langas.config(menu=meniu)

meniu_punktas = Menu(meniu)
meniu.add_cascade(label="Meniu", menu=meniu_punktas)

meniu_punktas.add_command(label="Išvalyti", command=istrinti_teksta)

meniu_punktas.add_command(label="Atkurti", command=atkurti_teksta)

meniu_punktas.add_separator()

meniu_punktas.add_command(label="Išeiti", command=uzdaryti_programa)

paskutinis_tekstas = ""  # Laikinai saugoti paskutinį atspausdintą tekstą

langas.mainloop()
