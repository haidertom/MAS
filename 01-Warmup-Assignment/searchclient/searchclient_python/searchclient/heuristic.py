from abc import ABCMeta, abstractmethod
from collections import defaultdict
import sys



class Heuristic(metaclass=ABCMeta):
	def __init__(self, initial_state: 'State'):
		# Here's a chance to pre-process the static parts of the level.
		pass


	def h(self, state: 'State') -> 'int':
		'''
		This function implements our heuristics:
		--> We calculate the distance from all boxes A to all goals a, B to b, ... + the distance from the agent to all boxes
		'''

		# get coordinates of all Boxes as dictionary of coordinate tuples
		boxesxy = defaultdict(list)
		for i, v in enumerate(state.boxes):
			for ii, vv in enumerate(v):
				if vv == None:
					pass
				elif vv in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
					boxesxy[vv].append((i, ii))

		#get coordinates of all goals as dictionary of coordinate tuples
		goalsxy = state.goalsxy

		# get agent coordinates as list of tuples
		agentxy = (state.agent_row, state.agent_col)

		btg = 0 # will be the cummulated sum of the distance of all Boxes To all Goals
		atb = 0 # will be the cummulated sum of the Agent To all Boxes

		for key, value in boxesxy.items():
			if key in goalsxy: # check if goal for that box exists
				for v in value:
					btg +=  sum(tuple(abs(x-y) for x, y in zip(v, goalsxy[key]))) # Manhatten distance boxes to all goals
					atb += sum(tuple(abs(x-y) for x, y in zip(v, agentxy))) # Manhatten distance agent to all boxes

		return int(btg+atb)


	@abstractmethod
	def f(self, state: 'State') -> 'int': pass

	@abstractmethod
	def __repr__(self): raise NotImplementedError


class AStar(Heuristic):
	def __init__(self, initial_state: 'State'):
		super().__init__(initial_state)

	def f(self, state: 'State') -> 'int':
		return state.g + self.h(state)

	def __repr__(self):
		return 'A* evaluation'


class WAStar(Heuristic):
	def __init__(self, initial_state: 'State', w: 'int'):
		super().__init__(initial_state)
		self.w = w

	def f(self, state: 'State') -> 'int':
		return state.g + self.w * self.h(state)

	def __repr__(self):
		return 'WA* ({}) evaluation'.format(self.w)


class Greedy(Heuristic):
	def __init__(self, initial_state: 'State'):
		super().__init__(initial_state)

	def f(self, state: 'State') -> 'int':
		return self.h(state)

	def __repr__(self):
		return 'Greedy evaluation'
