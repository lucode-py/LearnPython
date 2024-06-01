import customtkinter
import subprocess
import os
import signal
from PIL import Image


window = customtkinter.CTk()
window.geometry("550x900")
window.title("learn python")
customtkinter.set_appearance_mode("System")

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# resize des differentes image

image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "logo")

image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")),
                                               size=(20, 20))

variable_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "variable_dark.png")),
                                         dark_image=Image.open(os.path.join(image_path, "variable_white.png")),
                                         size=(20, 20))

condition_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "condition_dark.png")),
                                         dark_image=Image.open(os.path.join(image_path, "condition_white.png")),
                                         size=(20, 20))

fonction_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "fonction_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "fonction_white.png")),
                                             size=(20, 20))

play_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "play_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "play_white.png")),
                                             size=(20, 20))

boucle_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "boucle_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "boucle_white.png")),
                                             size=(20, 20))

one_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "1_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "1_white.png")),
                                             size=(20, 20))

two_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "2_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "2_white.png")),
                                             size=(20, 20))

three_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "3_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "3_white.png")),
                                             size=(20, 20))

four_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "4_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "4_white.png")),
                                             size=(20, 20))

five_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "5_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "5_white.png")),
                                             size=(20, 20))

six_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "6_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "6_white.png")),
                                             size=(20, 20))

seven_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "7_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "7_white.png")),
                                             size=(20, 20))

eight_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "8_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "8_white.png")),
                                             size=(20, 20))

nine_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "9_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "9_white.png")),
                                             size=(20, 20))

ten_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "10_dark.png")),
                                             dark_image=Image.open(os.path.join(image_path, "10_white.png")),
                                             size=(20, 20))

#demarage du playground
with open('sortie.txt', 'w') as fichier_sortie:
    subprocess.Popen(['python3', "playground_mac.py"], stdout=fichier_sortie, stderr=subprocess.STDOUT)

def change_appearance_mode_event(new_appearance_mode: str):
    customtkinter.set_appearance_mode(new_appearance_mode)

def reboot():
    commande = "pgrep Python"
    id_processus = subprocess.check_output(commande, shell=True, universal_newlines=True)


    pattern = "\n"  # Le motif jusqu'auquel vous souhaitez extraire la chaîne

    position = id_processus.find(pattern)  # Trouver la position du motif

    if position != -1:
        pid = id_processus[:position]  # Effectuer le découpage jusqu'à la position
    else:
        pid = id_processus  # Si le motif n'est pas trouvé, prendre toute la chaîne

    os.kill(int(pid), signal.SIGTERM)
    with open('sortie.txt', 'w') as fichier_sortie:
        subprocess.Popen(['python3', "playground_mac.py"], stdout=fichier_sortie, stderr=subprocess.STDOUT)


# sidebar
sidebar_frame = customtkinter.CTkFrame(window, width=180, corner_radius=0)
sidebar_frame.grid(row=0, column=0, sticky="nsew")
sidebar_frame.grid_rowconfigure(4, weight=1)


logo_label = customtkinter.CTkLabel(sidebar_frame, text="Learn Python", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

chapters = customtkinter.CTkScrollableFrame(master=sidebar_frame, width=100, height=700, fg_color="transparent")
chapters.grid(row=2, column=0, sticky="nsew")



#boutton du chapitre
chapter_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Les Variable",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=variable_image, anchor="w")
chapter_Variable.grid(row=1, column=0, sticky="ew")

#boutton defi

one_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 1",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=one_image, anchor="w")
one_Variable.grid(row=2, column=0, sticky="ew")

tow_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 2",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=two_image, anchor="w")
tow_Variable.grid(row=3, column=0, sticky="ew")

three_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 3",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=three_image, anchor="w")
three_Variable.grid(row=4, column=0, sticky="ew")

four_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 4",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=four_image, anchor="w")
four_Variable.grid(row=5, column=0, sticky="ew")

five_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 5",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=five_image, anchor="w")
five_Variable.grid(row=6, column=0, sticky="ew")

six_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 6",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=six_image, anchor="w")
six_Variable.grid(row=7, column=0, sticky="ew")

seven_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 7",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=seven_image, anchor="w")
seven_Variable.grid(row=8, column=0, sticky="ew")

eight_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 8",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=eight_image, anchor="w")
eight_Variable.grid(row=9, column=0, sticky="ew")

nine_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 9",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=nine_image, anchor="w")
nine_Variable.grid(row=10, column=0, sticky="ew")

ten_Variable = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 10",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=ten_image, anchor="w")
ten_Variable.grid(row=11, column=0, sticky="ew")

#boutton du chapitre
chapter_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                              text="Les Condition",
                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                              hover_color=("gray70", "gray30"),
                                              image=condition_image, anchor="w")
chapter_condition.grid(row=12, column=0, sticky="ew")
#boutton des defi

one_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 1",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=one_image, anchor="w")
one_condition.grid(row=13, column=0, sticky="ew")

