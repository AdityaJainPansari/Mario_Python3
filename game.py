from random import *
import os
from NonBlockingInput import *
from time import sleep,time
import numpy as np
import config
from character import *
from objects import *
import color
kb = KBHit()

def game_start():
	global map1
	map1=np.array([[' ' for i in range(config._columns*8)] for j in range(config._rows) ])
	for j in range(0,config._columns*8) :
		for i in range(1,config._rows) :
			if i==2 or i==config._rows-5 or ((i==config._rows-4 or i==config._rows-2) and j%4==0) or (i==config._rows-3 and (j+2)%4==0) or i==config._rows-1:
				map1[i][j]=config._brick
	map1[int((config._height1+config._height2)/2)][5]=config._power
	map1[int((config._height1+config._height2)/2)][6]=config._power
	map1[int((config._height1+config._height2)/2)][7]=config._power
	map1[int((config._height1+config._height2)/2)+1][5]=config._power
	map1[int((config._height1+config._height2)/2)+1][6]=config._power
	map1[int((config._height1+config._height2)/2)+1][7]=config._power
	cloud_cood=np.random.choice(range(int(config._columns/3)), int(config._columns/11), replace=False)
	cloud_cood=cloud_cood*24
	for x in cloud_cood :
		pitch=randint(0,6)
		map1[5+pitch][x-5]=config._cloud
		map1[5+pitch][x]=config._cloud
		map1[5+pitch][x+5]=config._cloud
		map1[8+pitch][x-5]=config._cloud
		map1[8+pitch][x]=config._cloud
		map1[8+pitch][x+5]=config._cloud

		map1[6+pitch][x+randint(3,5)]=config._cloud
		map1[6+pitch][x+7]=config._cloud
		map1[6+pitch][x-7]=config._cloud
		map1[6+pitch][x-randint(3,5)]=config._cloud
		map1[7+pitch][x+randint(3,5)]=config._cloud
		map1[7+pitch][x+7]=config._cloud
		map1[7+pitch][x-7]=config._cloud
		map1[7+pitch][x-randint(3,5)]=config._cloud

	piller_cood=np.random.choice(range(1,int(config._columns/10)), int(config._columns/25), replace=False)
	piller_cood=piller_cood*72
	for x in piller_cood :
		if (x>int(16*config._columns/3)-7 and x < int(16*config._columns/3)+1) or (x>int(8*config._columns/3)-7 and x < int(8*config._columns/3)+1):
			x=x+(12*(randint(0,2)-1))
		pitch=randint(min(config._height1+10,config._rows-11),config._rows-9)
		for i in range(pitch,config._rows-5) :
			for j in range(6) :
				map1[i][x+j]=config._brick
	global birds
	birds=[]
	bird_cood=np.random.choice(range(config._columns), int(config._columns/4), replace=False)
	bird_cood=bird_cood*24
	for b in bird_cood:
		birds.append(Bird(int(b)))

	global ducks
	ducks=[]
	duck_cood=np.random.choice(piller_cood, int(config._columns/40), replace=False)
	duck_cood-=5
	for d in duck_cood:
		ducks.append(Duck(int(d)))

	global roof_low
	roof_low=[]
	global treasure_low
	treasure_low=[]
	global roof_high
	roof_high=[]
	global treasure_high
	treasure_high=[]
	roof_low_cood=np.random.choice(range(4,int(16*config._columns/11)), int(config._columns), replace=False)
	roof_low_cood=roof_low_cood*5
	for cood in roof_low_cood:
		choose=randint(0,2)
		if choose==2 :
			treasure_low.append(Treasure(int(cood),config._height1))
		else :
			roof_low.append(Roof(int(cood),config._height1))
	roof_high_cood=np.random.choice(range(4,int(16*config._columns/11)), int(config._columns/3), replace=False)
	roof_high_cood=roof_high_cood*5
	for cood in roof_high_cood:
		choose=randint(0,2)
		if choose==2 :
			treasure_high.append(Treasure(int(cood),config._height2))
		else :
			roof_high.append(Roof(int(cood),config._height2))
	global flag
	flag=Flag(int(31*config._columns/4),config._height2)
	flag.print(map1)

