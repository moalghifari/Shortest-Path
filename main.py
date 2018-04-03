import math

class Node:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
    def printInfo(self):
        print ("Name \t\t: ", self.name)
        print ("x \t\t: ", self.x)
        print ("y \t\t: ", self.y)
    def getName(self):
        return self.name
    def getDistance(self,Node):
        selisihx = self.x - Node.x
        selisihy = self.y - Node.y
        return math.sqrt((selisihx)**2 + (selisihy)**2)


class ReadFile:
    def __init__(self):
        self.file_name = input('Masukkan nama file: ')
        self.file = open(self.file_name, 'r')
    def createListOfNode(self, listOfNode):
        file_line_list = self.file.readlines()
        i = 0
        while (file_line_list[i] != '*\n'):
            line_list = file_line_list[i].split()
            listOfNode.append(Node(line_list[0], int(line_list[1]), int(line_list[2])))
            i = i + 1
        for j in range(0, i):
            line_list = file_line_list[i+j+1].split()
            k = 1
            while (k < len(line_list)):
                # cari indeks si string
                temp = (listOfNode.getElmt(listOfNode.getIdx(line_list[k])), int(line_list[k+1]))
                listOfNode.getElmt(j).addAdjacency(temp)
                k = k + 2

class ListOfNode:
    def __init__(self):
        self.list = []
    def append(self,Node):
        self.list.append(Node)
    def getElmt(self,idx):
        return self.list[idx]
    def getIdx(self,name):
        l = 0
        while (l < len(self.list)):
            if (name == self.list[l].getName()):
                return l
            else:
                l = l+1
        return (-1)
    def getSize(self):
        return len(self.list)


def main():
    # membaca file eksternal
    nodelist = ListOfNode()
    r = ReadFile()
    r.createListOfNode(nodelist)

    nodelist.getElmt(0).printInfo()
    nodelist.getElmt(1).printInfo()
    # nodelist.getElmt(2).printInfo()
    # nodelist.getElmt(3).printInfo()
    # nodelist.getElmt(4).printInfo()
    # nodelist.getElmt(5).printInfo()
    # nodelist.getElmt(6).printInfo()
    # nodelist.getElmt(7).printInfo()

    start = input('Masukkan tempat awal: ')
    finish = input('Masukkan tempat tujuan: ')
    while ((nodelist.getIdx(start) == -1) or (nodelist.getIdx(finish) == -1)):
        start = input('Masukkan tempat awal: ')
        finish = input('Masukkan tempat tujuan: ')

if __name__ == '__main__':
    main()