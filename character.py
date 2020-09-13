import config
import numpy as np
import os
from random import randint
from time import time

class Character():
	def __init__(self, x, y, velocity):
		self._x = x
		self._y = y
		self._velocity=velocity


class Mario(Character):
	def __init__(self, x, y):
		super().__init__(x, y,0)
		self._d_instant=0
		self._a_instant=0
		self._level=1
		self._lives=3
		self._checkpoint=4
		self._score=0

	def killed(self):
		os.system('aplay -q ./sounds/player_down.wav &')
		self._level-=1
		if(self._level==0) :
			if(self._lives!=0):
				self._lives-=1
				self._level=1
			else :
				pass

	def move_forward(self,map_temp,pitch,flag):
		if (time()-self._d_instant<0.09):
			return pitch

		if not (self._x+2<(int(config._columns*15/2)+int(config._columns/2))-2):
			self._d_instant=time()
			return pitch
		for j in range(self._y,self._y-6,-1):
			if(map_temp[j][self._x+3-pitch]!=' '):
				self._d_instant=time()
				if self._x+3==flag._x:
					flag._mario=True
				return pitch
		self._x+=1
		if not self.check_base(map_temp,pitch):
			for j in range(self._y,self._y-6,-1):
				if(map_temp[j][self._x+3-pitch]!=' '):
					self._d_instant=time()
					if self._x+3==flag._x:
						flag._mario=True
					return pitch
			self._x+=1
		if (self._x>=int(16*config._columns/3)):
			self.checkpoint=int(16*config._columns/3)
		elif (self._x>=int(8*config._columns/3)):
			self.checkpoint=int(8*config._columns/3)
		if (self._x>=pitch+int(config._columns/2)) and self._x<=int(config._columns*15/2):
			self._d_instant=time()
			return int(self._x-config._columns/2)
		else:
			self._d_instant=time()
			return pitch
	def move_backward(self,map_temp,pitch):
		if (time()-self._a_instant<0.09):
			return

		if(self._x-2<=pitch):
			self._a_instant=time()
			return
		for j in range(self._y,self._y-6,-1):
			if(map_temp[j][self._x-3-pitch]!=' '):
				self._a_instant=time()
				return
		self._x-=1
		self._a_instant=time()

	def print(self,map_temp,pitch):

		map_temp[self._y-5][self._x-pitch]=config._mario_head
		map_temp[self._y-4][self._x-pitch-1]=config._mario_eye
		map_temp[self._y-4][self._x-pitch+1]=config._mario_eye
		map_temp[self._y-3][self._x-pitch]=config._mario_neck
		map_temp[self._y-2][self._x-pitch-2]=config._mario_hand_left
		map_temp[self._y-2][self._x-pitch+2]=config._mario_hand_right
		map_temp[self._y-2][self._x-pitch-1]=config._mario_skin
		map_temp[self._y-2][self._x-pitch+1]=config._mario_skin
		map_temp[self._y-1][self._x-pitch]=config._mario_base
		map_temp[self._y-1][self._x-pitch-1]=config._mario_skin
		map_temp[self._y-1][self._x-pitch+1]=config._mario_skin
		map_temp[self._y][self._x-pitch-2]=config._mario_leg_left
		map_temp[self._y][self._x-pitch+2]=config._mario_leg_right

	def jump(self,map_temp,pitch):
		if int(self._velocity)>0:

			truth,height=self.check_roof(map_temp,pitch)
			if  truth:
				self._velocity=-1
				return height

			for i in range(self._y,self._y-int(self._velocity),-1):
				self._y-=1
				truth,height=self.check_roof(map_temp,pitch)
				if  truth:
					self._velocity=-1
					return height
					break
			if self._velocity>0 :
				self._velocity-=1
		elif (self._velocity)<0 :
			if  self.check_base(map_temp,pitch):
				self._velocity=0

			for i in range(self._y,self._y-int(self._velocity)):
				self._y+=1
				if  self.check_base(map_temp,pitch):
					self._velocity=0
					break
			if self._velocity!=0 :
				self._velocity-=1
		else:
			self._velocity=0
			if not self.check_base(map_temp,pitch):
				self._velocity=-1
		return 0
	def check_base(self,map_temp,pitch):
		truth=False
		if not (map_temp[self._y+1][self._x-pitch-2]!=config._brick and map_temp[self._y+1][self._x-pitch-1]!=config._brick and map_temp[self._y+1][self._x-pitch]!=config._brick and map_temp[self._y+1][self._x-pitch+1]!=config._brick and map_temp[self._y+1][self._x-pitch+2]!=config._brick ) :
			truth=True
		for ch in ['C','O','I','N','S','<','>',u'\U00002358','*',config._duck_left,config._duck_right,config._duck_mouth,config._duck_eye] :
			if not (map_temp[self._y+1][self._x-pitch-2]!=ch and map_temp[self._y+1][self._x-pitch-1]!=ch and map_temp[self._y+1][self._x-pitch]!=ch and map_temp[self._y+1][self._x-pitch+1]!=ch and map_temp[self._y+1][self._x-pitch+2]!=ch ) :
				truth=True
		return truth
	def check_roof(self,map_temp,pitch):
		if (map_temp[self._y-3][self._x-pitch-2]!=config._brick and map_temp[self._y-5][self._x-pitch-1]!=config._brick and map_temp[self._y-6][self._x-pitch]!=config._brick and map_temp[self._y-5][self._x-pitch+1]!=config._brick and map_temp[self._y-3][self._x-pitch+2]!=config._brick ) :
			if (map_temp[self._y-3][self._x-pitch-2]==config._power or map_temp[self._y-5][self._x-pitch-1]==config._power or map_temp[self._y-6][self._x-pitch]==config._power or map_temp[self._y-5][self._x-pitch+1]==config._power or map_temp[self._y-3][self._x-pitch+2]==config._power ) :
				self._level=2
				return True,0
			return False,0
		if (map_temp[self._y-3][self._x-pitch-2]==config._power or map_temp[self._y-5][self._x-pitch-1]==config._power or map_temp[self._y-6][self._x-pitch]==config._power or map_temp[self._y-5][self._x-pitch+1]==config._power or map_temp[self._y-3][self._x-pitch+2]==config._power ) :
			self._level=2
		if self._y-7==config._height1 or self._y-6==config._height1 or self._y-4==config._height1:
			return True,config._height1
		elif self._y-7==config._height2 or self._y-6==config._height2 or self._y-4==config._height2:
			return True,config._height2
		return True,0

