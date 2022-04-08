def cal(i,j):
    if j == 0:
        return 1
    if i == j:
        return 1
    return cal(i-1,j-1)+cal(i-1,j)

matrix = [0] * 100000

Ncount = int(input())
Ni, Nj = 0,0
FloorB = 1
FloorE = 1
FloorLength = 1
count = 1
while True:
    if FloorB <= Ncount <= FloorE:
        Ni = count -1 
        Nj = Ncount - FloorB 
        break
    else:
        FloorB += FloorLength
        FloorE += FloorLength + 1
        FloorLength += 1
        count += 1
print(cal(Ni,Nj))




