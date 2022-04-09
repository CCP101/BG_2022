import math



num = int(input())
if num == 1:
    print(0)
else:
    Zlist = [2]
    ZElist = []
    for i in range(3,num):
        FLAG = False
        for j in range(2,int(math.sqrt(i)+1)):
            if i % j == 0:
                FLAG = True
                continue
        if FLAG == False:
            Zlist.append(i)
    for i in Zlist:
        if num % i == 0:
            ZElist.append(i)
    print(len(ZElist))
        
