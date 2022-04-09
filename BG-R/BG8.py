num = int(input())
count = 0
for i in range(1,num+1):
    Ncount = 0
    for j in range(1,i+1):
        if i % j == 0:
            Ncount += j ** 2
    count += Ncount
print(count%(10**9+7))
            
        
