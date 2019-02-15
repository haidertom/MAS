import heapq
from collections import defaultdict


# def index_2d(mylist, v):
# 	arr = []
# 	for i, x in enumerate(mylist):
# 		if v in x:
# 			arr.append((i,x.index(v)))
#
# 	return arr

#myList = [[None, "A", None, "A"], [None,"A", None, None]]

#coordsList = [[x, y] for x, li in enumerate(myList) for y, val in enumerate(li) if val== "A"]



#a = (-10,10)
#b = (4,4)

#c =  tuple( abs(x-y) for x, y in zip(a, b) )

#a = []

# row = 2
# col = 3
#
# a.append((row, col))
# a.append((row+1, col+1))
# print(a)
#print(sum(c))


# for a in boxesxy:
# 	for b in goalsxy:
# 		c +=  sum(tuple(abs(x-y) for x, y in zip(a, b))) # Manhatten distance all boxes to goals

#d += sum(tuple(abs(x-y) for x, y in zip(a, agentxy))) # Manhatten distance agent to boxes

# agentxy = (3,4)
#
# a = (10,10)
#
# z = zip(a, agentxy)
#
# i,j = agentxy
#
# c = [abs((x-y)) for x,y in zip(a, agentxy)]
#
# print(list(z))
# print(c)
# print(i)
# print(j)


# h = []
# heapq.heappush(h, (1, 'write'))
# heapq.heappush(h, (1, 'write'))
# heapq.heappush(h, (1, 'write spec'))
#
# a,b = heapq.heappop(h)
#
# print(b)
#
# print(len(h))

# goalsxy = {}
#
# a = 'a'
#
# goalsxy[a] = (2,3)
#
# print(goalsxy)


boxes = [['A', None, None, None, '+'], [None, None, None,], ['B', None, None]]
boxesxy = defaultdict(list)

for i, v in enumerate(boxes):
	for ii, vv in enumerate(v):
		if vv == None:
			pass
		elif vv in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
			boxesxy[vv].append((i, ii))

goalsxy = {}
goalsxy['A'] = (10,10)
goalsxy['B'] = (20,20)

btg = 0

for key, value in boxesxy.items():
	for v in value:
		btg +=  sum(tuple(abs(x-y) for x, y in zip(v, goalsxy[key])))



print('C' in goalsxy)
