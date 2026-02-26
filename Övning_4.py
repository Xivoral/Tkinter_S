import tkinter as tk

root = tk.Tk()
root.title("Byt knapptext")

#Funktion som byter text på knapparna
def byt_text():
    if knapp_vänster["text"]=="Vänster":
        knapp_vänster.config(text="Höger")
        knapp_höger.config(text="Vänster")
    else:
        knapp_vänster.config(text="Vänster")
        knapp_höger.config(text="Höger")
#Skapar knappar
knapp_vänster = tk.Button(root, text="Vänster", command=byt_text)
knapp_höger = tk.Button(root, text="Höger", command=byt_text)
#Använder grid för att placera knapparna
knapp_vänster.grid(row=0, column=0, padx=10, pady=10)
knapp_höger.grid(row=0, column=1, padx=10, pady=10)

root.mainloop()