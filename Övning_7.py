import tkinter as tk

root = tk.Tk()
root.title("Beräkna 50-årsdag")

def beräkna_50_årsdag():
    namn = namn_entry.get()
    try:
        födelseår = int(år_entry.get())
        år_50 = födelseår + 50
        resultat_label.config(text=f"År {år_50} fyller {namn} 50 år.")
    except ValueError:
        resultat_label.config(text="Skriv ett giltigt årtal.")
    
# Namn
namn_label = tk.Label(root, text="Skriv ett namn:")
namn_label.grid(row=0, column=0, padx=10, pady=10)

namn_entry = tk.Entry(root)
namn_entry.grid(row=0, column=1, padx=10, pady=10)

# Årtal
år_label = tk.Label(root, text="Födelseår:")
år_label.grid(row=1, column=0, padx=10, pady=10)

år_entry = tk.Entry(root)
år_entry.grid(row=1, column=1, padx=10, pady=10)

# Kör-knapp
kör_knapp = tk.Button(root, text="Beräkna", command=beräkna_50_årsdag)
kör_knapp.grid(row=2, column=0, columnspan=2, pady=10)

# Resultat
resultat_label = tk.Label(root, text="")
resultat_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()