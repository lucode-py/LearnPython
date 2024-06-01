import tkinter as tk

def afficher_frame(frame):
    frame.tkraise()

# Création de la fenêtre principale
fenetre = tk.Tk()

# Création des frames
frame1 = tk.Frame(fenetre)
frame2 = tk.Frame(fenetre)

# Ajout des widgets à chaque frame
# ...

# Affichage de la première frame au démarrage
frame1.pack()

lb1 = tk.Label(frame1, text='test').pack()
lb2 = tk.Label(frame2, text='test2').pack()

# Bouton pour passer à la frame suivante
bouton_suivant = tk.Button(fenetre, text="Suivant", command=lambda: afficher_frame(frame2))
bouton_suivant.pack()

# Bouton pour revenir à la frame précédente
bouton_precedent = tk.Button(fenetre, text="Précédent", command=lambda: afficher_frame(frame1))
bouton_precedent.pack()

# Démarrage de la boucle principale de la fenêtre
fenetre.mainloop()