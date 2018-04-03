import heapq

adjacencymatrix = [[-999,6,7,3,-999,-999],
                    [6,-999,-999,-999,-999,90],
                    [7,-999,-999,-999,10,-999],
                    [3,-999,-999,-999,-999],
                    [-999,90,10,-999,-999,-999],
                    [-999,-999,-999,-999,-999,20]
                    ]
heuristikmatrix = [[10,10,10,10,10,10],
                    [10,10,10,10,10,10],
                    [10,10,10,10,10,10],
                    [10,10,10,10,10,10],
                    [10,10,10,10,10,10],
                    [10,10,10,10,10,10],
                    ]
listOfState = []
#(costtotal, id, costf)
heapq.heappush(listOfState, (16, 1, 6))
heapq.heappush(listOfState, (17, 2, 7))
heapq.heappush(listOfState, (13, 3, 3))
found = True
while found:
    idx = listOfState[0][1]
    costf = listOfState[0][2]
    if (idx == 5):
        break
    heapq.heappop(listOfState)
    for i in range (0,6):
        if (adjacencymatrix[idx][i]==-999):
            continue
        heapq.heappush(listOfState, (adjacencymatrix[idx][i]+costf+10, i, adjacencymatrix[idx][i]+costf))
print(costf)