def game_over(flag,mario):
	os.system('clear')
	for i in range(int(config._rows/2)-5) :
		print()
	for i in config._image_game_over :
		for j in range(int(config._columns/2)-20) :
			print(' ',end='')
		print(i)
	print()
	print()
	for i in range(int(config._columns/2)-20) :
		print(' ',end='')
	print ('Game Score :', mario._score)
	print()
	print()
	if flag._mario :
		for i in range(int(config._columns/2)-20) :
			print(' ',end='')
		print ('Flag Bonus : ',int(flag._score))
		print()
		print()
		for i in range(int(config._columns/2)-20) :
			print(' ',end='')
		print ('Time Bonus (100*',int(countdown),') : ',100*int(countdown))
		print()
		print()
	for i in range(int(config._columns/2)-20) :
		print(' ',end='')
	total_score=0
	if flag._mario :
		print('Congratulations ! ',end='')
		total_score=mario._score+100*int(countdown)+flag._score
	else :
		total_score=mario._score
	print ('Your Total Score Is :',total_score)
	for i in range(int(config._rows/2)-10) :
		print()
	os.system('sleep 3')
	os.system('pkill -kill aplay')
	quit()

mario = Mario(int(7*config._columns), config._rows-7)
x=mario._x-4
count=1
instant=time()
os.system('aplay -q ./sounds/theme.wav &')
lives=3
score=0
countdown=10000
start_time=0

def remove_roof(mario,y):
	x=int(mario._x/5)*5
	if y==config._height1:
		for t in treasure_low:
			if (t._x==x) :
				os.system('aplay -q ./sounds/coin.wav & 1>&2')
				t._taken=True
				mario._score+=100
				roof_low.append(t)
				treasure_low.remove(t)
				return
		if mario._level>1 :
			for r in roof_low:
				if (r._x==x) :
					mario._score+=10
					roof_low.remove(r)
					return
	elif y==config._height2:
		for t in treasure_high:
			if (t._x==x) :
				os.system('aplay -q ./sounds/coin.wav & 1>&2')
				t._taken=True
				mario._score+=100
				roof_high.append(t)
				treasure_high.remove(t)
				return
		if mario._level>1 :
			for r in roof_high:
				if (r._x==x) :
					mario._score+=10
					roof_high.remove(r)
					return


game_start()

while (1) :

	restart=False
	if countdown<100 :
		os.system('aplay -q ./sounds/hurry_up.wav &')

	if time() - instant > 88:
		os.system('aplay -q ./sounds/theme.wav &')
		instant = time()

	if kb.kbhit():
		key = kb.getch()
	else:
		key = " "
	if key == 'q':
		os.system('pkill -kill aplay')
		quit()

	if key == 'd':
		x=mario.move_forward(map_temp,x,flag)
		if flag._mario :
			flag.print(map1)
			os.system('aplay -q ./sounds/level_clear.wav &')
			flag._score=(config._rows-mario._y)*1000
			restart=True

	if key == 'a':
		mario.move_backward(map_temp,x)

	if key == 'w':
		if mario.check_base(map_temp,x) :
			mario._velocity=max(int(config._rows/12),5)
			count=0

	os.system('sleep 0.04')
	map_temp=np.array(map1[1:config._rows,x:x+config._columns-1])
	for b in birds:
		if (b._x>=x+4 and b._x<=x+config._columns-4) :
			if(mario._x+2>=b._x-2 and mario._x-2<=b._x+2 and mario._y>=b._y and mario._y-5<=b._y+3):
				mario.killed()
				restart=True
			b.print(map_temp,x)
	for t in treasure_low:
		if (t._x>=x+5 and t._x<=x+config._columns-6) :
			t.print(map_temp,x)
	for r in roof_low:
		if (r._x>=x+5 and r._x<=x+config._columns-6) :
			r.print(map_temp,x)
	for t in treasure_high:
		if (t._x>=x+5 and t._x<=x+config._columns-6) :
			t.print(map_temp,x)
	for r in roof_high:
		if (r._x>=x+5 and r._x<=x+config._columns-6) :
			r.print(map_temp,x)

	for d in ducks:
		if (d._x>=x+4 and d._x<=x+config._columns-4) :
			d.print(map_temp,x)
	
	if count%3==0:
		height=mario.jump(map_temp,x)
		if(height!=0) :
			remove_roof(mario,height)
	count+=1
	mario.print(map_temp,x)
	for d in ducks:
		if (d._x>=x+4 and d._x<=x+config._columns-4) :
			truth=d.motion(map_temp,x,mario)
			if (truth):
				x=mario._checkpoint-4
				restart=True
				break
			d.print(map_temp,x)
	if start_time==0:
		start_time=time()
	countdown=10000-time()+start_time
	os.system('clear')
	for i in range(0,config._rows-1):
		for j in range(0,config._columns-1):
			print(color.getcolor(map_temp[i][j],mario),end='')
		print()
	print('Lives:',mario._lives,'\t','\t','\t','Score:',mario._score,'\t','\t','\t','Time:',int(countdown))
	print()
	if restart:
		if(mario._lives==0) or flag._mario:
			game_over(flag,mario)
			break
		mario._x=mario._checkpoint
		x=mario._x-4
	
print('end')