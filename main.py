import pygame as pg
from script import game



root = None
running = True
hostiles = []

def main():
    global root, running
    init()

    while running:

        for event in pg.event.get():

            if event.type == pg.QUIT:
                running = False
                exit()


def enemies():
    global running, hostiles



    while running:
        hostiles = game.enemies(hostiles)


def init():
    global root
    pg.init()

    root = pg.display.set_mode()


if __name__ == '__main__':
    main()

