import random

import enemy

player_pos = [800, 500]
screen_size = []
next_ai = False
hostiles = []
enemy_level = 1
sprites = [[],[]]

def game_init(s_size, p_pos):
    global screen_size, player_pos, sprites, enemy_level

    screen_size = s_size
    player_pos = p_pos
    enemy_level = 1
    sprites = [[],[]]



def enemies():
    global player_pos, next_ai, hostiles

    if next_ai :
        for hostile in hostiles:
            hostile.ai(player_pos)
            hostile.animation()

    return

def update():


    return

def draw(root):

    return root

def spawn(pos, creature="zombie"):
    global enemy_level, sprites, enemy_level, hostiles

    foe = None
    level = enemy_level + random.randint(0, 10) - 5

    if level <= 0:
        level = enemy_level

    match creature:
        case "zombie":
            foe = enemy.Zombie(pos, level, sprites)

        case default:
            return

    hostiles.append(foe)

    return



