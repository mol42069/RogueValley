import random
import pygame as pg
from script import enemy
from script.enums import Colors



player_pos = [800, 500]
screen_size = []
next_ai = False
hostiles = []
enemy_level = 1
sprites = [[],[]]

game_map = None
game_map_pos = [0, 0]

def game_init(s_size, p_pos):
    global screen_size, player_pos, sprites, enemy_level, game_map, colors

    game_map = pg.Surface((3840, 2160))
    game_map.fill(Colors.black.value)

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

    game_map.fill(Colors.light_grey.value)

    root.blit(game_map, game_map_pos)

    pg.display.update()

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



