import os



_rows,_columns=os.popen('stty size', 'r').read().split()
_rows=int(_rows)-2
_columns=int(_columns)

_height1=int(3*(_rows-7)/4)+2
_height2=int((_rows-7)/2)+1

_brick = u'\U00001699'
_power = '@'

_cloud = u'\U000017DA'

_bird_face = u'\U00002362'
_bird_beard = u'\U00002375'
_bird_wing_left = '\\'
_bird_wing_right = '/'
_bird_level = '_'

_mario_head='^'
_mario_eye=u'\U000025CE'
_mario_neck=u'\U00002358'
_mario_hand_right=u'\U000025DD'
_mario_hand_left=u'\U000025DC'
_mario_skin='|'
_mario_base='_'
_mario_leg_left=u'\U000025DE'
_mario_leg_right=u'\U000025DF'
_mario_eyebrow=u'\U000025E0'

_duck_left='<'
_duck_right='>'
_duck_mouth=u'\U00002358'
_duck_eye='*'

_image_game_over =["  ___   _   __  __ ___    _____   _____ ___ "," / __| /_\ |  \/  | __|  / _ \ \ / / __| _ \\","| (_ |/ _ \| |\/| | _|  | (_) \ V /| _||   /"," \___/_/ \_\_|  |_|___|  \___/ \_/ |___|_|_\\"]
