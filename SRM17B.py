#Problem Link : http://arena.siesgst.ac.in/contest/SRM17/problem/SRM17B

u = int(input())
for o in range(u):
    diff = 0
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    #print(a)
    for i in range(len(a)-1):
        if a[i+1] - a[i]!= 0:
            #print("diff = ",diff)
            diff = diff + (a[i+1]-a[i]-1)
    print(diff)