class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.adjacency = []
    def addAdjacency(self, tup):
        self.adjacency.append(tup)
    def printInfo(self):
        print ("Name \t\t: ", self.name)
        print ("x \t\t: ", self.x)
        print ("y \t\t: ", self.y)
        print ("Adjacency \t: ")
        for adj in self.adjacency:
            print ("-", adj[0].name , ", " , adj[1])


    

node1 = Node("NasiUduk", 5, 10)
node2 = Node("WarungBuTatang", 10, 10)
node2.addAdjacency((node1, 50))
node3 = Node("AyamGoang", 20, 10)
node3.addAdjacency((node1,100))
node3.addAdjacency((node2,300))
node1.printInfo()
node2.printInfo()
node3.printInfo()