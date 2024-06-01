import customtkinter as ctk

def afficher_frame(frame):
    frame.pack()
    fenetre.frame_actuelle = frame

def revenir_frame_precedente():
    frame_actuelle = fenetre.frame_actuelle
    frame_actuelle.pack_forget()
    frame_precedente = historique_frames.pop()
    afficher_frame(frame_precedente)

# Création de la fenêtre principale
fenetre = ctk.CTk()
fenetre.frame_actuelle = None  # Ajout d'un attribut pour suivre la frame actuelle

# Création des frames
frame1 = ctk.CTkFrame(fenetre)
frame2 = ctk.CTkFrame(fenetre)

# Ajout des widgets à chaque frame
# ...

# Affichage de la première frame au démarrage
afficher_frame(frame1)

# Historique des frames visitées
historique_frames = [frame1]

# Bouton pour passer à la frame suivante
bouton_suivant = ctk.CTkButton(fenetre, text="Suivant", command=lambda: afficher_frame(frame2))
bouton_suivant.pack()

# Bouton pour revenir à la frame précédente
bouton_precedent = ctk.CTkButton(fenetre, text="Précédent", command=revenir_frame_precedente)
bouton_precedent.pack()

# Démarrage de la boucle principale de la fenêtre
fenetre.mainloop()
