import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Beställ din drömpizza")

# --- Frame för pizzastorlek ---

storleksram = tk.LabelFrame(root, text="Välj storlek", padx=10, pady=10)
storleksram.grid(row=0, column=0, padx=10, pady=10)

storlek = tk.StringVar(value="Mellan")

tk.Radiobutton(storleksram, text="Liten", variable=storlek, value="Liten").pack(anchor="w")
tk.Radiobutton(storleksram, text="Mellan", variable=storlek, value="Mellan").pack(anchor="w")
tk.Radiobutton(storleksram, text="Stor", variable=storlek, value="Stor").pack(anchor="w")

# --- Frame för tilläg ---
tillägsram = tk.LabelFrame(root, text="Välj tillägg", padx=10, pady=10)
tillägsram.grid(row=0, column=1, padx=10, pady=10)

ost = tk.BooleanVar()
sås = tk.BooleanVar()
glutenfri = tk.BooleanVar()

tk.Checkbutton(tillägsram, text="Extra ost", variable=ost).pack(anchor="w")
tk.Checkbutton(tillägsram, text="Vitlökssås", variable=sås).pack(anchor="w")
tk.Checkbutton(tillägsram, text="Glutenfri botten", variable=glutenfri).pack(anchor="w")

# --- Önskemål (textfält) ---
önskemål_label = tk.Label(root, text="Egna önskemål")
önskemål_label.grid(row=1, column=0, sticky="w", padx=10)

önskemål_fält = tk.Text(root, height=4, width=40)
önskemål_fält.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# --- Skicka-knapp ---
def skicka_beställning():
    tillägg = []
    if ost.get(): tillägg.append("extra ost")
    if sås.get(): tillägg.append("vitlökssås")
    if glutenfri.get(): tillägg.append("glutenfri botten")

    kommentar = önskemål_fält.get("1.0", tk.END).strip()
    sammanfattning = f"Du har beställt en {storlek.get().lower()} pizza "

    if tillägg:
        sammanfattning += "med " + ", ".join(tillägg)
    if kommentar:
        sammanfattning += f".\nÖnskemål: {kommentar}"
    else:
        sammanfattning += "."
    
    messagebox.showinfo("Beställning skickad!", sammanfattning)

skicka_knapp = tk.Button(root, text="Skicka beställning", command=skicka_beställning)
skicka_knapp.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()