import pickle
import tkinter as tk
from tkinter import messagebox


class BiudzetasApp:
    def __init__(self):
        self.biudzetas = {}
        self.langas = tk.Tk()

        self.uzrasas_pajamos = tk.Label(self.langas, text="Pajamos:")
        self.uzrasas_pajamos.pack()

        self.pajamu_ivestis = tk.Entry(self.langas)
        self.pajamu_ivestis.pack()

        self.uzrasas_islaidos = tk.Label(self.langas, text="Išlaidos:")
        self.uzrasas_islaidos.pack()

        self.islaidu_ivestis = tk.Entry(self.langas)
        self.islaidu_ivestis.pack()

        self.prideti_pajamu_mygtukas = tk.Button(self.langas, text="Pridėti pajamas", command=self.prideti_pajamas)
        self.prideti_pajamu_mygtukas.pack()

        self.prideti_islaidas_mygtukas = tk.Button(self.langas, text="Pridėti išlaidas", command=self.prideti_islaidas)
        self.prideti_islaidas_mygtukas.pack()

        self.balanso_uzrasas = tk.Label(self.langas, text="Balansas: 0 €")
        self.balanso_uzrasas.pack()

        self.issaugoti_mygtukas = tk.Button(self.langas, text="Išsaugoti biudžetą", command=self.issaugoti_biudzeta)
        self.issaugoti_mygtukas.pack()

        self.ikelti_mygtukas = tk.Button(self.langas, text="Įkelti biudžetą", command=self.ikelti_biudzeta)
        self.ikelti_mygtukas.pack()

        self.rodyti_langa()

    def prideti_pajamas(self):
        pajamos = float(self.pajamu_ivestis.get())
        if pajamos > 0:
            self.biudzetas['pajamos'] = self.biudzetas.get('pajamos', 0) + pajamos
            self.atnaujinti_balansa()
            messagebox.showinfo("Pajamos pridėtos", f"Pajamos pridėtos: {pajamos} €")
        else:
            messagebox.showerror("Klaida", "Netinkamos pajamos")

        self.pajamu_ivestis.delete(0, tk.END)

    def prideti_islaidas(self):
        islaidos = float(self.islaidu_ivestis.get())
        if islaidos > 0 and islaidos <= self.biudzetas.get('pajamos', 0):
            self.biudzetas['islaidos'] = self.biudzetas.get('islaidos', 0) + islaidos
            self.atnaujinti_balansa()
            messagebox.showinfo("Išlaidos pridėtos", f"Išlaidos pridėtos: {islaidos} €")
        else:
            messagebox.showerror("Klaida", "Netinkamos išlaidos arba per didelė suma")

        self.islaidu_ivestis.delete(0, tk.END)

    def atnaujinti_balansa(self):
        balansas = self.biudzetas.get('pajamos', 0) - self.biudzetas.get('islaidos', 0)
        self.balanso_uzrasas.config(text=f"Balansas: {balansas} €")

    def issaugoti_biudzeta(self):
        with open('biudzetas.pickle', 'wb') as failas:
            pickle.dump(self.biudzetas, failas)

        messagebox.showinfo("Biudžetas išsaugotas", "Biudžetas buvo išsaugotas į failą")

    def ikelti_biudzeta(self):
        try:
            with open('biudzetas.pickle', 'rb') as failas:
                self.biudzetas = pickle.load(failas)

            self.atnaujinti_balansa()
            messagebox.showinfo("Biudžetas įkeltas", "Biudžetas buvo įkeltas iš failo")
        except FileNotFoundError:
            messagebox.showerror("Klaida", "Biudžeto failas nerastas")

    def rodyti_langa(self):
        self.langas.mainloop()


if __name__ == '__main__':
    programa = BiudzetasApp()
    programa.rodyti_langa()
