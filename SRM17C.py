#Problem Link : http://arena.siesgst.ac.in/contest/SRM17/problem/SRM17C

u = int(input())
for o in range(u):
    discount = 0
    n,p,q,r = list(map(int, input().split(" ")))
    products = list(map(int,input().split()))
    for i in products:
        if i >= 1600 and p >0:
            p = p-1
            discount = discount + 800
        elif i >= 800 and q > 0:
            q = q-1
            discount = discount + 400
        elif i >= 400 and r > 0:
            r = r-1
            discount = discount + 200
    print(discount)