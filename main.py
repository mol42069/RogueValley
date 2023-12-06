import pygame as pg
from script import game
import threading



root = None
running = True
hostiles = []
screen_size = []
player_pos = []

def main():
    global root, running
    init()

    while running:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
                exit()

            if event.type == pg.KEYDOWN:

                pass

            if event.type == pg.KEYUP:

                pass


def key_handler():


    return


def enemies():
    global running, hostiles

    while running:
        game.enemies()

    return

def disp():
    global root, running

    while running:
        root = game.draw(root)

    return

def update():
    global running

    while running:

        game.update()



def init():
    global root
    pg.init()
    root = pg.display.set_mode()
    game.game_init(screen_size, player_pos)

    update_thread = threading.Thread(target=update, args=())
    display_thread = threading.Thread(target=disp, args=())
    update_thread.start()
    display_thread.start()

if __name__ == '__main__':
    main()

