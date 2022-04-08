def backTracking(start, length, sum):
    if length == len(Nmatrix[0]):
        if sum not in set and sum > 0:
            # print(sum)
            set.update({sum: 0})
        return
    for i in range(len(Nmatrix)):
        backTracking(start + 1, length + 1, sum + Nmatrix[i][start])


set = {}
Ncount = int(input())
N2 = input()
Nlist = [int(j) for j in N2.split()]
Nmatrix = [Nlist.copy() for _ in range(3)]
for i in range(len(Nlist)):
    Nmatrix[1][i] = Nmatrix[1][i] * -1
    Nmatrix[2][i] = 0
sum = 0
backTracking(0, 0, sum)
print(len(set.keys()))
