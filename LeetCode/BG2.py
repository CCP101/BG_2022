Ncount = int(input())
Ncount //= 1000 
Ncount = Ncount % (3600*24)
h = Ncount // 3600
Ncount = Ncount % 3600
m = Ncount // 60 
s = Ncount % 60 
if h<10:
    h = str(0)+str(h)
if m<10:
    m = str(0)+str(m)
if s<10:
    s = str(0)+str(s)

print("{0}:{1}:{2}".format(h,m,s))