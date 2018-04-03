#buat tipe Node
#buat tipe Map (isinya list of node dan matrix)
#buat tipe SimpulHidup
#buat class ReadFile
import queue as Q
import math
from copy import deepcopy

class Node:
	index = -1
	def __init__(self,name,x,y):
		self.name = name
		self.x = x
		self.y = y
		self.isVisited = False
	def setName(self,name):
		self.name = name
	def setPos(self,x,y):
		self.x = x
		self.y = y
	def getName(self):
		return self.name
	def getPos(self):
		return (self.x,self.y)
	def getDistance(self,Node):
		selisihx = self.x - Node.x
		selisihy = self.y - Node.y
		return math.sqrt((selisihx)**2 + (selisihy)**2)
	def print(self):
		print ("Name : ", self.name)
		print ("x : ", self.x)
		print ("y : ", self.y)
	def visited(self):
		self.isVisited = True

class Map:
	def __init__(self,n):
		self.n = n
		self.nodes = [None] * n
		self.matrix = [[None] * n] * n
	def setNode(self,Node,idx):
		self.nodes[idx] = Node
	def setMatrix(self,row,col,bobot):
		self.matrix[row][col] = bobot
	def getNode(self,idx):
		return self.nodes[idx]
	def getMatrix(self,row,col):
		return self.matrix[row][col]
	def getNodeIdx(self,name):
		found = False
		i = 0
		while ((not found) and (i < self.n)):
			if (self.nodes[i].getName() == name):
				found = True
				return i
			else:
				i = i+1

class SimpulHidup:
	def __init__(self,root,node):
		self.cost = 0
		self.node = node
		self.root = root
	def getRoot(self):
		return self.root
	def getCost(self):
		return self.cost
	def setRoot(self,root):
		self.root = root
	def setCost(self,cost):
		self.cost = cost
	def addRoot(self,node):
		self.root.extend(node)
	def countCost(self,goalNode,Map):
		distance = self.node.getDistance(goalNode)
		prevcost = 0
		for i in range(len(self.root)-1):
			prevcost = prevcost + Map.getMatrix(Map.getNodeIdx(self.root[i].getName()), Map.getNodeIdx(self.root[i+1].getName()))
		if (len(self.root) != 0):
			prevcost = prevcost + Map.getMatrix(Map.getNodeIdx(self.root[len(self.root)-1].getName()), Map.getNodeIdx(self.node.getName()))
		self.cost = distance + prevcost
		return self.cost
	def __cmp__(self, other):
		return cmp(self.cost, other.cost)
	def __lt__(self, other):
		return (self.cost < other.cost)
	def print(self):
		print('current node')
		self.node.print()
		print('current cost')
		print(self.cost)
		print('root')
		for i in range(len(self.root)):
			self.root[i].print()
			print('-----')
		


class Queue:
	def __init__(self):
		self.queue = Q.PriorityQueue()
	def addQueue(self,simpulhidup):
		self.queue.put(simpulhidup)
	def popQueue(self):
		return self.queue.get()
	def expandQueue(self,Map,goalNode):
		smallestsimpulhidup = self.queue.get()
		if (smallestsimpulhidup.node.getName() == goalNode.getName()) :
			print('RESULTTT')
			smallestsimpulhidup.print()
		else:
			idx = Map.getNodeIdx(smallestsimpulhidup.node.getName())
			root = deepcopy(smallestsimpulhidup.root)
			root.append(smallestsimpulhidup.node)
			# print(root)
			for i in range(Map.n):
				if (Map.getMatrix(idx,i) != 99999):
					simpulhidup = SimpulHidup(root,Map.getNode(i))
					simpulhidup.countCost(goalNode,Map)
					self.addQueue(simpulhidup)
					simpulhidup.print()
			self.expandQueue(Map,goalNode)


def main():
	n = int(input('Masukkan n:'))
	M = Map(n)
	for i in range(n):
		nodename = input('Masukkan node name:')
		nodex = int(input('Masukkan node x:'))
		nodey = int(input('Masukkan node y:'))
		M.setNode(Node(nodename,nodex,nodey),i)
	for i in range(n):
		for j in range(n):
			matrixelmt = int(input('Masukkan matrix ke' + str(i) + ' ' + str(j) + ':'))
			M.setMatrix(i,j,matrixelmt)
	goalname = input('Masukkan nama goalNode')
	goalNode = M.getNode(M.getNodeIdx(goalname))
	# goalNode.print()
	startname = input('Masukkan nama startNode')
	startNode = M.getNode(M.getNodeIdx(startname))
	# startNode.print()
	simpulhidup = SimpulHidup([],startNode)
	simpulhidup.countCost(goalNode,M)
	# simpulhidup.print()
	astar = Queue()
	astar.addQueue(simpulhidup)
	astar.expandQueue(M,goalNode)





if __name__ == '__main__':
    main()