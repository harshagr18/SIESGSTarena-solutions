from math import sqrt,floor,ceil

x = int(input())
for i in range(x):
    a = int(input())
    if(sqrt(a)-int(sqrt(a)) == 0 ):
        print(0)
    else:
        prv = floor(sqrt(a))**2
        nxt = ceil(sqrt(a))**2
        nxt = nxt - a
        prv = a - prv
        print(min(nxt,prv)) 