#Importerar tkinter
import tkinter          


#Skapar the root
root = tkinter.Tk() 
#Namnger tkinter fönstret till "Mitt första program"
root.title("Mitt första program")

#Skapar en funktion som ändrar texten hos variabeln etikett till "Hej världen!"
def säg_hej():
    etikett.config(text="Hej världen!")

#Skapar en tkinter knapp med texten "Tryck här", när man trycker på knappen så kallar man på funktionen säg_hej
knapp = tkinter.Button(root, text="Tryck här", command=säg_hej)
#Skapar en padding på 10 pixlar på y-axeln och placerar i pack
#med andra ord så ska det vara 10 pixlars avstånd mellan knappen och andra widgets på y-axeln
knapp.pack(pady=10)
#Skapar en etikett som för tillfället inget står i, men när knappen trycks så kommer det att stå "Hej världen!"
etikett = tkinter.Label(root, text="")
#Skapar en padding på 10 pixlar på y-axeln och placerar i pack
etikett.pack(pady=10)
#Kallar på metoden mainloop(), det får applikationen att köra.
root.mainloop()