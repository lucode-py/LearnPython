from ursina import *
from wall import wall
from ursina.shaders.lit_with_shadows_shader import lit_with_shadows_shader
from mouvement import player

Entity.default_shader = lit_with_shadows_shader


app = Ursina()
window.borderless = False
window.size = (1100, 900)
wall()
player.position=(0,1,0)
Sky()
sun = DirectionalLight(shadow_map_resolution=(2048, 2048), shadows=True, rotation_x=35, rotation_y=25)
EditorCamera()
app.run()
