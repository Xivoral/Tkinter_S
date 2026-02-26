import tkinter as tk

root = tk.Tk()
root.title("Övning 3 - Byt bakgrundsfärg")

#funktioner som byter färg
def gör_röd():
    root.config(bg="red")

def gör_blå():
    root.config(bg="blue")
#skapar knapparna
knapp_röd = tk.Button(root, text="Röd", command=gör_röd)
knapp_röd.pack(pady=10)

knapp_blå = tk.Button(root, text="Blå", command=gör_blå)
knapp_blå.pack(pady=10)

root.mainloop()