from ursina import *
from wall import wall
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader
from mouvement import player
from edit_player import edit
import subprocess
from time import sleep


app = Ursina()
window.borderless = False
window.size = (1100, 900)
wall()
player.position=(0,1,0)
Sky()
EditorCamera()
app.run()