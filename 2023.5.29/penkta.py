from tkinter import *
from PIL import ImageTk, Image
import webbrowser

def keisti_raiskuma(event):
    global paveikslelis
    if event.keysym == "Right":
        ryskumas = ryskumo_scale.get() + 60.1
    elif event.keysym == "Left":
        ryskumas = ryskumo_scale.get() - 60.1
    else:
        return
    keisti_paveikslelio_ryskuma(ryskumas)

def keisti_dydi():
    global paveikslelis
    try:
        dydis = int(dydzio_laukas.get())
        keisti_paveikslelio_dydi(dydis)
    except ValueError:
        pass

def atverti_google(event):
    webbrowser.open("https://www.google.com")

def keisti_paveikslelio_ryskuma(ryskumas):
    global paveikslelis
    pakeistas_paveikslelis = paveikslelis.copy()
    ryskumas_filter = ImageEnhance.Sharpness(pakeistas_paveikslelis)
    pakeistas_paveikslelis = ryskumas_filter.enhance(ryskumas)
    atvaizdas = ImageTk.PhotoImage(pakeistas_paveikslelis)
    etikete.configure(image=atvaizdas)
    etikete.image = atvaizdas

def keisti_paveikslelio_dydi(dydis):
    global paveikslelis
    pakeistas_paveikslelis = paveikslelis.copy()
    pakeistas_paveikslelis = pakeistas_paveikslelis.resize((dydis, dydis), Image.LANCZOS)
    atvaizdas = ImageTk.PhotoImage(pakeistas_paveikslelis)
    etikete.configure(image=atvaizdas)
    etikete.image = atvaizdas

langas = Tk()
langas.title("Vaizdo redagavimas")

paveikslelio_kelias = "paveiksliukas.jfif"
paveikslelis = Image.open(paveikslelio_kelias)
atvaizdas = ImageTk.PhotoImage(paveikslelis)

langas.geometry("250x250")

pagrindinis_frame = Frame(langas)
pagrindinis_frame.pack(expand=True, fill=BOTH)

etikete = Label(pagrindinis_frame)
etikete.pack(pady=10)

ryskumo_scale = Scale(pagrindinis_frame, from_=-2000, to=2000, resolution=10, orient=HORIZONTAL, label="Raiškumas")
ryskumo_scale.set(1)
ryskumo_scale.pack(pady=10)

dydzio_frame = Frame(pagrindinis_frame)
dydzio_frame.pack()

dydzio_label = Label(dydzio_frame, text="Dydis:")
dydzio_label.pack(side=BOTTOM, fill=X)

dydzio_laukas = Entry(dydzio_frame)
dydzio_laukas.pack(side=BOTTOM, fill=X)

dydzio_mygtukas = Button(dydzio_frame, text="Pakeisti dydį", command=keisti_dydi)
dydzio_mygtukas.pack(side=BOTTOM, fill=X)

etikete.configure(image=atvaizdas)
etikete.bind('<MouseWheel>', keisti_raiskuma)
etikete.bind('<Button-1>', atverti_google)

langas.mainloop()
