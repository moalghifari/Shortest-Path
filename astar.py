from pylab import *
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import heapq
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
    def printNode(self):
    	print ("Name : ", self.name)
    	print ("x : ", self.x)
    	print ("y : ", self.y)

class Map:
    def __init__(self,n):
        self.n = n
        self.nodes = []
        self.matrix = []
    def setNode(self,Node,idx):
        self.nodes[idx] = Node
    def setMatrix(self,row,col,bobot):
        self.matrix[row][col] = bobot
    def getNode(self,idx):
        return self.nodes[idx]
    def getMatrix(self,row,col):
        return self.matrix[row][col]
    def printMatrix(self):
        print(self.matrix)
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
    def __init__(self, costtotal, idx, costf):
        self.costtotal = costtotal
        self.idx = idx
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
        print("Rute Yang Dilalui \t: ", end='')
        for i in range(0, len(self.path)-1):
            print(listOfNode[self.path[i]].getName(), ' -> ', end=''),
        print(listOfNode[self.path[len(self.path)-1]].getName())

def main():
    file_name = input('Masukkan nama file \t\t\t: ')
    files = open(file_name, 'r')

    file_line_list = files.readlines()
    n = int(file_line_list[0])
    M = Map(n)
    for i in range(n):
        idx = i+1
        line_list = file_line_list[idx].split()
        M.nodes.append(Node(line_list[0], float(line_list[1]), float(line_list[2])))
    for i in range(0,n):
        idx = i+n+1
        line_list = file_line_list[idx].split()
        listtemp = []
        for j in range(n):
            listtemp.append(float(line_list[j]))
        M.matrix.append(listtemp)
    startname = input('Masukkan nama tempat awal \t\t: ')
    startNode = M.getNodeIdx(startname)
    goalname = input('Masukkan nama tempat tujuan akhir \t: ')
    goalNode = M.getNodeIdx(goalname)
    startState = State(M.getNode(startNode).getDistance(M.getNode(goalNode)),startNode,0)
    startState.addPath(startNode)
    listOfState = []
    #(costtotal, id, costf)
    heapq.heappush(listOfState, startState)
    iterates = True
    while iterates:
        currentState = heapq.heappop(listOfState)
        idx = currentState.getIdx()
        costfb = currentState.getCostf()
        if (idx == goalNode):
            iterates = False
        else:
            for i in range (0,M.n):
                if not (M.matrix[idx][i]==-1 or currentState.isVisited(i)):
                    costf = M.getMatrix(int(idx),i) + costfb
                    costtotal = costf + M.getNode(i).getDistance(M.getNode(goalNode))
                    nextState = State(costtotal,i,costf)
                    nextState.path = copy.deepcopy(currentState.path)
                    nextState.addPath(i)
                    heapq.heappush(listOfState, nextState)
    print("Jarak Total \t\t:",currentState.getCostf())
    currentState.printPath(M.nodes)

    # Plot Jawaban
    All = []
    Sequence = []
    xPoints = []
    yPoints = []
    xSequence = []
    ySequence = []
    xA = [0.1,0.1]
    yA = [0.1,0.1]
    for i in range (len(M.nodes)):
        xPoints.append(M.nodes[i].x)
        yPoints.append(M.nodes[i].y)
    for i in range (len(currentState.path)):
        xSequence.append(M.nodes[currentState.path[i]].x)
        ySequence.append(M.nodes[currentState.path[i]].y)
        Sequence.append((M.nodes[currentState.path[i]].x,M.nodes[currentState.path[i]].y))
    for i in range (n):
        for j in range (n):
            if (M.matrix[i][j]!=-1):
                All.append((M.nodes[i].x,M.nodes[i].y))
                All.append((M.nodes[j].x,M.nodes[j].y))
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range (len(M.nodes)):    
        scatter(xPoints[i],yPoints[i], s=100 ,marker='o', c='grey')
        ax.text(xPoints[i]-100,yPoints[i], M.nodes[i].getName())
    scatter(xSequence,ySequence, s=100 ,marker='o', color="red")
    left,right = ax.get_xlim()
    low,high = ax.get_ylim()
    arrow( left, 0, right -left, 0, length_includes_head = True, head_width = 0.15 )
    arrow( 0, low, 0, high-low, length_includes_head = True, head_width = 0.15 )
    for i in range (0, len(All)-1, 2):
        xA[0]=All[i][0]
        xA[1]=All[i+1][0]
        yA[0]=All[i][1]
        yA[1]=All[i+1][1]
        ax.add_line(Line2D(xA, yA, linewidth=1, color='blue'))
    for i in range (0, len(Sequence)-1):
        xA[0]=Sequence[i][0]
        xA[1]=Sequence[i+1][0]
        yA[0]=Sequence[i][1]
        yA[1]=Sequence[i+1][1]
        ax.add_line(Line2D(xA, yA, linewidth=2, color='green'))
    grid()
    show()

if __name__ == '__main__':
    main()