class Bird(Character):
	def __init__(self,x):
		super().__init__(x,6+randint(0,6),randint(0,4)-2)

	def print(self,map_temp,pitch):
		map_temp[self._y][self._x-2-pitch]=config._bird_level
		map_temp[self._y][self._x+2-pitch]=config._bird_level
		map_temp[1+self._y][self._x-1-pitch]=config._bird_wing_left
		map_temp[1+self._y][self._x+1-pitch]=config._bird_wing_right
		map_temp[2+self._y][self._x-pitch]=config._bird_face
		map_temp[3+self._y][self._x-pitch]=config._bird_beard
		self._y=4+randint(0,6)
		self._x+=self._velocity
		if self._velocity>0:
			self._velocity=randint(0,2)
		elif self._velocity<0:
			self._velocity=randint(0,2)-2
		else :
			self._velocity=randint(0,4)-2

class Duck(Character):
	def __init__(self,x):
		if (x>=int(16*config._columns/3)):
			velocity=3
		elif (x>=int(8*config._columns/3)):
			velocity=2
		else :
			velocity=1
		super().__init__(x,config._rows-7,velocity)
		self._living=True

	def print(self,map_temp,pitch):
		map_temp[self._y][self._x-1-pitch]=config._duck_left
		map_temp[self._y][self._x-pitch]=config._duck_mouth
		map_temp[self._y][self._x+1-pitch]=config._duck_right
		if self._living :
			map_temp[self._y-1][self._x-1-pitch]=config._duck_eye
			map_temp[self._y-1][self._x+1-pitch]=config._duck_eye
		#self._y=4+randint(0,6)

	def motion(self,map_temp,pitch,mario):
		for i in range(self._velocity):
			if(self._x-2<mario._x and map_temp[self._y][self._x+2-pitch]==' ' and map_temp[self._y-1][self._x+2-pitch]==' '):
				self._x+=1
			elif (self._x+2>mario._x and map_temp[self._y][self._x-3-pitch]==' ' and map_temp[self._y-1][self._x-3-pitch]==' '):
				self._x-=1
			elif (map_temp[self._y][self._x+2-pitch]==config._mario_leg_left) :
				self._x+=1
				mario.killed()
				return True
			elif (map_temp[self._y][self._x-2-pitch]==config._mario_leg_right) :
				self._x-=1
				mario.killed()
				return True
			elif (map_temp[self._y-1][self._x+2-pitch]==config._mario_leg_left) :
				self._x+=1
				mario.killed()
				return True
			elif (map_temp[self._y-1][self._x-2-pitch]==config._mario_leg_right) :
				self._x-=1
				mario.killed()
				return True
			if (self._y-2==mario._y):
				if (mario._x-2<self._x+2) and (mario._x+2>self._x-2):
					os.system('aplay -q ./sounds/stomp.wav &')
					mario._score+=1000
					self._living=False 
					self._velocity=0
		return False
		