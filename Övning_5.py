import tkinter as tk

root = tk.Tk()
root.title("Beräkna kvadraten")

#Funktion som beräknar kvadraten och uppdaterar etiketten
def beräkna_kvadrat():
    try:
        tal = float(textruta.get())
        kvadrat = tal**2
        resultat_label.config(text=f"Kvadraten av {tal} är {kvadrat}") # Uppdaterar etiketten med resultatet
    except ValueError:
        resultat_label.config(text="Var god och skriv ett giltigt tal") # Hanterar ogiltig inmatning
    
#Skapa etikett, textröta, knapp
etikett = tk.Label(root, text="Skriv ett tal:")
etikett.grid(row=0, column=0, padx=10, pady=10)

textruta = tk.Entry(root)
textruta.grid(row=0, column=1, padx=10, pady=10)

knapp = tk.Button(root, text="Beräkna kvadrat", command=beräkna_kvadrat)
knapp.grid(row=1, column=0, columnspan=2, pady=10)

resultat_label = tk.Label(root, text="")
resultat_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()