tow_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 2",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=two_image, anchor="w")
tow_condition.grid(row=14, column=0, sticky="ew")

three_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 3",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=three_image, anchor="w")
three_condition.grid(row=15, column=0, sticky="ew")

four_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 4",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=four_image, anchor="w")
four_condition.grid(row=16, column=0, sticky="ew")

five_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 5",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=five_image, anchor="w")
five_condition.grid(row=17, column=0, sticky="ew")

six_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 6",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=six_image, anchor="w")
six_condition.grid(row=18, column=0, sticky="ew")

seven_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 7",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=seven_image, anchor="w")
seven_condition.grid(row=19, column=0, sticky="ew")

eight_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 8",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=eight_image, anchor="w")
eight_condition.grid(row=20, column=0, sticky="ew")

nine_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 9",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=nine_image, anchor="w")
nine_condition.grid(row=21, column=0, sticky="ew")

ten_condition = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 10",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=ten_image, anchor="w")
ten_condition.grid(row=22, column=0, sticky="ew")

#boutton du chapitre
chapter_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                              text="Les Fonction",
                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                              hover_color=("gray70", "gray30"),
                                              image=fonction_image, anchor="w")
chapter_function.grid(row=23, column=0, sticky="ew")

#boutton des defi

one_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 1",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=one_image, anchor="w")
one_function.grid(row=24, column=0, sticky="ew")

tow_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 2",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=two_image, anchor="w")
tow_function.grid(row=25, column=0, sticky="ew")

three_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 3",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=three_image, anchor="w")
three_function.grid(row=26, column=0, sticky="ew")

four_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 4",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=four_image, anchor="w")
four_function.grid(row=27, column=0, sticky="ew")

five_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 5",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=five_image, anchor="w")
five_function.grid(row=28, column=0, sticky="ew")

six_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 6",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=six_image, anchor="w")
six_function.grid(row=29, column=0, sticky="ew")

seven_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 7",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=seven_image, anchor="w")
seven_function.grid(row=30, column=0, sticky="ew")

eight_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 8",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=eight_image, anchor="w")
eight_function.grid(row=31, column=0, sticky="ew")

nine_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 9",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=nine_image, anchor="w")
nine_function.grid(row=32, column=0, sticky="ew")

ten_function = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 10",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=ten_image, anchor="w")
ten_function.grid(row=33, column=0, sticky="ew")

#boutton du chapitre
chapter_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                              text="Les Boucle",
                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                              hover_color=("gray70", "gray30"),
                                              image=boucle_image, anchor="w")
chapter_boucle.grid(row=34, column=0, sticky="ew")

# boutton defi

one_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 1",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=one_image, anchor="w")
one_boucle.grid(row=35, column=0, sticky="ew")

tow_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 2",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=two_image, anchor="w")
tow_boucle.grid(row=36, column=0, sticky="ew")

three_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 3",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=three_image, anchor="w")
three_boucle.grid(row=37, column=0, sticky="ew")

four_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 4",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=four_image, anchor="w")
four_boucle.grid(row=38, column=0, sticky="ew")

five_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 5",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=five_image, anchor="w")
five_boucle.grid(row=39, column=0, sticky="ew")

six_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 6",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=six_image, anchor="w")
six_boucle.grid(row=40, column=0, sticky="ew")

seven_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 7",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=seven_image, anchor="w")
seven_boucle.grid(row=41, column=0, sticky="ew")

eight_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 8",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=eight_image, anchor="w")
eight_boucle.grid(row=42, column=0, sticky="ew")

nine_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 9",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=nine_image, anchor="w")
nine_boucle.grid(row=43, column=0, sticky="ew")

ten_boucle = customtkinter.CTkButton(chapters, corner_radius=0, height=40, border_spacing=10,
                                           text="Defi 10",
                                           fg_color="transparent", text_color=("gray10", "gray90"),
                                           hover_color=("gray70", "gray30"),
                                           image=ten_image, anchor="w")
ten_boucle.grid(row=44, column=0, sticky="ew")

#partit bas de la sidebar

play_button = customtkinter.CTkButton(sidebar_frame, corner_radius=0, height=40, border_spacing=10,
                                              text="Executer le programe",
                                              fg_color="transparent", text_color=("gray10", "gray90"),
                                              hover_color=("gray70", "gray30"),
                                              image=play_image, anchor="w", command=reboot)
play_button.grid(row=10, column=0, sticky="s")

appearance_mode_menu = customtkinter.CTkOptionMenu(sidebar_frame, values=["Light", "Dark", "System"],
                                                                command=change_appearance_mode_event)
appearance_mode_menu.grid(row=11, column=0, padx=20, pady=20, sticky="s")



box_cour = customtkinter.CTkTextbox(window, width=330, font=("menlo", 15))
box_cour.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
box_cour.insert("5.5", "edit your code")

window.mainloop()