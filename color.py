import config

colors = {
    'Mario1'           : '\x1b[1;34m',
    'Mario2'           : '\x1b[1;31m',
    'Black'            : '\x1b[1;30m',
    'Blue'             : '\x1b[1;94m',
    'Green'            : '\x1b[1;92m',
    'Cyan'             : '\x1b[0;36m',
    'Red'              : '\x1b[0;31m',
    'Purple'           : '\x1b[0;35m',
    'Brown'            : '\x1b[0;33m',
    'Gray'             : '\x1b[0;37m',
    'Dark Gray'        : '\x1b[1;30m',
    'Light Blue'       : '\x1b[1;34m',
    'Light Cyan'       : '\x1b[1;36m',
    'Light Red'        : '\x1b[1;31m',
    'Light Purple'     : '\x1b[1;35m',
    'Yellow'           : '\x1b[1;33m',
    'White'            : '\x1b[1;37m'
}

def getcolor(charac,mario):
    color="White"

    if mario._level==1:
        if charac==config._mario_head or charac==config._mario_hand_right or charac==config._mario_base :
            color="Mario1"
        elif charac==config._mario_eye or charac==config._mario_hand_left or charac==config._mario_leg_left :
            color="Mario1"
        elif charac==config._mario_neck or charac==config._mario_skin or charac==config._mario_leg_right :
            color="Mario1"
    elif mario._level==2:
        if charac==config._mario_head or charac==config._mario_hand_right or charac==config._mario_base :
            color="Mario2"
        elif charac==config._mario_eye or charac==config._mario_hand_left or charac==config._mario_leg_left :
            color="Mario2"
        elif charac==config._mario_neck or charac==config._mario_skin or charac==config._mario_leg_right :
            color="Mario2"
    if charac==config._duck_left or charac==config._duck_right :
        color="Red"
    elif charac==config._duck_mouth or  charac==config._duck_eye :
        color="White"
    elif charac==config._bird_face or charac==config._bird_beard:
        color="Red"
    elif charac==config._bird_wing_left or charac==config._bird_wing_right:
        color="Light Blue"
    elif charac==config._bird_level:
        color="Cyan"
    elif charac==config._brick:
        color="Brown"
    elif charac==config._cloud:
        color="Blue"
    elif charac=='C' or charac=='O' or charac=='I' or charac=='N' or charac=='S' :
        color="Cyan"

    return(colors[color]+charac+'\x1b[100m')