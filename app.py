import tkinter as tk

fenetre = tk.Tk()
fenetre.title("Welf.io")
fenetre.geometry("600x400")

titre = tk.Label(fenetre, text="Welf.io", font=("Arial", 30))
titre.pack(pady=100)

fenetre.mainloop()
