import math


inp1 = input()
Linp1 = list(inp1.split(" "))
NT,length = int(Linp1[0]),int(Linp1[1])
points = []
for i in range(NT):
    point = []
    inp = input()
    Linp = list(inp.split(" "))
    x,y,v = int(Linp[0]),int(Linp[1]),int(Linp[2])
    point.append(x)
    point.append(y)
    point.append(v)
    point.append(math.sqrt(abs(x)**2 + abs(y)**2 ))
    point.append(-1)
    if x!=0 and y!=0:
        point.append(x/y)
    else:
        point.append(0)
    points.append(point.copy())


points = sorted(points,key = lambda x:x[3])
count = 1
for i in points:
    if i[3] <= length and i[4]== -1:
        i[4] = count
        length += i[2]
        if i[0]!=0 and i[1]!=0:
            for j in points:
                if i!=j and i[5] == j[5]:
                    if j[3] <= length:
                        j[4] = count
                        length += j[2]
                        count += 1
        
        else:
            if i[0]==0 or i[1]==0:
                for j in points:
                    if i!=j:
                        if i[0]== 0 and j[0]==0 and length >= j[1]:
                            j[4] = count
                            length += j[2]
                            count += 1
                        if i[1]== 0 and j[1]==0 and length >= j[0]:
                            j[4] = count
                            length += j[2]
                            count += 1
        count +=1
                        
    
output = []
for i in points:
    index = i[4]
    output.append(index)
print(output)
