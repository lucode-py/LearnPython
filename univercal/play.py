from customtkinter import *
import os
from PIL import Image, ImageTk

# Détecter le mode sombre ou clair
is_dark_mode = get_appearance_mode() == "Dark"

# Fonction pour charger les images
image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

variable_image = CTkImage(light_image=Image.open(os.path.join(image_path, "variable_dark.png")),
                                         dark_image=Image.open(os.path.join(image_path, "variable_white.png")),
                                         size=(200, 200))

condition_image = CTkImage(light_image=Image.open(os.path.join(image_path, "condition_dark.png")),
                                         dark_image=Image.open(os.path.join(image_path, "condition_white.png")),
                                         size=(200, 200))

fonction_image = CTkImage(light_image=Image.open(os.path.join(image_path, "fonction_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "fonction_white.png")),
                                             size=(200, 200))

play_image = CTkImage(light_image=Image.open(os.path.join(image_path, "play_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "play_white.png")),
                                             size=(200, 200))

boucle_image = CTkImage(light_image=Image.open(os.path.join(image_path, "boucle_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "boucle_white.png")),
                                             size=(200, 200))



# Fonction pour obtenir la couleur du fond en fonction du mode


# Application principale
app = CTk()
app.title("LearnPython Chapters")
app.geometry("1575x635")

# Mettre à jour l'apparence selon le mode système


# Cadre central
central_frame = CTkFrame(app, fg_color="transparent")
central_frame.pack(expand=True, padx=20, pady=20)

# Fonction pour créer un chapitre
chapter_frames = []
def create_chapter(frame, title, description, image_name, row, column):
    chapter_frame = CTkFrame(frame, corner_radius=12, height=200, width=200)
    chapter_frame.grid(row=row, column=column, padx=30, pady=20)
    chapter_frames.append(chapter_frame)
    title_label = CTkLabel(chapter_frame, text=title, font=("calibri", 25))
    title_label.pack(pady=12, side=TOP, padx=30)
    logo_label = CTkLabel(chapter_frame, image=image_name, text="")
    logo_label.image = image_name  # Keep a reference to avoid garbage collection
    logo_label.pack(pady=12)
    description_label = CTkLabel(chapter_frame, text=description)
    description_label.pack(padx=30, pady=30)
    start_button = CTkButton(chapter_frame, text="Commencer")
    start_button.pack(side=BOTTOM, pady=12)

# Créer les chapitres
create_chapter(central_frame, "Les variables", "Apprenez à utiliser les variables.", variable_image, 0, 0)
create_chapter(central_frame, "Les conditions", "Maîtrisez les conditions", condition_image, 0, 1)
create_chapter(central_frame, "Les boucles", "Comprenez les boucles for et while.", boucle_image, 0, 2)
create_chapter(central_frame, "Les fonctions", "Découvrez comment créer des fonctions.", fonction_image, 0, 3)



# Détecter les changements de mode
set_appearance_mode("System") 

app.mainloop()
