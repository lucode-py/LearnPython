import customtkinter
import subprocess
import os
import signal


window = customtkinter.CTk()
window.geometry("550x900")
window.title("learn python")
customtkinter.set_appearance_mode("System")



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
sidebar_frame = customtkinter.CTkFrame(window, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
window.grid_rowconfigure(4, weight=1)


logo_label = customtkinter.CTkLabel(sidebar_frame, text="Learn Python", font=customtkinter.CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

sidebar_button_1 = customtkinter.CTkButton(sidebar_frame, text="les Variables")
sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

play_button = customtkinter.CTkButton(sidebar_frame, text="Executer le programe", command=reboot)
play_button.grid(row=6, column=0, padx=20, pady=(10, 10))

appearance_mode_optionemenu = customtkinter.CTkOptionMenu(sidebar_frame, values=["Dark", "Light", "System"], command=change_appearance_mode_event)
appearance_mode_optionemenu.grid(row=11, column=0, padx=20, pady=(10, 10))



box_cour = customtkinter.CTkTextbox(window, width=330, font=("menlo", 15))
box_cour.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
box_cour.insert("5.5", "edit your code")

window.mainloop()