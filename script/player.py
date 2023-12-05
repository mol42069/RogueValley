
class Player:

    def __init__(self, player_sprites,starting_speed=5, pos=(800, 500), starting_dmg=5, starting_hp=50):
        self.hp = starting_hp
        self.damage = starting_dmg
        self.sprites = player_sprites
        self.pos = pos
        self.speed = starting_speed

        return