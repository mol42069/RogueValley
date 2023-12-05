import enemy

player_pos = [800, 500]
screen_size = []
next_ai = False

def game_init(s_size, p_pos):
    global screen_size, player_pos

    screen_size = s_size
    player_pos = p_pos



def enemies(hostiles):
    global player_pos, next_ai

    if next_ai :
        for hostile in hostiles:
            hostile.ai(player_pos)
            hostile.animation()

    return

def logic():


    return

def spawn(pos, hostiles, creature="zombie"):
    foe = None
    match creature:
        case "zombie":
            foe = enemy.Zombie(pos, level, ani_sprite, attacks_sprites)
        case default:
            return


    hostiles.append(foe)



    return



