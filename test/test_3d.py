from ursina import Ursina, Entity, Sky, EditorCamera, Button, invoke

class UrsinaApp():
    def __init__(self):
        super().__init__()
        self.app = Ursina()
        self.create_environment()

    def create_environment(self):
        self.player = Entity(model="cube", collider="box", y=1, scale=(1, 1, 1))
        self.wall()
        Sky()
        EditorCamera()

        # Bouton Exécuter
        run_button = Button(text='Exécuter', position=(0.7, -0.45), scale=(0.12, 0.05))
        run_button.on_click = self.execute_code
        self.command_queue = []
        self.executing = False

    def wall(self):
        Zpos = 5
        Xpos = 5
        compteur = 0
        for i in range(100):
            compteur += 1
            Entity(model="cube", collider="box", z=Zpos, x=Xpos, texture="grass")
            Zpos -= 1
            if compteur == 10:
                compteur = 0
                Xpos -= 1
                Zpos = 5

    def execute_code(self):
        try:
            with open("code.txt", "r") as file:
                code = file.read()
            exec(code, globals())
        except Exception as e:
            print(f"Erreur lors de l'exécution du code : {e}")

    def run(self):
        self.app.run()

    def add_command(self, command):
        self.command_queue.append(command)
        if not self.executing:
            self.execute_next_command()

    def execute_next_command(self):
        if self.command_queue:
            self.executing = True
            command = self.command_queue.pop(0)
            command()
            invoke(self.execute_next_command, delay=1)
        else:
            self.executing = False

# Fonctions de mouvement du joueur
def avancer():
    def action():
        if app.player.rotation_y == 0:
            app.player.z += 1
        elif app.player.rotation_y == 270:
            app.player.x += 1
        elif app.player.rotation_y == 90:
            app.player.x -= 1
        elif app.player.rotation_y == 180:
            app.player.z -= 1
    app.add_command(action)

def gauche():
    def action():
        app.player.rotation_y += 90
        if app.player.rotation_y == 360:
            app.player.rotation_y = 0
    app.add_command(action)

def droite():
    def action():
        app.player.rotation_y -= 90
        if app.player.rotation_y == 0:
            app.player.rotation_y = 360
    app.add_command(action)

if __name__ == "__main__":
    app = UrsinaApp()
    app.run()
