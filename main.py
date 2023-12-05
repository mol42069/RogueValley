import pygame as pg
from script import game



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


def init():
    global root
    pg.init()
    root = pg.display.set_mode()
    game.game_init(screen_size, player_pos)


if __name__ == '__main__':
    main()

