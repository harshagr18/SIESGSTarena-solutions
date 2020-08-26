# Problem Link - http://arena.siesgst.ac.in/contest/SRM17/problem/SRM17A

u = int(input())
for o in range(u):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    print(a[0],a[1])