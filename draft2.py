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
    def printPath(self, listOfNode):
        print('The Path :')
        for i in range(0, len(self.path)-1):
            print(listOfNode[self.path[i]].getName(), ' -> ', end='')
        print(listOfNode[self.path[len(self.path)-1]].getName())
def main():
    file_name = input('Masukkan nama file: ')
    file = open(file_name, 'r')
    file_lines = file.read().split('\n')
    n = int(file_lines[0])
    print(n)
    M = Map(n)
    i = 1
    while (i <= n):
        words = file_lines[i].split()
        name = words[0]
        M.setNode(Node(name,float(words[1]),float(words[2])),i-1)
        i += 1

    while (i <= 2*n):
        words = file_lines[i].split()
        j = i - n -1
        for k in range(n):
            if (words[k] != "None"):
                print("1 ", j, " ", k)
                M.setMatrix(j,k,float(words[k]) * M.nodes[j].getDistance(M.nodes[k]))
            else:
                print(j," ",k)
                M.setMatrix(j,k,99999)
        i += 1
    startname = input('Masukkan nama startNode : ')
    startNode = M.getNodeIdx(startname)
    goalname = input('Masukkan nama goalNode : ')
    goalNode = M.getNodeIdx(goalname)
    print(goalNode)
    startState = State(startNode,M.getNode(startNode).getDistance(M.getNode(goalNode)),0)
    startState.addPath(startNode)
    listOfState = []
    #(costtotal, id, costf)
    heapq.heappush(listOfState, startState)
    print("INI LOH ", len(listOfState))
    print(M.getNode(startState.getIdx()).getName())
    while True:
        currentState = copy.deepcopy(listOfState[0])
        idx = currentState.getIdx()
        costfb = currentState.getCostf()
        print(idx, " ", goalNode)
        if (idx == goalNode):
            print('XXXXXXXX')
            break
        heapq.heappop(listOfState)
        for i in range (0,M.n):
            # if (not(M.matrix[idx][i]==99999 or currentState.isVisited(i))):
            if (not(currentState.isVisited(i))):
            
                costf = M.matrix[idx][i] + costfb
                costtotal = costf + M.getNode(i).getDistance(M.getNode(goalNode))
                nextState = State(i,costtotal,costf)
                nextState.path = copy.deepcopy(currentState.path)
                nextState.addPath(i)
                heapq.heappush(listOfState, nextState)
    print(currentState.getCostf())
    currentState.printPath(M.nodes)

if __name__ == '__main__':
    main()