from ursina import *

app = Ursina()

player = Entity(model='quad', color=color.orange, scale_y=2)

def update():  
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1
    player.z += held_keys['w'] * .1
    player.z -= held_keys['s'] * .1

app.run() 