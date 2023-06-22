from ursina import *

player = Entity(model="cube", collider="box", y=1)


def avencée():
    global player
    if player.rotation_y == 0:
        player.z += 1
    elif player.rotation_y == 270:
        player.x += 1
    elif player.rotation_y == 90:
        player.x -= 1
    elif player.rotation_y == 180:
        player.z -= 1
        


def gauche():
    global player
    player.rotation_y += 90
    if player.rotation_y == 360:
        player.rotation_y = 0


def droite():
    global player
    player.rotation_y -= 90
    if player.rotation_y == 0:
        player.rotation_y = 360
