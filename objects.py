import config

class Object():
	def __init__(self, x, y):
		self._x = x
		self._y = y

	def get_x():
		return self._x

	def get_y():
		return self._y

class Roof(Object):
	def __init__(self, x, y):
		super().__init__(x, y)

	def print(self,map_temp,pitch):
		for i in range(0,2):
			for j in range(0,5):
				map_temp[self._y+i][self._x+j-pitch]=config._brick
		
class Treasure(Object):
	def __init__(self, x, y):
		super().__init__(x, y)
		self._taken=False

	def print(self,map_temp,pitch):
		if not self._taken :
			map_temp[self._y][self._x-pitch]='C'
			map_temp[self._y][self._x-pitch+1]='O'
			map_temp[self._y][self._x-pitch+2]='I'
			map_temp[self._y][self._x-pitch+3]='N'
			map_temp[self._y][self._x-pitch+4]='S'
			for i in range(1,2):
				for j in range(0,5):
					map_temp[self._y+i][self._x+j-pitch]=config._brick
		else :
			for i in range(0,2):
				for j in range(0,5):
					map_temp[self._y+i][self._x+j-pitch]=config._brick

class Flag(Object):
	def __init__(self,x,y):
		super().__init__(x, y)
		self._mario=False
		self._score=0

	def print(self,map1) :
		for i in range(self._y,config._rows-4):
			map1[i][self._x]=config._brick
		for i in range(self._x+1,self._x+9):
			map1[self._y][i]='*'
		for i in range(self._x+1,self._x+9):
			map1[self._y+10][i]='*'
		for i in range(self._y+1,self._y+10):
			map1[i][self._x+9]='*'
		if self._mario:
			map1[self._y+5][self._x+3]='M'
			map1[self._y+5][self._x+4]='A'
			map1[self._y+5][self._x+5]='R'
			map1[self._y+5][self._x+6]='I'
			map1[self._y+5][self._x+7]='O'
		else :
			map1[self._y+5][self._x+3]='E'
			map1[self._y+5][self._x+4]='N'
			map1[self._y+5][self._x+5]='E'
			map1[self._y+5][self._x+6]='M'
			map1[self._y+5][self._x+7]='Y'