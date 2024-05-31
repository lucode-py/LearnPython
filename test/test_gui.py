import customtkinter
import os

class LearnPythonIDE(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("LearnPython IDE")
        self.geometry("800x600")
        customtkinter.set_appearance_mode("System")

        # Widget Text pour le code Python
        self.code_text = customtkinter.CTkTextbox(self, height=20, font=("menlo", 15))
        self.code_text.pack(padx=10, pady=10, fill="both", expand=True)
        self.code_text.insert("1.0", "edit your code here")

        # Bouton pour sauvegarder le code
        self.save_button = customtkinter.CTkButton(self, text="Sauvegarder", command=self.save_code)
        self.save_button.pack(pady=10)

    def save_code(self):
        code = self.code_text.get("1.0", "end-1c")
        with open("code.txt", "w") as file:
            file.write(code)
        print("Code sauvegardé dans code.txt")

if __name__ == "__main__":
    app = LearnPythonIDE()
    app.mainloop()
