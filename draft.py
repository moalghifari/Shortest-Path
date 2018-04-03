import heapq

adjacencymatrix = [[-999,6,7,3,-999,-999],
                    [6,-999,-999,-999,-999,90],
                    [7,-999,-999,-999,10,-999],
                    [3,-999,-999,-999,-999, -999],
                    [-999,90,10,-999,-999,20],
                    [-999,-999,-999,-999,20,-999]
                    ]
heuristikmatrix = [[10,10,10,10,10,1],
                    [10,10,10,10,10,2],
                    [10,10,10,10,10,10],
                    [10,10,10,10,10,10],
                    [10,10,10,10,10,30],
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
    print(idx)
    costf = listOfState[0][2]
    if (idx == 5):
        break
    a = heapq.heappop(listOfState)
    for i in range (0,6):
        if (adjacencymatrix[idx][i]==-999):
            continue
        heapq.heappush(listOfState, (adjacencymatrix[idx][i]+costf+heuristikmatrix[idx][5], i, adjacencymatrix[idx][i]+costf))
print(costf)