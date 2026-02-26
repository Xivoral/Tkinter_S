import tkinter as tk

root = tk.Tk()
root.title("Beräkna summan")

# Funktion som beräknar och uppdaterar etiketten
def beräkna_summan():
    try:
        tal1 = int(textruta1.get()) #Hämtar det första talet från textrutan
        tal2 = int(textruta2.get()) #Hämtar det andra talet från textrutan
        summa = tal1 + tal2 # Beräknar summan
        resultat_label.config(text=f"Summan av {tal1} och {tal2} är {summa}") # Uppdaterar etiketten med resultaten

    except ValueError:
        resultat_label.config(text="Var god och skriv giltiga heltal") # Hanterar ogiltig inmatning

# Skapar etiketter, textrutor och knapp
etikett1 = tk.Label(root, text="Skriv det första talet:")
etikett1.grid(row=0, column=0, padx=10, pady=10)


textruta1 = tk.Entry(root)
textruta1.grid(row=0, column=1, padx=10, pady=10)

etikett2 = tk.Label(root, text="Skriv det andra talet:")
etikett2.grid(row=1, column=0, padx=10, pady=10)

textruta2 = tk.Entry(root)
textruta2.grid(row=1, column=1, padx=10, pady=10)

knapp = tk.Button(root, text="Kör", command=beräkna_summan)
knapp.grid(row=2, column=0, columnspan=2, pady=10)

resultat_label = tk.Label(root, text="")
resultat_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()