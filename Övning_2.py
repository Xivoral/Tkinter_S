#Importerar tkinter som tk, messagebox från tkinter biblioteket
import tkinter as tk
from tkinter import messagebox

#Skapar root, ger fönstret titeln "Övning 2 - Roligt att programmera"
root = tk.Tk()
root.title("Övning 2 - Roligt att programmera")

#Skapar en funktion fråga_om_programmering 
def fråga_om_programmering():
    svar = messagebox.askquestion("Fråga", "Tycker du att det är roligt att programmera?")
    if svar == "yes":
        etikett.config(text="Vad kul att höra!")
    else:
        etikett.config(text="Det blir roligare med tiden!")
#Skapar knapp som kör fråga_om_programmering funktionen när knappen klickas
knapp = tk.Button(root, text="Klicka här", command=fråga_om_programmering)
knapp.pack(pady=10)
#Skapar en etikett där resultatet av fråga_om_programmering ändrar texten i etiketten
etikett = tk.Label(root, text="")
etikett.pack(pady=10)
#Kör applikationen
root.mainloop()