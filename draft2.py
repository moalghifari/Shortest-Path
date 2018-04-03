import heapq
import queue as Q
import math
import copy
from copy import deepcopy

class Node:
    def __init__(self,name,x,y):
        self.name = name
        self.x = x
        self.y = y
    def setName(self,name):
    	self.name = name
    def setPos(self,x,y):
    	self.x = x
    	self.y = y
    def setIdx(self,idx):
        self.idx = idx
    def getName(self):
    	return self.name
    def getPos(self):
    	return (self.x,self.y)
    def getIdx(self):
        return self.idx
    def getDistance(self,Node):
    	selisihx = self.x - Node.x
    	selisihy = self.y - Node.y
    	return math.sqrt((selisihx)**2 + (selisihy)**2)
    def print(self):
    	print ("Name : ", self.name)
    	print ("x : ", self.x)
    	print ("y : ", self.y)

class Map:
    def __init__(self,n):
        self.n = n
        self.nodes = [None] * n
        # self.matrix = [[-999,6,7,3,-999,-999],
                    # [6,-999,-999,-999,-999,90],
                    # [7,-999,-999,-999,10,-999],
                    # [3,-999,-999,-999,-999, -999],
                    # [-999,90,10,-999,-999,20],
                    # [-999,-999,-999,-999,20,-999]
                    # ]
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

class State:
    def __init__(self, idx, costtotal, costf):
        self.idx = idx
        self.costtotal = costtotal
        self.costf = costf
        self.path = []
    def __lt__(self, other):
        return self.costtotal < other.costtotal
    def setIdx(self, idx):
        self.idx = idx
    def setCosttotal(self, costtotal):
        self.costtotal = costtotal
    def setCostf(self, costf):
        self.costf = costf
    def addPath(self, path):
        self.path.append(path)
    def getIdx(self):
        return self.idx
    def getCosttotal(self):
        return self.costtotal
    def getCostf(self):
        return self.costf
    def getPath(self):
        return self.path
    def isVisited(self, idx):
        return idx in self.path

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
    goalNode = M.getNodeIdx(goalname)
    startname = input('Masukkan nama startNode')
    startNode = M.getNodeIdx(startname)
    startState = State(startNode,M.getNode(startNode).getDistance(M.getNode(goalNode)),0)
    startState.addPath(startNode)
    listOfState = []
    #(costtotal, id, costf)
    heapq.heappush(listOfState, startState)
    heapq.heappush(listOfState, startState)
    while True:
        currentState = copy.deepcopy(listOfState[0])
        idx = currentState.getIdx()
        costfb = currentState.getCostf()
        if (idx == goalNode):
            break
        heapq.heappop(listOfState)
        for i in range (0,M.n):
            if (M.matrix[idx][i]==-999 or currentState.isVisited(i)):
                continue
            costf = M.matrix[idx][i] + costfb
            costtotal = costf + M.getNode(i).getDistance(M.getNode(goalNode))
            nextState = State(i,costtotal,costf)
            heapq.heappush(listOfState, nextState)
    print(currentState.getCostf())

if __name__ == '__main__':
    main()