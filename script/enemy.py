import math

class Enemy:

    def __init__(self, pos, level, hp, damage, ani_sprite, attacks_sprites, sec_cooldown=5):

        self.pos = pos
        self.level = level
        self.ani_count = 0
        self.ani_sprite = ani_sprite
        self.attacks_sprites = attacks_sprites
        self.hp = hp
        self.damage = damage
        self.sec_cooldown = sec_cooldown


    def animation(self):

        return

    def c_attack(self):
        # TODO: HERE WE START AN ATTACK ANIMATION AND THEN IF PLAYER HIT SUBTRACT DAMAGE FROM PLAYER HEALTH
        return

    def s_attack(self):
        # TODO: HERE WE START AN ATTACK ANIMATION AND THEN IF PLAYER HIT SUBTRACT DAMAGE FROM PLAYER HEALTH
        return

class Zombie(Enemy):

    def __init__(self, pos, level, ani_sprite, attacks_sprites, sec_cooldown=5):

        starting_hp = 10
        starting_damage = 2
        hp = starting_hp * (math.floor(level / 5) + 1)
        damage = starting_damage * (math.floor(level / 5) + 1)

        super().__init__(pos, level, hp, damage, ani_sprite, attacks_sprites, sec_cooldown)

    def c_attack(self):
        super().c_attack()


    def s_attack(self):
        super().s_attack()

    def ai(self, p_pos):

        return

# TODO: HERE WE ADD OTHER ENEMIES