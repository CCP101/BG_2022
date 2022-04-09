inp1 = input()
Linp1 = list(inp1.split(" "))
NT,MT = int(Linp1[0]),int(Linp1[1])
result = []
for _ in range(NT):
    temp = []
    inp = input()
    Linp = list(inp.split(" "))
    N,M = int(Linp[0]),int(Linp[1])
    temp.append(N)
    temp.append(M)
    result.append(temp.copy())

count = 0
for _ in range(MT):
    Cmax = 0
    iIndex = -1
    for i in range(NT):
        if result[i][0] > Cmax:
            Cmax = result[i][0]
            iIndex = i
    count += Cmax
    Ctemp = result[iIndex][0] - result[iIndex][1]
    if Ctemp < 0:
        result[iIndex][0] = 0
    else:
        result[iIndex][0] = Ctemp
print(count)
